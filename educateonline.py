contprog=0
contbsd=0
controb=0
contdscto=0
contsindscto=0
print("**********************************************************")
print("Bienvenido a EDUCATE-ONLINE")
print("El portal de cursos educativos online")
print("**********************************************************")
nombre=(input("Porfavor, indique su nombre: "))
print("**********************************************************")
rut=(input("Porfavor, indique su rut o n° de identificacion: "))
print("**********************************************************")
print("Buenas tardes estimado sr/a. "+str(nombre))
cursos=["PROGRAMACION","BASE DE DATOS","ROBOTICA"]
print("Los cursos que tenemos disponibles en EDUCATE-ONLINE son: "+str(cursos))
print("**********************************************************")

eleccion=(input("¿Cual curso desea aprender?: "))
valorprog=250000
valorbsd=310000
valorrobotica=280000

print("**********************************************************")
if eleccion == 'programacion':
    print("Usted debera pagar por este curso un total de: "+str(valorprog))
    contprog+=1

elif eleccion == 'base de datos':
    print("Usted debera pagar por este curso un total de: "+str(valorbsd))
    contbsd+=1

elif eleccion == 'robotica':
    print("Usted debera pagar por este curso un total de: "+str(valorrobotica))
    controb+=1

else:
    print("La sentencia que ingreso no es valida, vuelva a intentarlo")
print("**********************************************************")

dscto=input("¿Usted posee algun codigo de descuento?: ")
if dscto=='si':
    codigo=input("¿Cual es el codigo de descuento?: ")
    if codigo == 'EDUCATE-ONLINE':
        print("***************************************************")
        contdscto+=1
        if eleccion == 'programacion':
            dsctoprog=(valorprog*20)/100
            vfinalprog=valorprog-dsctoprog
            print("El valor final del curso de programacion es: ",(vfinalprog))

        elif eleccion == 'base de datos':
            dsctobsd=(valorbsd*20)/100
            vfinalbsd=valorbsd-dsctobsd
            print("El valor final del curso de base de datos es: ",(vfinalbsd))

        elif eleccion == 'robotica':
            dsctorob=(valorrobotica*20)/100
            vfinalrob=valorrobotica-dsctorob
            print("El valor final del curso de robotica es: ",(vfinalrob))
    else:
        print("**********************************************************")
        print("El codigo que ingreso no es valido")
if dscto=='no':
    print("Los valores de cada curso se mantienen")
    contsindscto+=1
print("------------------------------")
print("EL REGISTRO DEL CURSO SE HA REALIZADO EXITOSAMENTE")
print("------------------------------")
print("Su nombre es: "+nombre)
print("------------------------------")
print("Su rut o n° identificador es: "+rut)
print("------------------------------")
if dscto == 'si':
    print (contdscto, "curso con descuento fue asignado")
    print("------------------------------")
    if eleccion == 'programacion':
        print(contprog," Curso de programacion inscrito")
        print("El total que debera pagar por este curso es: "+str(float(vfinalprog)))

    elif eleccion == 'base de datos':
        print(contbsd," Curso de base de datos inscrito")
        print("El total que debera pagar por este curso es: "+str(float(vfinalbsd)))

    elif eleccion == 'robotica':
            print(controb," Curso de robotica inscrito")
            print("El total que debera pagar por este curso es: "+str(float(vfinalrob)))
        
if dscto == 'no':
    print (contsindscto, "curso sin descuento fue asignado")
    print("------------------------------")
    if eleccion == 'programacion':
        print(contprog," Curso de programacion inscrito")
        print("El total que debera pagar por este curso es: "+str(float(valorprog)))

    elif eleccion == 'base de datos':
        print(contbsd," Curso de base de datos inscrito")
        print("El total que debera pagar por este curso es: "+str(float(valorbsd)))
        
    elif eleccion == 'robotica':
            print(controb," Curso de robotica inscrito")
            print("El total que debera pagar por este curso es: "+str(float(valorrobotica)))

print("------------------------------")
print("MUCHAS GRACIAS POR PREFERIR EDUCATE ONLINE, HASTA LUEGO")
print("------------------------------")