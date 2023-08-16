from flask import Flask, request   
from controller import API
from flask_jwt_extended import JWTManager
from settings import my_password
import os
app = Flask(__name__)
API.init_app(app)
app.config["JWT_SECRET_KEY"] = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'
jwt = JWTManager(app)
app.config['PROPAGATE_EXCEPTIONS'] = True
print("flask started 1..............",my_password)


@app.before_request   
def before_request_callback():   
    path = request.path   
    method = request.method   
   
    print("path and request is ====", path + " [" + method + "]" )   
    
    print("before request----------")
    if my_password == 'nopassword':
        print("updating latest password")
        result = os.system(f"export my_password={'SHIRKANT'}")
        print("result----",result)
    print("latest password is :",os.environ.get("my_password"))    

@app.before_request
def update_env():
    print("before request----------")
    if my_password == 'nopassword':
        print("updating latest password")
        result = os.system(f"export my_password={'SHIRKANT'}")
        print("result----",result)
    print("latest password is :",os.environ.get("my_password"))    

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
