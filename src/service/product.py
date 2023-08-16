from pymongo import errors
from util.db_util import connectDButil
from service.servicebase import ServiceBase

class productinfo(ServiceBase):
    def __init__(self):
        super().__init__()
        pass
        self.collection = self.collection
        print("sssssssss",self.collection)


    def get_all(self):
        item = list(self.collection.find({},{"_id": 0 }))
        # item = list(self.collection.find({},{"_id": 0 }))
        print("ittttttttttttt",item)
        if item:
            self.logger.info("fetching all the records.")

            return item,200
        self.logger.error("No record exist !!!")
        return {"error": f"No record found"},404


    def get_one(self,name):
        print("checking name", name)
        item = self.collection.find_one({"Name":name},{"_id": 0 })
        print("ittttttttttttt",item)
        if item:

            return item,200
        self.logger.error(f"No record exist with name {name}")
        return {"error": f"No record found for {name}"},404



    def add_record_in_db(self,data):
        try:
            print("data",data)
            item = self.collection.insert_one(data)
            print("item---inserrt",item)
            # if item:
            return {"Message":f" {data['Name']} added successfully"},201
            return "Unable to insert",400 
        except Exception as error:
            print("error-------",error)
            return {"error":"Unable to insert"},400

