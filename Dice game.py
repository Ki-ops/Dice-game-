from tkinter import *
from PIL import ImageTk,Image
import random 

root=Tk()
root.title("!Endless Dice Game!")
root.geometry("600x400")

root.configure(background="Black")
img=ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

P1=Label(root,text="Player 1",bg="Black",fg="White",font=("Arial",18))
P1.place(relx=0.2,rely=0.3,anchor=CENTER)

P2=Label(root,text="Player 2",bg="Black",fg="White",font=("Arial",18))
P2.place(relx=0.8,rely=0.3,anchor=CENTER)

P1_score=Label(root,bg="Black",fg="White",font=("Arial",18))
P1_score.place(relx=0.2,rely=0.4,anchor=CENTER)

P2_score=Label(root,bg="Black",fg="White",font=("Arial",18))
P2_score.place(relx=0.8,rely=0.4,anchor=CENTER)

dice=Label(root,bg="Blue",fg="White",font=("Arial",18))
dice.place(relx=0.5,rely=0.5,anchor=CENTER)
player1_score=0
player2_score=0

def player_1():
    global player1_score
    r=random.randint(1, 6)
    dice["text"]="Player one dice number: "+str(r)
    player1_score=player1_score + r
    P1_score["text"]=str(player1_score)

def player_2():
    global player2_score
    r=random.randint(1,6)
    dice["text"]="Player two dice number: "+str(r)
    player2_score=player2_score + r
    P2_score["text"]=str(player2_score)
    
    
btn_1=Button(root,image=img,command=player_1)
btn_1.place(relx=0.2,rely=0.6,anchor=CENTER)

btn_2=Button(root,image=img,command=player_2)
btn_2.place(relx=0.8,rely=0.6,anchor=CENTER)


root.mainloop()

