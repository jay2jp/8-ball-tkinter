from tkinter import *

from tkinter import *
from PIL import Image, ImageTk
import random


window = Tk()

window.title("ball")
text = Label(window, text = "shake the ball!", font= ("Helvetica", 25))
text.grid(column = 0, row = 0)
window.geometry('220x300')
# the switching function goes here

ball = PhotoImage(file = "blankball.png")
ball = ball.zoom(20)
ball = ball.subsample(90)
#load some images in this
# = ball.resize(width = 210, height = 400)
# tkimage = ImageTk.PhotoImage(ball)
# Tk.Label(window, image=tkimage).pack()

label = Label(window, image = ball )


def clicked():
    x = random.randrange(1,21)
    print(x)
    choices = { 1 : 'nah.gif', 2 : 'certain.gif', 3: 'notnow.gif',4: 'concentrate.gif',5: 'decided.gif', 6: 'doubt.gif', 7: 'forsure.gif', 8: 'good.gif', 9: 'hazy.gif', 10 : 'later.gif', 11: "likely.gif", 12: "nah.gif", 13: 'nat.gif', 14: 'nay.gif', 15: 'ncount.gif', 16: 'nodoubt.gif', 17: 'not now.gif', 18: 'notgood.gif', 19: 'rely.gif', 20: 'toyes.gif'}
    result = choices.get(x,'default')


    ball.configure(file= result)




btn = Button(window, text="Shake!", command = clicked)
btn.grid(column=0, row=1)

label.grid(column=0,row=2)

window.mainloop()

