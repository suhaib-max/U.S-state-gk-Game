import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S.State Game")

# TODO: Adding shape image
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)  # available to tutle to use

data = pd.read_csv("50_states.csv")
all_state = data.state.to_list()

answer_state = screen.textinput(title="Guess The State", prompt="what's another state 's name")
# replacing screen.exitonclick() to turtle.mainloop() to screen onn

if answer_state in all_state:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]  # this will pull out the row
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_data.state.item())  # item will give first element in pandas series

turtle.mainloop()
