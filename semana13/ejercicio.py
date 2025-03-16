# importamos  tkinter
import tkinter as tk

# Creamos el metodo de agregar nombre para que al dar click en el boton agregar se agrege el nombre a la lista


def borrar_seleccionado():
    seleccion = lista_nombres.curselection()
    if seleccion:
        lista_nombres.delete(seleccion[0])


def agregar_nombre():
    nombre = entrada_nombre.get()
    if nombre.strip() != "":
        lista_nombres.insert(tk.END, nombre)
        entrada_nombre.delete(0, tk.END)  # Limpiar entrada


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista de Nombres")
ventana.geometry("300x400")

# Label
label = tk.Label(ventana, text="Ingrese un nombre:")
label.pack(pady=5)

# Caja de texto
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack(pady=5)

# Botón
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_nombre)
boton_agregar.pack(pady=5)

# Listbox
lista_nombres = tk.Listbox(ventana, width=30, height=10)
lista_nombres.pack(pady=10)

# Botón Borrar
boton_borrar = tk.Button(
    ventana, text="Borrar seleccionado", command=borrar_seleccionado)
boton_borrar.pack(pady=5)

# Ejecutar ventana
ventana.mainloop()
# lesto es un ejemplo de como se puede hacer una lista de nombres con tkinter
