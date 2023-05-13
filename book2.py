from pymongo import MongoClient

client = MongoClient('mongodb://masmuhamadjamaludin10:GPiccdZTeotp6y68@ac-qxx6olp-shard-00-00.lbomoax.mongodb.net:27017,ac-qxx6olp-shard-00-01.lbomoax.mongodb.net:27017,ac-qxx6olp-shard-00-02.lbomoax.mongodb.net:27017/?ssl=true&replicaSet=atlas-2kj0jp-shard-0&authSource=admin&retryWrites=true&w=majority')

db = client.dbsparta

db.cuaca.insert_one({
    'name': 'Kania', 
    'region': 'Karawang', 
    'temperatur': 29 
})

db.cuaca.insert_one({
    'name': 'Intan', 
    'region': 'Jakarta', 
    'temperatur': 30
})

db.cuaca.insert_one({
    'name': 'Kamal', 
    'region': 'Bandung', 
    'temperatur': 40
})