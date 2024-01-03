from app.db import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(20), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    
    def verificar_senha(self, senha):
        return self.senha == senha

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(20), nullable=False)
    modelo = db.Column(db.String(20), nullable=False)
    descricao = db.Column(db.String(120), nullable=False)
    lance_inicial = db.Column(db.Float(), nullable=False)
    lance_adicional = db.Column(db.Float(), nullable=False)
    vendido = db.Column(db.Boolean(), default=False, nullable=True)
    leilao_id = db.Column(db.Integer, db.ForeignKey('leilao.id'), nullable=False)
    tipo_produto_id = db.Column(db.Integer, db.ForeignKey('tipo_produto.id'), nullable=False)

class Financeiro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    banco = db.Column(db.String(50), nullable=False)

class Conta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agencia = db.Column(db.String(20), nullable=False)
    conta_corrente = db.Column(db.String(20), nullable=False)
    financeiro_id = db.Column(db.Integer, db.ForeignKey('financeiro.id'), nullable=False)

    
class Veiculos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), nullable=False, unique=True)
    ano = db.Column(db.String(4), nullable=False)
    qtd_portas = db.Column(db.Integer, nullable=False)
    
class Eletronico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voltagem = db.Column(db.String(3), nullable=False)

class Leilao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_futura = db.Column(db.DateTime(80), nullable=False)
    data_visitacao = db.Column(db.DateTime(80), nullable=False)
    detalhes = db.Column(db.String(120), nullable=False)
    qtd_produtos = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum('EM ABERTO', 'EM ANDAMENTO','FINALIZADO', name='status_enum'), server_default='EM ABERTO', nullable=False)


class LeilaoFinanceiro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conta_id = db.Column(db.Integer, db.ForeignKey('conta.id'), nullable=False)
    leilao_id = db.Column(db.Integer, db.ForeignKey('leilao.id'), nullable=False)

class TipoProduto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eletronico_veiculo = db.Column(db.Enum('Eletrônico', 'Veículo'), name='tipo_produto_enum')
    descricao = db.Column(db.String(50), nullable=False)
