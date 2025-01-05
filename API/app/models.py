from app import db

class Prediccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    prediccion = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Prediccion {self.id}>"
