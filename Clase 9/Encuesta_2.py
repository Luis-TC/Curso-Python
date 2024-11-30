import tkinter as tk

def saludo():
    label.config(text="¡Hola, mundo!")

ventana = tk.Tk()
ventana.title("Ejemplo Tkinter")

label = tk.Label(ventana, text="Presiona el botón")
label.pack()

boton = tk.Button(ventana, text="Saludar", command=saludo)
boton.pack()

ventana.mainloop()