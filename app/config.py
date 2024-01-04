class Config:
    FLASK_APP="run.py"
    FLASK_ENV="env"
    SECRET_KEY='secretkey'
    JWT_SECRET_KEY='jwtsecretkey'
    JWT_ACESS_TOKEN_EXPIRES=3600
    SQLALCHEMY_DATABASE_URI='sqlite:///leilao.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False