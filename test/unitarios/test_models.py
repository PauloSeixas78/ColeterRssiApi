import pytest
from main.models.elementoDao import ElementoDao
from main.models.coletaDao import ColetaDao
from main.models.coleta import Coleta
from main.models.elemento import Elemento
from main.models import db


def test_nova_coleta():
    coleta = Coleta(-20,"horizontal","2021-07-03 16:21:12.357246",5,4)
    assert coleta.rssi == -20
    assert coleta.orientacao == "horizontal"
    assert coleta.timestamp == "2021-07-03 16:21:12.357246"
    assert coleta.ap_fonte == 5
    assert coleta.xp == 4

def test_novo_elemento():
    elemento = Elemento("Ponto_1","00-01-03-04-05-06","horizontal",0,1,2)
    assert elemento.descricao == "Ponto_1"
    assert elemento.mac == "00-01-03-04-05-06"
    assert elemento.orientacao == "horizontal"
    assert elemento.posicao_x == 0
    assert elemento.posicao_y == 1
    assert elemento.posicao_z == 2



