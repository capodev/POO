# vamos a hacer una app de agendas con horas y fechas en tkinter
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
# pora que cora sin problemas el codigo debemos inatalar las librerias primero
# para instalar tkcalendar debemos de hacerlo con el siguiente comando
# pip install tkcalendar


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("700x400")

        self.eventos = []  # Lista para almacenar eventos

        self.setup_ui()

    def setup_ui(self):
        # Frame de entrada de datos
        frame_input = tk.Frame(self.root)
        frame_input.pack(pady=10)

        tk.Label(frame_input, text="Fecha:").grid(row=0, column=0)
        self.fecha_entry = DateEntry(
            frame_input, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_entry.grid(row=0, column=1)

        tk.Label(frame_input, text="Hora:").grid(row=1, column=0)
        self.hora_entry = tk.Entry(frame_input, width=10)
        self.hora_entry.grid(row=1, column=1)

        tk.Label(frame_input, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = tk.Entry(frame_input, width=30)
        self.desc_entry.grid(row=2, column=1)

        tk.Button(frame_input, text="Agregar Evento",
                  command=self.agregar_evento).grid(row=3, columnspan=2, pady=5)

        # Frame de lista de eventos
        frame_lista = tk.Frame(self.root)
        frame_lista.pack()

        self.tree = ttk.Treeview(frame_lista, columns=(
            "Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame de botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Eliminar Evento Seleccionado",
                  command=self.eliminar_evento).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Salir", command=self.root.quit).pack(
            side=tk.RIGHT, padx=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.eventos.append((fecha, hora, descripcion))
            self.tree.insert("", tk.END, values=(fecha, hora, descripcion))
        else:
            messagebox.showwarning(
                "Error", "Todos los campos deben ser llenados")

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno(
                "Confirmar", "¿Deseas eliminar este evento?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning(
                "Error", "Selecciona un evento para eliminar")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
