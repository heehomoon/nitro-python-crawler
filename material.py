#!/usr/bin/python3

# Make free proxy list text file 

import requests
import random
from lxml.html import fromstring

class Material:

    def __init__(self):

        f = open('user_agent_list.txt', 'r')
        self.user_agent_list = f.read().splitlines()    
        f.close()

        f = open('url_list.txt', 'r')
        self.urls = f.read().splitlines()    
        f.close()

    def getFreeProxies(self):

        headers = requests.utils.default_headers()

        user_agent = random.choice(self.user_agent_list)
        headers.update({"User-Agent": user_agent})

        # Free proxy site list 
        url = 'https://www.us-proxy.org/'
        url2 = 'https://free-proxy-list.net/uk-proxy.html'
        url3 = 'https://free-proxy-list.net/'
        url4 = 'https://free-proxy-list.net/anonymous-proxy.html'

        while True:
            try:
                response = requests.get(url, headers=headers, timeout=(0.7, 5))
                response2 = requests.get(url2, headers=headers, timeout=(0.7, 5))
                response3 = requests.get(url3, headers=headers, timeout=(0.7, 5))
                response4 = requests.get(url4, headers=headers, timeout=(0.7, 5))
                break
            except Exception as e:
                user_agent = random.choice(self.user_agent_list)
                headers = {"User-Agent": user_agent}

        parser = fromstring(response.text)
        parser2 = fromstring(response2.text)
        parser3 = fromstring(response3.text)
        parser4 = fromstring(response4.text)
        
        proxies = list()

        for i in parser.xpath('//tbody/tr')[:200]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.append(proxy)

        for i in parser2.xpath('//tbody/tr')[:100]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.append(proxy)

        for i in parser3.xpath('//tbody/tr')[:300]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.append(proxy)

        for i in parser4.xpath('//tbody/tr')[:100]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.append(proxy)


        return ["https://"+p for p in proxies]


    def getUserAgents(self):

        return self.user_agent_list
        

    def getUrls(self):

        return self.urls
