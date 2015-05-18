#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
#Importamos nuestra api que utiliza funciones de la api Soundcloud
import API_Soundcloud
#Importamos nuestra API personalizada con herramientas de la API de DropboxS
import API_dropbox

app = Flask(__name__)

"""
Autores:
David Blanco Fuentes
Oscar Delgado Miranda
Ildefonso de la Cruz Romero
Mighel Angen Perez Garcia

API principal de MusicApi.
Le damos funcionalidad para poder escuchar compartir descargar y hasta subir
a dropbox los remixes de nuestras caniones preferidas de Soundcloud.

"""

#Funciones para evitar error a la hora de buscar y no halla nada en el cruadro de busqueda
@app.route('/buscar/all/', methods=['POST'])
def Vacia_all():
	return render_template('busqueda_vacia.html')

@app.route('/buscar/stream/', methods=['POST'])
def Vacia_stream():
	return render_template('busqueda_vacia.html')


#Funcion que expone a modo de lista todas las cacniones que se puedan descargar, asi como
#el streaming de dicha cancion
@app.route('/buscar/all/<name>', methods=['POST'])
def Buscar(name):
	#En este caso ambas lista de nombres coincidiran en el contenido

	nombres_stream = []
	nombres_download = []
	#Se obtiene la URL necesaria para autentificarse en dropbox:
	url_dropbox = API_dropbox.Autorizar_dropbox()
	#Se obtienen las listas con las urls de stream y de descargas
	#y se modifican las listas con los nombres de los tracks correspondientes
	stream_urls = API_Soundcloud.Buscar_stream(name,nombres_stream,download = True)
	download_urls = API_Soundcloud.Buscar_Descargas(name,nombres_download)

	if( nombres_stream == []):	#EN CASO DE QUE NO SE ENCUENTREN RESULTADOS SE MUESTRA UN MENSAJE
		return render_template('Noencontrado.html')	
	else: #SI SE ENCUENTRA MOSTRAMOS EL HTML QUE CONTENDRA UNA LISTA DE LAS CANCIONES ASI COMO DE LA OPCION DE DESCARGA
		tam = len(nombres_stream)
		return render_template('busqueda.html', titulos=nombres_stream, enlaces_stream = stream_urls, enlaces_download = download_urls, tam_ = tam, auth_drop = url_dropbox)

#Funcion que expone a modo de lista SOLO el streaming de todas las canciones 
#que condicionan la busqueda. 
@app.route('/buscar/stream/<name>', methods=['POST'])
def Only_Stream(name):
	#lista de titulos de las caniones
	nombres = []
	#lista con los enlaces de streaming
	stream_urls = API_Soundcloud.Buscar_stream(name,nombres)
	if( nombres == []):	#En caso de que no se encuentren resultados mostramos un html diferente
		return render_template('Noencontrado.html')	
	else:		
		tam = len(nombres)
		return render_template('busqueda_stream.html', titulos=nombres, enlaces_stream = stream_urls,tam_ = tam)

#Funcion que sube a dropbox la musica descargada
#y llama a otro html en caso de que se suba con exito
@app.route('/guardar', methods= ['POST'])
def Guardar_dropbox():
	API_dropbox.Guardar_music()
	return render_template('Guardado.html')	


#Sitio principal de la pagina web
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)

