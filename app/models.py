from app.db import db
from datetime import datetime

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(20), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    lance = db.relationship('Lance', backref='cliente', lazy=True)
    
    def verificar_senha(self, senha):
        return self.senha == senha


# ! Produtos não vendidos deverão ser associados a um leilão futuro

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    marca = db.Column(db.String(20), nullable=False)
    modelo = db.Column(db.String(20), nullable=False)
    descricao = db.Column(db.String(120), nullable=False)
    lance_inicial = db.Column(db.Float(), nullable=False)
    lance_adicional = db.Column(db.Float(), nullable=False)
    vendido = db.Column(db.Boolean(), default=False, nullable=True)
    leilao_id = db.Column(db.Integer, db.ForeignKey('leilao.id'), nullable=False)
    tipo_produto_id = db.Column(db.Integer, db.ForeignKey('tipo_produto.id'), nullable=False)
    leilao = db.relationship('Leilao', backref=db.backref('produtos', lazy=True))
    # veiculo = db.relationship('Veiculo', backref=db.backref('produtos', lazy=True))
    # eletronico = db.relationship('Eletronico', backref=db.backref('produtos', lazy=True))
    
    
class Financeiro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    banco = db.Column(db.String(50), nullable=False)

class Conta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agencia = db.Column(db.String(20), nullable=False)
    conta_corrente = db.Column(db.String(20), nullable=False)
    financeiro_id = db.Column(db.Integer, db.ForeignKey('financeiro.id'), nullable=False)

# ! A decidir a maneira de como associar com Produto e colocar sua FK
class Veiculos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), nullable=False, unique=True)
    ano = db.Column(db.String(4), nullable=False)
    qtd_portas = db.Column(db.Integer, nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    
class Eletronico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voltagem = db.Column(db.String(3), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)


# ! Colocas as instituições financeiras no retorno
class Leilao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    data_futura = db.Column(db.DateTime(80), nullable=False)
    data_visitacao = db.Column(db.DateTime(80), nullable=False)
    detalhes = db.Column(db.String(120), nullable=False)
    qtd_produtos = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum('EM ABERTO', 'EM ANDAMENTO','FINALIZADO', name='status_enum'), server_default='EM ABERTO', nullable=False)
    lance = db.relationship('Lance', backref='leilao', lazy=True)
    
    def detalhes_leilao(self):
        
        produtos = Produto.query.filter_by(leilao_id=self.id).order_by(Produto.id).all()

        detalhes_leilao = {
            'id': self.id,
            'nome': self.nome,
            'data_futura': self.data_futura.strftime('%Y-%m-%dT%H:%M:%S'),
            'data_visitacao': self.data_visitacao.strftime('%Y-%m-%dT%H:%M:%S'),
            'detalhes': self.detalhes,
            'qtd_produtos': self.qtd_produtos,
            'status': self.status,
            'produtos': [{
                'dados_do_produto': {
                    'marca': produto.marca,
                    'modelo': produto.modelo,
                    'descricao': produto.descricao,
                    'lance_inicial': produto.lance_inicial,
                    'lance_adicional': produto.lance_adicional,
                    'vendido': produto.vendido,
                }
            } for produto in produtos]
        }

        return detalhes_leilao
    def verificar_atualizar_status(self):
        data_atual = datetime.now()
        if self.status == "FINALIZADO":
            return

        if self.data_futura <= data_atual < self.data_visitacao:
            self.status = 'EM ANDAMENTO'
        elif self.data_visitacao <= data_atual:
            self.status = 'FINALIZADO'

            for produto in self.produtos:
                ultimo_lance = Lance.query.filter_by(produto_id=produto.id).order_by(Lance.data.desc()).first()
                if ultimo_lance:
                    venda = Venda(valor=ultimo_lance.valor, cliente_id=ultimo_lance.cliente_id, produto_id=produto.id, leilao_id=self.id)
                    db.session.add(venda)
                    produto.vendido = True
            
            produtos_nao_vendidos = Produto.query.filter_by(leilao_id=self.id, vendido=False).all()
               
            proximo_leilao = Leilao.query.filter(Leilao.data_futura > data_atual).order_by(Leilao.data_futura).first()
            
            if proximo_leilao:
                for produto in produtos_nao_vendidos:
                    produto.leilao_id = proximo_leilao.id
                    produto.vendido = False 
        db.session.commit()

class Lance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.utcnow())
    valor = db.Column(db.Float, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    leilao_id = db.Column(db.Integer, db.ForeignKey('leilao.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)

class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    valor = db.Column(db.Float, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    leilao_id = db.Column(db.Integer, db.ForeignKey('leilao.id'), nullable=False)
    cliente = db.relationship('Cliente', backref=db.backref('vendas', lazy=True))
    produto = db.relationship('Produto', backref=db.backref('vendas', lazy=True))
    leilao = db.relationship('Leilao', backref=db.backref('vendas', lazy=True))

class LeilaoFinanceiro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conta_id = db.Column(db.Integer, db.ForeignKey('conta.id'), nullable=False)
    leilao_id = db.Column(db.Integer, db.ForeignKey('leilao.id'), nullable=False)

class TipoProduto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eletronico_veiculo = db.Column(db.Enum('Eletrônico', 'Veículo'), name='tipo_produto_enum')
    descricao = db.Column(db.String(50), nullable=False)
