from tkinter import *
from numpy.lib.function_base import flip
from numpy.lib.npyio import save
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("data/french_words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")

current_card = {}


def save_progress():
    data = pd.DataFrame(to_learn)
    data.to_csv("data/french_words_to_learn.csv", index=False)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_img, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_img, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="WHITE")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def success():
    to_learn.remove(current_card)
    next_card()
    save_progress()


def failure():
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# Canvas widget
canvas = Canvas(width=800, height=526)

# Image widgets
card_front = PhotoImage(file="images/card_front.gif")
card_back = PhotoImage(file="images/card_back.gif")
right_img = PhotoImage(file="images/right.gif")
wrong_img = PhotoImage(file="images/wrong.gif")

# Buttons
right_button = Button(
    image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=success)
wrong_button = Button(
    image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=failure)

# Layout Widgets
card_img = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(
    400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="Word", font=("Ariel", 60, "bold"))
right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
