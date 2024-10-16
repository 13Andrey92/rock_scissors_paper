import os
import sys
from tkinter import *
from random import *
from PIL import ImageTk


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


window = Tk()

WIDTH = (window.winfo_screenwidth() // 2) - 350
HEIGHT = (window.winfo_screenheight() // 2) - 400
base_color = "#7d7141"

window.geometry(f"700x700+{WIDTH}+{HEIGHT}")
window.title("Камень, ножницы, бумага")

window.resizable(False, False)

canvas = Canvas(bg=base_color, width=700, height=700)
canvas.pack(anchor=CENTER, expand=100)

stone_img = ImageTk.PhotoImage(file=r"Pics\stone.png")
scissors_img = ImageTk.PhotoImage(file=r"Pics\scissors.png")
paper_img = ImageTk.PhotoImage(file=r"Pics\paper.png")

rounds = 0
wins = 0
draws = 0
losses = 0

options = [stone_img, scissors_img, paper_img]


def reset_game():
    global rounds
    global wins
    global draws
    global losses
    rounds = 0
    wins = 0
    draws = 0
    losses = 0
    button_stone.configure(state=NORMAL)
    button_scissors.configure(state=NORMAL)
    button_paper.configure(state=NORMAL)
    text_win_scores.configure(text="0")
    text_draw_scores.configure(text="0")
    text_loss_scores.configure(text="0")
    rounds_number.configure(text="0")


def PC_turn_from_stone():
    global wins
    global draws
    global losses
    global rounds
    PC_choice = choice(options)
    image_PC.config(image=PC_choice, compound="right")
    if PC_choice == stone_img:
        draws += 1
        text_draw_scores.configure(text=draws)
    elif PC_choice == scissors_img:
        wins += 1
        text_win_scores.configure(text=wins)
    elif PC_choice == paper_img:
        losses += 1
        text_loss_scores.configure(text=losses)
    rounds += 1
    rounds_number.configure(text=rounds)

    if rounds == 5:
        finalization()


def PC_turn_from_scissors():
    global wins
    global draws
    global losses
    global rounds
    PC_choice = choice(options)
    image_PC.config(image=PC_choice, compound="right")
    if PC_choice == stone_img:
        losses += 1
        text_loss_scores.configure(text=losses)
    elif PC_choice == scissors_img:
        draws += 1
        text_draw_scores.configure(text=draws)
    elif PC_choice == paper_img:
        wins += 1
        text_win_scores.configure(text=wins)
    rounds += 1
    rounds_number.configure(text=rounds)

    if rounds == 5:
        finalization()


def PC_turn_from_paper():
    global wins
    global draws
    global losses
    global rounds
    PC_choice = choice(options)
    image_PC.config(image=PC_choice, compound="right")
    if PC_choice == stone_img:
        wins += 1
        text_win_scores.configure(text=wins)
    elif PC_choice == scissors_img:
        losses += 1
        text_loss_scores.configure(text=losses)
    elif PC_choice == paper_img:
        draws += 1
        text_draw_scores.configure(text=draws)
    rounds += 1
    rounds_number.configure(text=rounds)

    if rounds == 5:
        finalization()


def finalization():
        final_message.configure(text="Игра окончена!")
        button_stone.configure(state=DISABLED)
        button_scissors.configure(state=DISABLED)
        button_paper.configure(state=DISABLED)

        play_again = Button(canvas, text="Сыграем еще?", command=reset_game)
        play_again.place(x=540, y=155)

        if wins > 2:
            final_total.configure(text="Вы победили!", font=("Times New Roman", 18, "bold"), fg="#0ceb6c", bg=base_color)

        elif losses > 2:
            final_total.configure(text="Вы проиграли!", font=("Times New Roman", 18, "bold"), fg="#8f1526", bg=base_color)

        else:
            final_total.configure(text="Ничья!", font=("Times New Roman", 18, "bold"), fg="#FFFFFF", bg=base_color)



text_wins = Label(canvas, text="Победы", font=("Times New Roman", 18, "bold"), fg="#0ceb6c", bg=base_color)
text_wins.place(x=90, y=30)

text_win_scores = Label(canvas, text="0", font=("Times New Roman", 18, "bold"), fg="#0ceb6c", bg=base_color)
text_win_scores.place(x=130, y=70)

text_draws = Label(canvas, text="Ничья", font=("Times New Roman", 18, "bold"), fg="#FFFFFF", bg=base_color)
text_draws.place(x=310, y=30)

text_draw_scores = Label(canvas, text="0", font=("Times New Roman", 18, "bold"), fg="#FFFFFF", bg=base_color)
text_draw_scores.place(x=340, y=70)

text_losses = Label(canvas, text="Проигрыши", font=("Times New Roman", 18, "bold"), fg="#8f1526", bg=base_color)
text_losses.place(x=510, y=30)

text_loss_scores = Label(canvas, text="0", font=("Times New Roman", 18, "bold"), fg="#8f1526", bg=base_color)
text_loss_scores.place(x=570, y=70)

rounds_text = Label(canvas, text="Раунды:", font=("Times New Roman", 18, "bold"), fg="#000000", bg=base_color)
rounds_text.place(x=30, y=150)

rounds_number = Label(canvas, text="0", font=("Times New Roman", 18, "bold"), fg="#000000", bg=base_color)
rounds_number.place(x=130, y=150)

button_stone = Button(canvas, height=200, width=200, bg=base_color, image=stone_img, command=PC_turn_from_stone)
button_stone.place(x=30, y=450)

button_scissors = Button(canvas, height=200, width=200, bg=base_color, image=scissors_img, command=PC_turn_from_scissors)
button_scissors.place(x=250, y=450)

button_paper = Button(canvas, height=200, width=200, bg=base_color, image=paper_img, command=PC_turn_from_paper)
button_paper.place(x=470, y=450)

text_PC = Label(canvas, text="Компьютер:", font=("Times New Roman", 30, "bold"), fg="#000000", bg=base_color)
text_PC.place(x=30, y=270)

image_PC = Label(canvas, fg="#000000", bg=base_color)
image_PC.place(x=280, y=200)

final_message = Label(canvas, text="Играем 5 раундов", font=("Times New Roman", 18, "bold"), bg=base_color)
final_message.place(x=160, y=150)

final_total = Label(text="", font=("Times New Roman", 18, "bold"), bg=base_color)
final_total.place(x=357, y=150)

window.mainloop()
