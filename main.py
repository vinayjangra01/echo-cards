BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random

window = Tk()
window.title("Echo Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=500, height=500)

# Load image
my_image = PhotoImage(file="./images/card_front.png")


# Create canvas and place image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=my_image)
canvas.grid(row=0, column=0, columnspan=2)
canvas_lang = canvas.create_text(400, 150, text="French",  font=("Arial", 40, "italic"), fill="black")
canvas_word_id = canvas.create_text(400, 263, text="partir", font=("Arial", 60, "bold"), fill="black")


#handle button press
def handle_button_press():
    word_data = random.choice(records)
    canvas.itemconfig(canvas_word_id, text=word_data.get('French'))


wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=handle_button_press)
wrong_btn.grid(row=1, column=0)


right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=handle_button_press)
right_btn.grid(row=1, column=1)

canvas.image = my_image

words_data = pd.read_csv("./data/french_words.csv")
records = words_data.to_dict(orient="records") #each row becomes a dictionary



window.mainloop()