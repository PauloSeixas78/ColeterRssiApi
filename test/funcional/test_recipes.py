from urllib import response
import pytest
import json
from main import create_app
from main.models import db

@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app("test")
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
            yield testing_client

def test_home_page(test_client):
    resposta = test_client.get('/')
    assert resposta.status_code == 200
    assert b"API Coletor RSSI" in resposta.data


def test_adicionar_elemento(test_client):
    resposta = test_client.post('elemento/criar',
                                data = json.dumps({ 'descricao':"teste",
                                                    'mac':"00:01:02:03:04:05:06",
                                                    'orientacao':"horizontal",
                                                    'posicao_x':"0",
                                                    'posicao_y':"1",
                                                    'posicao_z':"2"
                                                }),
                                content_type="application/json")
    
    assert resposta.status_code == 200
    assert resposta.json["status"] == "success"
    assert resposta.json["message"] == 'Elemento criado com sucesso'


def test_ler_elemento(test_client):
    resposta = test_client.get('elemento/1')
    assert resposta.status_code == 200    
    data = json.loads(resposta.get_data())
    assert data['descricao'] == "teste"
    assert data['mac'] == "00:01:02:03:04:05:06"
    assert data['orientacao'] == "horizontal"
    assert data['posicao_x'] == 0.0
    assert data['posicao_y'] == 1.0
    assert data['posicao_z'] == 2.0

def test_atualizar_elemento(test_client):
    resposta = test_client.post('elemento/1',
                                data = json.dumps({ 'descricao':"teste_1",
                                                    'mac':"00:01:02:03:04:05:06",
                                                    'orientacao':"vertical",
                                                    'posicao_x':"2",
                                                    'posicao_y':"1",
                                                    'posicao_z':"0"
                                                }),
                                content_type="application/json")
    
    assert resposta.status_code == 200
    assert resposta.json["status"] == "success"
    assert resposta.json["message"] == 'Elemento atualizado com sucesso'


def test_excluir_elemento(test_client):
    resposta = test_client.delete('elemento/1')
    assert resposta.status_code == 200
    assert resposta.json["message"] == 'Elemento excluído com sucesso'    


def test_adicionar_coleta(test_client):
    resposta = test_client.post('coleta/criar',
                                data = json.dumps({ 'rssi':"-40",
                                                    'orientacao':"horizontal",
                                                    'timestamp':"2021-07-03 16:21:12",
                                                    'ap_fonte':"teste_1",
                                                    'xp':"teste_2"
                                                }),
                                content_type="application/json")
    
    assert resposta.status_code == 200
    assert resposta.json["status"] == "success"
    assert resposta.json["message"] == 'Coleta criada com sucesso'

def test_ler_coleta(test_client):
    resposta = test_client.get('coleta/1')
    assert resposta.status_code == 200    
    data = json.loads(resposta.get_data())
    assert data['rssi'] == -40
    assert data['orientacao'] == "horizontal"
    assert data['timestamp'] == "2021-07-03 16:21:12"
    assert data['ap_fonte'] == "teste_1"
    assert data['xp'] == "teste_2"

def test_atualizar_coleta(test_client):
    resposta = test_client.post('coleta/1',
                                data = json.dumps({ 'rssi':"-30",
                                                    'orientacao':"vertical",
                                                    'timestamp':"2021-07-05 16:21:12",
                                                    'ap_fonte':"teste_1",
                                                    'xp':"teste_2"
                                                }),
                                content_type="application/json")
    
    assert resposta.status_code == 200
    assert resposta.json["status"] == "success"
    assert resposta.json["message"] == 'Coleta atualizada com sucesso'

def test_excluir_coleta(test_client):
    resposta = test_client.delete('coleta/1')
    assert resposta.status_code == 200
    assert resposta.json["message"] == 'Coleta excluída com sucesso'  

