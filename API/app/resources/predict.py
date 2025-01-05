from flask_restful import Resource
from flask import request
from app import db
from app.models import Prediccion
from app.utils.load_model import model, vectorizer, label_columns
import pandas as pd

class Predict(Resource):
    def post(self):
        try:
            # Obtener los datos de la solicitud
            data = request.json
            if "texto" not in data:
                return {"error": "Falta el campo 'texto' en la solicitud"}, 400
            
            texto = data["texto"]

            # Procesar el texto
            texto_vectorizado = vectorizer.transform([texto])
            prediccion = model.predict(texto_vectorizado)

            # Convertir la predicción en un formato legible
            prediccion_df = pd.DataFrame(prediccion, columns=label_columns)
            prediccion_dict = prediccion_df.iloc[0].to_dict()

            # Guardar en la base de datos
            nueva_prediccion = Prediccion(texto=texto, prediccion=str(prediccion_dict))
            db.session.add(nueva_prediccion)
            db.session.commit()

            return {"texto": texto, "prediccion": prediccion_dict}, 200
        except Exception as e:
            return {"error": str(e)}, 500
