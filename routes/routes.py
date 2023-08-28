from flask import Blueprint
from controller.controller import index, create, insert,list,signup,login,login_signup,error,dashboard
from controller.controller import logout,create_blog,blogfeed
blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/create', methods=['GET'])(create)
blueprint.route('/insert', methods=['POST'])(insert)
blueprint.route('/list', methods=['GET'])(list)
blueprint.route('/signup', methods=['POST'])(signup)
blueprint.route('/login', methods=['POST'])(login)
blueprint.route('/login_signup', methods=['GET'])(login_signup)
blueprint.route('/*', methods=['GET'])(error)
blueprint.route('/logout', methods=['GET'])(logout)
blueprint.route('/dashboard', methods=['GET'])(dashboard)
blueprint.route('/create_blog', methods=['GET','POST'])(create_blog)
blueprint.route('/blog_feed', methods=['GET'])(blogfeed)



