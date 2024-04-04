import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip 

class EliminarCliente():
    def mostrarAyuda(self, event):
        messagebox.showinfo("Ayuda", "Debe diligenciar todos los campos marcados con *\n luego presione el botón ingresar.")

    def validarCedula(self, event):
        caracter = event.keysym 
        if(caracter.isdigit()): 
            self.txtCedula.config(bg="#FFFFFF") 
        else:
            if(event.keysym != "BackSpace"): 
                self.txtCedula.delete(len(self.txtCedula.get())-1, END) 
            
        if(len(self.txtNombre.get()) >= 8 and len(self.txtCedula.get()) >= 8):  
            self.btnAgregar.config(state="normal")  
        else:
            self.btnAgregar.config(state="disabled") 

    def validarNombre(self, event):
        caracter = event.keysym  
        if(caracter.isalpha()):  
            self.txtNombre.config(bg="#FFFFFF")  
        else:
            if(event.keysym != "BackSpace"):  
                self.txtNombre.delete(len(self.txtNombre.get())-1, END) 
            
        if(len(self.txtNombre.get()) >= 8 and len(self.txtCedula.get()) >= 8): 
            self.btnAgregar.config(state="normal")  
        else:
            self.btnAgregar.config(state="disabled") 

    def validarApellido(self, event):
        caracter = event.keysym  
        if(caracter.isalpha()):  
            self.txtApellido.config(bg="#FFFFFF")  
        else:
            if(event.keysym != "BackSpace"):  
                self.txtApellido.delete(len(self.txtApellido.get())-1, END) 
            
        if(len(self.txtApellido.get()) >= 8 and len(self.txtTelefono.get()) >= 10): 
            self.btnAgregar.config(state="normal")  
        else:
            self.btnAgregar.config(state="disabled")

    def validarTelefono(self, event):
        caracter = event.keysym 
        if(caracter.isdigit()): 
            self.txtTelefono.config(bg="#FFFFFF") 
        else:
            if(event.keysym != "BackSpace"): 
                self.txtTelefono.delete(len(self.txtTelefono.get())-1, END) 
            
        if(len(self.txtApellido.get()) >= 8 and len(self.txtTelefono.get()) >= 10):  
            self.btnAgregar.config(state="normal")  
        else:
            self.btnAgregar.config(state="disabled")

    def validarEmail(self, event):
        return True

    
    def __init__(self, Menu):
        self.ventana = tk.Toplevel(Menu)
        self.ventana.geometry("400x300")
        self.ventana.resizable(0,0)

        self.lblTitulo = tk.Label(self.ventana, text="Eliminar cliente ")
        self.lblTitulo.place(relx= 0.5, y=25, anchor='center')

        iconoAyuda = tk.PhotoImage(file= r"icons\help.png")
        self.btnAyuda =tk.Button(self.ventana, image= iconoAyuda)
        self.btnAyuda.place(relx=1, x=-40, y=10, width=25, height=25)
        Tooltip(self.btnAyuda, "Presione para obtener ayuda!\nAlt+a")
        self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)
        self.ventana.bind('<Alt-a>', self.mostrarAyuda)
        
        self.lblCedula = tk.Label(self.ventana, text="Cedula*:")
        self.lblCedula.place(x=70, y=50)

        self.lblNombre = tk.Label(self.ventana, text="Nombre*:")
        self.lblNombre.place(x=70, y=90)

        self.lblApellido = tk.Label(self.ventana, text="Apellido*:")  
        self.lblApellido.place(x=70, y=130)

        self.lblTelefono = tk.Label(self.ventana, text="Teléfono*:")  
        self.lblTelefono.place(x=70, y=170)

        self.lblEmail = tk.Label(self.ventana, text="Email:")
        self.lblEmail.place(x=70, y=210)

        self.txtCedula = tk.Entry(self.ventana, width=25)
        self.txtCedula.place(x=170, y=50)
        Tooltip(self.txtCedula, "Ingrese su número de Cédula, mínimo 8 caracteres.\nSolo números [0-9]")
        self.txtCedula.bind('<KeyRelease>', self.validarCedula)

        self.txtNombre = tk.Entry(self.ventana, width=25)
        self.txtNombre.place(x=170, y=90)
        Tooltip(self.txtNombre, "Ingrese su nombre completo, mínimo 8 caracteres.\nSolo letras [a-z]")
        self.txtNombre.bind('<KeyRelease>', self.validarNombre)

        self.txtApellido = tk.Entry(self.ventana, width=25)
        self.txtApellido.place(x=170, y=130)
        Tooltip(self.txtApellido, "Ingrese su apellido, mínimo 8 caracteres.\nSolo letras [a-z]")
        self.txtNombre.bind('<KeyRelease>', self.validarApellido)

        self.txtTelefono = tk.Entry(self.ventana, width=25)
        self.txtTelefono.place(x=170, y=170)
        Tooltip(self.txtTelefono, "Ingrese su numero de telefono, mínimo 10 caracteres.\nSolo letras [0-9]")
        self.txtNombre.bind('<KeyRelease>', self.validarTelefono)

        self.txtEmail = tk.Entry(self.ventana, width=25)
        self.txtEmail.place(x=170, y=210)
        Tooltip(self.txtEmail, "Ingrese su Correo Electrónico.\nSolo recibe letas, números y los caracteres especiales listados [a-z, 0-9, @, -, _ ]")
        self.txtEmail.bind('<KeyRelease>', self.validarEmail)

        
        self.btnBuscar = tk.Button(self.ventana, text="Buscar", command=self.busqueda)
        self.btnBuscar.place(x=345, y=45)
        Tooltip(self.btnBuscar, "Presione para Buscar un Usuario a Eliminar")
        
        iconoEliminar= tk.PhotoImage(file= r"icons\user_add.png")
        self.btnEliminar = tk.Button(self.ventana, text="Agregar", width=60, height=20, command=self.agregar,image=iconoEliminar, compound=LEFT, state="disabled")
        self.btnEliminar.place(x=70, y=260)
        Tooltip(self.btnEliminar, "Presione para Registrarse como usuario o presione la tecla 'Enter'.\n")
        
        iconoLimpiar = tk.PhotoImage(file= r"icons\textfield_delete.png")
        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar",  width=60, height=20, command=self.limpiar, image=iconoLimpiar, compound=LEFT)
        self.btnLimpiar.place(x=162, y=260)
        Tooltip(self.btnLimpiar, "Presione para Limpiar los campos de texto.\nAlt+l")
        
        iconoSalir = tk.PhotoImage(file= r"C:\Users\2DNAIARA\Desktop\Taller 3 beta\Taller 3 beta\icons\cancel.png")
        self.btnSalir = tk.Button(self.ventana, text="Salir",  width=60, height=20, command=self.salir, image=iconoSalir, compound=LEFT)
        self.btnSalir.place(x=255, y=260)
        Tooltip(self.btnSalir, "Presione para Salir de la Aplicación.\nAlt+s")
        
        

    def busqueda(self):
        pass

    def agregar(self):
        pass

    def limpiar(self):
        self.txtCedula.delete(0, tk.END)
        self.txtNombre.delete(0, tk.END)
        self.txtApellido.delete(0, tk.END)
        self.txtTelefono.delete(0, tk.END)
        self.txtEmail.delete(0, tk.END)

    def salir(self):
        opcion = messagebox.askyesnocancel("Confirmar", "Está seguro que quiere salir de la Aplicación?")
        if(opcion == True):
            self.ventana.destroy()  
        else:
            pass  

        self.btnSalir.bind('<Button-1>', self.salir)  
        self.btnLimpiar.bind('<Button-1>', self.limpiar)  
        self.ventana.bind('<Alt-s>', self.salir)  
        self.ventana.bind('<Alt-l>', self.limpiar)
