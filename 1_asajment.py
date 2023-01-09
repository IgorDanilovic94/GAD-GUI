from tkinter import *
counter=0
def mouse_click(event):
    global counter
    print('Brojac ocitava: ',counter)
    counter+=1

window = Tk()
window.minsize(500, 400)
label = Label( window, text="Click here")
label.pack()

label.bind( "<Triple-Button>", mouse_click)

window.mainloop()
