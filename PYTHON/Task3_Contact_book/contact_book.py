import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "contacts.json"

BG = "#2D1B3D"
CARD = "#44318D"
BTN = "#F97316"
ACCENT = "#FDBA74"
TEXT = "white"


class ContactManager:

    def __init__(self, root):

        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("900x700")
        self.root.configure(bg=BG)

        self.contacts = []
        self.load_contacts()

        self.create_ui()
        self.display_contacts()

    # ---------------- UI ---------------- #

    def create_ui(self):

        title = tk.Label(
            self.root,
            text="📞 CONTACT MANAGEMENT SYSTEM",
            font=("Segoe UI", 22, "bold"),
            bg=BG,
            fg=ACCENT
        )
        title.pack(pady=15)

        top_frame = tk.Frame(self.root, bg=BG)
        top_frame.pack(fill="x", padx=20)

        self.search_entry = tk.Entry(
            top_frame,
            font=("Segoe UI", 12),
            width=30
        )
        self.search_entry.pack(side="left", padx=5)

        search_btn = tk.Button(
            top_frame,
            text="🔍 Search",
            bg=BTN,
            fg="white",
            font=("Segoe UI", 10, "bold"),
            command=self.search_contact
        )
        search_btn.pack(side="left", padx=5)

        add_btn = tk.Button(
            top_frame,
            text="➕ Add Contact",
            bg=BTN,
            fg="white",
            font=("Segoe UI", 10, "bold"),
            command=self.open_add_window
        )
        add_btn.pack(side="right")

        self.count_label = tk.Label(
            self.root,
            text="",
            bg=BG,
            fg=ACCENT,
            font=("Segoe UI", 11, "bold")
        )
        self.count_label.pack(pady=10)

        # Scroll Area

        self.canvas = tk.Canvas(
            self.root,
            bg=BG,
            highlightthickness=0
        )

        scrollbar = tk.Scrollbar(
            self.root,
            orient="vertical",
            command=self.canvas.yview
        )

        self.card_frame = tk.Frame(
            self.canvas,
            bg=BG
        )

        self.card_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window(
            (0, 0),
            window=self.card_frame,
            anchor="nw"
        )

        self.canvas.configure(
            yscrollcommand=scrollbar.set
        )

        self.canvas.pack(
            side="left",
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

    # ---------------- DATA ---------------- #

    def load_contacts(self):

        if os.path.exists(FILE_NAME):

            with open(FILE_NAME, "r") as file:
                self.contacts = json.load(file)

    def save_contacts(self):

        with open(FILE_NAME, "w") as file:
            json.dump(self.contacts, file, indent=4)

    # ---------------- DISPLAY ---------------- #

    def display_contacts(self, data=None):

        for widget in self.card_frame.winfo_children():
            widget.destroy()

        if data is None:
            data = self.contacts

        self.count_label.config(
            text=f"Total Contacts : {len(data)}"
        )

        for index, contact in enumerate(data):

            card = tk.Frame(
                self.card_frame,
                bg=CARD,
                bd=2,
                relief="ridge"
            )

            card.pack(
                fill="x",
                padx=10,
                pady=8
            )

            tk.Label(
                card,
                text=f"👤 {contact['name']}",
                bg=CARD,
                fg="white",
                font=("Segoe UI", 14, "bold")
            ).pack(anchor="w", padx=10, pady=3)

            tk.Label(
                card,
                text=f"📞 {contact['phone']}",
                bg=CARD,
                fg="white",
                font=("Segoe UI", 11)
            ).pack(anchor="w", padx=10)

            tk.Label(
                card,
                text=f"📧 {contact['email']}",
                bg=CARD,
                fg="white",
                font=("Segoe UI", 11)
            ).pack(anchor="w", padx=10)

            tk.Label(
                card,
                text=f"🏠 {contact['address']}",
                bg=CARD,
                fg="white",
                font=("Segoe UI", 11)
            ).pack(anchor="w", padx=10, pady=5)

            btn_frame = tk.Frame(
                card,
                bg=CARD
            )
            btn_frame.pack(anchor="e", pady=5)

            tk.Button(
                btn_frame,
                text="✏ Edit",
                bg=BTN,
                fg="white",
                command=lambda i=index:
                self.open_edit_window(i)
            ).pack(side="left", padx=5)

            tk.Button(
                btn_frame,
                text="🗑 Delete",
                bg="crimson",
                fg="white",
                command=lambda i=index:
                self.delete_contact(i)
            ).pack(side="left", padx=5)

    # ---------------- ADD ---------------- #

    def open_add_window(self):

        self.open_form()

    # ---------------- EDIT ---------------- #

    def open_edit_window(self, index):

        self.open_form(index)

    # ---------------- FORM ---------------- #

    def open_form(self, index=None):

        win = tk.Toplevel(self.root)
        win.geometry("400x350")
        win.title("Contact Form")
        win.configure(bg=BG)

        labels = [
            "Name",
            "Phone",
            "Email",
            "Address"
        ]

        entries = []

        for label in labels:

            tk.Label(
                win,
                text=label,
                bg=BG,
                fg="white",
                font=("Segoe UI", 11)
            ).pack(pady=5)

            entry = tk.Entry(
                win,
                width=35
            )
            entry.pack()

            entries.append(entry)

        if index is not None:

            contact = self.contacts[index]

            entries[0].insert(0, contact["name"])
            entries[1].insert(0, contact["phone"])
            entries[2].insert(0, contact["email"])
            entries[3].insert(0, contact["address"])

        def save():

            name = entries[0].get()
            phone = entries[1].get()
            email = entries[2].get()
            address = entries[3].get()

            if not name or not phone:
                messagebox.showerror(
                    "Error",
                    "Name and Phone required"
                )
                return

            contact = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }

            if index is None:
                self.contacts.append(contact)
            else:
                self.contacts[index] = contact

            self.save_contacts()
            self.display_contacts()

            win.destroy()

        tk.Button(
            win,
            text="💾 Save Contact",
            bg=BTN,
            fg="white",
            font=("Segoe UI", 11, "bold"),
            command=save
        ).pack(pady=20)

    # ---------------- DELETE ---------------- #

    def delete_contact(self, index):

        confirm = messagebox.askyesno(
            "Delete",
            "Delete this contact?"
        )

        if confirm:

            self.contacts.pop(index)

            self.save_contacts()
            self.display_contacts()

    # ---------------- SEARCH ---------------- #

    def search_contact(self):

        keyword = self.search_entry.get().lower()

        result = []

        for contact in self.contacts:

            if (
                keyword in contact["name"].lower()
                or
                keyword in contact["phone"]
            ):
                result.append(contact)

        self.display_contacts(result)


# ---------------- MAIN ---------------- #

root = tk.Tk()

app = ContactManager(root)

root.mainloop()