from marshmallow import Schema, fields

class ClienteSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    email = fields.Email(required=True)
    senha = fields.Str(required=True, load_only=True)
    telefone = fields.Str(required=True)
    cpf = fields.Str(required=True)
    
class LeilaoSchema(Schema):
    id = fields.Int(dump_only=True)
    data_futura = fields.DateTime(required=True)
    data_visitacao = fields.DateTime(required=True)
    detalhes = fields.Str(required=True)
    qtd_produtos = fields.Int(required=True)
    status = fields.Str()