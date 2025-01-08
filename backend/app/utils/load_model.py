import joblib

# Cargar el modelo y el vectorizador
model = joblib.load("random_forest_model.pkl")
vectorizer = joblib.load("vectorizerRF.pkl")

# Lista de etiquetas
label_columns = [
    "insulto", "amenaza", "rumores_difamatorios", "comentarios_humillantes", "lenguaje_discriminatorio",
    "acoso_sexual", "manipulacion_emocional", "lenguaje_vulgar", "acoso_general", "redes_sociales",
    "suicidio_autolesion"
]
