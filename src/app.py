from flask import Flask
from controller import API
from flask_jwt_extended import JWTManager
from settings import *
app = Flask(__name__)
API.init_app(app)
app.config["JWT_SECRET_KEY"] = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'
jwt = JWTManager(app)
app.config['PROPAGATE_EXCEPTIONS'] = True
print("flask started..............")
if __name__ == "__main__":
    app.run(host='0.0.0.0')
