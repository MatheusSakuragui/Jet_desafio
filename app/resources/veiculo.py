from flask_restful import Resource, reqparse
from app.models import Veiculos
from app.schemas import VeiculoSchema
from app.swaggerdocs.veiculoswagger import SWAGGER_DOCS
from app.db import db

class VeiculoResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('placa', type=str, required=True, help='Placa não informado')
        self.reqparse.add_argument('ano', type=str, required=True, help='Ano não informado')
        self.reqparse.add_argument('qtd_portas', type=str, required=True, help='Quantidade de portas não informada')
        self.reqparse.add_argument('produto_id', type=int, required=True, help='Id produto não informado')
        super(VeiculoResource, self).__init__()
        
    
    def get(self, id):
        veiculo = Veiculos.query.get_or_404(id)
        schema = VeiculoSchema()
        return schema.dump(veiculo)
    
    def post(self):
        args = self.reqparse.parse_args()
        veiculo_schema = VeiculoSchema()
        erros = veiculo_schema.validate(args)
        if erros:
            return erros, 400
        veiculo = Veiculos(**args)
        db.session.add(veiculo)
        db.session.commit()
        response_data = veiculo_schema.dump(veiculo)
        return response_data, 201
    
    def put(self, id):
        veiculo = Veiculos.query.get_or_404(id)
        args = self.reqparse.parse_args()
        veiculo.placa = args['placa']
        veiculo.ano = args['ano']
        veiculo.qtd_portas = args['qtd_portas']
        veiculo.id_produto = args['produto_id']
        db.session.commit()
        veiculo_schema = VeiculoSchema()
        response_data = veiculo_schema.dump(veiculo)
        return response_data, 200
        
    def delete(self, id):
            veiculo = Veiculos.query.get_or_404(id)
            db.session.delete(veiculo)
            db.session.commit()
            veiculo_schema = VeiculoSchema()
            response_data = veiculo_schema.dump(veiculo)
            return response_data, 200    
        
VeiculoResource.get.__doc__ = SWAGGER_DOCS["GET"]
VeiculoResource.post.__doc__ = SWAGGER_DOCS["POST"]
VeiculoResource.put.__doc__ = SWAGGER_DOCS["PUT"]
VeiculoResource.delete.__doc__ = SWAGGER_DOCS["DELETE"] 
        