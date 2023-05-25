from pymongo import MongoClient


from pymongo import MongoClient
# client = MongoClient("mongodb://127.0.0.1:27017")
# print("Connection Successful !!!")
# client.close()


class connectDButil():
    def __init__(self,db_name = "shoppingsite"):
        self.host='localhost', 
        self.port=27017,
        self.username = "A"
        self.password = "b"
        self.client = MongoClient()
        self.db_client = self.client[db_name]


    def get_collection(self,collection_name):
        col = self.db_client[collection_name]
        return col