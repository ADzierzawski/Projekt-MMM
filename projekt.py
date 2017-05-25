# -*- coding: utf-8 -*-
 #!/usr/bin/python
import matplotlib.pyplot as plt
import tkinter as tkin
from PIL import ImageTk, Image
 
def rk4 (n10, n20, a1, a2, b1, b2, c1, c2, h, tk):
   
    n = int(tk/h)
    vn1 = [0] * (n + 1)
    vn2 = [0] * (n + 1)
 
    vn1[0] = n1 = n10
    vn2[0] = n2 = n20
 
    for i in range(1, (n+1)):        
        k11 = func(n1, n2, a1, b1, c1,)
        k21 = func(n2, n1, a2, b2, c2,)
 
        k12 = func(n1+k11*0.5*h, n2+k21*0.5*h, a1, b1, c1,)
        k22 = func(n2+k21*0.5*h, n1+k11*0.5*h, a2, b2, c2,)
       
        k13 = func(n1+k12*0.5*h, n2+k22*0.5*h, a1, b1, c1,)
        k23 = func(n2+k22*0.5*h, n1+k12*0.5*h, a2, b2, c2,)
       
        k14 = func(n1+k13*h, n2+k23*h, a1, b1, c1,)
        k24 = func(n2+k23*h, n1+k13*h, a2, b2, c2,)
       
        vn1[i] = n1 = n1 + h*(k11 + 2*k12 + 2*k13 + k14)/6
        vn2[i] = n2 = n2 + h*(k21 + 2*k22 + 2*k23 + k24)/6
           
    return vn1, vn2
 
def func (n_main, n_second, a, b, c):
    return n_main * (a - b*n_main - c*n_second)

plt.ion()
plt.rcParams['figure.figsize'] = 10,8

def plot(vt, vn1, vn2):
    plt.figure()
    plt.plot(vt, vn1, label='pierwszy gatunek')
    plt.plot(vt, vn2, label='drugi gatunek')
    plt.xlabel('czas')
    plt.ylabel('populacja')
    plt.title('')
    plt.legend(loc=0)
    plt.savefig('wykres.png', bbox_inches='tight')
    plt.close()
 
n10 = 100000
n20 = 100000
a1 = 0.1
a2 = 0.1
b1 = 0.0000008
b2 = 0.0000008
c1 = 0.000001
c2 = 0.0000001
 
h = 1
tk = 100
names = ["populacja 1: ","urodzenia","populacja","choroby","walka","populacja 2: ","urodzenia","populacja","choroby","walka","parametry:","krok","czas sym."]
variables = [0,a1,n10,b1,c1,0,a2,n20,b2,c2,0,h,tk] 

vn1, vn2 = rk4(n10, n20, a1, a2, b1, b2, c1, c2, h, tk)
 
vt = [0] * int(tk/h + 1)
for i in range(0, int(tk/h + 1)):
    vt[i] = h*i
 
#for x, y, z in list(zip(vt, vn1, vn2)):
#    print("%5.1f %12.3f %12.3f" % (x, y, z)
            
plot(vt, vn1, vn2)

top = tkin.Tk()

def readVariables():
    p=1
    global params
    params = [0] * 13
    for i in names:
        if (p!= 1 and p!=6 and p!=11):
            params[p-1] = float(entry_box[p-1].get())
            #print(params[p-1])
        p+=1
    vn1, vn2 = rk4(params[2],params[7], params[1], params[6], params[3], params[8], params[4], params[9], params[11], params[12])

    vt = [0] * int(params[12]/params[11] + 1)
    for i in range(0, int(params[12]/params[11] + 1)):
        vt[i] = params[11]*i
      
    plt.ion()
    plt.rcParams['figure.figsize'] = 10,8
            
    plot(vt, vn1, vn2)
    img[0] = ImageTk.PhotoImage(Image.open("wykres.png"))
    panel = tkin.Label(top, image = img[0])
    panel.grid(row= 1, rowspan = len(names) , column=3)
    
    
def insertDefault():
    global entry_box
    n=1
    entry_box = dict()
    for i in names:
        tkin.Label(top, text=str(names[n-1])).grid(row=n, column=1)
        if (n!= 1 and n!=6 and n!=11):
                entry_box_var= tkin.StringVar()
                entry_box[n-1]= tkin.Entry(top, textvariable=str(entry_box_var))
                entry_box[n-1].grid(row=n, column=2)
                entry_box_var.set(variables[n-1])
        n+=1


insertDefault()

default = tkin.Button(top, text="wpisz domyslne", bd=5, command = insertDefault ).grid(row=len(names)+1, column=1)    
confirm = tkin.Button(top, text="wczytaj", bd = 5, command = readVariables ).grid(row=len(names)+1, column=2)   #command = readVariables 
img= [None]
img[0] = ImageTk.PhotoImage(Image.open("wykres.png"))
panel = tkin.Label(top, image = img[0])
panel.grid(row= 1, rowspan = len(names) , column=3)
top.mainloop()