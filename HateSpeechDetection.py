from tkinter import *
from textblob import TextBlob
import mysql.connector
from tkinter import messagebox
def comments():
    global y
    y=""
    conn=mysql.connector.connect(host="localhost::3306",user="root",passwd="muskan",database="comment")
    cursor=conn.cursor()
    sql="select * from comments"
    cursor.execute(sql)
    data=cursor.fetchall()
    for x in data:
        y=y+x[0]+'\n'+'\n'
    comment2.config(text=y,font=('Helvetica',10))
   
def file():
    global x
    global string
    string=""
    with open('lex.txt','r') as f:
        x=f.readline()
        while len(x)>0:
            string=string+x
            x=f.readline()
def sentiment():
    global sens
    coms=comment.get()
    blob=TextBlob(coms)
    if((blob.sentiment.polarity)<0):
        comment.delete(0,END)
        messagebox.showinfo("ALERT", "Obnoxious comment")
    else:
        conn= mysql.connector.connect(host="localhost::3306",user="root",passwd="muskan",database="comment")
        cursor=conn.cursor()
        coms=str(coms)
        sql="INSERT INTO comments (com) VALUES ('{}');".format(coms)
        cursor.execute(sql)
        conn.commit()
        comment.delete(0,END)
         
window=Tk()

window.title("BLOG")
window.configure(background='white')
f=Frame(window)
f.pack()
blog=Label(f,font=('Times New Roman',12))
file()

blog.pack(side=LEFT,fil=BOTH)
blog.config(text=str(string),fg="black",bg="white")
##f2=Frame(window)
##f2.pack()
##f4=Frame(window)
##f4.pack(side=LEFT)
f3=Frame(window)
f3.pack(side=LEFT)
##comment3=Label(f3,text="COMMENTS\n",fg="black",bg="white",font=("Arial",15))
comment2=Label(f3,fg="black",bg="white")
comments()
comment2.pack(side=LEFT)

f4=Frame(window)
f4.pack(side=BOTTOM)

comment=Entry(f4,width=100)
comment.pack()
b=Button(f4,text="comment",command=sentiment,bg="white")
b.pack(side=BOTTOM)
window.mainloop()
