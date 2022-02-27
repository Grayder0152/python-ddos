import os

BASE_DIR = os.path.dirname(__file__)
SYS_NAME = os.name
MAX_REQUESTS = 5000

HOSTS = [
    "http://test.house-of-memory.digital/api.php",
    "http://46.4.63.238/api.php"
]
DEFAULT_THREADS_COUNT = 200
DEFAULT_SITE_URL = ['https://www.sber-bank.by', 'https://belarusbank.by']
DEFAULT_PROXIES = [
    {"id": 1, "ip": "46.3.150.156:8000", "auth": "0ShxVd:409mML"},
    {"id": 2, "ip": "158.46.182.200:8000", "auth": "6UFEv4:8XEzkD"},
    {"id": 3, "ip": "45.143.166.77:8000", "auth": "Gve4X0:mANhyq"},
    {"id": 4, "ip": "193.32.155.93:8000", "auth": "bThA0L:SnTPPS"},
    {"id": 5, "ip": "45.151.100.187:8000", "auth": "k5wde6:Do5sMv"},
    {"id": 6, "ip": "46.3.151.127:8000", "auth": "0ShxVd:409mML"},
    {"id": 7, "ip": "45.146.182.111:8000", "auth": "HUZwbg:GuM1Ke"}
]
