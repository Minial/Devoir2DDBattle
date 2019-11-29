import requests, json, re, pymongo, sys
from bs4 import BeautifulSoup
from bson import ObjectId


"""
Ouverture de la base MongoDB, et clean de l'ancienne
"""

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["DD_Creatures"]
col = db["Creatures"]

try:#mongoDB
    x = col.delete_many({})
    print(x.deleted_count, " documents deleted.")
except:
    sys.exit("service MongoDB non trouvé, veuillez le démarrer")



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
#print(liste_pages_to_crawl)



"""
Crawling de chacune des url trouvées, avec differenciation pour les types de monstres 
(ex : Drake Lava, Drake Mist, Drake Shadow, ...)
"""

all_base = []
#for k in range(0, len(liste_pages_to_crawl)):
#Modifier ici pour faire des tests sur moins de creatures
#Par exemple for k in range(100, 120):
for k in range(0, len(liste_pages_to_crawl)):
    if(k%50 == 0):
        print("Compteur : Creatures traitees : " + str(k))
    URL = liste_pages_to_crawl[k]
    reponse = requests.get(URL)
    soup = BeautifulSoup(reponse.text, "html.parser")
    prems = True
    creature_nom = "ERROR NAME"
    creature_spells = []
    for link in soup.find_all(True, {'class': ['stat-block-title', 'stat-block-2']}):
        #print(str(link))
        # DES QU'UN TITRE NOIR EST TROUVE, C'EST LE NOM D'UN MONSTRE
        if(link.get('class')==['stat-block-title']):
            banned = False
            strlink = str(link)
            #print(strlink)
            for ban in banned_list:
                if(ban in strlink):
                    banned = True
                    break
            if(not banned):
                if("<b>" in strlink):
                    if(prems):
                        creature_nom = strlink.split("<b>")[1].split("<")[0].split("\t")[0]
                        prems = False
                        creature_spells = []
                    else:
                        creature_json = {
                            "name": creature_nom,
                            "spells": creature_spells,
                            "URL": URL
                        }
                        creature_nom = strlink.split("<b>")[1].split("<")[0].split("\t")[0]
                        creature_spells = []
                        all_base.append(creature_json)
                        col.insert_one(creature_json)
                else:
                    if(prems):
                        creature_nom = strlink.split(">")[1].split("<")[0].split("\t")[0]
                        creature_spells = []
                        prems = False
                    else:
                        creature_json = {
                            "name": creature_nom,
                            "spells": creature_spells,
                            "URL": URL
                        }
                        creature_nom = strlink.split(">")[1].split("<")[0].split("\t")[0]
                        creature_spells = []
                        all_base.append(creature_json)
                        col.insert_one(creature_json)
                        
        # DES QU'UN SPELL EST TROUVE, C'EST UN SPELL CASTABLE PAR LE DERNIER MONSTRE TROUVE   
        elif(link.get('class')==['stat-block-2']):
            strlink = str(link)
            soup2 = BeautifulSoup(strlink, "html.parser")
            for link2 in soup2.find_all('a'):
                strlink2 = str(link2)
                if('/spells/' in strlink2):
                    #print(strlink2)
                    creature_spells.append(strlink2.split('/spells/')[1].split('.html')[0])
        
    creature_json = {
        "name": creature_nom,
        "spells": creature_spells,
        "URL": URL
    }
    all_base.append(creature_json)
    col.insert_one(creature_json)
    
    
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

json_creatures = JSONEncoder().encode(all_base)
    
with open('creatures.json', 'w', encoding='utf-8') as f:
    json.dump(json_creatures, f, ensure_ascii=False, indent=4)
    
client.close()
print(all_base)
