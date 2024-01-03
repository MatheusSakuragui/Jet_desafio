from flask_restful import Resource, reqparse
from app.models import Produto
from app.schemas import ProdutoSchema
from app.db import db

class ProdutoResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('marca', type=str, required=True, help='Marca do produto não informado')
        self.reqparse.add_argument('modelo', type=str, required=True, help='Modelo do produto não informado')
        self.reqparse.add_argument('descricao', type=str, required=True, help='Descrição do produto não informado')
        self.reqparse.add_argument('lance_inicial', type=float, required=True, help='Lance inicial do produto não informado')
        self.reqparse.add_argument('lance_adicional', type=float, required=True, help='Lance inicial do produto não informado')
        self.reqparse.add_argument('vendido', type=bool, default=False)
        super(ProdutoResource, self).__init__()
    
    def get(self, id):
        produto = Produto.query.get_or_404(id)
        schema = ProdutoSchema()

        return schema.dump(produto)
    
    def post(self):
        args = self.reqparse.parse_args()
        produto_schema = ProdutoSchema()
        erros = produto_schema.validate(args)

        if erros:
            return erros, 400
        
        produto = Produto(**args)
        db.session.add(produto)
        db.session.commit()
        response_data = produto_schema.dump(produto)
        
        return response_data, 201
    
    def put(self, id):
        produto = Produto.query.get_or_404(id)
        args = self.reqparse.parse_args()
        produto_schema = ProdutoSchema()
        erros = produto_schema.validate(args)

        if erros:
            return erros, 400
        
        for key, value in args.items():
            setattr(produto, key, value)

        db.session.commit()
        response_data = produto_schema.dump(produto)

        return response_data, 200

    def delete(self, id):
        produto = Produto.query.get_or_404(id)
        db.session.delete(produto)
        db.session.commit()
        
        return {'message': 'Produto deletado com sucesso'}, 200