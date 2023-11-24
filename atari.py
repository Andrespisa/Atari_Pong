import turtle
a="bienbenido"
b="a mi juego"
print(a+" "+b)

# Pantalla
wn = turtle.Screen()
wn.title("Atari Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Cargar formas
wn.addshape("boton.gif")
wn.addshape("boton1.gif")
wn.addshape("pong.gif")

# Atari logo
logo = turtle.Turtle()
logo.shape("pong.gif")
logo.penup()
logo.goto(0, 150)

# Botón
start = turtle.Turtle()
start.shape("boton.gif")
start.penup()
start.goto(0, 0)


def on_button_press():
    start.shape("boton1.gif")
    

def on_button_release():
    start.shape("boton.gif")
    
    

turtle.listen()
turtle.onkeypress(on_button_press, "space")
turtle.onkeyrelease(on_button_release, "space")

#loope
def close_window():
    try:
        wn.bye()
    except turtle.Terminator:
        pass

wn.onkeypress(close_window, "Escape")
wn.listen()

# loop
while True:
    try:
        wn.update()
    except turtle.Terminator:
        break