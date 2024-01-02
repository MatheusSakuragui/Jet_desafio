class Config:
    FLASK_APP="run.py"
    FLASK_ENV="envBack"
    SECRET_KEY='secretkey'
    JWT_SECRET_KEY='jwtsecretkey'
    SQLALCHEMY_DATABASE_URI='sqlite:///leilao.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False