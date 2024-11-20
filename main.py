from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, flip_card)

def is_known():
    data = pandas.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index = False)
    words.remove(current_card)

    next_card()

def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

window = Tk()
window.title("Flash Card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)


canvas = Canvas(height=526, width=800)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
canvas_img = canvas.create_image( 400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 40, "italic"))

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_image, command=is_known)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_image, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()




window.mainloop()