from tkinter import *
from random import *

root=Tk()
root.configure(bg="#83f0f2")
root.title("RATOS : THE RUN")
#root.attributes("-fullscreen",True)

def get_number(x):
	if x == '\u2680':
		return(1)
	elif x == '\u2681':
		return(2)
	elif x == '\u2682':
		return(3)
	elif x == '\u2683':
		return(4)
	elif x == '\u2684':
		return(5)
	elif x == '\u2685':
		return(6)

def dice(a):
    for i in range(60):
        if (i<=a):
            Label(root,bg="#f257a7",width=2,height=1).place(x=(i+5)*22,y=350)
        else:
            Label(root,bg="#0f0c69",width=2,height=1).place(x=(i+5)*22,y=350)

def dice2(b):
    for i in range(60):
        if (i<=b):
            Label(root,bg="#f257a7",width=2,height=1).place(x=(i+5)*22,y=425)
        else:
            Label(root,bg="#0f0c69",width=2,height=1).place(x=(i+5)*22,y=425)

x2 = x1 = 0
j = kam =1

def roll_dice():
        global x2,j,kam,x1
        d1 = choice(my_dice)
        sd1 = get_number(d1)
        dice_label1.config(text=d1)
        total = sd1
        if(kam %2 == 0):
                if (j==2):
                        x1 = (total-1)+x1
                else:
                        x1 = (total)+x1
                j+=1
                if (x1==59):
                        dice2(x1)
                        my_button.config(text="PLAYER-1")
                        result.config(text="PLAYER-2 HAS WON THE GAME CONGRATULATIONS!!!")
                elif (x1>59):
                        x1=x1-total
                        total_label.config(text=f"PLAYER-2 NEEDED {59-x1} TRY AGAIN!")
                        my_button.config(text="PLAYER-1")
                else:
                        dice2(x1)
                        total_label.config(text=f"PLAYER-2 ROLLED : {total}")
                        my_button.config(text="PLAYER-1")
        else:
                if (j==1):
                        x2 = (total-1)+x2
                else:
                        x2 = (total)+x2
                j+=1
                if (x2==59):
                        dice(x2)
                        result.config(text="PLAYER-1 HAS WON THE GAME CONGRATULATIONS!!!")
                elif (x2>59):
                        x2=x2-total
                        total_label.config(text=f"PLAYER-1 NEEDED {59-x2} TRY AGAIN!")
                        my_button.config(text="PLAYER-2")
                else:
                        dice(x2)
                        total_label.config(text=f"PLAYER-1 ROLLED : {total}")
                        my_button.config(text="PLAYER-2")
        kam +=1

my_dice = ['\u2680', '\u2681','\u2682','\u2683','\u2684','\u2685',]

title=Label(root,text=" RATOS : THE RUN ",font=("MS Serif",40,"bold"),fg="#fc036b",bg="#83f0f2").pack(pady=25)

total_label = Label(root, text="", font=("Arial Black", 25), fg="#075e06", bg="#83f0f2")
total_label.pack(pady=20)

result=Label(root,text="",font=("Arial Black",30),fg="#0f0c69",bg="#83f0f2")
result.pack(pady=20)

dice_label1 = Label(root, text='\u2685', font=("Helvetica", 125), fg="#075e06",bg="#83f0f2")
dice_label1.place(x=700, y=450)

s1=Label(root,text=" 1 ",font=("Arial Black",30),fg="#0f0c69",bg="#83f0f2")
s1.place(x=50,y=330)
s2=Label(root,text=" 2 ",font=("Arial Black",30),fg="#0f0c69",bg="#83f0f2")
s2.place(x=50,y=402)

my_frame=Frame(root,bg="#83f0f2")
my_frame.place(x=1450,y=325)
f1=Label(my_frame,text=" E ",font=("Arial Black",25),fg="#0f0c69",bg="#83f0f2")
f1.pack()
f2=Label(my_frame,text=" N ",font=("Arial Black",25),fg="#0f0c69",bg="#83f0f2")
f2.pack()
f3=Label(my_frame,text=" D ",font=("Arial Black",25),fg="#0f0c69",bg="#83f0f2")
f3.pack()


my_button = Button(root, text="PLAYER-1", command=roll_dice, font=("Arial Black", 20),bg="#83f0f2",fg="#075e06")
my_button.place(x=680,y=625)

root.mainloop()


