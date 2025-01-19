from tkinter import *

BACKGROUND_COLOR = "#BGCOLOR" #TODO

window = Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR, height=500, width=500)

canvas = Canvas(width=400, height=200)

card_front_img = PhotoImage(file="images/card_front_small.png")
canvas.create_image(200, 100, image=card_front_img)
canvas.create_text(200, 50, text="Title", font=("Ariel", 20, "normal"))
canvas.create_text(200, 100, text="Word", font=("Ariel", 30, "bold"))
canvas.config( bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong_small.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right_small.png")
known_button = Button(image=tick_image, highlightthickness=0)
known_button.grid(row=1, column=1)

window.mainloop()


