#Menu de la tienda
print("Estas en La Tienda Kekos")
menu=input("Que accion quiere hacer: comprar o vender \r\n")
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
        input("por favor ingrese nombre y apellido: \r\n")
        input("Por favor digite su numero de documento: \r\n")
        input("por favor ingrese su edad \r\n")
        compra=input("Cual de los productos desea llevar \r\n")
        if compra in "Sal":
            print("Empieza tu compra")
            can5= int(input("Sal \r\n"))
            def cant5():
                global can5
            cant5=  can5 + precio1 * 1.15
            canT1= cant5
            print(canT1)   
        if compra == "Lentejas":
            print("Empieza tu compra")
            can6= int(input("Lentejas \r\n"))
            def can6():
                global cant6
            cant6= can6 + precio2 * 1.15
            canT2= cant6 
            print(canT2)
    #Input para preguntarle al cliente si quiere seguir comprando.
    opcion= input("¿Quiere seguir comprando? \r\n")
    #El while lo coloque por si decia que "si" queria comprar entonces
    #colocara cuantas cantidades llevara.
    while opcion =="si":
        #El print que mostrara los productos disponibles. 
        print("¿Que otros productos quiere?", "Porductos que hay disponibles", artic, precio1,"500000", artic1,precio2,"700000")
        #Esta variables van ha almacenar las cantidades que pida el cliente.
        can= int(input("Sal \r\n"))
        can1= int(input("Lentejas \r\n"))
        opcion1=input("¿Quiere seguir comprando? \r\n")
        #La funcion del break es hacer que rompa el ciclo,
        # y que no sea repetitivo y pare el ciclo.
        break
    #Este if no coloque por si el cliente dice que no quiere comprar nada mas. 
    def cant(int):
        global can 
    if opcion == "no":
        cant= cant(int())*precio1
        cant1= can1*precio2
        canT= cant+cant1
        print(canT)
        print("Estas en La Tienda Kekos")
        menu=input("Que accion quiere hacer: comprar o vender \r\n")   

if menu in "vender":
    print("Has seleccionado el modulo de vender")
    dep2=int(input("Para inicar deposite un valor mayor a 1 millon de pesos \r\n"))
    while dep2 >= 1000000:
        input("por favor ingrese nombre y apellido: \r\n")
        input("por favor ingrese su numero de documento: \r\n")
        input("por favor ingrese su edad: \r\n")
        print("¿Que otros productos quiere?", "Porductos que hay disponibles", artic, "precio1","500000", artic1,"precio2", "700000")
        cant1=int(input("Sal\r\n"))
        cant2=int(input("Lentejas\r\n"))
        cant3= cant1*precio1
        cant4= cant2*precio2
        if cant3+cant4 > 1000000:
            total1=cant3+cant4-30000
            print(total1)
        print("¿Que desea vender? \r\n")
        venta= input("Lentejas \r\n")
        print("Tendra un descuento por esta venta")
        if venta in "si":
            ventat= can * 0.03
            ventaT= ventat

        if venta in "no":
            print("tendra un descuento por esta venta")
            venta1=input("Sal \r\n")
            ventat2= can1 * 0.03
            ventaT= ventat2
        break


















