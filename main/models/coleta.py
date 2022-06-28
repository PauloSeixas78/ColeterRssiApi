
from main.models import db

class Coleta(db.Model):
    """
    Esta classe representa as medicoes de potencia de sinal nos pontos de teste ou referencia.
    Attributes:
        id (Integer): Este atributo e a chave primaria da tabela 
        rssi(String): Este atributo representa a potencia do sinal fornecido pelo ponto de acesso        
        orientacao (String): Este atributo representara a rotacao do celular horizontal ou vertical
        timestamp (Datetime): Este atributo representara o intante da coleta
        ap_fonte (Integer): Este atributo representara o indice do acesso point que fornece o RSSI
        xp (Integer): Este atributo represetara o indice o ponto de medicao (teste ou referencia) 
    """
    __tablename__ = "coletas"
    id = db.Column(db.Integer, primary_key = True)
    rssi = db.Column(db.Float)
    orientacao = db.Column(db.String)
    timestamp = db.Column(db.DateTime)
    ap_fonte = db.Column(db.Integer)
    xp = db.Column(db.Integer)


    def __init__(self, rssi, orientacao, timestamp, ap_fonte,xp) -> None:
        """
        Metodo de inicializaçao da tabela elementos
        Parametros:
            id (Integer): Este atributo e a chave primaria da tabela 
            rssi(String): Este atributo representa a potencia do sinal fornecido pelo ponto de acesso        
            orientacao (String): Este atributo representara a rotacao do celular horizontal ou vertical
            timestamp (Datetime): Este atributo representara o intante da coleta
            ap_fonte (Integer): Este atributo representara o indice do acesso point que fornece o RSSI
            xp (Integer): Este atributo represetara o indice o ponto de medicao (teste ou referencia)
        """
        self.rssi = rssi
        self.orientacao = orientacao
        self.timestamp = timestamp
        self.ap_fonte = ap_fonte
        self.xp = xp


