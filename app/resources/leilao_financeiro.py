from flask import request
from flask_restful import Resource
from .models import db, LeilaoFinanceiro, LeilaoFinanceiroSchema

leilao_financeiro_schema = LeilaoFinanceiroSchema()
leilao_financeiros_schema = LeilaoFinanceiroSchema(many=True)

class LeilaoFinanceiroResource(Resource):
    def __init__(self):
        self.reqparse.add_argument('conta_id', type=int, required=True, help='ID da conta não informado')
        self.reqparse.add_argument('leilao_id', type=int, required=True, help='ID do leilão não informado')
        super(LeilaoFinanceiroResource, self).__init__()

    def get(self, leilao_financeiro_id):
        leilao_financeiro = LeilaoFinanceiro.query.get_or_404(leilao_financeiro_id)
        return leilao_financeiro_schema.dump(leilao_financeiro)

    def post(self):
        json_data = request.get_json()
        leilao_financeiro = leilao_financeiro_schema.load(json_data)
        
        db.session.add(leilao_financeiro)
        db.session.commit()

        return leilao_financeiro_schema.dump(leilao_financeiro), 201

    def put(self, leilao_financeiro_id):
        leilao_financeiro = LeilaoFinanceiro.query.get_or_404(leilao_financeiro_id)
        json_data = request.get_json()
        
        leilao_financeiro.conta_id = json_data['conta_id']
        leilao_financeiro.leilao_id = json_data['leilao_id']

        db.session.commit()

        return leilao_financeiro_schema.dump(leilao_financeiro)

    def delete(self, leilao_financeiro_id):
        leilao_financeiro = LeilaoFinanceiro.query.get_or_404(leilao_financeiro_id)
        db.session.delete(leilao_financeiro)
        db.session.commit()

        return {'message': 'Leilão Financeiro deletado com sucesso'}, 204
