import turtle

screen = turtle.Screen()
screen.title("U.S.State Game")

# TODO: Adding shape image
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)  # available to tutle to use

answer_state = screen.textinput(title="Guess The State", prompt="what's another state 's name")
print(answer_state)

# replacing screen.exitonclick() to turtle.mainloop() to screen onn
turtle.mainloop()
