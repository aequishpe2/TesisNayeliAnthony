import pandas as pd
import re
import unicodedata
from nltk.corpus import stopwords

# Descargar stopwords si no están disponibles
import nltk
nltk.download('stopwords')

# Cargar el archivo CSV
def load_data(file_path):
    return pd.read_csv(file_path, encoding='utf-8')

# Función para limpiar texto
def clean_text(text):
    if isinstance(text, str):
        # Normalizar texto a forma 'NFD' y eliminar solo los acentos
        text = unicodedata.normalize('NFD', text)
        text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
        # Eliminar comillas dobles
        text = text.replace('"', '')
        # Eliminar caracteres no deseados
        text = re.sub(r'[^\w\s.,?!]', '', text)
        # Convertir a minúsculas
        text = text.strip().lower()
        # Eliminar stopwords
        stop_words = set(stopwords.words('spanish'))
        text = ' '.join(word for word in text.split() if word not in stop_words)
        return text
    return ""

# Eliminar columnas no deseadas
def drop_columns(data, columns):
    return data.drop(columns=columns, errors='ignore')

# Aplicar limpieza al texto y reemplazar la columna existente
def clean_text_column(data, column_name):
    data[column_name] = data[column_name].apply(clean_text)
    return data

# Guardar el dataset limpio
def save_cleaned_data(data, output_path):
    data.to_csv(output_path, index=False)

# Ruta del archivo original y el archivo de salida
input_file = 'C:\Tesis\data\dataset_spanish (1).csv'
output_file = 'C:\Tesis\dataset_spanish1.csv'

# Pipeline ETL
data = load_data(input_file)
data = drop_columns(data, ['index', 'Date'])
data = clean_text_column(data, 'Text')
save_cleaned_data(data, output_file)

print(f"El dataset limpio ha sido guardado en: {output_file}")
