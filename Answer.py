print("Bienvenido a la aerolinea Delvalle Airlines")

nacional=1
intercontinental=2

vuelo=int(input("Digite 1 si su vuelo es nacional , digite 2 si su vuelo es intercontinental"))
kg=int(input("Digite el peso total en kilos del paquete"))
km=int(input("Digite la cantidad de kilometros del paquete"))

cont=0
cm=237500

while (cont<cm):
    cont= kg + cont
    print("La aeronave tiene un peso total(En carga) de..",cont)

    if kg >= 10:
        if vuelo==1:
            if kg>100:
                desc=(4500*kg + 4000*km)*0.15
                pb=4500*kg + 4000*km - desc
                print("El precio base de su envio nacional con su descuento es",pb,"pesos")
            else:
                pb=4500*kg + 4000*km
                print("El precio base de su envio nacional es..",pb,"pesos")
        else:
            if km>8000 and kg>400:
                desc=(4500*kg + 8000*(0.621371*km))*0.10
                pb=4500*kg + 8000*(0.621371*km) - desc
                print("El precio base de su envio intercontiental con descuento es",pb,"pesos")
            else:
                pb=4500*kg + 8000*(0.621371*km)
                print("El precio base de su envio intercontinental es..",pb,"pesos")                                         
    else:
        print("No aceptamos paquetes de menos de 10kg")    

print("El avion ya no soporta mas")             