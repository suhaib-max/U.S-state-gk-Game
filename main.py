import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S.State Game")

# TODO: Adding shape image
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)  # available to tutle to use

data = pd.read_csv("50_states.csv")


answer_state = screen.textinput(title="Guess The State", prompt="what's another state 's name")
# replacing screen.exitonclick() to turtle.mainloop() to screen onn
turtle.mainloop()
