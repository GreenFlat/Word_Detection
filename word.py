# -*- coding: UTF-8 -*- 
import os
import sys
import tweepy
import hashlib

"""" Tokens de app twiiter """
ckey = 'ckey'
csecret = 'csecret'
atoken = 'atoken'
asecret = 'atoken'

""" Autenticación """
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

""" Leer un conjunto de tweets de un perfil especifico """
stuff = api.user_timeline(screen_name = 'joseppsarmcam', count = 100, include_rts = False)

""" Definición de variables de apoyo """
lista = []
diccionario = {}

""" Lectura de cada uno de los tweets y su decodificación caracterés no imprimibles """
for status in stuff:
    cad = status.text.encode(sys.stdout.encoding, errors='replace')
    lista += cad.split()
""" Eliminando cualquier palabra repetida en los tweets """
conjunto = set(lista)
lista = list(conjunto)

""" Creación del diccionario """
for element in lista:
    md5 = hashlib.md5(element)
    diccionario[element] = md5.hexdigest()

def main(str):
    palabras = diccionario.keys()
    for palabra in palabras:
        if diccionario[palabra] == str:
            print "El hash " + str + " corresponde a la palabra:\n" + palabra
            return
        else:
            continue
    return
            
""" Verificando que hay objeto en los diccionarios """
main(diccionario['hay'])