from tkinter import *
from tkinter import messagebox
import base64

def decrypt():
    password = code.get()

    if password == "98889":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt_message = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Roboto 15", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        
        text2.insert(END, decrypt_message)
    
    elif password == "":
        messagebox.showerror("Decryption", "Input Password")
    
    elif password != "9889":
        messagebox.showerror("Decryption", "Invalid password")

def encrypt():
    password = code.get()

    if password == "9889":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt_message = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Roboto 15", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        
        text2.insert(END, encrypt_message)
    
    elif password == "":
        messagebox.showerror("Encryption", "Input Password")
    
    elif password != "9889":
        messagebox.showerror("Encryption", "Invalid password")

def reset():
    code.set("")
    text1.delete(1.0, END)

def main_screen():
    global screen
    global code
    global text1
    
    screen = Tk()
    screen.geometry("500x400")
    screen.title("MP-08 Message Encoder and Decoder")
    
    Label(screen, text="Enter text for encryption and decryption", fg="black", font=("Calibri", 17)).place(x=10, y=10)
    text1 = Text(screen, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=450, height=100)

    Label(screen, text="Enter Secret Key For Encryption And Decryption", fg="black", font=("Calibri", 17)).place(x=10, y=170)
    
    code = StringVar()
    Entry(screen, textvariable=code, width=25, bd=0, font=("Arial", 25), show="*").place(x=10, y=200)
    
    Button(screen, text="ENCRYPT", height=2, width=30, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(screen, text="DECRYPT", height=2, width=30, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=250, y=250)
    Button(screen, text="RESET", height=2, width=65, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)
    
    screen.mainloop()

main_screen()
