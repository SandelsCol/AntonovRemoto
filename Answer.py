print("Bienvenido a la aerolinea Delvalle Airlines")
nacional=1
intercontinental=2

vuelo=int(input("Digite 1 si su vuelo es nacional , digite 2 si su vuelo es intercontinental"))
kg=int(input("Digite el peso total en kilos del paquete"))

if vuelo==1:
    km=int(input("Digite la cantidad de kilometros del paquete"))
    pb=4500*kg + 4000*km
    print("El precio base es..",pb)
else:
    milla=int(input("Digite la distancia total en millas del paquete"))
    pb=4500*kg + 8000*milla
    print("El precio base es..",pb)    