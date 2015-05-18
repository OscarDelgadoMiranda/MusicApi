#!/usr/bin/python
# -*- coding: utf-8 -*-
#IMportamos las API de dropbox y soundcloud
#que son las APIs que hemos enlazado
import soundcloud
import dropbox

#Apartamos en otro fichero aparte las contraseñas tanto de soundcloud y dropbox
def oauth_login_soundcloud():
	ID = '5db6a183fe52f30d9df1399d6802bc97'
	return ID

def oauth_login_dropbox(lista):
	lista.append('dtjqo38ewt3zs30')  #app_key
	lista.append('raco98mwk35w5ox')  #app_secret
	lista.append('app_folder')  #app_type
	return lista
