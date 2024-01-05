from flask_restful import Resource
from app.models import Leilao
from app.resources.lance import LanceResourceLista
from flask import Flask, jsonify, send_file
from app.swaggerdocs.leilaoDETswagger import SWAGGER_DOCS
from io import BytesIO

class LeilaoDETResource(Resource):
    def get(self,id):#id do leilao
        leilao: Leilao = Leilao.query.get(id)
        LeilaoDict = leilao.detalhes_leilao()
        
        for produto in LeilaoDict.get('produtos', []):
            produto['historico_de_lances'] = LanceResourceLista.get(LanceResourceLista,produto['id'])
            
            
        detalhes_leilao_json = jsonify(LeilaoDict).get_data()
        output = BytesIO()
        output.write(detalhes_leilao_json)
        output.seek(0)
        return send_file(output, as_attachment=True, download_name=f'leilao{id}.DET', mimetype='application/json')
    
LeilaoDETResource.get.__doc__ = SWAGGER_DOCS['GET']
        