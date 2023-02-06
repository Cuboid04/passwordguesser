from tkinter import *
root=Tk()
root.title("Password Guesser")
root.geometry("600x600")

import random 
label=Label(root)
array_3d=[[["A","B","C","D","E","F","G","H"],["king","queen"],["1","2","3","4","5","6"]]]
newpass=Label(root)
guess=Entry(root)

def generate():
    random_no1=random.randint(0,7)
    random_no2=random.randint(0,1)
    random_no3=random.randint(0,5)
    guessedpass=guess.get()
    l1=array_3d[0][0][random_no1]
    l2=array_3d[0][1][random_no2]
    l3=array_3d[0][2][random_no3]
    newpass["text"] = "New Password = " + l1+l2+l3
    
    label["text"]= "Guessed Password = " + str(guessedpass)
    
btn=Button(root, text="New Password", command=generate)
btn.place(relx=0.5, rely=0.6, anchor=CENTER)
label.place(relx=0.5, rely=0.5, anchor=CENTER)
newpass.place(relx=0.5, rely=0.7, anchor=CENTER)
guess.place(relx=0.5, rely=0.4, anchor=CENTER)

root.mainloop()