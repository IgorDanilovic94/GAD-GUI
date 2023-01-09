import tkinter as tk

root = tk.Tk()

width=400
height=400


canvas=tk.Canvas(root,width=400,height=400)

canvas.pack()

kvadrat1=canvas.create_rectangle(150, 150, 190, 190, fill='blue', outline='blue')
kvadrat2=canvas.create_rectangle(210, 210, 250, 250, fill='green', outline='green')
kvadrat3=canvas.create_rectangle(210, 150, 250, 190, fill='red', outline='red')
kvadrat4=canvas.create_rectangle(150, 210, 190, 250, fill='yellow', outline='yellow')

def redraw():
    kordinate_kvadrata1 = canvas.coords(kvadrat1)
    kordinate_kvadrata2 = canvas.coords(kvadrat2)
    kordinate_kvadrata3 = canvas.coords(kvadrat3)
    kordinate_kvadrata4 = canvas.coords(kvadrat4)

    #if (kordinate_kvadrata1[1] == 0):
            #root.after(1, root.destroy)
    
    canvas.move(kvadrat1, -5, -5)
    canvas.move(kvadrat2, 5, 5)
    canvas.move(kvadrat3, 5, -5)
    canvas.move(kvadrat4, -5, 5)

    canvas.after(80,redraw)

redraw()


root.mainloop()

