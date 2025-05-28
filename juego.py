#Preguntar por la respuesta número 1.
RES1 = input("Estas en un bosque oscuro al amanecer, dos caminos se abren ante ti: Un camino oscuro y estrecho y un camino con espesa niebla donde el terreno parece humedo y resbaladizo. ¿Vas por el camino OSCURO o el camino HUMEDO? ")

#Convertir respuesta número 1 a mayusculas para que sea legible.
RES1 = RES1.upper()

#Configurar variantes en la respuesta 1.
if RES1 == "OSCURO" :
	RES2 = input("Te encuentras con un puente de piedra, donde un anciano te ofrece un acertijo: Si adivinas correctamente, te llevaré a un gran tesoro. ¿ADIVINAS el acertijo o IGNORAS y regresas por el camino? ")
elif RES1 == "HUMEDO" :
	RES2 = input("El sendero te lleva a una cueva oscura. En su interior, una figura fantasmal aparece y te ofrece tres puertas: Una puerta DORADA que brilla con luz cálida, una puerta PLATEADA cubierta de extrañas inscripciones, una puerta de HIERRO oxidada pero con una energia misteriosa. ¿Cual eliges?: ")
else :
	print("Respuesta inválida.")

#Convertir respuesta número 2  a mayusculas para que sea legible.
RES2 = RES2.upper()

#Configurar variantes en la respuesta 2
if RES2 == "ADIVINAS":
	RES3 = input("Llegas a un claro donde una gran torre se alza ante ti. La entrada está custodiada por un guardián imponente. El guardián te ofrece tres desafíos: Un COMBATE fisico contra el, resolver un complicado ROMPECABEZAS, RETIRARTE sin intentar ¿Que eliges? ")
elif RES2 == "DORADA":
	RES3 =input("La puerta te lleva a un jardín escondido, lleno de criaturas fantásticas. Una de ellas, una mariposa gigante, te ofrece un regalo mágico. Pero hay un precio: perder algo valioso. ¿ACEPTAR el regalo y arriesgarte o RECHAZAR y seguir explorando el jardin? ")
elif RES2 == "PLATEADA":
	RES3 =input("Te encuentras en una biblioteca infinita, llena de libros antiguos. Un bibliotecario te ofrece un libro en particular: El destino de los perdidos. Solo puedes leerlo si decides: LEER el libro con la esperanza de entender tu futuro o IGNORARLO temiendo que cambie tu destino. ¿Que decides? ")
elif RES2 == "IGNORAS":
	RES3 = input("Decides dar la vuelta y el bosque se vuelve más oscuro. Te pierdes en un laberinto de árboles. En un claro, encuentras un rostro tallado en una roca. ¿Que haces? ¿TOCAS el rostro o BUSCAS otro camino?")
elif RES2 == "HIERRO":
	RES3 = input("Te adentras en un pasillo subterráneo y te aparece una criatura sombría que te ofrece poder a cambio de tu alma. ¿ACEPTAS o rechazas y tratas de ESCAPAR?")

#Convertir respuesta número 3 a mayusculas para que sea legible.
RES3 = RES3.upper()

#Configurar variantes en la respuesta 3.
if RES3 == "COMBATE":
	print("")