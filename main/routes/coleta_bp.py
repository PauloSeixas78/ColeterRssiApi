from flask import Blueprint

from main.controlllers.controller import atualizar_coleta, criar_coleta, excluir_coleta, ler_coleta

coleta_bp = Blueprint("coleta_bp", __name__)

coleta_bp.route("/criar", methods=["POST"])(criar_coleta)
coleta_bp.route("/<int:coleta_id>", methods=["GET"])(ler_coleta)
coleta_bp.route("/<int:coleta_id>", methods=["POST"])(atualizar_coleta)
coleta_bp.route("/<int:coleta_id>", methods=["DELETE"])(excluir_coleta)