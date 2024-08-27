from tkinter import *
from tkinter import messagebox

import base64
import os

def decrypt():
    key = code.get()

    if key == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.resizable(0, 0)
        screen2.configure(bg="#00bd56")

        message = text.get(1.0, END)
        dec_message = message.encode("ascii")
        base64_bytes = base64.b64decode(dec_message)
        base64_message = base64_bytes.decode("ascii")

        Label(screen2, text="decrypted Message: ", font="arial 10 bold", bg="#00bd56", fg="white").place(x=10, y=10)
        text2 = Text(screen2, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, base64_message)
    elif key == "":
        messagebox.showerror("Error", "Input Key")
    elif key != "1234":
        messagebox.showerror("Error", "Wrong Key")

def encrypt():
    key = code.get()

    if key == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.resizable(0, 0)
        screen1.configure(bg="#ed3833")

        message = text.get(1.0, END)
        enc_message = message.encode("ascii")
        base64_bytes = base64.b64encode(enc_message)
        base64_message = base64_bytes.decode("ascii")

        Label(screen1, text="Encrypted Message: ", font="arial 10 bold", bg="#ed3833", fg="white").place(x=10, y=10)
        text2 = Text(screen1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, base64_message)
    elif key == "":
        messagebox.showerror("Error", "Input Key")
    elif key != "1234":
        messagebox.showerror("Error", "Wrong Key")


def msg():
    
    global screen
    global code
    global text

    screen = Tk()
    screen.geometry("400x500")
    screen.resizable(0, 0)

    # Icon 
    image_icon=PhotoImage(file="key.png")
    screen.iconphoto(False, image_icon)
    screen.title("Message App")

    def reset():
        text.delete(1.0, END)
        code.set("")

    # Label
    Label(screen, text=" Enter text for encryption and decryption", fg="black", font=("Calibri", 13, "bold")).place(x=20, y=10)
    # Text
    text = Text(font="robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text.place(x=20, y=40, width=360, height=250)

    # Secret Key
    Label(text="Enter Secret Key", fg="black", font=("Calibri", 13, "bold")).place(x=20, y=300)

    code=StringVar()
    Entry(textvariable=code, width=30, bd=5, font="arial 15", show="*").place(x=20, y=330)

    # Button
    Button(text="Encrypt", width=19, height=2, bg="#ed3833", bd=0, fg="white", font="arial 10 bold", command=encrypt).place(x=20, y=380)
    Button(text="Decrypt", width=19, height=2, bg="#00bd56", bd=0, fg="white", font="arial 10 bold", command=decrypt).place(x=200, y=380)
    Button(text="RESET", width=42, height=2, bg="#1089ff", bd=0, fg="white", font="arial 10 bold", command=reset).place(x=20, y=430)

    screen.mainloop()

msg()