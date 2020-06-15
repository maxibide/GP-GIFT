q_name = input("Ingrese el nombre de la pregunta: ")
q_encabeza = input("Ingrese el encabezado de la pregunta: ")
todas_ninguna = input('Desea agregar opciones del tipo "Todas/Ninguna es correcta" (s/n)')

with open('true.txt') as t:
    true_options = t.readlines()
with open('false.txt') as f:
    false_options = f.readlines()

if todas_ninguna != 's':

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
            
            if q_encabeza == "":
                o.write("Señale la opción <b>CORRECTA</b>:{\n")
            else:
                o.write(q_encabeza + "señale la opción <b>CORRECTA</b>:{\n")
        
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
            
            if q_encabeza == "":
                o.write("Señale la opción <b>INCORRECTA</b>:{\n")
            else:
                o.write(q_encabeza + "señale la opción <b>INCORRECTA</b>:{\n")
            for option in options:
                o.write(option)
            o.write('}\n\n')

else:

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
            
            if q_encabeza == "":
                o.write("Señale la opción <b>CORRECTA</b>:{\n")
            else:
                o.write(q_encabeza + "señale la opción <b>CORRECTA</b>:{\n")
        
            for option in options:
                o.write(option)
            
            o.write("~Todas son correctas.\n")
            o.write("~Ninguna es correcta.\n")  
            o.write('}\n\n')

    # Agrega la opción "Todas son correctas"
    with open('output.txt', 'a') as o:
        o.write("::" + q_name + chr(101) + "::")
        if q_encabeza == "":
           o.write("Señale la opción <b>CORRECTA</b>:{\n")
        else:
           o.write(q_encabeza + "señale la opción <b>CORRECTA</b>:{\n")
        for i in range(4):
            o.write("~" + true_options[i])
                
        o.write("=Todas son correctas.\n")
        o.write("~Ninguna es correcta.\n")  
        o.write('}\n\n')

    # Agrega la opción "Todas son correctas"
    with open('output.txt', 'a') as o:
        o.write("::" + q_name + chr(102) + "::")
        if q_encabeza == "":
            o.write("Señale la opción <b>CORRECTA</b>:{\n")
        else:
            o.write(q_encabeza + "señale la opción <b>CORRECTA</b>:{\n")
        for i in range(4):
            o.write("~" + false_options[i])
          
        o.write("~Todas son correctas.\n")
        o.write("=Ninguna es correcta.\n")  
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
            o.write("::" + q_name + chr(103 + x) + "::")
            
            if q_encabeza == "":
                o.write("Señale la opción <b>INCORRECTA</b>:{\n")
            else:
                o.write(q_encabeza + "señale la opción <b>INCORRECTA</b>:{\n")
            for option in options:
                o.write(option)
            
            o.write("~Todas son incorrectas.\n")
            o.write("~Ninguna es incorrecta.\n")  
            o.write('}\n\n')


    # Agrega la opción "Todas son incorrectas"
    with open('output.txt', 'a') as o:
        o.write("::" + q_name + chr(107) + "::")
        if q_encabeza == "":
            o.write("Señale la opción <b>INCORRECTA</b>:{\n")
        else:
            o.write(q_encabeza + "señale la opción <b>INCORRECTA</b>:{\n")
        for i in range(4):
            o.write("~" + false_options[i])
                
        o.write("=Todas son incorrectas.\n")
        o.write("~Ninguna es correcta.\n")  
        o.write('}\n\n')

    # Agrega la opción "Todas son correctas"
    with open('output.txt', 'a') as o:
        o.write("::" + q_name + chr(108) + "::")
        if q_encabeza == "":
            o.write("Señale la opción <b>INCORRECTA</b>:{\n")
        else:
            o.write(q_encabeza + "señale la opción <b>INCORRECTA</b>:{\n")
        for i in range(4):
            o.write("~" + true_options[i])
                
        o.write("~Todas son correctas.\n")
        o.write("=Ninguna es correcta.\n")  
        o.write('}\n\n')