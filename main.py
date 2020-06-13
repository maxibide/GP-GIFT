q_name = input("Ingrese el nombre de la pregunta: ")

with open('true.txt') as t:
    true_options = t.readlines()
with open('false.txt') as f:
    false_options = f.readlines()

# Preguntas del tipo "señale la opción correcta"
for x in range(4):
    options = []
    for i in range(4):
        if i == x:
            options.append('=' + true_options[x])
        else:
            options.append('~' + false_options[i])
    
    with open('output.txt', 'a') as o:
        o.write("::" + q_name + chr(97 + x) + "::")
        o.write("Señale la opción CORRECTA:{\n")
        for option in options:
            o.write(option)
        o.write('}\n\n')

# Preguntas del tipo "señale la opción incorrecta"
for x in range(4):
    options = []
    for i in range(4):
        if i == x:
            options.append('=' + false_options[x])
        else:
            options.append('~' + true_options[i])

    with open('output.txt', 'a') as o:
        o.write("::" + q_name + chr(101 + x) + "::")
        o.write("Señale la opción INCORRECTA:{\n")
        for option in options:
            o.write(option)
        o.write('}\n\n')