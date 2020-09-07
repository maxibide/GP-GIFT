import sys


def crear_preguntas(nombre, correctas, incorrectas, encabezado, tipo, version):
    """Crear las preguntas a partir de un número de opciones verdaderas y falsas"""

    if len(correctas) != len(incorrectas):
        print("Es necesario que el número de opciones verdaderas sea igual al número de opciones falsas")
        sys.exit()

    for x in range(len(correctas)):
        opciones = []
        for i in range(len(correctas)):
            if i == x:
                opciones.append('=' + correctas[x])
            else:
                opciones.append('~' + incorrectas[i])

        grabar_preguntas(nombre, opciones, encabezado, tipo, version, x)


def grabar_preguntas(nombre, opciones, encabezado, tipo, version, numero):
    """Graba las preguntas en el archivo output.txt"""

    with open('output.txt', 'a') as o:
        o.write("::" + nombre + chr(version + numero) + "::")

        if encabezado == "":
            o.write(tipo)
        else:
            o.write(encabezado + " " + tipo)

        for opcion in opciones:
            o.write(opcion)

        o.write('}\n\n')


nombre = input("Ingrese el nombre de la pregunta: ")
encabezado = input("Ingrese el encabezado de la pregunta: ")

with open('true.txt') as t:
    verdaderas = t.readlines()
with open('false.txt') as f:
    falsas = f.readlines()

crear_preguntas(nombre, verdaderas, falsas, encabezado,
                "Señale la opción <b>CORRECTA</b>:{\n", 97)

crear_preguntas(nombre, falsas, verdaderas, encabezado,
                "Señale la opción <b>INCORRECTA</b>:{\n", 97 + len(verdaderas))

print("Se adjuntaron " + str(len(verdaderas) * 2) + " preguntas en el archivo output.txt")