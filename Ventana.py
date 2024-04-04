import tkinter as tk
from tkinter import *
from tkinter import messagebox
from CrearCliente import CrearCliente
from EliminarCliente import EliminarCliente
from ModificarCliente import ModificarCliente
from Menu import Menu
from Tooltip import Tooltip

class Login():
    def mostrarAyuda(self, event):
        messagebox.showinfo("Ayuda", "Debe diligenciar todos los campos marcados con *\n luego presione el botón ingresar.")

    def validarIngreso(self):
        usuario = self.txtUsuario.get()
        contraseña = self.txtPassword.get()
        if usuario == "" or contraseña == "":
            messagebox.showerror("Error", "Por favor ingrese su usuario y contraseña.")
        else:
            if usuario == "nicolass" and contraseña == "12345678":
                miMenu = Menu(self.ventana)
                messagebox.showinfo("Éxito", f"Bienvenid@, {usuario}!")
                
            else:
                messagebox.showerror("Error", "Usuario y/o contraseña incorrectos")
    
    def validarUs(self, event):
        return True

    def validarPass(self, event):
        return True  

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("400x300")
        self.ventana.resizable(0,0)

        self.lblTitulo = tk.Label(self.ventana, text="Iniciar Sesión ")
        self.lblTitulo.place(relx=0.5,y=25,anchor='center')

        iconoAyuda = tk.PhotoImage(file= r"icons\help.png")
        self.btnAyuda =tk.Button(self.ventana, image= iconoAyuda)
        self.btnAyuda.place(relx=1, x=-45, y=18, width=25, height=25)
        Tooltip(self.btnAyuda, "Presione para obtener ayuda!\nAlt+a")
        self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)
        self.ventana.bind('<Alt-a>', self.mostrarAyuda)

        self.lblUsuario = tk.Label(self.ventana, text="Usuario*:")
        self.lblUsuario.place(x=62, y=80)

        self.lblPassword = tk.Label(self.ventana, text="Contraseña*:")
        self.lblPassword.place(x=40, y=160)

        self.txtUsuario = tk.Entry(self.ventana, width=25)
        self.txtUsuario.place(x=170, y=80)
        Tooltip(self.txtUsuario, "Ingrese su Usuario.\nPuede contener letras, números, puntos, signos, etc [a-z, 0-9, .]")
        self.txtUsuario.bind('<KeyRelease>', self.validarUs)

        self.txtPassword = tk.Entry(self.ventana, width=25, show="*")
        self.txtPassword.place(x=170, y=160)
        Tooltip(self.txtPassword, "Ingrese su Password.\nSolo letras, números y el punto [a-z, 0-9, .]")
        self.txtPassword.bind('<KeyRelease>', self.validarPass)

        self.txtPassword.bind("<KeyRelease>", self.validarLongitud)

        iconoRegistrar = tk.PhotoImage(file= r"icons\user_add.png")
        self.btnIngresar = tk.Button(self.ventana, text="Ingresar",image=iconoRegistrar, compound=LEFT, width=60, height=20, command=lambda: self.validarIngreso(), state="disabled")
        self.btnIngresar.place(x=100, y=250)

        iconoSalir = tk.PhotoImage(file= r"icons\cancel.png")
        self.btnSalir = tk.Button(self.ventana, text="Salir",image=iconoSalir, compound=LEFT, width=50, height=20, command=self.ventana.destroy)
        self.btnSalir.place(x=220, y=250)
        
        self.ventana.mainloop()

    def validarLongitud(self, event):
        Longitud = len(self.txtPassword.get())
        if Longitud >= 8:
            self.btnIngresar.configure(state="normal")


        else:
            self.btnIngresar.configure(state="disabled")

        

    