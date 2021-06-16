from tkinter import *
import pandas
import random

# Variables
BACKGROUND_COLOR = "#B1DDC6"
language_type = "Flashy"
word = "German Flashcards"

# /------------------------- DATA MANAGEMENT -------------------------/
german_english_df = pandas.read_csv("data/german_to_english.csv")
language_data_dict = german_english_df.to_dict(orient='records')


# /------------------------- CUSTOM FUNCTIONS -------------------------/
def next_word():
    current_card = random.choice(language_data_dict)
    new_word = current_card['German']
    canvas.itemconfig(card_title, text="German")
    canvas.itemconfig(card_text, text=f"{new_word}")


# /------------------------- GUI ELEMENTS -------------------------/
window = Tk()
window.minsize(width=850, height=576)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
tick_img = PhotoImage(file="./images/right.png")
cross_img = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=536, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = canvas.create_image(400, 273, image=card_front_img)
card_title = canvas.create_text(390, 160, text=f"{language_type}", font=('Arial', 27, 'italic'))
card_text = canvas.create_text(390, 290, text=f"{word}", font=('Arial', 54, 'bold'))

canvas.grid(row=0, column=0, columnspan=2)

tick_button = Button(image=tick_img, highlightthickness=0, bd=0, command=next_word)
tick_button.grid(row=1, column=1)

cross_button = Button(image=cross_img, highlightthickness=0, bd=0, command=next_word)
cross_button.grid(row=1, column=0)

# error showing
window.mainloop()
