from marshmallow import Schema, fields

class ClienteSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    email = fields.Email(required=True)
    senha = fields.Str(required=True, load_only=True)
    telefone = fields.Str(required=True)
    cpf = fields.Str(required=True)
    
    
class VeiculoSchema(Schema):
    id = fields.Int(dump_only=True)
    placa = fields.Str(required=True)
    ano = fields.Str(required=True)
    qtd_portas = fields.Str(required=True)
    

class EletronicoSchema(Schema):
    id = fields.Int(dump_only=True)
    voltagem = fields.Str(required=True)