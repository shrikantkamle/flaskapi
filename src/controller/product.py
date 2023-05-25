from flask import request

from flask_restx import Resource, Namespace,fields
from service.product import productinfo
from flask_jwt_extended import jwt_required

NS =  Namespace("mobile", description = "product details")

product = [{"name":"samsung","price":5000,"type":"mobile"},{"name":"nokia","price":7000,"type":"mobile"},
           {"name":"apple","price":10000,"type":"mobile"},{"name":"oneplus","price":45000,"type":"mobile"}]


items_details = {"description" : "Labworld Wet and Dry bulb Thermometer Hygrometer Humidity meter instrument Wall mounted wooden base for home,workspace and Godawns,28 cm long"}

    

ADD_PRODUCT =  NS.model("product", {
    "Name": fields.String(required = True),
    "Price": fields.String(required = True),
    "Type": fields.String(required = True)
})


@NS.route('/')
class productDetails(Resource):

    @jwt_required()
    def get(self):
        return productinfo().get_all()

@NS.route('/<string:name>')
class productDetailOne(Resource):
    @jwt_required()
    def get(self,name):
        # item = next((i for i in product if i["name"] == name),None)
        # print("samsung",item)
        # if item:
        #     items_details["name"] = name
            return productinfo().get_one(name)
        # return "No record found" ,404
    
@NS.route('/add')
@NS.expect(ADD_PRODUCT)
class productDetails(Resource):
    @jwt_required()
    def post(self):
        return productinfo().add_record_in_db(request.json)
    
@NS.route('/remove/<string:name>')
class productDetails(Resource):
    @jwt_required()
    def delete(self,name):
        print
        return f"deleted {name}",200    