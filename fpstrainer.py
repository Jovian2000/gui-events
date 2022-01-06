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
        root.unbind(task)
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