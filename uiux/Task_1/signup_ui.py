import tkinter as tk
from tkinter import messagebox

# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("Learning App")
root.state("zoomed")      # Full screen (Windows)
root.configure(bg="#6C8EF5")

# Colors
BG = "#6C8EF5"
CARD = "white"
BLUE = "#3D7EFF"
TEXT = "#222222"


# ---------------- COMMON FUNCTIONS ----------------

def clear():
    for widget in root.winfo_children():
        widget.destroy()


def create_card():
    card = tk.Frame(root, bg=CARD, width=450, height=650)
    card.place(relx=0.5, rely=0.5, anchor="center")
    card.pack_propagate(False)
    return card


# ---------------- WELCOME SCREEN ----------------

def welcome_screen():
    clear()
    root.configure(bg=BG)

    card = create_card()

    tk.Label(
        card,
        text="Welcome",
        font=("Segoe UI", 28, "bold"),
        bg=CARD,
        fg=BLUE
    ).pack(pady=20)

    tk.Label(
        card,
        text="📚",
        font=("Arial", 90),
        bg=CARD
    ).pack()

    tk.Label(
        card,
        text="Welcome To My Learning",
        font=("Segoe UI", 20, "bold"),
        bg=CARD,
        fg=TEXT
    ).pack(pady=10)

    tk.Label(
        card,
        text="Create your account and\nstart learning today!",
        font=("Segoe UI", 12),
        bg=CARD,
        fg="gray"
    ).pack()

    tk.Button(
        card,
        text="Sign Up",
        bg=BLUE,
        fg="white",
        font=("Segoe UI", 14, "bold"),
        width=20,
        height=2,
        bd=0,
        command=signup_screen
    ).pack(pady=35)

    tk.Button(
        card,
        text="Already have an account? Login",
        bg=CARD,
        fg=BLUE,
        bd=0,
        font=("Segoe UI", 11),
        command=login_screen
    ).pack()


# ---------------- LOGIN SCREEN ----------------

def login_screen():
    clear()
    root.configure(bg=BG)

    card = create_card()

    tk.Label(
        card,
        text="Login",
        font=("Segoe UI", 24, "bold"),
        bg="white",
        fg=BLUE
    ).pack(pady=20)

    tk.Label(
        card,
        text="Welcome Back!",
        font=("Segoe UI", 11),
        bg="white",
        fg="gray"
    ).pack()

    tk.Label(
        card,
        text="Email",
        bg="white",
        anchor="w"
    ).pack(fill="x", padx=45, pady=(20, 0))

    email = tk.Entry(card, font=("Segoe UI", 12), width=30)
    email.pack(ipady=8, padx=45)

    tk.Label(
        card,
        text="Password",
        bg="white",
        anchor="w"
    ).pack(fill="x", padx=45, pady=(15, 0))

    password = tk.Entry(card, show="*", font=("Segoe UI", 12), width=30)
    password.pack(ipady=8, padx=45)

    remember = tk.IntVar()

    tk.Checkbutton(
        card,
        text="Remember Me",
        variable=remember,
        bg="white"
    ).pack(anchor="w", padx=40, pady=10)

    def login():
        if email.get() == "" or password.get() == "":
            messagebox.showerror("Error", "Please enter Email and Password.")
            return

        messagebox.showinfo(
            "Success",
            "Login Successful!\nWelcome to My Learning."
        )

    tk.Button(
        card,
        text="Login",
        bg=BLUE,
        fg="white",
        font=("Segoe UI", 13, "bold"),
        width=20,
        height=2,
        bd=0,
        command=login
    ).pack(pady=20)

    tk.Button(
        card,
        text="Back to Welcome",
        bg="white",
        fg=BLUE,
        bd=0,
        font=("Segoe UI", 11),
        command=welcome_screen
    ).pack()


# ---------------- SIGNUP SCREEN ----------------

def signup_screen():
    clear()
    root.configure(bg=BG)

    card = create_card()

    tk.Label(
        card,
        text="Sign Up",
        font=("Segoe UI", 24, "bold"),
        bg="white",
        fg=BLUE
    ).pack(pady=15)

    tk.Label(
        card,
        text="Create your account",
        font=("Segoe UI", 11),
        bg="white",
        fg="gray"
    ).pack()

    tk.Label(
        card,
        text="Full Name",
        bg="white",
        anchor="w"
    ).pack(fill="x", padx=45, pady=(20, 0))

    name = tk.Entry(card, font=("Segoe UI", 12), width=30)
    name.pack(ipady=8, padx=45)

    tk.Label(
        card,
        text="Email",
        bg="white",
        anchor="w"
    ).pack(fill="x", padx=45, pady=(15, 0))

    email = tk.Entry(card, font=("Segoe UI", 12), width=30)
    email.pack(ipady=8, padx=45)

    tk.Label(
        card,
        text="Password",
        bg="white",
        anchor="w"
    ).pack(fill="x", padx=45, pady=(15, 0))

    password = tk.Entry(card, show="*", font=("Segoe UI", 12), width=30)
    password.pack(ipady=8, padx=45)

    tk.Label(
        card,
        text="Confirm Password",
        bg="white",
        anchor="w"
    ).pack(fill="x", padx=45, pady=(15, 0))

    confirm = tk.Entry(card, show="*", font=("Segoe UI", 12), width=30)
    confirm.pack(ipady=8, padx=45)

    agree = tk.IntVar()

    tk.Checkbutton(
        card,
        text="I agree to the Privacy Policy",
        variable=agree,
        bg="white"
    ).pack(anchor="w", padx=40, pady=15)

    def signup():
        if (name.get() == "" or email.get() == "" or
                password.get() == "" or confirm.get() == ""):
            messagebox.showerror("Error", "Please fill all fields.")
            return

        if password.get() != confirm.get():
            messagebox.showerror("Error", "Passwords do not match.")
            return

        if agree.get() == 0:
            messagebox.showwarning(
                "Warning",
                "Please accept Privacy Policy."
            )
            return

        messagebox.showinfo(
            "Success",
            "Account Created Successfully!"
        )

        login_screen()

    tk.Button(
        card,
        text="Sign Up",
        bg=BLUE,
        fg="white",
        font=("Segoe UI", 13, "bold"),
        width=20,
        height=2,
        bd=0,
        command=signup
    ).pack(pady=15)

    tk.Button(
        card,
        text="Already have an account? Login",
        bg="white",
        fg=BLUE,
        bd=0,
        font=("Segoe UI", 11),
        command=login_screen
    ).pack()


# ---------------- START ----------------

welcome_screen()
root.mainloop()