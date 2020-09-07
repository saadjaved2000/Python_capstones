import tkinter as tk
from tkinter import *
import tkinter.messagebox
Window = tk.Tk()
Window.title("Tic Tac Toe")

pa = tk.StringVar()
pb = tk.StringVar()
p1 = tk.StringVar()
p2 = tk.StringVar()

player1_name = tk.Entry(textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = tk.Entry(textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 0

def finish():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)



def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, pb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        pb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        Win()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        Win()
        flag += 1
    else:
        tk.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def Win():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        finish()
        tk.messagebox.showinfo("Tic-Tac-Toe", pa)

    elif(flag == 8):
        tk.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        finish()
        tk.messagebox.showinfo("Tic-Tac-Toe", pb)


buttons = tk.StringVar()

label = tk.Label(text="Player 1:", font=('arial', 20), bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)


label = tk.Label(text="Player 2:", font=('arial', 20), bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)

button1 = tk.Button(text=" ", font=('arial', 20), bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = tk.Button(text=' ', font=('arial', 20), bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = tk.Button(text=' ',font=('arial', 20), bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = tk.Button(text=' ', font=('arial', 20), bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = tk.Button(text=' ', font=('arial', 20), bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = tk.Button(text=' ', font=('arial', 20), bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = tk.Button(text=' ', font=('arial', 20), bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = tk.Button( text=' ', font=('arial', 20), bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = tk.Button(text=' ', font=('arial', 20), bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

tk.mainloop()
