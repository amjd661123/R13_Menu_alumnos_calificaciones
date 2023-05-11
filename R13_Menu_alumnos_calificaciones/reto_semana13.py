# 1 Establecer menu
import adicionalumno as ad


print('''
Para agregar un alumno presiona 1
Para ver la los alunos y sus calificaciones presiona 2 
Para salir presiona "s"
''')
opcion = input("Por favor ingrese la opción deseada: ")

while True:
  
        if opcion == "1":
         ad.Agregar_Alumno()
            
        elif opcion == "2":
            print(ad.Agregar_Alumno)  
            
        while opcion == "s":
            opcion == input(print("Esta seguro de querer termianr el programa responder s/n: "))
            if opcion == "s":
                print("has elegido terminar el programa")
                
        else:
            opción = input("Porfavor Ingresa un 1, 2 o s: ") 
