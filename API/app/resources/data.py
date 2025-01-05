from flask_restful import Resource
from app.models import Prediccion

class DataList(Resource):
    def get(self):
        try:
            registros = Prediccion.query.all()
            result = [
                {"id": registro.id, "texto": registro.texto, "prediccion": eval(registro.prediccion)}
                for registro in registros
            ]
            return {"data": result}, 200
        except Exception as e:
            return {"error": str(e)}, 500
