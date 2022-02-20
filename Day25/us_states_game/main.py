import turtle
import pandas
import time

FONT = ("Courier", 15, 'normal')

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.tracer(0)
turtle.shape(image)

correct_guesses = []


correct_guess_count = 0
csv_file = pandas.read_csv("50_states.csv")

while len(correct_guesses) < 50:
    time.sleep(0.1)
    screen.update()
    answer_state = screen.textinput(title=f"{correct_guess_count}/50 State Correct",
                                    prompt="What's another state's name?").title()
    states = csv_file.state
    states_list = states.to_list()

    if answer_state == "Exit":
        state_to_learn = []
        for state in states_list:
            if state not in correct_guesses:
                state_to_learn.append(state)
        state_to_learn_dic = {
            'states': state_to_learn
        }
        pd = pandas.DataFrame(state_to_learn_dic)
        pd.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        state_data = csv_file[csv_file.state == answer_state]
        state_x = int(state_data.x)
        state_y = int(state_data.y)

        write_states = turtle.Turtle()
        write_states.penup()
        write_states.hideturtle()
        write_states.goto(state_x, state_y)
        write_states.write(answer_state, font=FONT)

        if answer_state not in correct_guesses:
            correct_guesses.append(answer_state)
            correct_guess_count = len(correct_guesses)









