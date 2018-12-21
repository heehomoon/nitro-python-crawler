nitro-python-crawler
====================
nitro-python-crawler is web crawler, used to crawl websites and extract structured data from their pages.

### Overview

* Multi-threading 
* Free-proxy
* Rotate IP and User-agents


### Requirements

* Python 2.7 or Python 3.4+
* Works on Linux, Mac OSX


### Required Python3 Modules

* requests
* python3-lxml
* beautifulsoup4


## Install for Python3

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
> Put urls to crawl in the urllist.txt
>
    $ vi urllist.txt

> Create a extractor method 
>
    $ vi extractor.py

> Execute
>
    $ python3 crawler.py




