import turtle
import pandas

screen = turtle.Screen()
screen.title("US Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
states_guessed = []
list_answers = []

while len(states_guessed) < 50:
    answer_state = screen.textinput(title=f"{len(states_guessed)}/50 Guessed",
                                    prompt="Guess a State:").title()

    if answer_state == "Exit":
        print("You missed those:")
        print(all_states)
        new_data = pandas.DataFrame(all_states)
        new_data.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        all_states.remove(answer_state)
        states_guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
