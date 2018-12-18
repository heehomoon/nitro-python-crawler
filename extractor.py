#!/usr/bin/python3

class Extractor:

    
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