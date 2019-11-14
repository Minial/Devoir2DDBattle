import requests, json, re, pymongo, sys, sqlite3
from bs4 import BeautifulSoup

"""
Creation de la liste des URL de toutes les creatures a crowler, sur chacun des bestiaires
"""

#BASE_URL = ["http://legacy.aonprd.com/bestiary/monsterIndex.html", "http://legacy.aonprd.com/bestiary2/additionalMonsterIndex.html", "http://legacy.aonprd.com/bestiary3/monsterIndex.html", "http://legacy.aonprd.com/bestiary4/monsterIndex.html", "http://legacy.aonprd.com/bestiary5/index.html"]

BASE_URL = ["http://legacy.aonprd.com/bestiary/monsterIndex.html", "http://legacy.aonprd.com/bestiary2/additionalMonsterIndex.html", "http://legacy.aonprd.com/bestiary3/monsterIndex.html", "http://legacy.aonprd.com/bestiary4/monsterIndex.html", "http://legacy.aonprd.com/bestiary5/index.html"]
banned_link_list = ["introduction.html","monsterIndex.html","variantMonsterIndex.html","monsterCohorts.html","animalCompanions.html","monstersAsPCs.html","monsterRoles.html","encounterTables.html","monsterCreation.html","monsterAdvancement.html","universalMonsterRules.html","creatureTypes.html","monsterFeats.html"]
banned_list = ["Statistics", "Advancement", "Aberration", "Animal", "Construct", "Rabies", "Phantom Armor"]


liste_pages_to_crawl = []

for k in range(0, len(BASE_URL)):
    URL = BASE_URL[k]
    reponse = requests.get(URL)
    soup = BeautifulSoup(reponse.text, "html.parser")
    
    
    for link in soup.find_all('a'):
        monstre = link.get('href')
        if not(monstre.startswith( '..' ) or monstre.startswith( '#' ) or monstre.startswith( 'http://' ) or monstre.startswith( 'additionalMonsterIndex.html' ) or monstre in banned_link_list):
            if ("#" in monstre):
                monstre = (monstre.split("#"))[0]
            if(k>0):
                liste_pages_to_crawl.append("/bestiary"+str(k+1)+"/"+monstre)
            else:
                liste_pages_to_crawl.append("/bestiary/"+monstre)
        
liste_pages_to_crawl = list(set(liste_pages_to_crawl))
liste_pages_to_crawl.sort()


for k in range(0, len(liste_pages_to_crawl)):
    liste_pages_to_crawl[k] = "http://legacy.aonprd.com"+liste_pages_to_crawl[k]
print(liste_pages_to_crawl)



"""
Crawling de chacune des url trouvées, avec differenciation pour les types de monstres 
(ex : Drake Lava, Drake Mist, Drake Shadow, ...)
"""
liste_creatures = []
#for k in range(0, len(liste_pages_to_crawl)):
for k in range(0, len(liste_pages_to_crawl)):
    URL = liste_pages_to_crawl[k]
    reponse = requests.get(URL)
    soup = BeautifulSoup(reponse.text, "html.parser")
    prems = True
    creature_nom = "ERROR NAME"
    creature_spells = []
    for link in soup.find_all('p'):
        if(link.get('class')==['stat-block-title']):
            banned = False
            strlink = str(link)
            print(strlink)
            for ban in banned_list:
                if(ban in strlink):
                    banned = True
                    break
            if(not banned):
                if("<b>" in strlink):
                    if(prems):
                        creature_nom = strlink.split("<b>")[1].split("<")[0].split("\t")[0]
                        prems = False
                    else:
                        creature_json = {
                            "name": creature_nom
                        }
                        creature_nom = strlink.split("<b>")[1].split("<")[0].split("\t")[0]
                        liste_creatures.append(creature_json)
                else:
                    if(prems):
                        creature_nom = strlink.split(">")[1].split("<")[0].split("\t")[0]
                        prems = False
                    else:
                        creature_json = {
                            "name": creature_nom
                        }
                        creature_nom = strlink.split(">")[1].split("<")[0].split("\t")[0]
                        liste_creatures.append(creature_json)
            
    creature_json = {
        "name": creature_nom
    }
    liste_creatures.append(creature_json)
    print(liste_creatures)
    print("-----------")

