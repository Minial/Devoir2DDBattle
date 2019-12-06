import pymongo
from bs4 import BeautifulSoup

"""
Fonction qui retourne tous les sorts du jeu
Utile pour l'index inverse et pour l'interface
"""

def get_all_spells():

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["DD_Creatures"]
    col = db["Creatures"]


    all_spells = []
       
    myquery = { "spells": { "$ne": [] } }
    
    mydoc = col.find(myquery, {"_id":0, "spells":1})
    
    for x in mydoc:
      for k in x.get("spells"):
          if (k not in all_spells):
              all_spells.append(k)
    
    #print(all_spells)
    #print(len(all_spells))
    return(all_spells)
    
    client.close()
    
    
def get_all_creatures():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["DD_Creatures"]
    col = db["Creatures"]


    all_names = []
       
    myquery = { "name": { "$ne": [] } }
    
    mydoc = col.find(myquery, {"_id":0, "name":1})
    
    for x in mydoc:
      for k in x.get("name"):
          if (k not in all_names):
              all_names.append(k)
    
    #print(all_spells)
    #print(len(all_spells))
    return(all_names)
    
    client.close()
    

def getUrlSpell(spell):
    """
    Renvoie l'URL d'un spell donné. La forme est un peu bizarre, on a du
    travailler pour l'obtenir afin d'éviter des 404
    """
    to_return = spell
    k = 0
    t = len(spell)
    while(k < t):
        if(to_return[k].isupper()):
            to_return = to_return[:k]+"-"+to_return[k].lower()+to_return[k+1:]
            k = 0
            t += 1
        k+=1
    return("http://legacy.aonprd.com/ultimateMagic/spells/" + spell + ".html#" + to_return)
        
print(getUrlSpell("ceciEstUnSuperTest"))
            