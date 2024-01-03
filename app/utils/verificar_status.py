from app.models import Leilao
from app.scheduler import scheduler

def verificar_e_atualizar_status_leiloes():
    with scheduler.app.app_context():
        leiloes = Leilao.query.all()
        for leilao in leiloes:
            leilao.verificar_atualizar_status()
