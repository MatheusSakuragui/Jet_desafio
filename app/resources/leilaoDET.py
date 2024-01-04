from flask_restful import Resource
from app.models import Leilao
from app.resources.lance import LanceResourceLista

class LeilaoDETResource(Resource):
    def get(self,id):#id do leilao
        leilao: Leilao = Leilao.query.get(id)
        LeilaoDict = leilao.detalhes_leilao()
        
        for produto in LeilaoDict.get('produtos', []):
            produto['historico_de_lances'] = LanceResourceLista.get(LanceResourceLista,produto['id'])
            
        return LeilaoDict
        