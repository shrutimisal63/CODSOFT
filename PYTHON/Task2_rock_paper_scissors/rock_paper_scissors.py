import tkinter as tk
import random

# ---------------- VARIABLES ---------------- #

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0
current_user_choice = ""

# ---------------- GAME LOGIC ---------------- #

def play(user_choice):
    global current_user_choice

    current_user_choice = user_choice

    user_choice_label.config(
        text=f"👤 Your Choice: {user_choice}"
    )

    computer_choice_label.config(
        text=""
    )

    result_label.config(
        text="🤖 Computer is Thinking..."
    )

    animate_thinking(0)


def animate_thinking(count):

    dots = "." * (count % 4)

    result_label.config(
        text=f"🤖 Computer is Thinking{dots}"
    )

    if count < 8:
        root.after(
            250,
            lambda: animate_thinking(count + 1)
        )
    else:
        show_result()


def show_result():

    global user_score
    global computer_score

    computer_choice = random.choice(choices)

    computer_choice_label.config(
        text=f"💻 Computer Choice: {computer_choice}"
    )

    user_choice = current_user_choice

    if user_choice == computer_choice:
        result = "🤝 It's a Tie!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or
        (user_choice == "Paper" and computer_choice == "Rock")
        or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You Win!"
        user_score += 1

    else:
        result = "😢 Computer Wins!"
        computer_score += 1

    result_label.config(text=result)

    score_label.config(
        text=f"🏆 You: {user_score}     💻 Computer: {computer_score}"
    )

    flash_result()


# ---------------- ANIMATIONS ---------------- #

def flash_result():
    colors = [
        "#facc15",
        "#22c55e",
        "#38bdf8",
        "#f97316",
        "#ef4444"
    ]

    animate_color(0, colors)


def animate_color(index, colors):

    if index < 15:

        result_label.config(
            fg=colors[index % len(colors)]
        )

        root.after(
            120,
            lambda: animate_color(index + 1, colors)
        )


def animate_title():

    colors = [
        "#38bdf8",
        "#22c55e",
        "#f97316",
        "#facc15"
    ]

    current = animate_title.counter

    title.config(
        fg=colors[current]
    )

    animate_title.counter = (
        current + 1
    ) % len(colors)

    root.after(500, animate_title)


animate_title.counter = 0


# ---------------- RESET ---------------- #

def reset_game():

    global user_score
    global computer_score

    user_score = 0
    computer_score = 0

    user_choice_label.config(
        text="👤 Your Choice:"
    )

    computer_choice_label.config(
        text="💻 Computer Choice:"
    )

    result_label.config(
        text="Choose Rock, Paper or Scissors",
        fg="white"
    )

    score_label.config(
        text="🏆 You: 0     💻 Computer: 0"
    )


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Rock Paper Scissors Ultimate")
root.geometry("800x600")
root.configure(bg="#0f172a")
root.resizable(False, False)

title = tk.Label(
    root,
    text="✊ ✋ ✌ ROCK PAPER SCISSORS",
    font=("Segoe UI", 24, "bold"),
    bg="#0f172a"
)

title.pack(pady=20)

animate_title()

score_label = tk.Label(
    root,
    text="🏆 You: 0     💻 Computer: 0",
    font=("Segoe UI", 14, "bold"),
    bg="#0f172a",
    fg="white"
)

score_label.pack(pady=10)

button_frame = tk.Frame(
    root,
    bg="#0f172a"
)

button_frame.pack(pady=30)

rock_btn = tk.Button(
    button_frame,
    text="✊ ROCK",
    width=15,
    height=2,
    bg="#22c55e",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    command=lambda: play("Rock")
)

rock_btn.grid(row=0, column=0, padx=15)

paper_btn = tk.Button(
    button_frame,
    text="✋ PAPER",
    width=15,
    height=2,
    bg="#3b82f6",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    command=lambda: play("Paper")
)

paper_btn.grid(row=0, column=1, padx=15)

scissors_btn = tk.Button(
    button_frame,
    text="✌ SCISSORS",
    width=15,
    height=2,
    bg="#f97316",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    command=lambda: play("Scissors")
)

scissors_btn.grid(row=0, column=2, padx=15)

user_choice_label = tk.Label(
    root,
    text="👤 Your Choice:",
    font=("Segoe UI", 14),
    bg="#0f172a",
    fg="white"
)

user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(
    root,
    text="💻 Computer Choice:",
    font=("Segoe UI", 14),
    bg="#0f172a",
    fg="white"
)

computer_choice_label.pack(pady=10)

result_label = tk.Label(
    root,
    text="Choose Rock, Paper or Scissors",
    font=("Segoe UI", 18, "bold"),
    bg="#0f172a",
    fg="white"
)

result_label.pack(pady=25)

reset_btn = tk.Button(
    root,
    text="🔄 NEW GAME",
    width=18,
    height=2,
    bg="#ef4444",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    command=reset_game
)

reset_btn.pack(pady=20)

footer = tk.Label(
    root,
    text="CodSoft Python Internship Project",
    font=("Segoe UI", 10),
    bg="#0f172a",
    fg="gray"
)

footer.pack(side="bottom", pady=10)

root.mainloop()