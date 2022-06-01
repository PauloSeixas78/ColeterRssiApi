from flask import Blueprint

from main.controlllers.controller import criar_elemento, ler_elemento, atualizar_elemento, excluir_elemento

elemento_bp = Blueprint("elemento_bp", __name__)

elemento_bp.route("/criar", methods=["POST"])(criar_elemento)
elemento_bp.route("/<elemento_id>", methods=["GET"])(ler_elemento)
elemento_bp.route("/<elemento_id>", methods=["POST"])(atualizar_elemento)
elemento_bp.route("/<elemento_id>", methods=["DELETE"])(excluir_elemento)