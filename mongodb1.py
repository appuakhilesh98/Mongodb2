import pymongo

from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://root1:8086Akhil@cluster1.iyvdn1x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

d= {
    "name": "Akhilesh",
    "email_id":"akhileshcg98@gmail.com",
    "mob no" : "7349411964"
}
d= {
    "name": "Akhilesh",
    "email_id":"akhileshcg98@gmail.com",
    "mob no" : "7349411964"
}
d= {
    "name": "Akhilesh",
    "email_id":"akhileshcg98@gmail.com",
    "mob no" : "7349411964"
}

d= {
    "name": "Akhilesh",
    "email_id":"akhileshcg98@gmail.com",
    "mob no" : "7349411964"
}

d= {
    "name": "Akhilesh",
    "email_id":"akhileshcg98@gmail.com",
    "mob no" : "7349411964"
}

db1=client['mongodb1']
coll = db1['test']
coll.insert_one(d)