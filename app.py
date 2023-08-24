from flask import Flask
from flask_migrate import Migrate
from routes.routes import blueprint
from models.models import db


def create_app():
    app = Flask(__name__,template_folder='templates')  # flask app object
    app.config.from_object('config')  # Configuring from Python Files

    db.init_app(app)
     # Initializing the database
    return app


app = create_app()  # Creating the app
# Registering the blueprint
app.register_blueprint(blueprint, url_prefix='/')
migrate = Migrate(app, db)  # Initializing the migration


if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)