import turtle
import numpy as np
import random

wn=turtle.Screen()
wn.title("cookie with probability")
wn.bgcolor("black")

wn.register_shape("C:\\Users\\User\\Desktop\\cookie.gif")
wn.register_shape("C:\\Users\\User\\Desktop\\cookie2.gif")


cookie = turtle.Turtle()
cookie2 = turtle.Turtle()



c=cookie.shape("C:\\Users\\User\\Desktop\\cookie.gif")
#y=cookie2.shape("C:\\Users\\User\\Desktop\\cookie2.gif")
#np.random.choice([c,y],p=[0.8,0.2])
cookie.speed(0)
#cookie2.speed(0)


clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0,400)
pen.write (f"Clicks: {clicks}", align="center", font = ("Courier New",32,"normal"))



def clicked(x,y):
    global clicks
    h=[1,2,5]
    
    #p=random.choices(o,weights=(60,35,15),k=3)
    clicks += np.random.choice(h,p=[0.6,0.3,0.1])
    #clicks += (random.choices(h,weights=(60,30,10),k=3))
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font = ("Courier New",32,"normal"))
 
        

cookie.onclick(clicked)
#cookie2.oneclick(clicked)
#cookie2.onclick(clicked)

wn.mainloop()
