from app.db import db
from flask_migrate import Migrate
from flask import Flask
from app.config import Config
from flask_jwt_extended import JWTManager
from flask_restful import Api
from app.resources.cliente import ClienteResource
from app.resources.leilao import LeilaoResource, LeilaoResourceLista

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    JWTManager(app)
    Migrate(app, db)
    db.init_app(app)
    
    api = Api(app)
    api.add_resource(ClienteResource, '/clientes', '/clientes/<int:id>')
    api.add_resource(LeilaoResource, '/leilao', '/leilao/<int:id>')
    api.add_resource(LeilaoResourceLista, '/listaleilao')
    
    return app