BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

window = Tk()
window.title("Echo Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=500, height=500)

# Load image
my_image = PhotoImage(file="./images/card_back.png")


# Create canvas and place image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=my_image)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0)
wrong_btn.grid(row=1, column=0)


right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0)
right_btn.grid(row=1, column=1)

canvas.image = my_image


window.mainloop()