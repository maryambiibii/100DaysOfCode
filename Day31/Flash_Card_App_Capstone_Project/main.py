from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
list_of_current_card = []

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------- Save the Progress ------------------------------- #
def save_progress():
    global list_of_current_card
    to_learn.remove(list_of_current_card[-1])
    print(len(to_learn))
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    new_card()


# ---------------------------- Reset the Timer ------------------------------- #
def reset_timer():
    window.after_cancel(window)
    canvas.itemconfig(canvas_image, image=front_img)
    new_card()


# ---------------------------- Flip the Cards ------------------------------- #
def show_english_card():
    current_card = list_of_current_card[-1]
    english_word = current_card["English"]
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")


# ---------------------------- Create New Flash Card ------------------------------- #
def new_card():
    global list_of_current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french_word = current_card["French"]
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    list_of_current_card.append(current_card)
    flip_timer = window.after(3000, show_english_card)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, show_english_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

command = lambda: [reset_timer(), save_progress()]
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=command)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=command)
wrong_button.grid(row=1, column=0)

new_card()

window.mainloop()
