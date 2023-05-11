def Agregar_Alumno():
    while True:
        try:
         n = int(input("Numero de alumnos a capturar: ")) #1.-Solicita el numero de alumnos a capturar equivalente al contador
         break 
        except ValueError:
            print('Debes introducir un número')
        

            contador = 0 

            avg = {} # 2.- Declara diccionario a utilizar {avg}

            while contador < n: #3.- Aplica condicionante de contador
                opcion = input("Agregar (1) o terminar (2): ") #4.- Indica opción de Agregar o terminar
                if opcion == '1': 
                    contador += 1 #5.- Bonanza al contador
                    # nombre = input("Nombre del Alumno ").capitalize() #6.- Declara y solicita variable nombre
                    while True:
                        nombre = input("Introduce el nombre del alumno: ").capitalize()
                        if nombre == "":
                            print("No has introducido un nombre")
                        else:
                            break
                    
                    while True:
                        try:
                            aux = int(input(f"Numero de calificaciónes a  capturar para {nombre}: "))#7.- Declara y Solicita la variable que es el numero de calificacione que capturara
                            break
                        except ValueError:
                            print('Debes introducir un número')
                    notes = []#9.- Declara lista para calificaciones
                    
                    for i in range(aux):#10.- Declara condición para el numero de calificaciones (aux) se tienen que aderir a la lista notes
                        notes.append(float(input(f'Calificación {i+1} de {aux} para {nombre}: ')))
                        i += 1
                        
                    avg[nombre] = sum(notes)/aux #11.- Declara que del diccionario {avg} ubique el índice o posición nombre y sume el valor de notas (notes) y lo divida entre el número de calificaciones
                    print(notes)
                    return avg
                elif opcion == '2':
                    break
                else :
                    print("Se ha ingresado una opción invalida")
                    
            def Impresion_Promedio(): 
                    
                print(avg)    
                for i in avg.keys(): #Declara condicion de que para cada posición o indice Nombre en las llaves del diccionario avg  se imprima los valores de avg para el valor previamente indicado en este caso nombre
                    print(f'Promedio para {i}: {avg[i]}')
