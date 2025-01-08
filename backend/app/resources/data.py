from flask_restful import Resource
from app.models import Prediccion

class DataList(Resource):
    def get(self):
        try:
            registros = Prediccion.query.all()
            result = []
            for registro in registros:
                try:
                    result.append({
                        "id": registro.id,
                        "texto": registro.texto,
                        "prediccion": eval(registro.prediccion) if isinstance(registro.prediccion, str) else registro.prediccion
                    })
                except Exception as e:
                    print(f"Error procesando registro {registro.id}: {str(e)}")
                    continue
            
            return {"data": result}, 200
        except Exception as e:
            return {"error": str(e)}, 500
