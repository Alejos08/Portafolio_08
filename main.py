import os
from data.datos import lista_menu
from programas.sumas import sumar2
from Juego.juegos import game_1

os.system("cls")

estado =True

while estado:
    print("+---------------------------------+")
    print("|Natalejos                       :>|")
    print("|                                 |")
    print(f"|[1]:  {lista_menu[0]}")
    print(f"|[2]:  {lista_menu[1]}")
    print(f"|[3]:  {lista_menu[2]}")
    print(f"|[4]:  {lista_menu[3]}")
    print(f"|[5]:  {lista_menu[4]}")
    print(f"|[0]: salir")

#Respuera el dato ingresado
    r = int(input("|[?]:"))

#pregunta si el dato ingresado es una de las opciones disponibles
    if r == 0:
        estado=False
    elif r == 1:
        sumar2()

    if r == 5:
        game_1()





 #limpiar la terminal
#os.system("cls")
    
    # codigo fuera del bucle, se ejecutan si el bucle deja de ser verdadero
print("[saliendo del programa...]")


 
