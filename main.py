from tkinter import *
import pandas
import random
import os

# Variables
BACKGROUND_COLOR = "#B1DDC6"
language_type = "Flashy"
word = "German Flashcards"
current_card = {}


# /------------------------- CUSTOM FUNCTIONS -------------------------/
def next_word():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(language_list_dict)
    german_word = current_card['German']
    canvas.itemconfig(card_title, text="German", fill='black')
    canvas.itemconfig(card_text, text=f"{german_word}", fill='black')
    canvas.itemconfig(card_status, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    english_word = current_card['English']
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_text, text=f"{english_word}", fill='white')
    canvas.itemconfig(card_status, image=card_back_img)


def is_known():
    language_list_dict.remove(current_card)
    new_df = pandas.DataFrame(language_list_dict)
    new_df.to_csv('data/words_to_learn.csv', index=False)
    next_word()


# /------------------------- DATA MANAGEMENT -------------------------/
if os.path.isfile('data/words_to_learn.csv'):
    german_english_df = pandas.read_csv('data/words_to_learn.csv')
else:
    german_english_df = pandas.read_csv("data/german_to_english.csv")

language_list_dict = german_english_df.to_dict(orient='records')
print(len(language_list_dict))

# /------------------------- GUI ELEMENTS -------------------------/
window = Tk()
window.minsize(width=850, height=576)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
tick_img = PhotoImage(file="./images/right.png")
cross_img = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=536, bg=BACKGROUND_COLOR, highlightthickness=0)
card_status = canvas.create_image(400, 273, image=card_front_img)
card_title = canvas.create_text(390, 160, text=f"{language_type}", font=('Arial', 27, 'italic'))
card_text = canvas.create_text(390, 290, text=f"{word}", font=('Arial', 54, 'bold'))

flip_timer = window.after(3000, flip_card)

canvas.grid(row=0, column=0, columnspan=2)

tick_button = Button(image=tick_img, highlightthickness=0, bd=0, command=is_known)
tick_button.grid(row=1, column=1)

cross_button = Button(image=cross_img, highlightthickness=0, bd=0, command=next_word)
cross_button.grid(row=1, column=0)

# error showing
window.mainloop()
