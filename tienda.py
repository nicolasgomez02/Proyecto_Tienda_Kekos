#Menu de la tienda
print("Estas en La Tienda Kekos")
menu=input("Que accion quiere hacer: comprar o vender o salirse \r\n")
#Variables de los productos de la tienda en este caso coloque dos
artic="Sal"
artic1="Lentejas"
precio1= 500000
precio2= 700000
#En primer lugar lo que hice fue hacer un if donde pudiera elegir 
# entre dos opciones que son comprar y vender.
if menu in "comprar":
    print("Has seleccionado el modulo de comprar")
    dep= int(input("Para iniciar deposite un valor mayor de 300 mil pesos \r\n"))
    #coloque un if aqui porque queria decirle que si el valor que deposia
    #es mayor o igual a 300 mil.
    if dep >= 300000:
        #Los inputs para que el cliente pueda ingresar los datos
        nom1=input("por favor ingrese nombre y apellido: \r\n")
        doc1=input("Por favor digite su numero de documento: \r\n")
        phon1=input("por favor ingrese su telefono: \r\n")
        email1=input("por favor ingrese su correo: \r\n")
        #Print de los productos disponiles.
        print("los productos que estan disponibles: \r\n", artic,"y",artic1)
        #input de que procutos quiere comprar.
        compra=input("Cual de los productos desea llevar \r\n")
        #condicion de si eligi "Sal"
        if compra in "Sal":
            #print que indica que la compra va a iniciar.
            print("Empieza tu compra")
            #variable de cantidad de productos.
            can5= int(input("Sal \r\n"))
            #Operacion al agregar del IVA con el producto "Sal". 
            cant7= precio1 / 1.15
            cant5= cant7 * 0.15
            canT1= cant5
            if cant5 > 1000000:
                total1=cant5-30000
            print(round(canT1))
            #Print de la informacion que hizo el cliente.
            print("Nombre cliente:", nom1 ,"\r\n", "Numero de documento:",doc1,"\r\n", "Telefono del cliente:",phon1,"\r\n", "Correo del cliente:",email1,"\r\n", "Cantidad total con IVA:", canT1,"\r\n" )   
            #Condicion de si eligi "Lentejas".
            if compra == "Lentejas":
                print("Empieza tu compra")
                #operacion al agregar del IVA con el producto "Lentejas".
                can6= int(input("Lentejas \r\n"))
                cant8= precio2 / 1.15
                cant6= cant8 * 0.15 
                canT2= cant6 
                if canT2 > 1000000:
                    total4=canT2-30000
                #Print con round, el round sirve para redondear o acomodar un numero decimal con muchos valores. 
                print(round(canT2))
                print("nombre cliente: ", nom1,"\r\n", "numero de documento:",doc1,"\r\n", "Telefono del cleinte:",phon1,"\r\n","Cantidad total con IVA:", canT2, "\r\n")
    #Variable con input para preguntarle al cliente si quiere seguir comprando.
    opcion= input("¿Quiere seguir comprando? \r\n")
    #El while lo coloque por si decia que "si" queria comprar entonces
    #colocara cuantas cantidades llevara.
    while opcion =="si":
        #El print que mostrara los productos disponibles. 
        print("¿Quiere pedir mas cantidades prodcutos?", "Porductos que hay disponibles", artic, precio1, artic1,precio2,)
        # las variables de las cantidades que quiere llevar.
        can= int(input("Sal \r\n"))
        can1= int(input("Lentejas \r\n"))
        #Variable con input para que el cliente pueda tomar una decision.
        opcion1=input("¿Quiere seguir comprando? \r\n")
        #Operacion para calcular el precio total de los productos.
        cant= can*precio1
        cant1= can1*precio2
        canT= cant+cant1
        if cant > 1000000:
            total1=cant-30000
        print(canT)
        #Condicion por si el cliente elige la opcion "si".
        if opcion1 == "si":
            #Imprime la informacion o el recibo.
            print("nombre cliente:", nom1, "\r\n", "numero de documento:",doc1,"\r\n", "Telefono del cliente:",phon1,"\r\n","Cantidad de productos extras comprados:", canT,"\r\n")     
        if opcion1 == "no":
            print("nombre cliente:", nom1, "\r\n", "numero de documento:",doc1,"\r\n", "Telefono del cliente:",phon1,"\r\n","Cantidad de productos extras comprados:", canT,"\r\n")
        #El break sirve para romper un ciclo, para que solo se repita una sola vez, osea ya cuando la condicion se cumple. 
        break
    while opcion in "no":
           print("Estas en La Tienda Kekos")
           menu1=input("Que accion quiere hacer: comprar o vender o salirse \r\n")
           if menu1 in "comprar":
               print("Has seleccionado el modulo de comprar")
               dep1= int(input("Para iniciar deposite un valor mayor de 300 mil pesos \r\n"))
               if dep1 >= 300000:
                   nom2=input("por favor ingrese nombre y apellido: \r\n")
                   doc2=input("Por favor digite su numero de documento: \r\n")
                   phon2=input("por favor ingrese su telefono \r\n")
                   email2=input("por favor ingrese su correo: \r\n")
                   print("los productos que estan disponibles: \r\n", artic, artic1)
                   compra1=input("Cual de los productos desea llevar \r\n")
                   if compra1 in "Sal":
                     print("Empieza tu compra")
                     can5= int(input("Sal \r\n"))
                     cant9= precio1 / 1.15
                     can5=  cant9 * 0.15
                     canT1= can5
                   if canT1 > 1000000:
                     total1=canT1-30000
                     print(round(canT1))
                     print("nombre cliente:", nom2, "\r\n", "numero de documento:",doc2, "\r\n", "Telefono del cleinte:",phon2, "\r\n", "Correo del cliente:",email2, "\r\n", "Cantidad total con IVA:", canT1, "\r\n")

                   if compra == "Lentejas":
                    print("Empieza tu compra")
                    can6= int(input("Lentejas \r\n"))
                    cant8= precio2 / 1.15
                    cant6= cant8 * 0.15 
                    canT2= cant6
                    if canT2 > 1000000:
                     total1=canT2-30000
                    print(round(canT2))
                    print("nombre cliente:", nom2,"\r\n", "numero de documento:",doc2,"\r\n", "Telefono del cleinte:",phon2,"\r\n", "Correo del cliente:",email2,"\r\n", "Cantidad total con IVA:","\r\n", canT2,"\r\n" )
                     
           else:
            print("Has seleccionado el modulo de vender")
            dep3=int(input("Para inicar deposite un valor mayor a 1 millon de pesos \r\n"))
            while dep3 >= 1000000:
                  nom3=input("por favor ingrese nombre y apellido: \r\n")
                  doc3=input("por favor ingrese su numero de documento: \r\n")
                  phon3=input("por favor ingrese su telefono: \r\n")
                  email3= input("por favor digite su email:\r\n")
                  print("¿Cuantos productos quiere vender?")
                  canti1=int(input("Sal\r\n"))
                  canti2=int(input("Lentejas\r\n"))
                  canti3= canti1*precio1
                  canti4= canti2*precio2
                  cant0= canti3 + canti4
                  Total2= can5 * 0.3
                  Total3= can5 - Total2
                  print("El descuento por esta venta es: ", Total3)
                  print("nombre cliente:", nom3,"\r\n", "numero de documento:",doc3,"\r\n", "Telefono del cliente:",phon3,"\r\n", "Correo del cliente:",email3,"\r\n", "venta con descuento:", Total3,"\r\n")  
                  break
        #Esta es la opcion de vender   
if menu in "vender":
    print("Has seleccionado el modulo de vender")
    dep2=int(input("Para inicar deposite un valor mayor a 1 millon de pesos \r\n"))
    while dep2 >= 1000000:
        nom=input("por favor ingrese nombre y apellido: \r\n")
        doc=input("por favor ingrese su numero de documento: \r\n")
        phon=input("por favor ingrese su telefono: \r\n")
        email=input("por favor ingrese su email:\r\n")
        print("¿Cuantos productos quiere vender?")
        cant1=int(input("Sal\r\n"))
        cant2=int(input("Lentejas\r\n"))
        cant3= cant1*precio1
        cant4= cant2*precio2
        if cant3+cant4 > 1000000:
            total1=cant3+cant4-30000
            Total= cant6 * 0.3
            Total4= cant6 - Total
            print("El descuento por esta venta es: ", Total4)
            print("nombre cliente:", nom,"\r\n", "numero de documento:",doc,"\r\n", "Telefono del cleinte:",phon,"\r\n", "Correo del cliente:",email,"\r\n", "venta con descuento:", Total4,"\r\n")
            break
else:
    print("Muchas gracias por estar en nuestra tienda y que vuelva muy pronto")

















