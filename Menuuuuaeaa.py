print("Bienvenido a tu carrito de compras.\n")

nombres = []
precios = []
	
while True:
	
	print("Selecciona una opcion\n")
	print("1. Añadir al carrito")
	print("2. Ver el carrito")
	print("3. Remover del carrito")
	print("4. Total del carrito")
	print("5. Salir del carrito")
	
	opcion = int(input("Ingresa una opcion: "))
	
	if opcion == 1 :
		print("Añadir al carrito\n")
		nombre = input("Ingresa el nombre del articulo: ")
		precio = int(input("Ingresa el precio del articulo: "))
		nombres.append(nombre)
		precios.append(precio)
		print(f"\nAgregaste {nombre} al carrito con el precio de {precio}\n")
	
	if opcion == 2 :
		print("Ver el carrito\n")
		for i in range(len(nombres)):
			print(f"{nombres[i]} : ${precios[i]}")
	
	if opcion == 3 :
		print("Eliminar del carrito\n")
		nombre = input("Ingresa el nombre del articulo: ")
		precio = int(input("Ingresa el precio del articulo: "))
		nombres.remove(nombre)
		precios.remove(precio)
	
	if opcion == 4 :
		print("Total del carrito\n")
		total = sum(precios)
		print(total)
	
	if opcion == 5 :
		print("Saliste del carrito")
		break