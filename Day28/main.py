import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_text.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        timer_title.config(text="Break", bg=RED, fg=GREEN, font=(FONT_NAME, 40, "normal"))
        count_down(long_break_sec)
    elif REPS % 2 == 0:
        timer_title.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 40, "normal"))
        count_down(short_break_sec)
    else:
        timer_title.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "normal"))
        count_down(work_sec)
    return REPS


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor(count / 60)
    count_second = count % 60
    if count_second == 0:
        count_second = "00"

    if int(count_second) != 0 and int(count_second) < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            mark = mark + "✔"
            check_text.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "normal"))
timer_title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)

start_button = Button(text="Start", width=1, bd=0, highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

check_text = Label(fg=GREEN, bg=YELLOW)
check_text.grid(row=3, column=1)

reset_button = Button(text="Reset", width=1, bd=0, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()


