import tkinter as tk 

#create main window
root=tk.Tk()
root.title("Simple Animation")

#create Canvas
canvas=tk.Canvas(root,width="400",height="300",bg="white")
canvas.pack()

#create Oval
oval=canvas.create_oval(50,50,100,100,fill="brown")

#move oval function
def move_oval():
    canvas.move(oval,2,0) #moves right by 2 pixels.
    canvas.after(50,move_oval) #call again after 50 ms

#starts the animation
move_oval()

#run the application
root.mainloop()