from __future__ import print_function
import tweepy
import csv

# Llaves de autenticación de Twitter
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAB47xQEAAAAA8qZm7lpFRTkbPIxr2R7NI1DH2vg%3D3NjjeucE4rYdtK6QXImxS2X04i2i2RR0hqikaEQEMLsoGbWYAT'  # Reemplaza con tu token de autenticación

# Nombre del archivo CSV donde se guardarán los tweets
output_file = 'tweets_dataset.csv'

# Crear el archivo CSV y escribir los encabezados
with open(output_file, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['idt', 'tweet', 'fecha_creacion'])  # Encabezados

# Clase personalizada heredando de tweepy.StreamingClient
class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        try:
            # Guardar en el archivo CSV
            with open(output_file, mode='a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([tweet.id, tweet.text, tweet.created_at])
            print(f"Tweet guardado: ID={tweet.id}, Texto={tweet.text}")
        except Exception as e:
            print(f"Error al guardar tweet: {e}")

    def on_error(self, status_code):
        print(f"Ha ocurrido un error: {status_code}")
        return False  # Detener el stream en caso de error grave

# Crear y configurar el Stream
stream = MyStream(bearer_token)

# Configurar las reglas para el filtro
rules = [
    tweepy.StreamRule("babosa OR asco OR webon OR yape OR malo lang:es")  # Palabras clave y idioma
]
# Eliminar reglas existentes
existing_rules = stream.get_rules().data
if existing_rules:
    rule_ids = [rule.id for rule in existing_rules]
    stream.delete_rules(ids=rule_ids)

# Agregar nuevas reglas
stream.add_rules(rules)

# Iniciar el Stream
try:
    stream.filter()
except KeyboardInterrupt:
    print("Stream detenido manualmente.")
