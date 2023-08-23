import turtle
import random

ekran = turtle.Screen()
ekran.bgcolor("Light blue")
ekran.title("GAME")
FONT = ('Arial', 30 ,'normal')
size = 15
yy = 20
xx = -20
turtle_list = []
score = 0
gameover = False

score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.color("dark blue")
top_height = ekran.window_height() / 2
y= top_height * 0.9
score_turtle.penup()
score_turtle.setpos(0,y)
score_turtle.write("Score : 0" , move =False,align="center",font=FONT)
gerisayim_turtle = turtle.Turtle()
def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score # score değiştirmek içim unutma global diye belirtmek lazım
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Score {score}", move =False,align="center",font=FONT)
        #print ( x , y)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.goto(x*size, y*size)
    turtle_list.append(t)

def setup_turtle (xx,yy):
    for i in range(5):
        for a in range(5):
            make_turtle(xx, yy )
            xx=xx+10
        xx=-20
        yy = yy-10

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtle_randomly():
    if not gameover:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        #listelerde random elemanı seçme
        ekran.ontimer(show_turtle_randomly,500)
        #fonksiyon kendi fonkisyonunu loopa sokuyor bu sayede

def gerisayım(time):
    global gameover
    gerisayim_turtle.hideturtle()
    gerisayim_turtle.penup()
    top_height = ekran.window_height() / 2
    y= top_height * 0.9
    gerisayim_turtle.setpos(0,y-30)
    gerisayim_turtle.clear()
    if time > 0:
        gerisayim_turtle.clear()
        gerisayim_turtle.write(f"Time : {time}" , move =False,align="center",font=FONT)
        ekran.ontimer(lambda: gerisayım(time - 1), 1000)
    else:
        gameover = True
        gerisayim_turtle.clear()
        hide_turtles()
        gerisayim_turtle.write(f"Oyun Bitti" , move =False,align="center",font=FONT)



turtle.tracer(0)
#setup_score_turtle()
setup_turtle (xx,yy)
hide_turtles()

show_turtle_randomly()
gerisayım(10)
turtle.tracer(1)

turtle.mainloop()

