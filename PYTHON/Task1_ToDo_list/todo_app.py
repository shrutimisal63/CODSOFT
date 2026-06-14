import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

FILE_NAME = "tasks.json"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TO-DO LIST")
        self.root.geometry("700x550")
        self.root.configure(bg="#1e1e2f")

        self.tasks = []
        self.load_tasks()

        title = tk.Label(
            root,
            text="📋 TO-DO LIST",
            font=("Segoe UI", 20, "bold"),
            bg="#1e1e2f",
            fg="#00d4ff"
        )
        title.pack(pady=10)

        input_frame = tk.Frame(root, bg="#1e1e2f")
        input_frame.pack(pady=10)

        self.task_entry = tk.Entry(
            input_frame,
            width=30,
            font=("Segoe UI", 12)
        )
        self.task_entry.grid(row=0, column=0, padx=5)

        self.priority = ttk.Combobox(
            input_frame,
            values=["High", "Medium", "Low"],
            width=10
        )
        self.priority.set("Medium")
        self.priority.grid(row=0, column=1, padx=5)

        add_btn = tk.Button(
            input_frame,
            text="Add Task",
            bg="#00c853",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            command=self.add_task
        )
        add_btn.grid(row=0, column=2, padx=5)

        self.task_listbox = tk.Listbox(
            root,
            width=80,
            height=18,
            bg="#2b2b40",
            fg="white",
            font=("Consolas", 11),
            selectbackground="#00d4ff"
        )
        self.task_listbox.pack(pady=10)

        button_frame = tk.Frame(root, bg="#1e1e2f")
        button_frame.pack()

        complete_btn = tk.Button(
            button_frame,
            text="✔ Complete",
            bg="#0288d1",
            fg="white",
            width=15,
            command=self.complete_task
        )
        complete_btn.grid(row=0, column=0, padx=10)

        delete_btn = tk.Button(
            button_frame,
            text="🗑 Delete",
            bg="#d50000",
            fg="white",
            width=15,
            command=self.delete_task
        )
        delete_btn.grid(row=0, column=1, padx=10)

        self.progress_label = tk.Label(
            root,
            text="Completed: 0/0",
            bg="#1e1e2f",
            fg="white",
            font=("Segoe UI", 11, "bold")
        )
        self.progress_label.pack(pady=10)

        self.refresh_tasks()

    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self):
        task_text = self.task_entry.get().strip()

        if not task_text:
            messagebox.showwarning("Warning", "Please enter a task!")
            return

        self.tasks.append({
            "task": task_text,
            "priority": self.priority.get(),
            "completed": False
        })

        self.task_entry.delete(0, tk.END)
        self.save_tasks()
        self.refresh_tasks()

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)

        completed = 0

        for task in self.tasks:
            status = "✔" if task["completed"] else "⏳"

            if task["completed"]:
                completed += 1

            display = (
                f"{status}  "
                f"{task['task']}  "
                f"[{task['priority']}]"
            )

            self.task_listbox.insert(tk.END, display)

        self.progress_label.config(
            text=f"Completed: {completed}/{len(self.tasks)}"
        )

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["completed"] = True

            self.save_tasks()
            self.refresh_tasks()

        except:
            messagebox.showinfo(
                "Info",
                "Please select a task."
            )

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]

            self.tasks.pop(index)

            self.save_tasks()
            self.refresh_tasks()

        except:
            messagebox.showinfo(
                "Info",
                "Please select a task."
            )

root = tk.Tk()
app = TodoApp(root)
root.mainloop()