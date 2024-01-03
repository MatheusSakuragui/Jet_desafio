from flask_restful import Resource, reqparse
from app.models import Leilao
from app.schemas import LeilaoSchema
from datetime import datetime
from app.db import db

class LeilaoResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('data_futura', type=str, required=True, help='Data futura não informada')
        self.reqparse.add_argument('data_visitacao', type=str, required=True, help='Data de visitação não informada')
        self.reqparse.add_argument('detalhes', type=str, required=True, help='Detalhes não informados')
        self.reqparse.add_argument('qtd_produtos', type=str, required=True, help='Quantidade de produtos não informado')
        self.reqparse.add_argument('status', type=str, required=False, default="EM ABERTO")
        super(LeilaoResource, self).__init__()
    
    def get(self, id):
        leilao = Leilao.query.get_or_404(id)
        detalhes_leilao = leilao.detalhes_leilao()
        return detalhes_leilao , 200
    
    def put(self, id):
        args = self.reqparse.parse_args()
        leilao_schema = LeilaoSchema()
        erros = leilao_schema.validate(args)
        if erros:
            return erros, 400
        
        leilao: Leilao = Leilao.query.get_or_404(id)
        
        print(args)
        
        for key, value in args.items():
            if value is not None:
                setattr(leilao, key, value)
                
        leilao.data_futura = datetime.strptime(args['data_futura'], '%Y-%m-%dT%H:%M:%S')
        leilao.data_visitacao = datetime.strptime(args['data_visitacao'], '%Y-%m-%dT%H:%M:%S')
        
        db.session.add(leilao)
        db.session.commit()
        
        response_data = leilao_schema.dump(leilao)
        return response_data, 201
    
    def post(self):
        args = self.reqparse.parse_args()
        leilao_schema = LeilaoSchema()
        erros = leilao_schema.validate(args)
        if erros:
            return erros, 400
        
        leilao = Leilao(**args)
        leilao.data_futura = datetime.strptime(args['data_futura'], '%Y-%m-%dT%H:%M:%S')
        leilao.data_visitacao = datetime.strptime(args['data_visitacao'], '%Y-%m-%dT%H:%M:%S')
        
        db.session.add(leilao)
        db.session.commit()
        
        response_data = leilao_schema.dump(leilao)
        return response_data, 201
    
    def delete(self, id):
        leilao = Leilao.query.get_or_404(id)
        db.session.delete(leilao)
        db.session.commit()
        return {}, 201
    
class LeilaoResourceLista(Resource):        
    def get(self):
        leilao = Leilao.query.all()
        schema = LeilaoSchema()
        return schema.dump(leilao, many=True)