#!/usr/bin/python3
# Genera informes en documentos HTML para resumir noticias en varios archivos para imprimir luego

def contenido(archivos:list) -> str:
    '''
        Aglutina en un texto único los textos
        de cada archivo nombrado en la lista que
        recibe como parámetro.
    '''

    contenidos = ''

    for archivo in archivos:

        archivo = open(archivo.__str__(), 'r')

        for linea in archivo.readlines():

            contenidos += linea

        archivo.close()

        contenidos += '\n\n'

    return contenidos

def hipertexto(texto:list) -> str:
    '''
        Obtiene texto con un formato HTML a partir
        de la lista con texto de titulos y texto de redaccion
    '''
    # Voy creando de a poco con respectivas etiquetas el documento de marcado
    pagina = '<!DOCTYPE html>\n\t<html lang = "es">\n\t\t<head>\n\t\t\t'

    pagina += '<meta viewport = "width = device-width, height = device-height, scale = 1" />\n\t\t\t'

    pagina += '<meta charset = "utf-8" />\n\t\t</head>\n\t\t'

    pagina += '<body margin = "0" padding = "0 auto" style = "font-size: 3em; display: inline-block; text-align: center;">\n\t\t\t'
    # Agrega listado de titulos en un bloque
    pagina += '<div>\n\t\t\t\t<p><b>' + texto[0].__str__() + '</b><hr />\n\t\t\t\t</p>'

    pagina += '\n\t\t\t</div>'

    pagina += '\n\t\t\t<div>'
    # Agrega texto con toda la redaccion
    pagina += '\n\t\t\t\t<p>' + texto[1].__str__() + '\n\t\t\t\t</p>\n\t\t\t</div>'

    pagina += '\n\t\t</body>'

    pagina += '\n\t</html>'

    return pagina

def generar(nombre:str, info:list):
    '''
        Escribe documento HTML con determinado nombre a partir de un
        texto.
    '''
    archivo = open(nombre.__str__(), 'w')

    archivo.write(hipertexto([nombre, contenido(info)]))

    archivo.close()
# Desde linea de comandos recibo archivos para generar en HTML el informe que unifica info de archivos
import sys

generar(f'{sys.argv[1].replace(".", "_").__str__()}.html', sys.argv[1::])
