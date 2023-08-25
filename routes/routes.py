from flask import Blueprint
from controller.controller import index, create, insert,list,signup,login

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/create', methods=['GET'])(create)
blueprint.route('/insert', methods=['POST'])(insert)
blueprint.route('/list', methods=['GET'])(list)
blueprint.route('/signup', methods=['GET','POST'])(signup)
blueprint.route('/login', methods=['POST'])(login)
