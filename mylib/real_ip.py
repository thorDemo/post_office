import requests
import re


def real_ip():
    response = requests.get('https://www.ip.cn')
    data = re.search(r'Your IP</span>: (.*)</span>', response.text)
    return data.group(1)

