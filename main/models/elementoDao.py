from multiprocessing import synchronize
from main.models import elemento
from main.models.elemento import Elemento


class ElementoDao():
    def __init__(self,db):
        self.__db = db

    def criar(self, elemento):
        try:
            self.__db.session.add(elemento)
            self.__db.session.commit()
            return True
        except:
            return False

    def atualizar(self,id,elemento):
        try:
            self.__db.session.query(Elemento).filter(Elemento.id == id).update({  
                                                    Elemento.descricao: elemento.descricao,
                                                    Elemento.mac: elemento.mac,
                                                    Elemento.posicao_x: elemento.posicao_x,
                                                    Elemento.posicao_y: elemento.posicao_y,
                                                    Elemento.posicao_z: elemento.posicao_z
                                                    }
                                                    ,synchronize_session = False)
            self.__db.session.commit()
            return True
        except:
            return False

    def ler(self,id):
        try:
            elemento = self.__db.session.query(Elemento).filter(Elemento.id == id).first()
            return elemento           
        except:
            return None

    def ler_todas(self,id):
        try:
            return Elemento.session.query.all()
        except:
            return None

    def excluir(self,id):
        try:
            query = self.__db.session.query(Elemento).filter(Elemento.id == id).all()
            for elemento in query:
                self.__db.session.delete(elemento)
                self.__db.session.commit()
                return True
            return False
        except:
            return None