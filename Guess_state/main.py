import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess the States")
image = "indian_states.gif"
screen.addshape(image)

turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

data = pandas.read_csv("29_states.csv")
all_states = data.state.to_list()

guess_states = []
while len(guess_states) < 30:
    guessed_state = screen.textinput(title=f"{len(guess_states)}/ 29 states guessed",
                                     prompt="What's the next states name?").title()
    if guessed_state == "Exit":
        missing_states = [states for states in all_states if states not in guess_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if guessed_state in all_states:
        guess_states.append(guessed_state)
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state_data = data[data.state == guessed_state]
        state.goto(int(state_data.x), int(state_data.y))
        state.write(guessed_state)

