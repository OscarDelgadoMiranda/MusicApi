# Include the Dropbox SDK
import dropbox
from dropbox import client,session,rest
import Auth
#necesario para moverse entre directorios del PC
import os
import getpass
# Get your app key and secret from the Dropbox developer website

#Obtenemos las keys necesarias para iniciar sesion en dropbox
auth = []
auth = Auth.oauth_login_dropbox(auth)
sesion = session.DropboxSession(auth[0], auth[1], auth[2])

#Generamos un token con la sesion anterior
request_token = sesion.obtain_request_token()

#funcion que genera la URL para autentificar el usuario
def Autorizar_dropbox():
	#Pasamos request_token como parametro para construir una url
	#que se utiliza para autentificar al usuario
	url = sesion.build_authorize_url(request_token)
	return url 

#Construimos una funcion para guardar toda la musica que se halla descargado
def Guardar_music():
	# Validamos el token
	access_token = sesion.obtain_access_token(request_token)
	#creamos cliente
	cliente = client.DropboxClient(sesion)
	#Obtenemos el nombre de la carpeta personal para contruir la ruta
	nombre_usuario = getpass.getuser()
	#construimos la ruta
	path = '/home/'+nombre_usuario+'/Downloads/'
	#En caso de que la ruta no coincida con la version inglesa usamos la version en espanol
	if not os.path.isdir(path):
		path = path = '/home/'+nombre_usuario+'/Descargas/'

	#Nos preparamos para recorrer losficheros en busca de la musica
	musica = []
	ficheros = []
	ficheros = os.walk(path)
	print path
	for root, dirs, files in ficheros:
		for fichero in files:
			(nombreFichero, extension) = os.path.splitext(fichero)
			if(extension == ".mp3" or extension ==".wav"):
				musica.append(nombreFichero+extension)
	
	#recorremos los tracks encontrados para subirlo a dropbox
	for track in musica:	
		f = open(path+track, 'rb')
		response = cliente.put_file('/Music/'+track, f , overwrite=True)
