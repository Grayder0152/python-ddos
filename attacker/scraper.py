import cloudscraper
from pyuseragents import random as random_useragent

from config import HOSTS, DEFAULT_PROXIES


class Scraper:
    def __init__(self):
        self.scraper = cloudscraper.create_scraper(
            browser={'browser': 'firefox', 'platform': 'android', 'mobile': True}
        )
        self.proxies: iter = self._parse_proxies()

    def _parse_proxies(self) -> iter:
        proxies = []
        self.update_headers()
        for host in HOSTS:
            try:
                resp = self.scraper.get(host, timeout=5)
                proxies.extend(resp.json()['proxy'])
                resp.close()
            except Exception:
                pass
        if len(proxies) == 0:
            proxies = DEFAULT_PROXIES
        return iter(proxies)

    def update_headers(self, headers: dict = None):
        self.scraper.headers.update(
            {
                'Content-Type': 'application/json',
                'cf-visitor': 'https',
                'User-Agent': random_useragent(),
                'Connection': 'keep-alive',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'ru',
                'x-forwarded-proto': 'https',
                'Accept-Encoding': 'gzip, deflate, br'
            } if headers is None else headers
        )

    def update_proxies(self):
        try:
            proxy = self.proxies.__next__()
        except StopIteration:
            raise StopIteration("You used all proxies.")

        proxy_url = f'{proxy["ip"]}://{proxy["auth"]}'
        self.scraper.proxies.update({'http': proxy_url, 'https': proxy_url})

    def send_request_to_site(self, site_url: str):
        response = self.scraper.get(site_url)
        return response
