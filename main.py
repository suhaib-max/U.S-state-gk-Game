import turtle

screen = turtle.Screen()
screen.title("U.S.State Game")

# TODO: Adding shape image
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)  # available to tutle to use



# replacing screen.exitonclick() to turtle.mainloop() to screen onn
turtle.mainloop()
