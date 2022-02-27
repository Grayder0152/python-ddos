import os.path
from gc import collect
from os import system
from time import sleep

from config import SYS_NAME, BASE_DIR


def clear_console():
    system('clear' if SYS_NAME == 'posix' else 'cls')


def cleaner():
    while True:
        sleep(30)
        clear_console()
        collect()


def load_sites_for_attack_from_file(file_path: str = os.path.join(BASE_DIR, 'site_for_attack.txt')):
    sites = []
    with open(file_path) as f:
        for site in f.read().split('\n'):
            if site.startswith('http'):
                sites.append(site)
    return sites
