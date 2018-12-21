#!/usr/bin/python3

from soup import Soup
from material import Material
from extractor import Extractor

import setting 
import queue
import threading

# Bring proxies, user_agents, urls
m = Material()
proxies = m.getFreeProxies()
user_agents = m.getUserAgents() 
urls =  m.getUrls()

# Put url list into queue
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
    soup, proxies = s.getSoup(url, user_agents, proxies)
    
    e = Extractor()
    title = e.getProdcutTitle(soup)

    # If it failed to crawl data, re-crawl by put url into queue again
    if(title == ""):
        urlQueue.put(url)


def startCrawling():

    threads = list()

    for i in range(0, setting.THREAD_NUM):
        threads.append(myCrawlThread())

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


startCrawling()

