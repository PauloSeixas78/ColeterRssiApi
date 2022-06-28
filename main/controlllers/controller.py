import json
import sys
from flask import render_template, redirect, url_for, request, abort,jsonify

from main.models.coletaDao import ColetaDao
from main.models.coleta import Coleta
from main.models.elementoDao import ElementoDao
from main.models.elemento import Elemento
from main.models import db
from datetime import datetime


def index():   
    return "<h1>API Coletor RSSI</h1>"

def criar_elemento():
    elementodao = ElementoDao(db)
    content_type = request.headers.get("Content-Type")
    if (content_type == "application/json"):
        data = request.json
        elemento = Elemento(descricao = data["descricao"],
                            mac = data["mac"],
                            orientacao = data["orientacao"],
                            posicao_x = data["posicao_x"],
                            posicao_y = data["posicao_y"],
                            posicao_z = data["posicao_z"]
                            )
        result = elementodao.criar(elemento)
        if result==True:
            response_object = {
                'status': 'success',
                'message': 'Elemento criado com sucesso'
            }
            return response_object
        else:
            response_object = {
                'status': 'fail',
                'message': 'Falha ao criar elemento'
            }
    return response_object

def ler_elemento(elemento_id):
    elementodao = ElementoDao(db)
    elemento = elementodao.ler(elemento_id) 
    elemento_json = elemento_to_json(elemento)    
    return elemento_json

def atualizar_elemento(elemento_id):
    elementodao = ElementoDao(db)
    content_type = request.headers.get("Content-Type")
    if (content_type == "application/json"):
        data = request.json
        elemento = Elemento(descricao = data["descricao"],
                            mac = data["mac"],
                            orientacao = data["orientacao"],
                            posicao_x = data["posicao_x"],
                            posicao_y = data["posicao_y"],
                            posicao_z = data["posicao_z"]
                            )
        result = elementodao.atualizar(elemento_id,elemento)
        if result==True:
            response_object = {
                'status': 'success',
                'message': 'Elemento atualizado com sucesso'
            }
            return response_object
        else:
            response_object = {
                'status': 'fail',
                'message': 'Falha ao atualizar elemento'
            }
    return response_object

def excluir_elemento(elemento_id):
    elementodao = ElementoDao(db)
    result = elementodao.excluir(elemento_id)
    if result==True:
            response_object = {
                'status': 'success',
                'message': 'Elemento excluído com sucesso'
            }
            return response_object
    else:
            response_object = {
                'status': 'fail',
                'message': 'Falha ao excluir elemento'
            }
            return response_object

def elemento_to_json(elemento):
    elemento_json={}
    elemento_json["descricao"] = elemento.descricao
    elemento_json["mac"] = elemento.mac
    elemento_json["orientacao"] = elemento.orientacao
    elemento_json["posicao_x"] = elemento.posicao_x
    elemento_json["posicao_y"] = elemento.posicao_y
    elemento_json["posicao_z"] = elemento.posicao_z
    return elemento_json


def criar_coleta():
    coletadao = ColetaDao(db)
    content_type = request.headers.get("Content-Type")
    if (content_type == "application/json"):
        data = request.json
        coleta = Coleta(rssi = data["rssi"],
                        orientacao = data["orientacao"],
                        timestamp = datetime.strptime(data['timestamp'],"%Y-%m-%d %H:%M:%S"),
                        ap_fonte = data["ap_fonte"],
                        xp = data["xp"]
                        )
        result = coletadao.criar(coleta)
        if result==True:
            response_object = {
                'status': 'success',
                'message': 'Coleta criada com sucesso'
            }
        else:
            response_object = {
                'status': 'fail',
                'message': 'Falha ao criar coleta'
            }
    return response_object

def ler_coleta(coleta_id):
    coletadao = ColetaDao(db)
    coleta = coletadao.ler(coleta_id) 
    coleta_json = coleta_to_json(coleta)    
    return coleta_json

def atualizar_coleta(coleta_id):
    coletadao = ColetaDao(db)
    content_type = request.headers.get("Content-Type")
    if (content_type == "application/json"):
        data = request.json
        coleta = Coleta(rssi = data["rssi"],
                        orientacao = data["orientacao"],
                        timestamp = datetime.strptime(data['timestamp'],"%Y-%m-%d %H:%M:%S"),
                        ap_fonte = data["ap_fonte"],
                        xp = data["xp"]
                        )
        result = coletadao.atualizar(coleta_id,coleta)
        if result==True:
            response_object = {
                'status': 'success',
                'message': 'Coleta atualizada com sucesso'
            }
            return response_object
        else:
            response_object = {
                'status': 'fail',
                'message': 'Falha ao atualizar coleta'
            }
    return response_object
    

def excluir_coleta(coleta_id):
    coletadao = ColetaDao(db)
    result = coletadao.excluir(coleta_id)
    if result==True:
            response_object = {
                'status': 'success',
                'message': 'Coleta excluída com sucesso'
            }
            return response_object
    else:
            response_object = {
                'status': 'fail',
                'message': 'Falha ao excluir coleta'
            }
            return response_object


def coleta_to_json(coleta):
    coleta_json={}
    coleta_json["rssi"] = coleta.rssi
    coleta_json["orientacao"] = coleta.orientacao
    coleta_json["timestamp"] = coleta.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    coleta_json["ap_fonte"] = coleta.ap_fonte
    coleta_json["xp"] = coleta.xp
    return coleta_json