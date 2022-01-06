# gui-events
## F1.8.02.L1 - Clicker v2
De klikker word nu geel als je met je cursor over het label gaat
``` python

def yellowBackground(event):
    root.configure(bg = "yellow")

def colourChanges(event):
    global count
    if count > 0:
        root.configure(bg = "green")
    elif count < 0:
        root.configure(bg = "red")
    else:
        root.configure(bg = "grey")

def Up():
    global count
    count += 1
    countLabel.configure(text = count)
    colourChanges("")

def down():
    global count
    count -= 1
    countLabel.configure(text = count)
    colourChanges("")

countLabel.bind("<Enter>", yellowBackground)
countLabel.bind("<Leave>", colourChanges)
root.mainloop()
``` 
Ik heb dus .bind gebruikt, 1 functie bijgevoegd, 1 functie aangepast met event 
en 2 functies aangepast met het aanroepen van de functie colourChanges
## F1.8.02.L2 - Clicker v3
De klikker kan nu het getal x3 doen of /3
``` python 
countCheck = ""

def multiplyOrDivide(event):
    global count, countCheck
    if countCheck == "Multiply":
        count *= 3
    elif countCheck == "Divide":
        count /= 3 
    countLabel.configure(text = count)

def Up():
    global count, countCheck
    count += 1
    countLabel.configure(text = count)
    colourChanges("")
    countCheck = "Multiply"
    
def down():
    global count, countCheck
    count -= 1
    countLabel.configure(text = count)
    colourChanges("")
    countCheck = "Divide"

countLabel.bind("<Double-Button>", multiplyOrDivide)
```
1 variable erbij gezet, 1 functie erbij geplaatst en 2 functies aangepast
en de muis knop verbonden (alleen met dubbel klikken)
## F1.8.02.L3 - Clicker v4
Ik heb nu wat knoppen verbonden met het programma
``` python
def upButton(event):
    up()

def downButton(event):
    down()

def spaceButton(event):
    multiplyOrDivide("")

root.bind("<Up>", upButton) and root.bind("<+>", upButton)
root.bind("<Down>", downButton) and root.bind("-", downButton)
root.bind("<space>", spaceButton)
```
3 nieuwe functies en paar knoppen verbonden met het programma
(Ik heb ook de functie up() naar kleine letters veranderd)
## F1.8.02.O2 - Simple FPS trainer v1
Hierbij de Simple FPS trainer
``` python
import tkinter as tk
import sys
import os
from tkinter.messagebox import askyesno
import random

root = tk.Tk()
root.title("Simple FPS trainer")
root.geometry("500x500")
root.configure(bg="DarkOliveGreen4")
timer = 20
points = 0
taskLists = ["w", "a", "s", "d", "space", "<Button>", "<Double-Button>", "<Triple-Button>"]

def buttonTask():
    task = random.choice(taskLists)
    taskLabel = tk.Label(root, text = "Press: " + task, font =("Arial", 14))
    taskLabel.pack()
    taskLabel.place(x=random.randint(0,385), y=random.randint(75,450))
    def keyTask(event):
        global points
        taskLabel.destroy()
        points += pointValue        
        labelPoints.configure(text = (str(points) + " points"))
        if task == "a" or task == "w" or task == "s" or task == "d" or task == "space":
            root.unbind("<"+task+">")
        root.after(500, buttonTask)
    if task == "<Button>" or task == "<Double-Button>" or task == "<Triple-Button>":
        pointValue = 2
        taskLabel.bind(task, keyTask)
        if task == "<Button>":
            taskLabel.configure(text = "Singel click")
        elif task == "<Double-Button>":
            taskLabel.configure(text = "Double click")
        elif task == "<Triple-Button>":
            taskLabel.configure(text = "Triple click")
    else:
        pointValue = 1
        root.bind(("<"+task+">"), keyTask)

def start():
    global timer
    startButton.destroy()
    labelTimer.configure(text ="Time remaining " + str(timer))
    if timer > 0:
        timer -= 1      
        root.after(1000, start)
    else:
        YesOrNo()

def YesOrNo(): 
    answer = askyesno(
        title = "Again",
        message = "Congratulations, you have " + str(points) + " points, wanna play again?")
    if answer:
        restart()
    else:
        root.destroy()

# Als je deze functie aanroept, dan restart hij het programma
def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
        
labelTimer = tk.Label(
    root,
    text = ("Time remaining " + str(timer)),
    font = ("Arial", 16),
    bg = "grey5",
    fg = "snow"
)
labelTimer.place(relwidth=0.5, anchor = "nw")

labelPoints = tk.Label(
    root,
    text = (str(points) + " points"),
    font = ("Arial", 16),
    bg = "grey5",
    fg = "snow"
)
labelPoints.place(relx = 1.0,  relwidth=0.5, anchor = "ne")

startButton = tk.Button(
    root,
    font = ("Arial", 16),
    bg = "snow",
    fg = "grey5",
    command = lambda:[start(), buttonTask()],
    text = "Click here to start",
)
startButton.pack()
startButton.place(relx = 0.5, rely = 0.5, anchor = "center")

root.mainloop()
```
