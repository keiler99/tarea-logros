dia = input("Introduce un día: ")

semana = "Lunes", "Martes", "Miercoles", "Jueves", "Viernes"
finde = "Sabado" , "Domingo" 

if dia in semana : print("Día de semana")
elif dia in finde : print("Fin de semana")
else : print("Inválido")