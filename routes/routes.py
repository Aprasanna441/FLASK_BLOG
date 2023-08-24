from flask import Blueprint
from controller.controller import index, create, insert,list

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/create', methods=['GET'])(create)
blueprint.route('/insert', methods=['GET'])(insert)
blueprint.route('/list', methods=['GET'])(list)