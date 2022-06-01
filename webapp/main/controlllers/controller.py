import sys
from flask import render_template, redirect, url_for, request, abort

from main.models.coleta import Coleta
from main.models.elemento import Elemento

from flask_sqlalchemy import SQLAlchemy

def index():
    return "ok"

def criar_coleta():
    return "ok + str(coleta_id)"

def ler_coleta(coleta_id):
    return "ok "+ str(coleta_id)

def atualizar_coleta():
    return "ok"

def excluir_coleta():
    return "ok"

def criar_elemento():
    return "ok"

def ler_elemento():
    return "ok"

def atualizar_elemento():
    return "ok"

def excluir_elemento():
    return "ok"