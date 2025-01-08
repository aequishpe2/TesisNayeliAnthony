# Archivo: app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

# Inicialización de la base de datos
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuración más permisiva de CORS para desarrollo
    CORS(app, resources={
        r"/*": {
            "origins": "*",
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization", "Accept"],
            "supports_credentials": True
        }
    })
    
    api = Api(app)

    # Configuración de la base de datos PostgreSQL
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:110101@localhost:5432/predicciones"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inicializar extensiones
    db.init_app(app)

    # Registrar recursos
    from app.resources.predict import Predict
    from app.resources.data import DataList

    api.add_resource(Predict, "/predict")
    api.add_resource(DataList, "/data")

    return app