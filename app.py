from flask import Flask
from config import Config
from extensions import db
from flask_migrate import Migrate
from routes import main
from models.user import User # important to import as it ensures User is recognized by the db. 
# If not imported flask-migrate wont detect it and no migration file will be created.

app = Flask(__name__) #create the Flask app instance

app.register_blueprint(main) #Load configurations

app.config.from_object(Config) #Register the blueprint

db.init_app(app) #Initialize SQLAlchemy with the app

migrate = Migrate(app, db) #Set up Flask-Migrate

# start the application
if __name__ == "__main__":
    app.run(debug=True)
