nitro-python-crawler
====================
nitro-python-crawler is web crawler, used to crawl websites and extract structured data from their pages.

## Overview

* Multi-threading 
* Free-proxy
* Rotate IP and User-agents


## Requirements

* Python 2.7 or Python 3.4+
* Works on Linux, Mac OSX


## Required Python3 Modules

* requests
* python3-lxml
* beautifulsoup4


## Install

1. **Install modules**
> Python 2.7.9+ and 3.4+ ship with pip

On Ubuntu(and similar Linux systems):

    $ sudo pip3 install requests
    $ sudo pip3 install lxml
    $ sudo pip3 install bs4


2. **Git clone**
>
    $ git clone https://github.com/heehomoon/nitro-python-crawler.git


3. **How to use**
> Put urls to crawl in the url_list.txt
>
    $ vi url_list.txt
```
    <code>
    https://www.amazon.com/dp/B0054LHI5A
    https://www.amazon.com/dp/B01LZ3RLPC
    https://www.amazon.com/dp/B00Y2CQRZY
    </code>
```
> Create a extractor method 
>
    $ vi extractor.py
```
    <code>
    def getProdcutTitle(self, soup):

    title = ""

    if(soup.find('span', {'id': 'productTitle'})):
        title = soup.find('span', {'id': 'productTitle'}).text
    elif(soup.find('span', {'id': 'ebooksProductTitle'})):
        title = soup.find('span', {'id': 'ebooksProductTitle'}).text
    elif(soup.find('span', {'id': 'fineArtTitle'})):
        title = soup.find('span', {'id': 'fineArtTitle'}).text

    title = title.strip()

    return title   
    </code>
```
> Execute
>
    $ python3 crawler.py




