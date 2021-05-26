import turtle
import random
from playsound import playsound
import time



# wn setup
res1 = 300
res2 = 300
wn = turtle.Screen()
wn.screensize(res1, res2)
wn.title("MouseAndCat game by peanutcuber")
wn.tracer()
wn.addshape('mouse.gif')
wn.addshape('cat.gif')
wn.bgpic('bg.gif')
# music

playsound('8bit.mp3', block=False)


# main


def game():
    global wn


    # cat setup
    c = turtle.Turtle()
    c.color('red')
    c.shape('cat.gif')
    c.penup()
    c.setpos(0, 0)

    # mouse setup
    m = turtle.Turtle()
    m.color("green")
    m.speed(3)
    m.shape("mouse.gif")
    m.penup()
    m.setpos(random.randint(-300, 300), random.randint(-300, 300))

    # score
    currentscore = 0
    sf = open(r'highscore.txt', "a+")
    sf.close()
    sf = open(r'highscore.txt', "r")
    rl = int('0' + sf.read())

    # pen1

    p1 = turtle.Turtle()
    p1.penup()
    p1.ht()
    p1.setpos(150, 300)
    p1.color('black')
    p1.write("highscore:" + str(rl), align='center',
            font=("Comic Sans MS", 20, "normal"))


    # pen2
    p2 = turtle.Turtle()
    p2.penup()
    p2.speed(0)
    p2.ht()
    p2.setpos(-150, 300)
    p2.color('black')
    p2.write("current score:" + str(currentscore), align='center')

    # pen3
    p3 = turtle.Turtle()
    p3.penup()
    p3.speed(0)
    p3.ht()
    p3.setpos(0, 300)
    p3.color('black')
    p3.write("work", align='center', font=("Comic Sans MS", 10, "normal"))
    # movement


    def playerUp():
        c.sety(c.ycor()+20)


    def playerDown():
        c.sety(c.ycor()-20)


    def playerRight():
        c.setx(c.xcor()+20)


    def playerLeft():
        c.setx(c.xcor()-20)

    wn.listen()
    wn.onkeypress(playerUp, "w")
    wn.onkeypress(playerDown, "s")
    wn.onkeypress(playerRight, "d")
    wn.onkeypress(playerLeft, "a")



    strt = wn.textinput('start me','plz')
    if strt is None or strt.lower().startswith('y'):
        Startime = time.time()
        while True:
            wn.listen()
            timer = int(time.time()-Startime)
            p3.undo()
            p3.write(timer)
            p2.undo()
            p2.write("current score:" + str(currentscore),align='center', font=("Comic Sans MS", 20, "normal"))
            x = random.randint(-300, 300)
            y = random.randint(-300, 300)
            m.setheading(m.towards(x, y))
            m.goto(x, y)
            if timer <= 30:
                if m.distance(c.pos()) <= 80:
                    currentscore += 1


            else:
                if currentscore > rl:
                    sf.close()
                    sf = open('highscore.txt', "w+")
                    sf.write(str(currentscore))
                    sf.close()
                    wn.textinput("New Recored", 'Vewy Good')
                    break
                else:
                    sf.close()
                    wn.textinput("Noob", 'noobity noob')
                    break

        def restart():
            rstrt = wn.textinput('Restart?', 'yes')
            if rstrt is None or rstrt.lower().startswith('y'):
                wn.clear()
                game()
            else:
                wn.clear()
                wn.bye()
        restart()
    else:
        wn.clear()
        wn.bye()

game()
