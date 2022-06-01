import os

#Identifica o diretório base da aplicação
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    """
    Esta classe aramazena as configuracoe gerais da app.
    Attributes:
        SECRET_KEY: Chave secreta
        DEBUG: Determina o modo em qual a aplicação flask irá rodar, na prática se vai ou não gerar logs de depuração
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'coletor_rssi')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class ConfigDesenvolvimento(Config):
    """
    Esta classe recebe herança da classe config e diz respeito as configuracoes no contexto de desenvolvimento.
    Attributes:
        DEBUG: assinalada True no contexto de desenvolvimento para habilitar a geração de logs
        SQLALCHEMY_DATABASE_URI : endereço do banco de dados, no caso da base de desenvolvimento
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'des_coletor_rssi.db')

class ConfigTeste(Config):
    """
    Esta classe recebe herança da classe config e diz respeito as configuracoes no contexto de teste.
    Attributes:
        DEBUG: assinalada True no contexto de teste para habilitar a geração de logs
        SQLALCHEMY_DATABASE_URI : endereço do banco de dados, no caso da base de desenvolvimento
        PRESERVE_CONTEXT_ON_EXCEPTION: Não apresentar o contexto da solicitação de uma exceção 
        SQLALCHEMY_TRACK_MODIFICATIONS: responsável por rastrear alterações em objetos no banco e emitir um sinal se setada pra True
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test_coletor_rssi.db')

class ProductionTeste(Config):
    """
    Esta classe recebe herança da classe config e diz respeito as configuracoes no contexto de teste.
    Attributes:
        DEBUG: assinalada True no contexto de teste para habilitar a geração de logs
        SQLALCHEMY_DATABASE_URI : endereço do banco de dados, no caso da base de desenvolvimento
        PRESERVE_CONTEXT_ON_EXCEPTION: Não apresentar o contexto da solicitação de uma exceção 
        SQLALCHEMY_TRACK_MODIFICATIONS: responsável por rastrear alterações em objetos no banco e emitir um sinal se setada pra True
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'prod_coletor_rssi.db')

config_por_nome = dict(
    dev=ConfigDesenvolvimento,
    test=ConfigTeste,
    prod=ProductionTeste
)

key = Config.SECRET_KEY


