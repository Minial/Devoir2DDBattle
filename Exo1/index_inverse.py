import pymongo
from bs4 import BeautifulSoup
from liste_sorts import get_all_spells

def index_inverse(sort):

    res = []
    all_spells = get_all_spells()
    if(sort not in all_spells):
        print("Ce sort n'existe pas")
        return(None)
    
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["DD_Creatures"]
    col = db["Creatures"]
    
    myquery = { "spells": { "$ne": [] } }
    mydoc = col.find(myquery, {"_id":0, "name":1, "spells":1})
    for x in mydoc:
      if (sort in x.get("spells")):
          res.append(x.get("name"))
    return(res)
      


# IMPORTANT
# Les noms des sorts commencent par des minuscules
# Un sort avec un espace est traduit comme l'exemple suivant
# Sort : Inflict serious wounds >> Nom officiel : inflictSeriousWounds