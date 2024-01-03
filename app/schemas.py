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
    
class LeilaoSchema(Schema):
    id = fields.Int(dump_only=True)
    data_futura = fields.DateTime(required=True)
    data_visitacao = fields.DateTime(required=True)
    detalhes = fields.Str(required=True)
    qtd_produtos = fields.Int(required=True)
    status = fields.Str()


class LanceSchema(Schema):
    id = fields.Int(dump_only=True)
    data = fields.DateTime(required=True)
    valor = fields.Float(required=True)
    cliente_id = fields.Int(required=True)
    leilao_id = fields.Int(required=True)