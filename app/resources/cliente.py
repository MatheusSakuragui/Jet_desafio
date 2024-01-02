from flask_restful import Resource, reqparse
from app.models import Cliente
from app.schemas import ClienteSchema
from app.db import db

class ClienteResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('nome', type=str, required=True, help='Nome do cliente não informado')
        self.reqparse.add_argument('email', type=str, required=True, help='Email do cliente não informado')
        self.reqparse.add_argument('senha', type=str, required=True, help='Senha do cliente não informada')
        self.reqparse.add_argument('telefone', type=str, required=True, help='Telefone do cliente não informado')
        self.reqparse.add_argument('cpf', type=str, required=True, help='CPF do cliente não informado')
        super(ClienteResource, self).__init__()
    
    def get(self, id):
        cliente = Cliente.query.get_or_404(id)
        schema = ClienteSchema()
        return schema.dump(cliente)
    
    def post(self):
        args = self.reqparse.parse_args()
        cliente_schema = ClienteSchema()
        erros = cliente_schema.validate(args)
        if erros:
            return erros, 400
        cliente = Cliente(**args)
        db.session.add(cliente)
        db.session.commit()
        response_data = cliente_schema.dump(cliente)
        
        return response_data, 201