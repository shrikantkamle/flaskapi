from flask_restx import Api


from .product import NS as product_ns
from .login import NS as login_ns

authorizations = {"Bearer auth": {"type": "apiKey", "in": "header", "name": "Authorization"}}

# api = Api(
#     version="1.0",
#     title="Flask API with JWT-Based Authentication",
#     description="Welcome to the Swagger UI documentation site!",
    # doc="/ui",

#     authorizations=authorizations,
# )

API = Api(version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
    security = "Bearer auth"   
    ,authorizations=authorizations)


API.add_namespace(product_ns)
API.add_namespace(login_ns)