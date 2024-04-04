import tkinter as tk 
from tkinter import *
from tkinter import messagebox 
from Tooltip import Tooltip
from CrearCliente import CrearCliente
from EliminarCliente import EliminarCliente
from ModificarCliente import ModificarCliente

class Menu():

    def abrir_crear_cliente(self):
        crear_cliente = CrearCliente(self.ventana)

    def abrir_eliminar_cliente(self):
        eliminar_cliente = EliminarCliente(self.ventana)

    def abrir_modificar_cliente(self):
        modificar_cliente = ModificarCliente(self.ventana)
    
        # Crear una nueva ventana para el Menú Principal
        # self.ventana.geometry("400x300")
    def __init__(self, loggin):
        self.ventana = tk.Toplevel(loggin)
        self.ventana.geometry("400x300")
        self.ventana.focus_set() #Esta función asigna el foco a la ventana secundaria
        self.ventana.title("Menu Principal")
        self.ventana.resizable(0,0)

        # Crear una barra de menú
        barra_menu = tk.Menu(self.ventana)
        self.ventana.config(menu=barra_menu)

        # Menú Gestionar Clientes
        gestionarc = tk.Menu(barra_menu)
        barra_menu.add_cascade(label="Gestionar Clientes", menu=gestionarc)

        # Opciones de la cascada
        gestionarc.add_command(label="Crear Cliente",  command=lambda: self.abrir_crear_cliente())
        gestionarc.add_command(label="Eliminar Cliente",  command=lambda: self.abrir_eliminar_cliente())
        gestionarc.add_command(label="Modificar Cliente",  command=lambda: self.abrir_modificar_cliente())

        Gestionarcu = tk.Menu(barra_menu)
        barra_menu.add_cascade(label="Gestionar Cuentas", menu=Gestionarcu)

        Gestionartra = tk.Menu(barra_menu)
        barra_menu.add_cascade(label="Gestionar Transacciones", menu=Gestionartra)
        
        ConsultarInf = tk.Menu(barra_menu)
        barra_menu.add_cascade(label="Consultar Informacion", menu=ConsultarInf)

        Salir = tk.Menu(barra_menu)
        barra_menu.add_cascade(label="Salir", menu=Salir)
    