from flask import Flask, request   
from controller import API
from flask_jwt_extended import JWTManager
from settings import my_password
import os
import logging as logger
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')

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
    logger.info("sssssssssssssssssssssss")
    print("path and request is ====", path + " [" + method + "]" )   
    
    print("before request----------")
    logger.info("before request----------")
    if my_password == 'nopassword':
        import os
        import subprocess

        my_env = {**os.environ, 'PATH': '/usr/sbin:/sbin:' + os.environ['PATH']}

        subprocess.Popen(["export"], env=my_env)
        logger.info("updating latest password")
        print("updating latest password")
        # result = os.system(f"export my_password={'HELLOWORLD'}")
        # result = os.system(f"SETX /m my_password {'SHIRKANT'}")
        # logger.info(f"result---- {result}")
    new_password = os.environ.get("my_password")    
    logger.info(f"latest password is :")    
    logger.info(f"latest password is :{new_password}")    

if __name__ == "__main__":
    app.run(host='0.0.0.0')
