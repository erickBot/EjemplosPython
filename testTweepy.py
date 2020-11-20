#-*- coding: utf-8 -*-

import tweepy
import requests
import time
import datetime

#llaves api de la cuenta de twitter
consumer_key='XXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#inicia el modulo tweepy
api = tweepy.API(auth)

# Consulta los datos del sensor en la IP del esp32
response = requests.get('http://192.168.1.39:80')

# Setup del timestamp 
t = time.time()
timegood = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

# Convierte la respuesta del servidor de esp32 en un diccionario de Python
sensor_data = response.json()

temperature = sensor_data['variables']['temperature']
humidity = sensor_data['variables']['humidity']

#imprime ultimos tweet en la consola
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

#envia un tweet en mi cuenta
api.update_status('Soy un bot creado por Erick Pasache: \nLa temperatura en la Ciudad de Piura,Peru es: {} ℃ \nLa humedad es: {} %% RH \n{}  '.format(temperature, humidity, timegood))
