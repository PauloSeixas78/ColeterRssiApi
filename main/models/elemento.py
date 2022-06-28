from main.models import db

class Elemento(db.Model):
    """
    Esta classe representa os elementos da rede como pontos de acesso (roteadores), referência ou testes.
    Attributes:
        id (Integer): Este atributo e a chave primaria da tabela 
        descricao(String): Este atributo e o nome que sera dado ao elemento da rede   
        mac(String): Este atributo e o endereco MAC do elemento da rede para evitar repetidores       
        posicao_x (Float): Este atributo representara a posicao x do ponto referencial a ser adotado
        posicao_y (Float): Este atributo representara a posicao y do ponto referencial a ser adotado
        posicao_z (Float): Este atributo representara a posicao z do ponto referencial a ser adotado

    """
    __tablename__ = "elementos"
    id = db.Column(db.Integer, primary_key = True)
    descricao = db.Column(db.String)
    mac = db.Column(db.String)
    orientacao = db.Column(db.String)
    posicao_x = db.Column(db.Float)
    posicao_y = db.Column(db.Float)
    posicao_z = db.Column(db.Float)

    def __init__(self,descricao,mac,orientacao,posicao_x,posicao_y,posicao_z) -> None:
        """
        Metodo de inicializaçao da tabela elementos
        Parametros:
        descricao(String): Este atributo e o nome que sera dado ao elemento da rede  
        mac(String): Este atributo e o endereco MAC do elemento da rede para evitar repetidores      
        posicao_x (Float): Este atributo representara a posicao x do ponto referencial a ser adotado
        posicao_y (Float): Este atributo representara a posicao y do ponto referencial a ser adotado
        posicao_z (Float): Este atributo representara a posicao z do ponto referencial a ser adotado
        """
        self.descricao = descricao
        self.mac = mac
        self.orientacao = orientacao
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.posicao_z = posicao_z

