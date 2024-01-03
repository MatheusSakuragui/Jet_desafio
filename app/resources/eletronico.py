from flask_restful import Resource, reqparse
from app.models import Eletronico
from app.schemas import EletronicoSchema
from app.db import db

class EletronicoResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('voltagem', type=str, required=True, help='Voltagem não informado')
        self.reqparse.add_argument('produto_id', type=int, required=True, help='Produto id nao foi informado')
        super(EletronicoResource, self).__init__()
        
    
    def get(self, id):
        eletronico = Eletronico.query.get_or_404(id)
        eletronico_schema = EletronicoSchema()
        return eletronico_schema.dump(eletronico)
    
    def post(self):
        args = self.reqparse.parse_args()
        eletronico_schema = EletronicoSchema()
        erros = eletronico_schema.validate(args)
        if erros:
            return erros, 400
        eletronico = Eletronico(**args)
        db.session.add(eletronico)
        db.session.commit()
        response_data = eletronico_schema.dump(eletronico)
        return response_data, 201
    
    def put(self, id):
        eletronico = Eletronico.query.get_or_404(id)
        args = self.reqparse.parse_args()
        eletronico.voltagem = args['voltagem']
        eletronico.produto_id = args['produto_id']
        db.session.commit()
        eletronico_schema = EletronicoSchema()
        response_data = eletronico_schema.dump(eletronico)
        return response_data, 200
        
    def delete(self, id):
            eletronico = Eletronico.query.get_or_404(id)
            db.session.delete(eletronico)
            db.session.commit()
            eletronico_schema = EletronicoSchema()
            response_data = eletronico_schema.dump(eletronico)
            return response_data, 200
                