from flask_sqlalchemy import SQLAlchemy
from app.db import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(20), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    
    def verificar_senha(self, senha):
        return self.senha == senha
    
class Leilao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_futura = db.Column(db.DateTime(80), nullable=False)
    data_visitacao = db.Column(db.DateTime(80), nullable=False)
    detalhes = db.Column(db.String(120), nullable=False)
    qtd_produtos = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum('EM ABERTO', 'EM ANDAMENTO','FINALIZADO', name='status_enum'), server_default='EM ABERTO', nullable=False)
