from tkinter import *

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = Tk()
root.geometry("400x600")
root.title("Calculator")

screen = StringVar()

entry = Entry(root, textvar=screen, font="lucida 30 bold")
entry.pack(fill=X, ipadx=8, pady=10, padx=10)

button_frame = Frame(root)
button_frame.pack()

list_of_numbers = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
i = 0
for number in list_of_numbers:
    button = Button(button_frame, text=number, font="lucida 15 bold")
    button.grid(row=int(i/3), column=i%3, padx=2, pady=2)
    button.bind("<Button-1>", click)
    i += 1

list_of_operators = ['+', '-', '*', '/', 'C', '=']
i = 0
for operator in list_of_operators:
    button = Button(button_frame, text=operator, font="lucida 15 bold")
    button.grid(row=int(i/2)+4, column=i%2, padx=2, pady=2)
    button.bind("<Button-1>", click)
    i += 1

root.mainloop()