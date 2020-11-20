#-*-coding: utf-8-*-
import os

def menu():
    print("*******************Bienvenido al Menu de Opciones*********************")
    print("1. Categorias")
    print("2. Productos")
    print("3. Clientes")
    print("4. Salir")
    print("***********************************************************************")
    print()
    num = int(input("Indica una opcion: "))

    if num == 1 :
        Categorias() 
    elif num == 2:
        Productos()
    elif num == 3:
        Clientes()
    elif num == 4:
        Salir()

def Categorias():
    print("*****************Bienvenido a la Opcion de Categorias******************")
    print("1. Limpieza")
    print("2. Cocina")
    print("3. Juguetes")
    print("4. Salir")
    print("***********************************************************************")
    file = open("categorias.txt", "w")
    file.write("Opcion de categorias abierto.\n")
    file.close()
    num2 = int(input("Indica una opcion: "))

    if num2 == 4:
        menu()

def Productos():
    print("*****************Bienvenido a la Opcion de Productos******************")
    print("1. Cervezas")
    print("2. Ropa")
    print("3. Vinos")
    print("4. Salir")
    print("***********************************************************************")
    file = open("productos.txt", "w")
    file.write("Opcion de productos abierto.\n")
    file.close()
    num3 = int(input("Indica una opcion: "))

    if num3 == 4:
        menu()

def Clientes():
    print("*****************Bienvenido a la Opcion de Clientes******************")
    print("1. Juan Lopez")
    print("2. Marina Garcia")
    print("3. Jose Manrique")
    print("4. Salir")
    print("***********************************************************************")
    file = open("clientes.txt", "w")
    file.write("Opcion de clientes abierto.\n")
    file.close()
    num4 = int(input("Indica una opcion: "))

    if num4 == 4:
        menu()

def Salir():
    print("Gracias por visitarnos")
    exit()

if __name__ == "__main__":
    menu()