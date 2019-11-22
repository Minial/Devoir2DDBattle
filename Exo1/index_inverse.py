import pymongo
from bs4 import BeautifulSoup

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["DD_Creatures"]
col = db["Creatures"]

