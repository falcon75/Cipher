from tkinter import *
import message as msg

def encode():
    line = msg.message(messageInputE.get())
    outputE.delete(0.0, END)
    outputE.insert(END, line.caesar(int(shiftInputE.get())))

def decode():
    line = msg.message(messageInputD.get())
    outputD.delete(0.0, END)
    outputD.insert(END, line.caesar(int(shiftInputD.get())*-1))
    

window = Tk()
window.title("Caeser Cipher")
window.configure(background="white")

Label (window, bg="black", width=77) .grid(row=1, columnspan=5)
Label (window, text="Caesar Cipher Program", bg="white", fg="black", font="none 20 bold") .grid(row=2, column=0, columnspan=5, ipadx=5, ipady=5)
Label (window, bg="black", width=77) .grid(row=3, columnspan=5)
Label (window, text="Message:", bg="white", fg="black", font="none 12") .grid(row=4, column=0, sticky=W)
Label (window, text="Shift:", bg="white", fg="black", font="none 12") .grid(row=4, column=1, sticky=W)
Label (window, text="Output:", bg="white", fg="black", font="none 12") .grid(row=4, column=3, sticky=W)

messageInputE = Entry(window, width=40)
messageInputE.grid(row=5, column=0, sticky=W)
shiftInputE = Entry(window, width=5)
shiftInputE.grid(row=5, column=1, sticky=W)
messageInputD = Entry(window, width=40)
messageInputD.grid(row=6, column=0, sticky=W)
shiftInputD = Entry(window, width=5)
shiftInputD.grid(row=6, column=1, sticky=W)

Button(window, text="Encode", width=7, command=encode) .grid(row=5, column=2, sticky=W)
Button(window, text="Decode", width=7, command=decode) .grid(row=6, column=2, sticky=W)

outputE = Text(window, height=1, width=25)
outputE.grid(row=5, column=3, sticky=W)
outputD = Text(window, height=1, width=25)
outputD.grid(row=6, column=3, sticky=W)

window.mainloop()
