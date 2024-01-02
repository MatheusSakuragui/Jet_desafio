from marshmallow import Schema, fields

class ClienteSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    email = fields.Email(required=True)
    senha = fields.Str(required=True, load_only=True)
    telefone = fields.Str(required=True)
    cpf = fields.Str(required=True)

class ProdutoSchema(Schema):
    id = fields.Int(dump_only=True)
    marca = fields.Str(required=True)
    modelo = fields.Str(required=True)
    descricao = fields.Str(required=True)
    lance_inicial = fields.Float(required=True)
    lance_adicional = fields.Float(required=True)
    vendido = fields.Bool(default=False, required=False)