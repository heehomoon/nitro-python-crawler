#!/usr/bin/python3

from soup import Soup
from material import Material

import queue
import threading

m = Material()

proxies = m.getFreeProxies()
user_agents = m.getUserAgents()  

# Put url list into queue
urls =  m.getUrls()
urlQueue = queue.Queue()
[urlQueue.put(url) for url in urls]

class myCrawlThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):

        while True:
            if (urlQueue.empty()):   
                break
            else:
                getCrawledData(urlQueue.get_nowait())

def getCrawledData(url):

    global proxies
    global user_agents

    s = Soup()
    soup_lxml, soup_html, proxies = s.getSoup(url, user_agents, proxies)

    title = ""

    if(soup_lxml.find('span', {'id': 'productTitle'})):
        title = soup_lxml.find('span', {'id': 'productTitle'}).text
    elif(soup_lxml.find('span', {'id': 'ebooksProductTitle'})):
        title = soup_lxml.find('span', {'id': 'ebooksProductTitle'}).text
    elif(soup_lxml.find('span', {'id': 'fineArtTitle'})):
        title = soup_lxml.find('span', {'id': 'fineArtTitle'}).text

    title = title.strip()

    print(title)

def startCrawling():

    threads = list()

    for i in range(0, 10):
        threads.append(myCrawlThread())

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


# queue에 url 넣고 
startCrawling()

