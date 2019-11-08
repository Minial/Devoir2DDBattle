import requests, json, re, pymongo, sys, sqlite3
from bs4 import BeautifulSoup

"""
Creation de la liste des URL de toutes les creatures a crowler, sur chacun des bestiaires
"""

BASE_URL = ["http://legacy.aonprd.com/bestiary/monsterIndex.html", "http://legacy.aonprd.com/bestiary2/additionalMonsterIndex.html", "http://legacy.aonprd.com/bestiary3/monsterIndex.html", "http://legacy.aonprd.com/bestiary4/monsterIndex.html", "http://legacy.aonprd.com/bestiary5/index.html"]

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
            if(k>0):
                liste_pages_to_crawl.append("/bestiary"+str(k+1)+"/"+monstre)
            else:
                liste_pages_to_crawl.append("/bestiary/"+monstre)
        
liste_pages_to_crawl = list(set(liste_pages_to_crawl))
liste_pages_to_crawl.sort()
print(liste_pages_to_crawl)


for k in range(0, len(liste_pages_to_crawl)):
    liste_pages_to_crawl[k] = "http://legacy.aonprd.com"+liste_pages_to_crawl[k]
print(liste_pages_to_crawl)



"""
Crawling de chacune des url trouvées, avec differenciation pour les types de monstres 
(ex : Drake Lava, Drake Mist, Drake Shadow, ...)
"""
liste_creatures = []
for k in range(2, 3):
    URL = liste_pages_to_crawl[k]
    reponse = requests.get(URL)
    soup = BeautifulSoup(reponse.text, "html.parser")
    prems = True
    creature_nom = "CECI N EST CENSE APPARAITRE NULLE PART"
    creature_spells = []
    for link in soup.find_all('p'):
        if(link.get('class')==['stat-block-title']):
            if(prems):
                creature_nom = str(link).split("<b>")[1].split(" <")[0]
                prems = False
            else:
                creature_json = {
                    "name": creature_nom
                }
                creature_nom = str(link).split("<b>")[1].split(" <")[0]
                liste_creatures.append(creature_json)
            
    creature_json = {
        "name": creature_nom
    }
    liste_creatures.append(creature_json)
    print(liste_creatures)
    print("-----------")
  
