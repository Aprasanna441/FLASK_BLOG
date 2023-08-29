from flask import Flask
from flask_migrate import Migrate
from routes.routes import blueprint
from models.models import db,User
from controller.controller import controllers


#flask db init to initialize migration

# flask db migrate -m "Initial migration."
# flask db upgrade

def create_app():
    app = Flask(__name__,template_folder='templates')  # flask app object
    app.config.from_object('config')  # Configuring from Python Files

    db.init_app(app)
     # Initializing the database
    return app


from flask_session import Session
from flask_login import LoginManager
login_manager = LoginManager()
app = create_app()  # Creating the app
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


login_manager.init_app(app)
login_manager.login_view = 'blueprint.login_signup' 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Registering the blueprint
app.register_blueprint(blueprint, url_prefix='/')
app.register_blueprint(controllers)

migrate = Migrate(app, db)  # Initializing the migration




if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)