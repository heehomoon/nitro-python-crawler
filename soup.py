#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import random

from lxml.html import fromstring

from material import Material
import setting 

class Soup:

    def __init__(self):
        self.fail_count = 0
        self.m = Material()

    def getSoup(self, url, user_agents, proxies):

        headers = requests.utils.default_headers()
        user_agent = random.choice(user_agents)
        headers.update({"User-Agent": user_agent})

        while True:

            proxy = random.choice(proxies)

            try:
                session = requests.Session()
                cookies = dict(session.get(url).cookies)
                response = session.post(url, headers=headers, proxies={"https": proxy}, timeout=(1.2, 5), cookies=cookies)

                # If there is bot detection statement => True
                if(False):                
                
                    if (proxy in proxies):
                        proxies.remove(proxy)   # Remove proxy which got detected from proxies set 

                    continue

                if(setting.LXML_PARSER):
                    # Using lxml parser
                    soup = BeautifulSoup(response.content, "lxml")

                if(setting.HTML_PARSER):
                    # Using html parser
                    soup =  BeautifulSoup(response.content, "html.parser") 

                break

            except Exception as e:

                self.fail_count += 1

                # if the number of fail count is more than 50, reset proxies pool
                if (self.fail_count >= setting.FAIL_COUNT):
                    proxies = self.m.getFreeProxies()


        return soup, proxies

 