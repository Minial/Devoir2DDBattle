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