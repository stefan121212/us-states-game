import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
list_of_guessed_states = []

while len(list_of_guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(list_of_guessed_states)}/50 States correct",
                                    prompt="What's another state's name?").title()
    answer_state
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in list_of_guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in list_of_guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in data.state.values:
        state = data[data.state == answer_state]
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        text.goto(int(state.x), int(state.y))
        text.write(answer_state)
        if answer_state not in list_of_guessed_states:
            list_of_guessed_states.append(answer_state)

screen.exitonclick()
