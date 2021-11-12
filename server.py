import rpyc
from pymongo import MongoClient
import pymongo
CONNECTION_STRING = "mongodb://jlalmeidaf:8QfBCD2BHsK6Ri5l@cluster0-shard-00-00.isocp.mongodb.net:27017,cluster0-shard-00-01.isocp.mongodb.net:27017,cluster0-shard-00-02.isocp.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-42glha-shard-0&authSource=admin&retryWrites=true&w=majority"

client = MongoClient(CONNECTION_STRING)

db = client['Chat']

collection = db['msgs']

# chat = ""

class ChatServer(rpyc.Service):
	def __init__(self,conn):
		self.nickname = None

	def exposed_set_nickname(self, nickname):
		self.nickname = nickname

	def exposed_set_mensage(self, msg, nickname):
		global collection
		item_msg = {
			"dest" : nickname,
			"msg" : self.nickname + ": " + msg
		}
		collection.insert_one(item_msg)
		# chat = self.nickname + ": " + msg

	def exposed_get_mensage(self):
		global collection
		msgs = collection.find()
		for msg in msgs:
			if msg['dest'] == self.nickname:
				collection.delete_one(msg)
				return msg['msg']

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(ChatServer, port=18861)
    t.start()