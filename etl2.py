import pandas as pd
import re
from nltk.corpus import stopwords
import nltk


nltk.download('stopwords')
spanish_stopwords = set(stopwords.words('spanish'))

# Cargar el archivo de comentarios
file_path = 'C:\Tesis\data\comentarios5.csv'
comentarios_data = pd.read_csv(file_path)

# Eliminar filas con valores faltantes en 'texto' (columna clave para el análisis)
comentarios_data.dropna(subset=['Texto'], inplace=True)

# Define a function to clean the text data
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\n', ' ', text)  # Remove newlines
    text = re.sub(r'[^a-záéíóúüñ\s]', '', text)  # Remove special characters (including emojis)
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    words = text.split()
    words = [word for word in words if word not in spanish_stopwords]  # Remove stopwords
    return ' '.join(words)

comentarios_data['texto_limpio'] = comentarios_data['Texto'].apply(clean_text)

# Define el diccionario de categorías de ciberacoso
cyberbullying_categories = {
    'insulto': [
        'idiota', 'estúpido', 'tonto', 'imbécil', 'estúpida', 'perdedor',
        'inútil', 'fracasado', 'tonta', 'feo', 'fea', 'gordo', 'gorda',
        'baboso', 'babosa', 'malnacida'
    ],
    'amenaza': [
        'matar', 'lastimar', 'destruir', 'te voy a', 'te haré', 'te arrepentirás',
        'estás muerto', 'vas a pagar', 'golpearte', 'quemar', 'ahogar', 'acabar'
    ],
    'rumores_difamatorios': [
        'mentiroso', 'ladrona', 'ladrón', 'falso', 'falsa', 'infiel', 'zorra',
        'rata', 'golfa'
    ],
    'comentarios_humillantes': [
        'nadie te quiere', 'nadie te soporta', 'desagradable', 'despreciable',
        'patético', 'asqueroso', 'eres una vergüenza', 'desgracia', 'fracaso'
    ],
    'lenguaje_discriminatorio': [
        'maricón', 'puto', 'puta', 'negro', 'indio', 'homosexual', 'marica',
        'desviado', 'atrasado', 'especial'
    ],
    'acoso_sexual': [
        'perra', 'zorra', 'pervertido', 'fotos íntimas', 'enviar nudes',
        'tetas', 'fotos desnudas', 'nudes', 'chúpame', 'desnudos', 'porno', 'acoso'
    ],
    'manipulacion_emocional': [
        'no vales nada', 'no sirves', 'estás solo', 'no te quieren', 'no eres nada',
        'no eres importante', 'nadie te necesita', 'sin valor', 'sin importancia',
        'sin sentido', 'te odian', 'nadie te extrañará'
    ],
    'lenguaje_vulgar': [
        'mierda', 'cabrón', 'chingada', 'pendejo', 'pinche', 'culo', 'puto',
        'chupa', 'maldita', 'carajo', 'mamar','sapa'
    ],
    'acoso_general': [
        'burla', 'hostigar', 'molestar', 'atacar', 'intimidar', 'acosar',
        'amedrentar', 'hacer bullying', 'ofender', 'despreciar', 'discriminar',
        'humillar','matón'
    ],
    'redes_sociales': [
        'bloquear', 'reportar', 'eliminar', 'denunciar', 'unfollow', 'banear',
        'stalkear', 'hackear', 'troll', 'fake', 'catfish'
    ],
    'suicidio_autolesion': [
        'suicidarse', 'cortarse', 'morir', 'matarme', 'quiero morir', 'sin vida',
        'sin esperanza', 'cortarme las venas', 'nadie me extrañará', 'no quiero vivir',
        'quiero desaparecer'
    ]
}

# Eliminar la columna 'author' si existe
if 'author' in comentarios_data.columns:
    comentarios_data.drop(columns=['author'], inplace=True)

# Añadir columnas para cada categoría para indicar si se detectan palabras clave
for category, keywords in cyberbullying_categories.items():
    comentarios_data[category] = comentarios_data['texto_limpio'].apply(
        lambda text: any(keyword in text for keyword in keywords)
    )

# Guardar los datos transformados en un nuevo archivo CSV
output_path = 'C:\Tesis\dataset_transformed5.csv'
comentarios_data.to_csv(output_path, index=False)

print(f"Transformed data saved to {output_path}")