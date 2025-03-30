import tkinter as tk
from idlelib.colorizer import color_config
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")

        # Lista de tareas
        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.grid(row=0, column=0, padx=10, pady=10)

        # Botón para añadir tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", width=20, command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Botón para marcar tarea como completada
        self.complete_button = tk.Button(root, text="Marcar como Completada", width=20, command=self.complete_task)
        self.complete_button.grid(row=1, column=0, padx=10, pady=10)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(root, text="Eliminar Tarea", width=20, command=self.delete_task)
        self.delete_button.grid(row=1, column=1, padx=10, pady=10)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, height=10, width=40, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Vincular tecla Enter para añadir tarea
        self.entry.bind("<Return>", self.add_task_event)

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.entry.delete(0, tk.END)
            self.update_task_list()

    def add_task_event(self, event):
        self.add_task()

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            task["completed"] = True
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task["task"]
            if task["completed"]:
                display_text = f"{display_text} (Completada)"
                # display_text.tag_configure
            self.task_listbox.insert(tk.END, display_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
#its a good example to practice que chevere la verdad