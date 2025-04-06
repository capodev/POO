import tkinter as tk
from tkinter import messagebox

class Tarea:
    def __init__(self, texto):
        self.texto = texto
        self.completada = False

    def __str__(self):
        return self.texto + (" [Completada]" if self.completada else "")


class AplicacionTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.tareas = []

        self.entrada = tk.Entry(root, width=40)
        self.entrada.pack(pady=10)
        self.entrada.bind("<Return>", self.agregar_tarea_evento)

        self.lista_tareas = tk.Listbox(root, width=50, height=10)
        self.lista_tareas.pack(pady=10)

        self.boton_agregar = tk.Button(root, text="Agregar Tarea", command=self.agregar_tarea)
        self.boton_agregar.pack()

        self.boton_completar = tk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completar.pack()

        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack()

        self.root.bind("<c>", self.marcar_completada_evento)
        self.root.bind("<d>", self.eliminar_tarea_evento)
        self.root.bind("<Delete>", self.eliminar_tarea_evento)
        self.root.bind("<Escape>", lambda e: self.root.quit())

    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            texto = tarea.texto
            if tarea.completada:
                texto += " [Completada]"
            self.lista_tareas.insert(tk.END, texto)

    def agregar_tarea(self):
        texto = self.entrada.get().strip()
        if texto:
            self.tareas.append(Tarea(texto))
            self.entrada.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            idx = seleccion[0]
            self.tareas[idx].completada = True
            self.actualizar_lista()
        else:
            messagebox.showinfo("Info", "Selecciona una tarea para marcar como completada.")

    def marcar_completada_evento(self, event):
        self.marcar_completada()

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            idx = seleccion[0]
            del self.tareas[idx]
            self.actualizar_lista()
        else:
            messagebox.showinfo("Info", "Selecciona una tarea para eliminar.")

    def eliminar_tarea_evento(self, event):
        self.eliminar_tarea()


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionTareas(root)
    root.mainloop()
