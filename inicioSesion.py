import tkinter as tk


ventana = tk.Tk()
ventana.title("Lab.app")
ventana.geometry("320x400")
ventana.resizable(False,False)

def home():
    home=tk.Tk()
    home.title("Inicio")
    home.geometry("320x400")

    cuadro2 = tk.Frame(home, bg="yellow", bd=3, relief="ridge")
    cuadro2.pack(pady=40, padx=20, fill="both", expand=True)

    bienvenida = tk.Label(cuadro2, text="Bienvenido a Instagram", bg="yellow")
    bienvenida.pack(pady=80)

cuadro = tk.Frame(ventana, bg="pink", bd=3, relief="ridge")
cuadro.pack(pady=40, padx=20, fill="both", expand=True)


titulo_labapp = tk.Label(cuadro, text= "instagram", font= "arial", bg= "pink")
titulo_labapp.pack(pady=15)


etiqueta_nombre = tk.Label(cuadro, text="Introduce tu usuario:", bg= "pink")
etiqueta_nombre.pack(pady=5)
entrada_nombre = tk.Entry(cuadro)
entrada_nombre.pack(pady=5)


etiqueta_contrasena= tk.Label(cuadro, text="Introduce tu contraseña:", bg= "pink")
etiqueta_contrasena.pack(pady=5)
entrada_contrasena = tk.Entry(cuadro)
entrada_contrasena.pack(pady=5)


usuario_correcto = "jokernull"
contrasena_correcta = "1"


def iniciar_sesion():
    nombre_usuario = entrada_nombre.get()
    contrasena = entrada_contrasena.get()
    if nombre_usuario == usuario_correcto and contrasena == contrasena_correcta:
        ventana.destroy()
        home()
    else:
        saludo.config(text=f"¡Inicio de sesion incorrecto!", fg="red")

def salir():
    ventana.destroy()

boton = tk.Button(cuadro, text="Inciar sesion",bg= "green",  command=iniciar_sesion)
boton.pack(pady=10)

boton_salida= tk.Button(cuadro, text= "Salir", bg= "red",command=salir)
boton_salida.pack()


saludo = tk.Label(cuadro, text="", bg= "pink")
saludo.pack()


ventana.mainloop()

