from multiprocessing import synchronize
from main.models.coleta import Coleta
from datetime import datetime


class ColetaDao:
    def __init__(self,db):
        self.__db = db        

    def criar(self,coleta):
        try:
            self.__db.session.add(coleta)
            self.__db.session.commit()
            return True
        except:
            raise
            return False

    def ler(self,id):
        try:
            coleta = self.__db.session.query(Coleta).filter(Coleta.id == id).first()
            return coleta           
        except:
            return None


    def ler_todas(self,id):
        try:
            return Coleta.session.query.all()
        except:
            return None

    def atualizar(self,id,coleta):
        try:
            self.__db.session.query(Coleta).filter(coleta.id == id).update({Coleta.rssi: coleta.rssi,
                                                                            Coleta.orientacao: coleta.orientacao,
                                                                            Coleta.timestamp: coleta.timestamp,
                                                                            Coleta.ap_fonte: coleta.ap_fonte,
                                                                            Coleta.xp: coleta.xp}
                                                                            ,synchronize_session = False)
            self.__db.session.commit()
            return True
        except:
            raise
            return False
    
    def excluir(self,id):
        try:
            coleta = self.__db.session.query(Coleta).filter(Coleta.id == id).first()
            self.__db.session.delete(coleta)
            self.__db.session.commit()
            return True
        except:
            raise
            return None


    


    


        



