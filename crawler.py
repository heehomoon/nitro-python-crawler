#!/usr/bin/python3

from soup import Soup
from material import Material

import setting 
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
    soup, proxies = s.getSoup(url, user_agents, proxies)

    title = ""

    if(soup.find('span', {'id': 'productTitle'})):
        title = soup.find('span', {'id': 'productTitle'}).text
    elif(soup.find('span', {'id': 'ebooksProductTitle'})):
        title = soup.find('span', {'id': 'ebooksProductTitle'}).text
    elif(soup.find('span', {'id': 'fineArtTitle'})):
        title = soup.find('span', {'id': 'fineArtTitle'}).text

    title = title.strip()

    print(title)


def startCrawling():

    threads = list()

    for i in range(0, setting.THREAD_NUM):
        threads.append(myCrawlThread())

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


startCrawling()

