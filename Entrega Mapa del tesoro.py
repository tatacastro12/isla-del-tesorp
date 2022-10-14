from time import sleep

#Anicialización del bucle infinito para re-ejecutar el codigo
while True:
   print("\n")
   print ("Bienvenido... ¿Quieres jugar un juego >:)?")
   print("-------------------------------------------------\n")
   sleep(2)
#Primera seleccion para elegir si jugar o no
   seleccion = int(input("Escribe el numero de tu seleccion\n  1. Si! >:) \n  2. No! >:(\n"))

   if seleccion == 1: #Si la seleccion es 1 se ejecuta el juego
    sleep(1)
    print("-------------------------------------------------\n")
    print("Que interesante...\n")
    print("-------------------------------------------------\n")
    sleep(2)
    print("Narrador: Te comienzas a adentrar en la isla (se escuchan pajaros de fondo mientras avanzas por la vegetación)")
    sleep(6)
    print("Narrador: Oh no te encontraste con 2 caminos, que conveniente no...?\n RAPIDO! elije a donde ir >:)\n")
    sleep(3)

    if seleccion == 2: #Si la eleccion es 2 rompe el codigo
        print("Entonces que haces aqui...")
        sleep(3)
        break

#Inicialización para tomar el camino
    camino1 = int(input(" 1. Derecha\n 2. Izquierda\n"))
        
    if camino1 == 1: #elejiste derecha
        sleep(1)
        print ("Caminas a la derecha.... !!OH NO, ENCONTRASTE UN AGUJERO!!\n")
        sleep(3)
        print ("Caes en el agujero y mueres")
        sleep(2)
        
    
    
    if camino1 == 2: #elejiste izquierda
        sleep(1)
        print("Caminas a la izquierda... Te encuentras con un lago!")
        sleep(3)
        print("-------------------------------------------------\n")

        #Seleccion de decision si nadar o no
        nadar = int(input("¿Quieres nadar?\n  1.Si\n  2.No\n"))

        if nadar == 1: #Elejiste nadar
            print("Comienzas a nadar con todas tus fuerzas!")
            sleep(3)
            print("Sales del agua bastante cansado.... (Se escuchan pisadas cerca)")
            sleep(3)
            print("!!ES UNA TRIBU!! (y no parecen muy felices...)\n Te comienzan a atacar")
            sleep(3)
            print("Aunque suplicaste no tuvieron piedad alguna... (Moristes)")
            sleep(5)
        
        elif nadar == 2: #elejiste rodear el lago
            sleep(1)
            print("-------------------------------------------------\n")
            print("Rodeas el lago y caminas por un buen rato hasta que de lejos ves unas puertas...\n")
            sleep(3)
            print("Encuentras 3 puertas gigantes\n -(pensamiento: sera que aqui vivian gigantes?) .....\n -(pensamiento) Se esta haciendo de noche, creo que deberia entrar a alguna puerta \"Se escuchan aullidos de fondo\"")
            print("-------------------------------------------------\n")
            sleep(6)

            #Decision sobre a que puerta entrar
            puertas = int(input("¿A cual puerta entraras?\n  1.Roja\n  2.Amarillo\n  3.Azul\n"))

            if puertas == 1: #Elejiste la puerta roja
                print("Entrando a la puerta Roja...")
                sleep(2)
                print("Sigues caminando luego de ingresar a la puerta roja...\n Deambulas en la oscuridad y resbalas por una rampa y curiosamente habia un hoyo en llamas!!!")
                print(5)
                print("Luego de unos alarmantes llantos por tu parte...\n Moristes")
    
            if puertas ==2: #Elejiste la puerta amarilla
                print("Entrando a la puerta Amarilla...")
                sleep(2)
                print("Caminas por un buen rato hasta que encuentras un castillo!! \n -Luego de decidirte te pusiste en marcha a explorarlo hasta que encontraste un tesoro!!!!\n  (pensamiento) ahora solo tengo que salir de aqui...\n")
                sleep(7)
                print("Ingresaste a una sala oculta y encontraste un Jet privado con un mayordomo :o\n ")
                sleep(3)
                print("Escapas de la isla!!! ")
                sleep(3)
                #Re-Ejecucion del juego
                replay = int(input("Juego terminado - gracias por jugar, ¿Deseas jugar otra vez?\n  1.Si\n  2.No"))

                if replay == 1:
                    print("")
                elif replay == 2:
                    break
            if puertas == 3: #Elejiste la puerta azul
                print("Entrando a la puerta azul")
                sleep(2)
                print("Escuchas aullidos pero aun asi decidiste avanzar...\n -Te topaste con una familia de lobos hambrientos e intentas correr por tu vida!!\n No pudiste escapar y luego de un intenso dolor moriste...")
                sleep(5)
                #Re-Ejecucion del juego
                replay1 =int(input("Juego terminado - gracias por jugar, ¿Deseas jugar otra vez?\n  1.Si\n  2.No"))

                if replay1 == 1:
                    print("")
                elif replay1 == 2:
                    break
    else: #Si el usuaio pone otro numero que no sea el 1 o 2 le tirara error y re ejecutara el codigo
        print("Selecciona una opción valida")