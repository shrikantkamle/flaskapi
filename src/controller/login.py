from flask import request

from flask_restx import Resource, Namespace,fields
from service.login import Login

NS =  Namespace("login", description = "product details")

    

LOGIN =  NS.model("Login", {
    "user": fields.String(required = True),
    "password": fields.String(required = True)
})


@NS.expect(LOGIN)
@NS.route('/login')
class login(Resource):
    def post(self):

        return Login().valiate_user(request.json)
