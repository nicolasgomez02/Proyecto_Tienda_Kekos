

print("Estas en La Tienda Kekos")
menu=input("Que accion quiere hacer: comprar o vender \r\n")

artic="Sal"
artic1="Lentejas"
precio1= 500000
precio2= 700000

if menu in "comprar":
    print("Has seleccionado el modulo de comprar")
    dep= int(input("Para iniciar deposite un valor mayor de 300 mil pesos \r\n"))
    if dep >= 300000:
        input("por favor ingrese nombre y apellido: \r\n")
        input("Por favor digite su numero de documento: \r\n")
        input("por favor ingrese su edad \r\n")
        opcion= input("¿Quiere seguir comprando? \r\n")
    while opcion =="si":
        print("¿Que otros productos quiere?", "Porductos que hay disponibles", artic, "precio1","500000", artic1,"precio2", "700000")
        can= int(input("Sal \r\n"))
        can1= int(input("Lentejas \r\n"))
        opcion=input("¿Quiere seguir comprando? \r\n")
        break
    if opcion in "no":
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
        break




