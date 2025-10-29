import tkinter as tk

def saludar():
    nombre_usuario = entrada_nombre.get()
    saludo.config(text=f"¡Hola, {nombre_usuario}!")

ventana = tk.Tk()
ventana.title("Saludo")
ventana.geometry("320x400")

etiqueta_nombre = tk.Label(ventana, text="Introduce tu nombre:")
etiqueta_nombre.pack()

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

boton = tk.Button(ventana, text="Saludar",bg= "green",  command=saludar)
boton.pack()

saludo = tk.Label(ventana, text="")
saludo.pack()

ventana.mainloop()

