#!/usr/bin/python
# -*- coding: utf-8 -*-

import soundcloud
import Auth

# create a client object with your app credentials
ID = Auth.oauth_login_soundcloud()

client = soundcloud.Client(client_id= ID)


#se define una funcion que devuelva una lista de los enlaces de streming.
#Le pasamos el string a buscar y una lista donde nos devolvera los titulos de las canciones.
#El contenido de las posiciones de ambas listas(nombre, y urls) coincidiran con el nombre del track y su enlace.
#si queremos que nos muestre solo las url de las canciones que se puedan descargar download = True
def Buscar_stream(busqueda,nombre,download = False):
	tracks = client.get('/tracks', q=busqueda, license='cc-by-sa')
	urls = []
	if(download == True):
		for track in tracks:
			if(track.downloadable == True):
				#debido a un error en la API de souncloud debemos formar el enlace volviendo a autentificar el cliente
				url = track.stream_url + "?client_id=" + ID
				#anadimos los enlaces y los nombres a las listas correspondientes
				urls.append(url)
				nombre.append(track.title)
	else:
		for track in tracks:
				#debido a un error en la API de souncloud debemos formar el enlace volviendo a autentificar el cliente
				url = track.stream_url + "?client_id=" + ID
				#anadimos los enlaces y los nombres a las listas correspondientes
				urls.append(url)
				nombre.append(track.title)

	return urls


#se define una funcion que devuelva una lista de los enlaces de descarga.
#Le pasamos el string a buscar y una lista donde nos devolvera los titulos de las canciones.
#El contenido de las posiciones de ambas listas(nombre, y descargas) coincidiran con el nombre del track y su enlace
def Buscar_Descargas(busqueda, nombre):
	tracks = client.get('/tracks', q=busqueda, license='cc-by-sa')
	descargas = []
	for track in tracks:
		if(track.downloadable == True):
			#debido a un error en la API de souncloud debemos formar el enlace volviendo a autentificar el cliente
			cancion_descarga = track.download_url + "?client_id=" + ID
			#anadimos los enlaces y los nombres a las listas correspondientes
			descargas.append(cancion_descarga)
			nombre.append(track.title)
	return descargas


