import turtle
import numpy as np
import random
import time

wn=turtle.Screen()
wn.title("cookie with probability")
wn.bgcolor("black")

wn.register_shape("C:\\Users\\User\\Desktop\\cookie.gif")


cookie = turtle.Turtle()


cookie.shape("C:\\Users\\User\\Desktop\\cookie.gif")

cookie.speed(0)


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
    
    clicks += np.random.choice(h,p=[0.6,0.3,0.1])
   
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font = ("Courier New",32,"normal"))
 

cookie.onclick(clicked)


is_paused = False

def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused=True

wn.listen()
wn.onkeypress(toggle_pause,"p")            

time_limit = 8
start_time = time.time()

while True: 


    if not is_paused:
     elapsed_time = time.time() - start_time
     print(time_limit - int(elapsed_time))
    if elapsed_time > time_limit:
    
     turtle.write("GAME OVER",align="center", font = ("Courier New",70,"normal"))
     exit()
    if clicks = 80:
      start_time = time.time()-elapsed_time + 1   
    if clicks >= 100:
     turtle.write("WELL PLAYED",align="center", font = ("Courier New",70,"normal")) 
     exit()
    else:
     start_time= time.time()-elapsed_time
     wn.update()



