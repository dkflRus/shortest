from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

from main import way

coords=[]
texts=[]

win=Tk()
win.geometry("700x500")
k=0

win.resizable(False, True)

info = Label(win,text = "Press left button to add a building (it will be switched to home automatically, for manual switching middle click it)", wraplength=700)
info.place(x = 0,y = 380)


def importCoords():
    global coords

    try:coords = [[float(w) for w in q.split(";")] for q in open(fd.askopenfilename(),"r").read().split("\n")]
    except Exception as e:info.config(text = "Error:"+e)

    update()
ttk.Button(win,text="Import",command=lambda:importCoords()).place(x=145,y=350)

def exportCoords():
    global coords

    open(fd.askopenfilename(),"w").write("\n".join([";".join([str(w) for w in q]) for q in coords]))
ttk.Button(win,text="Export",command=lambda:exportCoords()).place(x=220,y=350)

def build(event):
   global coords
   
   x=event.x
   y=event.y
   coords.append([x,y])

   update()

def delete(event):
    global coords

    #print(coords)

    n=getDot(event.x,event.y)#,minLen=15)
    if n==None:return

    x,y=coords.pop(n)
    #print(x,"|",y)
    canvas.create_oval(x,y,x,y,outline="white", width=10)

    update()

def makeHome(event):
    global coords
    n=getDot(event.x,event.y)#,minLen=15)
    if n==None or n==0:return
    coords[0],coords[n]=coords[n],coords[0]
    #print(n)
    update()
    
def getDot(x,y,minLen=None):
    global coords
    
    ans=None
    lenAns=None
    for q in range(len(coords)):
        currLen=((coords[q][0]-x)**2+(coords[q][1]-y)**2)**.5
        if lenAns==None or currLen<lenAns:
            ans=q
            lenAns=currLen
    if minLen==None or minLen<=lenAns:return ans
    else:pass#print(ans)

def update():
    global coords,texts

    #print(coords)

    for q in texts:
        q.destroy()
    canvas.create_rectangle(0,0,700,350,fill="white",outline="white")
    
    for q in range(0,len(coords)):
        #print(q)
        x,y=coords[q]
        if q==0:canvas.create_rectangle(x-5,y-5,x+5,y+5,fill="red",outline="red")
        else:canvas.create_oval(x,y,x,y,outline="black", width=10)
        texts.append(Label(win,text = str(q)))
        texts[-1].place(x = x,y = y)

    if len(coords)==0:info.config(text = "Press left button to add a building (it will be switched to home automatically, for manual switching middle click it)")
    elif len(coords)==1:info.config(text = "Add one more building (to delete building or home right click it)")
    elif k<=0:info.config(text = "Set k (int,>0) in the text box below")
    else:
        ans,fullLen=way(coords,k)
        ans+=[0]#Логический костыль
        info.config(text="Path is "+"->".join([str(q) for q in ans])+", length is "+str(fullLen))

        for q in range(len(ans)-1):
            canvas.create_line(coords[ans[q]][0], coords[ans[q]][1], coords[ans[q+1]][0], coords[ans[q+1]][1], arrow=LAST)


def updateK(*args):
    global k

    try:
        k=kVar.get()
        update()
    except:k=0

canvas=Canvas(win, width=700, height=350, background="white")

canvas.grid(row=0, column=0)
canvas.bind('<Button-1>', build)
canvas.bind('<Button-2>', makeHome)
canvas.bind('<Button-3>', delete)

kVar = IntVar()
kEnt = Entry(win, textvariable=kVar,bd =3)
kEnt.place(x = 0,y = 350)
kVar.trace("w", updateK)

win.mainloop()