

from flask_restx import Resource, Namespace


NS =  Namespace("product", description = "product details")

@NS.route('/')
class productDetails(Resource):
    def get(self):

        return "ok",200