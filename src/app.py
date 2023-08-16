from flask import Flask
from controller import API
from flask_jwt_extended import JWTManager
from settings import my_password
import os
app = Flask(__name__)
API.init_app(app)
app.config["JWT_SECRET_KEY"] = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'
jwt = JWTManager(app)
app.config['PROPAGATE_EXCEPTIONS'] = True
print("flask started..............",my_password)

@app.before_request
def update_env():
    if my_password == 'nopassword':
        os.system(f"export my_password={'SHIRKANT'}")
    print("latest password is :",os.environ.get("my_password"))    

if __name__ == "__main__":
    app.run(host='0.0.0.0',DEBUG=True)
