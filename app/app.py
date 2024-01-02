from app.db import db
from flask_migrate import Migrate
from flask import Flask
from app.config import Config
from flask_jwt_extended import JWTManager
from flask_restful import Api
from app.resources.cliente import ClienteResource
from app.resources.eletro import EletronicoResource
from app.resources.veiculo import VeiculoResource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    JWTManager(app)
    Migrate(app, db)
    db.init_app(app)
    
    api = Api(app)
    api.add_resource(ClienteResource, '/clientes', '/clientes/<int:id>')
    
   
    api.add_resource(VeiculoResource,'/veiculo','/veiculo/<int:id>')
    api.add_resource(EletronicoResource, '/eletronico/','/eletronico/<int:id>')
    
    
    return app