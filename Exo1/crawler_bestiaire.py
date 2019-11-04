import requests, json, re, pymongo, sys, sqlite3
from bs4 import BeautifulSoup


BASE_URL = ["http://legacy.aonprd.com/bestiary/monsterIndex.html", "http://legacy.aonprd.com/bestiary2/additionalMonsterIndex.html", "http://legacy.aonprd.com/bestiary3/monsterIndex.html", "http://legacy.aonprd.com/bestiary4/monsterIndex.html", "http://legacy.aonprd.com/bestiary5/index.html"]

liste_pages_to_crawl_all = []
liste_pages_to_crawl = []


for k in range(0, len(BASE_URL)):
    URL = BASE_URL[k]
    reponse = requests.get(URL)
    soup = BeautifulSoup(reponse.text, "html.parser")
    
    
    for link in soup.find_all('a'):
        monstre = link.get('href')
        if not(monstre.startswith( '..' ) or monstre.startswith( '#' ) or monstre.startswith( 'http://' ) or monstre.startswith( 'additionalMonsterIndex.html' )):
            if ("#" in monstre):
                monstre = (monstre.split("#"))[0]
        
            liste_pages_to_crawl.append("/bestiary"+str(k+1)+"/"+monstre)
        
        
liste_pages_to_crawl = list(set(liste_pages_to_crawl))
liste_pages_to_crawl.sort()
print(liste_pages_to_crawl)





       



    

