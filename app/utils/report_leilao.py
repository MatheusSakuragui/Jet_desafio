from app.models import Produto

def report_leilao(self):
    produtos = Produto.query.filter_by(leilao_id=self.id).order_by(Produto.id).all()
    print(produtos)