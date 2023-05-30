from pymongo import MongoClient


from pymongo import MongoClient
# client = MongoClient("mongodb://127.0.0.1:27017")
# print("Connection Successful !!!")
# client.close()


class connectDButil():
    def __init__(self,db_name = "shoppingsite"):

        self.client = MongoClient(        
        host='test_mongodb',
        port=27017,
        username='root',
        password='pass', 
        authSource="admin")
        self.db_client = self.client[db_name]


    def get_collection(self,collection_name):
        col = self.db_client[collection_name]
        return col