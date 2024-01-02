from flask_restful import Resource, reqparse
from app.models import Veiculo
from app.schemas import VeiculoSchema
from app.db import db

class VeiculoResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('placa', type=str, required=True, help='Placa não informado')
        self.reqparse.add_argument('ano', type=str, required=True, help='Ano não informado')
        self.reqparse.add_argument('qtd_portas', type=str, required=True, help='Quantidade de portas não informada')
        super(VeiculoResource, self).__init__()
        
    
    def get(self, id):
        veiculo = Veiculo.query.get_or_404(id)
        schema = VeiculoSchema()
        return schema.dump(veiculo)
    
    def post(self):
        args = self.reqparse.parse_args()
        veiculo_schema = VeiculoSchema()
        erros = veiculo_schema.validate(args)
        if erros:
            return erros, 400
        veiculo = Veiculo(**args)
        db.session.add(veiculo)
        db.session.commit()
        response_data = veiculo_schema.dump(veiculo)
        return response_data, 201
    
    def put(self, id):
        veiculo = Veiculo.query.get_or_404(id)
        args = self.reqparse.parse_args()
        veiculo.placa = args['placa']
        veiculo.ano = args['ano']
        veiculo.qtd_portas = args['qtd_portas']
        db.session.commit()
        veiculo_schema = VeiculoSchema()
        response_data = veiculo_schema.dump(veiculo)
        return response_data, 200
        
    def delete(self, id):
            veiculo = Veiculo.query.get_or_404(id)
            db.session.delete(veiculo)
            db.session.commit()
            veiculo_schema = VeiculoSchema()
            response_data = veiculo_schema.dump(veiculo)
            return response_data, 200    
        