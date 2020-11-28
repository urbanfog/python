from tkinter import *
from tkinter import font
print(TkVersion)
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 2
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 7:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)
    elif not reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    min = count // 60
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    if min < 10:
        min = f"0{min}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
    if reps % 2 == 0:
        check_marks["text"] + "✔"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Widgets
title = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
start_button = Button(text="Start", bg=YELLOW,
                      highlightthickness=0, command=start_timer)
reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0)
check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
image = PhotoImage(file="tomato.gif")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))

# Layout
title.grid(row=0, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
check_marks.grid(row=3, column=1)
canvas.grid(row=1, column=1)


window.mainloop()
