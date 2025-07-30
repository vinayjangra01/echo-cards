BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random

window = Tk()
window.title("Echo Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=500, height=500)
current_card = {}

#flip card
def flip_card():
    global current_card
    canvas.itemconfig(canvas_lang, text="French", fill="black")
    canvas.itemconfig(canvas_word_id, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_background, image=card_back)
    show_buttons()


window.after(3000, flip_card)

# Load image
card_back = PhotoImage(file="./images/card_front.png")
card_front = PhotoImage(file="./images/card_back.png")

# Create canvas and place image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_background = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
canvas_lang = canvas.create_text(400, 150, text="",  font=("Arial", 40, "italic"), fill="black")
canvas_word_id = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")



def hide_buttons():
    wrong_btn.grid_remove()
    right_btn.grid_remove()

def show_buttons():
    wrong_btn.grid()
    right_btn.grid()


def next_card():
    global current_card
    current_card =random.choice(records)
    canvas.itemconfig(canvas_lang, text="English", fill="white")
    canvas.itemconfig(canvas_word_id, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_background, image=card_front)
    hide_buttons()


#handle button press
def handle_button_press():
    word_data = random.choice(records)
    canvas.itemconfig(canvas_word_id, text=word_data.get('French'))


wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)


right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=next_card)
right_btn.grid(row=1, column=1)


words_data = pd.read_csv("./data/french_words.csv")
records = words_data.to_dict(orient="records") #each row becomes a dictionary

next_card()


window.mainloop()