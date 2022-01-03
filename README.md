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
