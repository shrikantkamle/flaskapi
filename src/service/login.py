
from flask_jwt_extended import create_access_token
import datetime

class Login():

    def valiate_user(self,data):
        if data["user"] == "user" and data["password"] == "password" :
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(data["user"]), expires_delta=expires)
            return {'token': access_token}, 200
        else:
            return {'error': 'Email or password invalid'}, 401    

