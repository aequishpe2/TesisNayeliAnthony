from __future__ import print_function
import tweepy
from pymongo import MongoClient
import csv
from datetime import datetime

# Conexión con MongoDB
cliente = MongoClient('127.0.0.1', 27017)
bd = cliente.twitter
tweets = bd.datos

# Llaves de acceso para la API de Twitter
consumer_key = 'NJYKtzK4EFc53YfEB0UEQ1ClN'
consumer_secret = '04gLCyNvQxfZsZZemnmLOTld5TQh1Iw48Xaqpjo0xLnegRPVqZ'
access_token = '1863449889608515584-rYzYyTjJ7CMQSB7UkxExpahwrGNCSt'
access_secret = 'LNSF1z4v0S0laJ3lrKm25InAGw8HTOP4irn0Mt65x9rmG'

# Nombre del archivo CSV donde se guardarán los tweets
output_file = 'tweets_dataset.csv'

# Crear el archivo CSV y escribir los encabezados
with open(output_file, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['idt', 'tweet', 'fecha_creacion'])  # Encabezados

# Clase personalizada heredando de tweepy.Stream
class MyStream(tweepy.Stream):
    def on_status(self, status):
        if not hasattr(status, 'retweeted_status'):  # Ignorar retweets
            try:
                # Manejar tweets extendidos
                tweet_text = status.extended_tweet['full_text'] if hasattr(status, 'extended_tweet') else status.text
                tweet = {
                    "idt": str(status.id),
                    "tweet": tweet_text,
                    "fecha_creacion": status.created_at
                }
                # Guardar en el archivo CSV
                with open(output_file, mode='a', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([tweet['idt'], tweet['tweet'], tweet['fecha_creacion']])
                print(f"Tweet guardado: {tweet}")
            except Exception as e:
                print(f"Error al guardar tweet: {e}")

    def on_error(self, status_code):
        print(f"Ha ocurrido un error: {repr(status_code)}")
        return False  # Detener el stream en caso de error grave

    def on_timeout(self):
        print("Timeout")
        return False  # Detener el stream en caso de timeout

# Autenticación en Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_secret)

# Crear y configurar el Stream
stream = MyStream(consumer_key, consumer_secret, access_token, access_secret)

# Iniciar el Stream con los filtros deseados
stream.filter(
    track=["babosa", "asco", "webon", "malo", "tonto", "estupido", "gay", "estupida"],  # Palabras clave
    languages=['es']  # Idioma español
)
