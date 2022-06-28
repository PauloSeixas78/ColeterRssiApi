from flask import Blueprint

from main.controlllers.controller import index

index_main = Blueprint("", __name__)

index_main.route("/", methods=["GET"])(index)