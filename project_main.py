from tkinter import*
from tkinter import ttk
import tkinter.messagebox as msg
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
import time
import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import urllib
import webbrowser
import urllib.request
import sqlite3
import random
import os
from tempfile import NamedTemporaryFile
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
global tf
global tl
tf=0
tl=0
global L
L=[]
global rol
rol=[]
file=open("room.txt","r")
l=file.readline()
while l:
    if l==None:
        break
    rol.append(l[:3])
    l=file.readline()
file.close()
def checkout1(w):
    w.destroy()
    win=Tk()
    win.title("check out")
    win.geometry("600x401")
    win.config(background="midnight blue")
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:main(win)).place(x=10,y=20)
    
    Label(win,text="Check Out",font=('Segoe UI Semibold',22,'bold'),height=1,width=25,bg='gold',fg='black').place(x=100,y=30)
    Label(win,text="Name",font=('Segoe UI Semibold',20,'bold'),bg='gold',fg='black').place(x=100,y=150)
    global cname
    cname=Entry(win,font=('Segoe UI Semibold',20,'bold'))
    cname.place(x=180,y=150)
    Label(win,text="Room No.",font=('Segoe UI Semibold',20,'bold'),bg='gold',fg='black').place(x=50,y=200)
    global crno
    crno=Entry(win,font=('Segoe UI Semibold',20,'bold'))
    crno.place(x=181,y=200)
    Button(win,text='Check Out',font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black',command=lambda:checkout2(win)).place(x=250,y=300)
    win.mainloop()

def checkout2(w):
    top=Toplevel()
    top.title("Check Out")
    top.geometry('1024x768')
    top.config(background="midnight blue")
    Label(top,text='Thank You for Visting Us',font=('Segoe UI Semibold',36,'bold'),height=1,bg='gold',fg='black').place(x=200,y=30)
    global crlist
    global refno
    global rol
    global cname
    global crno
    global rr
    nam=cname.get()
    rno=crno.get()
    rr=0
    
    fc=open("custlog.txt","r+")
    l1=fc.readline()
    if l1!=None:
        s=l1.split()
        b=0
        while l1:
            b+=1
            if nam==s[0]:
                l1.replace(s[0]," ")
                l1.replace(s[1]," ")
                l1.replace(s[2]," ")
            l1=fc.readline()    
    fc.close()
    if rol!=None:
        if rno in rol:
            p=rol.pop(rno)
            p=0
    if rno[0]=='1':
        rr=2000
    if rno[0]=='2':
        rr=4000
    if rno[0]=='3':
        rr=6000
    if rno[0]=='4':
        rr=8000
    if rno[0]=='5':
        rr=10000
    Button(top,text="Click here to get Receipt",font=('Segoe UI Semibold',20,'bold'),bg='gold',fg='black',command=lambda:receipt()).place(x=380,y=175)
    l=Label()
    for i in range(10,0,-1):
        l["text"]=i
        top.update()
        time.sleep(1)
    l["text"]="Done"
    crlist.clear()
    top.destroy()
    w.destroy()
    win=Tk()
    main(win)
    win.mainloop()
def laundry(w):
    w.destroy()
    win = Tk()
    win.geometry("890x580")
    win.title(" LAUNDRY ")
    win.configure(bg="midnight blue")
    Tops = Frame(win,bg="midnight blue",width = 1600,height=50,relief=SUNKEN)
    Tops.pack(side=TOP)
    f1 = Frame(win,width = 900,bg="midnight blue",height=700,relief=SUNKEN)
    f1.pack(side=LEFT)
    f2 = Frame(win ,bg="midnight blue",width = 400,height=700,relief=SUNKEN)
    f2.pack(side=RIGHT)
    lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="LAUNDRY",bg="gold",fg="Black",bd=10,anchor='w')
    lblinfo.grid(row=0,column=0)
    def Ref():
        x=random.randint(12980, 50876)
        randomRef = str(x)
        rand.set(randomRef)
        cof =int(shirt.get())
        colshirt= int(pant.get())
        cob= int(vests.get())
        cofi= int(bags.get())
        cochee= int(briefs.get())
        codr= int(socks.get())
        costofshirt = cof*25
        costofpant = colshirt*40
        costofvests = cob*350
        costofbags = cofi*50
        costofcolourvests = cochee*30
        costofsocks = codr*35
        costofmeal = "Rs.",str('%.2f'% (costofshirt +  costofpant + costofvests + costofbags + costofcolourvests + costofsocks))
        PayTax=((costofshirt +  costofpant + costofvests + costofbags +  costofcolourvests + costofsocks)*0.33)
        Totalcost=(costofshirt +  costofpant + costofvests + costofbags  + costofcolourvests + costofsocks)
        Ser_Charge=((costofshirt +  costofpant + costofvests + costofbags + costofcolourvests + costofsocks)/99)
        Service="Rs.",str('%.2f'% Ser_Charge)
        OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
        global tl
        tl=0
        tl=int(PayTax + Totalcost + Ser_Charge)
        PaidTax="Rs.",str('%.2f'% PayTax)
        Service_Charge.set(Service)
        cost.set(costofmeal)
        Tax.set(PaidTax)
        Subtotal.set(costofmeal)
        Total.set(OverAllCost)
        rand.set("")
        shirt.set("")
        pant.set("")
        vests.set("")
        bags.set("")
        socks.set("")
        briefs.set("")
    def back(w):
        Subtotal.set("")
        cost.set("")
        Total.set("")
        Service_Charge.set("")
        Tax.set("")
        w.destroy()
        win=Tk()
        checkin(win)
    rand = StringVar()
    shirt = StringVar()
    pant = StringVar()
    vests = StringVar()
    bags = StringVar()
    Subtotal = StringVar()
    Total = StringVar()
    Service_Charge =StringVar()
    socks = StringVar()
    Tax = StringVar()
    cost = StringVar()
    briefs = StringVar()
    lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="red",bg="midnight blue",bd=20,anchor='w')
    lblreference.grid(row=0,column=0)
    txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=6,bg="gold" ,justify='right')
    txtreference.grid(row=0,column=1)
    lblshirt = Label(f1, font=( 'aria' ,16, 'bold' ),text="  shirt ",fg="gold",bg="midnight blue",bd=10,anchor='w')
    lblshirt.grid(row=2,column=0)
    txtshirt = Entry(f1,font=('ariel' ,16,'bold'), textvariable=shirt , bd=6,insertwidth=4,bg="gold" ,justify='right')
    txtshirt.grid(row=2,column=1)
    lblpant = Label(f1, font=( 'aria' ,16, 'bold' ),text="pant ",fg="gold",bg="midnight blue",bd=10,anchor='w')
    lblpant.grid(row=3,column=0)
    txtpant = Entry(f1,font=('ariel' ,16,'bold'), textvariable=pant , bd=6,insertwidth=4,bg="gold" ,justify='right')
    txtpant.grid(row=3,column=1)
    lblvests = Label(f1, font=( 'aria' ,16, 'bold' ),text="vests ",fg="gold",bg="midnight blue",bd=10,anchor='w')
    lblvests.grid(row=4,column=0)
    txtvests = Entry(f1,font=('ariel' ,16,'bold'), textvariable=vests , bd=6,insertwidth=4,bg="gold" ,justify='right')
    txtvests.grid(row=4,column=1)
    lblbags = Label(f1, font=( 'aria' ,16, 'bold' ),text="bags ",fg="gold",bg="midnight blue",bd=10,anchor='w')
    lblbags.grid(row=5,column=0)
    txtbags = Entry(f1,font=('ariel' ,16,'bold'), textvariable=bags , bd=6,insertwidth=4,bg="gold" ,justify='right')
    txtbags.grid(row=5,column=1)
    lblbriefs = Label(f1, font=( 'aria' ,16, 'bold' ),text=" brief",fg="gold",bg="midnight blue",bd=10,anchor='w')
    lblbriefs.grid(row=6,column=0)
    txtbriefs = Entry(f1,font=('ariel' ,16,'bold'), textvariable=briefs , bd=6,insertwidth=4,bg="gold" ,justify='right')
    txtbriefs.grid(row=6,column=1)
    lblsocks = Label(f1, font=( 'aria' ,16, 'bold' ),text="socks",fg="gold",bg="midnight blue",bd=10,anchor='w')
    lblsocks.grid(row=1,column=0)
    txtsocks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=socks , bd=6,insertwidth=4,bg="gold" ,justify='right')
    txtsocks.grid(row=1,column=1)
    lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cost",fg="gold",bg="midnight blue",bd=10,anchor='w')
    lblcost.grid(row=2,column=2)
    txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="grey" ,justify='right')
    txtcost.grid(row=2,column=3)
    lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="gold",bg="midnight blue",bd=10,anchor='w')
    lblService_Charge.grid(row=3,column=2)
    txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="grey" ,justify='right')
    txtService_Charge.grid(row=3,column=3)
    lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="gold",bg="midnight blue",bd=10,anchor='w')
    lblTax.grid(row=4,column=2)
    txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="grey" ,justify='right')
    txtTax.grid(row=4,column=3)
    lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="gold",bg="midnight blue",bd=10,anchor='w')
    lblSubtotal.grid(row=5,column=2)
    txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="grey" ,justify='right')
    txtSubtotal.grid(row=5,column=3)
    lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="red",bg="midnight blue",bd=10,anchor='w')
    lblTotal.grid(row=6,column=2)
    txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="gold" ,justify='right')
    txtTotal.grid(row=6,column=3)
    btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="gold",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="red",command=lambda:Ref())
    btnTotal.grid(row=8, column=1)
    btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="gold",font=('ariel' ,16,'bold'),width=10, text="BACK", bg="red",command=lambda:back(win))
    btnexit.grid(row=8, column=3)
    win.mainloop()

def rmdin(w):
    w.destroy()
    win=Tk()
    win.title("Room Dining")
    win.geometry('600x401')
    win.config(background="cyan")
    photo=PhotoImage(file='order.gif')
    Label(win,image=photo).place(x=0,y=0)
    Label(win,text="Place Your Order",font=('Segoe UI Semibold',22,'bold'),height=1,bg='cyan',fg='black').place(x=150,y=30)
    vs=StringVar()
    vs.set("SOUPS")
    vst=StringVar()
    vst.set("STARTERS")
    vts=StringVar()
    vts.set("TANDOOR STARTERS")
    vsa=StringVar()
    vsa.set("SALADS")
    vq=StringVar()
    vq.set("QUESADILLAS")
    vw=StringVar()
    vw.set("WRAP")
    vp=StringVar()
    vp.set("PASTAS")
    ve=StringVar()
    ve.set("ENCHILADAS")
    vsi=StringVar()
    vsi.set("SIZZLERS")
    vsw=StringVar()
    vsw.set("SANDWICH")
    vb=StringVar()
    vb.set("BURGER")
    vpi=StringVar()
    vpi.set("PIZZAS")
    vib=StringVar()
    vib.set("INDIAN BREADS")
    vig=StringVar()
    vig.set("INDIAN GRAVY")
    vir=StringVar()
    vir.set("INDIAN RICE")
    vc=StringVar()
    vc.set("CHINIESE")
    vsm=StringVar()
    vsm.set("SMOOTHIES")
    vd=StringVar()
    vd.set("DESSERTS")
    vhb=StringVar()
    vhb.set("HOT BEVERAGES")
    vic=StringVar()
    vic.set("ICE CREAM")
    o1=OptionMenu(win,vs,"Cream of Tomato","Spicy Veg and Coriander","Sweet Corn & Veg","Cream of Spinach & mushroo").place(x=20,y=100)
    o2=OptionMenu(win,vst,"Cheese Corn Ball","French Fries","Masala Garlic Bread","Mexican Nanchos","Nanchos Veg Supreme").place(x=105,y=100)
    o3=OptionMenu(win,vts,"Paneer Tikka","Veg Seekh Kebab","Achari Paneer Tikka","Hariyali Paneer Tikka","Madrasi Mushroom","Dingri Achari Adraki").place(x=205,y=100)
    o4=OptionMenu(win,vsa,"Pasta & yoghurt Salad","Corn Bean & Pasta Salad ","Russian Salad","Green Salad").place(x=365,y=100)
    o5=OptionMenu(win,vq,"Cheese & Bean Quesadilla","Cheese & Paneer Quesadilla","Cheese & Corn Quesadilla").place(x=455,y=100)
    o6=OptionMenu(win,vw,"Mexican Veg Wrap","Paneer&Mushroom Wrap","Splender Club Wrap").place(x=20,y=150)
    o7=OptionMenu(win,vp,"Penne Arabitta","Farfalle Pesto Cream Sauce","Mexican Pasta Delight","Red Sauce Pasta").place(x=105,y=150)
    o8=OptionMenu(win,ve,"Mexican Bean & Cheese ","Spicy Paneer Enchiladas","Corn & Cheese Enchiladas").place(x=205,y=150)
    o9=OptionMenu(win,vsi,"Italian Sizzler","Indian Sizzler","Paneer & Corn Sizzler","Fricassee of Paneer & Corn").place(x=365,y=150)
    o10=OptionMenu(win,vsw,"Spicy Paneer Sandwich","Texas Veg Sandwich","Greek Veg Sandwich","Veg Club Sandwich").place(x=455,y=150)
    o11=OptionMenu(win,vb,"Veg Cheese Burger","Texas Burger","Double Burger").place(x=20,y=200)
    o12=OptionMenu(win,vpi,"Mushroom Delight Pizza","Veg Jungle Pizza","Veg Romantic Pizza","Deluxe Veg Pizza").place(x=105,y=200)
    o13=OptionMenu(win,vib,"Naan","Roti","Butter Naan","Cheese Garlic Naan","Kashmiri Naan","Butter Roti","Kulcha","Paratha").place(x=205,y=200)
    o14=OptionMenu(win,vig,"Dal Makhini","Dal Tadka","Paneer Butter Masala","Palak Paneer","Mushroom Masala","Malai Veg Kofta","Paneer Lababdar","Veg Saagwala").place(x=365,y=200)
    o15=OptionMenu(win,vir,"Pulav","Veg Briyani","Ghee Rice","Cashew Nut Rice","Veg Fried Rice").place(x=455,y=200)
    o16=OptionMenu(win,vc,"Veg Noodles","Sezchuan Noodles","Sezchuan Fried Rice","Gobi Manchurian","Mushroom Manchurian","Paneer Manchurian").place(x=20,y=250)
    o17=OptionMenu(win,vsm,"Vanila","Stawberry","Chocolate","Punjabi Lassi","Banana Lassi","La Summer Rain").place(x=105,y=250)
    o18=OptionMenu(win,vd,"Gulab Jamun","Gajar Halwa","Sizzling Brownie").place(x=205,y=250)
    o19=OptionMenu(win,vhb,"Filter Coffee","Tea","Milk","Hot Chocolate").place(x=325,y=250)
    o20=OptionMenu(win,vic,"Vanila","Stawberry","Chocolate").place(x=455,y=250)
    Button(win,text="Order Now!",font=('Segoe UI Semibold',20,'bold'),bg='gold',fg='black',command=lambda:odconf(win)).place(x=250,y=300)
    def odconf(w):
        w.destroy()
        win=Tk()
        win.title("Room Dining")
        win.geometry('1024x601')
        win.config(background="midnight blue")
        global vs1
        global vst2
        global vts3
        global vsa4
        global vq5
        global vw6
        global vp7
        global ve8
        global vsi9
        global vsw10
        global vb11
        global vpi12
        global vib13
        global vig14
        global vir15
        global vc16
        global vsm17
        global vd18
        global vhb19
        global vic20
        #Label(win,text="Your Order",font=('Segoe UI Semibold',22,'bold'),height=1,bg='gold',fg='black').place(x=250,y=20)
        Label(win,text=vs.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=20,y=30)
        vs1=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vs1.place(x=400,y=30)
        if vs.get()=="SOUPS":
            vs1.config(state=DISABLED)
        
        else:
            vs1.insert(END,"1")
        Label(win,text=vst.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=20,y=80)
        vst2=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vst2.place(x=400,y=80)
        if vst.get()=="STARTERS":
            vst2.config(state=DISABLED)
        else:
            vst2.insert(END,"1")
            
        Label(win,text=vts.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=20,y=130)
        vts3=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vts3.place(x=400,y=130)
        if vts.get()=="TANDOOR STARTERS":
            vts3.config(state=DISABLED)
        else:
            vts3.insert(END,"1")
            
        Label(win,text=vsa.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=20,y=180)
        vsa4=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vsa4.place(x=400,y=180)
        if vsa.get()=="SALADS":
            vsa4.config(state=DISABLED)
        else:
            vsa4.insert(END,"1")
            
        Label(win,text=vq.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=20,y=230)
        vq5=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vq5.place(x=400,y=230)
        if vq.get()=="QUESADILLAS":
            vq5.config(state=DISABLED)
        else:
            vq5.insert(END,"1")
            
        Label(win,text=vw.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=20,y=280)
        vw6=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vw6.place(x=400,y=280)
        if vw.get()=="WRAP":
            vw6.config(state=DISABLED)
        else:
            vw6.insert(END,"1")
            
        Label(win,text=vp.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=20,y=330)
        vp7=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vp7.place(x=400,y=330)
        if vp.get()=="PASTAS":
            vp7.config(state=DISABLED)
        else:
            vp7.insert(END,"1")
            
        Label(win,text=ve.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=20,y=380)
        ve8=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        ve8.place(x=400,y=380)
        if ve.get()=="ENCHILADAS":
            ve8.config(state=DISABLED)
        else:
            ve8.insert(END,"1")
            
        Label(win,text=vsi.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=20,y=430)
        vsi9=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vsi9.place(x=400,y=430)
        if vsi.get()=="SIZZLERS":
            vsi9.config(state=DISABLED)
        else:
            vsi9.insert(END,"1")
            
        Label(win,text=vsw.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=20,y=480)
        vsw10=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vsw10.place(x=400,y=480)
        if vsw.get()=="SANDWICH":
            vsw10.config(state=DISABLED)
        else:
            vsw10.insert(END,"1")
            
        Label(win,text=vb.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=500,y=30)
        vb11=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vb11.place(x=900,y=30)
        if vb.get()=="BURGER":
            vb11.config(state=DISABLED)
        else:
            vb11.insert(END,"1")
            
        Label(win,text=vpi.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=500,y=80)
        vpi12=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vpi12.place(x=900,y=80)
        if vpi.get()=="PIZZAS":
            vpi12.config(state=DISABLED)
        else:
            vpi12.insert(END,"1")
            
        Label(win,text=vib.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=500,y=130)
        vib13=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vib13.place(x=900,y=130)
        if vib.get()=="INDIAN BREADS":
            vib13.config(state=DISABLED)
        else:
            vib13.insert(END,"1")
            
        Label(win,text=vig.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=500,y=180)
        vig14=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vig14.place(x=900,y=180)
        if vig.get()=="INDIAN GRAVY":
            vig14.config(state=DISABLED)
        else:
            vig14.insert(END,"1")
            
        Label(win,text=vir.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=500,y=230)
        vir15=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vir15.place(x=900,y=230)
        if vir.get()=="INDIAN RICE":
            vir15.config(state=DISABLED)
        else:
            vir15.insert(END,"1")
            
        Label(win,text=vc.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=500,y=280)
        vc16=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vc16.place(x=900,y=280)
        if vc.get()=="CHINIESE":
            vc16.config(state=DISABLED)
        else:
            vc16.insert(END,"1")
            
        Label(win,text=vsm.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=500,y=330)
        vsm17=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vsm17.place(x=900,y=330)
        if vsm.get()=="SMOOTHIES":
            vsm17.config(state=DISABLED)
        else:
            vsm17.insert(END,"1")
            
        Label(win,text=vd.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=500,y=380)
        vd18=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vd18.place(x=900,y=380)
        if vd.get()=="DESSERTS":
            vd18.config(state=DISABLED)
        else:
            vd18.insert(END,"1")
            
        Label(win,text=vhb.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=500,y=430)
        vhb19=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vhb19.place(x=900,y=430)
        if vhb.get()=="HOT BEVERAGES":
            vhb19.config(state=DISABLED)
        else:
            vhb19.insert(END,"1")
            
        Label(win,text=vic.get(),font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=500,y=480)
        vic20=Entry(win,font=('Segoe UI Semibold',20,'bold'),insertwidth=1,width=1)
        vic20.place(x=900,y=480)
        if vic.get()=="ICE CREAM":
            vic20.config(state=DISABLED)
        else:
            vic20.insert(END,"1")
            
        Button(win,text="Order",font=('Segoe UI Semibold',18,'bold'),bg='gold',fg='black',command=lambda:od(win)).place(x=420,y=530)
        print(tf)
        def od(w):
            top=Toplevel()
            top.title("Order")
            top.geometry('600x401')
            photo=PhotoImage(file='foodprep .gif')
            Label(top,image=photo).place(x=0,y=0)
            global vs1
            global vst2
            global vts3
            global vsa4
            global vq5
            global vw6
            global vp7
            global ve8
            global vsi9
            global vsw10
            global vb11
            global vpi12
            global vib13
            global vig14
            global vir15
            global vc16
            global vsm17
            global vd18
            global vhb19
            global vic20
            global tf
            tf=0
            if bool(vs1.get())==True:
                t1=(int(vs1.get())*150)
                tf+=t1
            if bool(vst2.get())==True:
                t2=(int(vst2.get())*120)
                tf+=t2
            if bool(vts3.get())==True:
                t3=(int(vts3.get())*225)
                tf+=t3
            if bool(vsa4.get())==True:
                t4=(int(vsa4.get())*100)
                tf+=t4
            if bool(vq5.get())==True:
                t5=(int(vq5.get())*175)
                tf+=t5
            if bool(vw6.get())==True:
                t6=(int(vw6.get())*125)
                tf+=t6
            if bool(vp7.get())==True:
                t7=(int(vp7.get())*220)
                tf+=t7
            if bool(ve8.get())==True:
                t8=(int(ve8.get())*185)
                tf+=t8
            if bool(vsi9.get())==True:
                t9=(int(vsi9.get())*265)
                tf+=t9
            if bool(vsw10.get())==True:
                t10=(int(vsw10.get())*100)
                tf+=t10
            if bool(vb11.get())==True:
                t11=(int(vb11.get())*120)
                tf+=t11
            if bool(vpi12.get())==True:
                t12=(int(vpi12.get())*230)
                tf+=t12
            if bool(vib13.get())==True:
                t13=(int(vib13.get())*60)
                tf+=t13
            if bool(vig14.get())==True:
                t14=(int(vig14.get())*225)
                tf+=t14
            if bool(vir15.get())==True:
                t15=(int(vir15.get())*180)
                tf+=t15
            if bool(vc16.get())==True:
                t16=(int(vc16.get())*255)
                tf+=t16
            if bool(vsm17.get())==True:
                t17=(int(vsm17.get())*130)
                tf+=t17
            if bool(vd18.get())==True:
                t18=(int(vd18.get())*90)
                tf+=t18
            if bool(vhb19.get())==True:
                t19=(int(vhb19.get())*50)
                tf+=t19
            if bool(vic20.get())==True:
                t20=(int(vic20.get())*90)
                tf+=t20
            Label(top,text='Your Order is Being Prepared..',font=('Segoe UI Semibold',22,'bold'),height=1,bg='gold',fg='black').place(x=50,y=50)
            Label(top,text='Time Left:',font=('Segoe UI Semibold',22,'bold'),height=1,bg='gold',fg='black').place(x=50,y=100)
            l=Label(top)
            l.config(bg="red")
            l.config(height=1,font=('times',22,'bold'))
            l.place(x=200,y=100)
            for i in range(10,0,-1):
                l["text"]=i
                top.update()
                time.sleep(1)
            l.config(bg='red')
            l.config(fg='white')
            l["text"]="your order is ready!"
            Label(top,text="Total Amount :"+" "+str(tf),font=('Segoe UI Semibold',14,'bold'),height=1,bg='white',fg='black').place(x=200,y=200)
            Button(top,text='Done',font=("Segoe UI Semibold",14),height=1,bg='white',fg='black',command=lambda:checkin(win)).place(x=250,y=300)
            Label(top,text='Please Rate Our Service',font=('Segoe UI Semibold',14,'bold'),height=1,bg='white',fg='black').place(x=50,y=350)
            Button(top,text='Rate Us',font=("Segoe UI Semibold",14),height=1,bg='white',fg='black',command=lambda:rateus(win)).place(x=270,y=350)
            top.mainloop()
    win.mainloop()
    
def loginad(w):
    w.destroy()
    win=Tk()
    win.title("Login ")
    win.geometry('600x401')
    win.config(background="midnight blue")
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:main(win)).place(x=10,y=20)
    Label(win,text="ADMINISTATOR LOGIN",font=('Segoe UI Semibold',22,'bold'),height=1,width=25,bg='gold',fg='black').place(x=100,y=30)
    Label(win,text="Username",font=('Segoe UI Semibold',20,'bold'),bg='gold',fg='black').place(x=50,y=150)
    global u_name
    u_name=Entry(win,font=('Segoe UI Semibold',20,'bold'))
    u_name.place(x=180,y=150)
    Label(win,text="Password",font=('Segoe UI Semibold',20,'bold'),bg='gold',fg='black').place(x=50,y=200)
    global passwd 
    passwd=Entry(win,font=('Segoe UI Semibold',20,'bold'),show="*")
    passwd.place(x=170,y=200)
    Button(win,text='Login',font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black',command=lambda:log1(win)).place(x=250,y=300)
    def log1(w):
        global u_name
        global passwd
        u="admin"
        p="modern"
        
        if u_name.get()==u and passwd.get()==p:
            u_name.delete(0,END)
            passwd.delete(0,END)
            msg.showinfo("Login","successful")
            w.destroy()
            win=Tk()
            admin(win)
        else:
            msg.showwarning("Login","Invaild")
        
    win.mainloop()

def roomaloca(w):
    w.destroy()
    win=Tk()
    win.title("Room Alocation")
    win.geometry('300x250')
    win.config(background="midnight blue")
    Label(win,text="Please Select the Room Type",font=('Segoe UI Semibold',15,'bold'),bg='gold',fg='black').place(x=10,y=30)
    global roomtp
    roomtp=StringVar()
    Radiobutton(win,text="Single",font=('Segoe UI Semibold',15,'bold'),value='t1',variable=roomtp,bg='gold',fg='black',command=None).place(x=20,y=70)
    Radiobutton(win,text="Deluxe",font=('Segoe UI Semibold',15,'bold'),value='t2',variable=roomtp,bg='gold',fg='black',command=None).place(x=170,y=70)
    Radiobutton(win,text="Grand",font=('Segoe UI Semibold',15,'bold'),value='t3',variable=roomtp,bg='gold',fg='black',command=None).place(x=20,y=120)
    Radiobutton(win,text="Prime",font=('Segoe UI Semibold',15,'bold'),value='t4',variable=roomtp,bg='gold',fg='black',command=None).place(x=170,y=120)
    Radiobutton(win,text="Suite",font=('Segoe UI Semibold',15,'bold'),value='t5',variable=roomtp,bg='gold',fg='black',command=None).place(x=100,y=175)
    Button(win,text='Done',font=('Segoe UI Semibold',10,'bold'),bg='white',fg='black',command=lambda:roomalocb(win)).place(x=250,y=200)
    win.mainloop()
    
def roomalocb(w):
    global roomtp
    global L
    global r
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    msg.showinfo("login","Username=<Your name> \n Password=<Your Room no.>_akshay")
    t=roomtp.get()
    if t=='t1':
        q=random.randint(101,110)
        if q not in L:
            r=q
            L.append(q)
        elif q<=105:
            q=q-1
            if q not in L:
                r=q
                L.append(q)
        elif q>105:
            q=q+1
            if q not in L:
                r=q
                L.append(q)
        print (L)
    if t=='t2':
        q=random.randint(201,210)
        if q not in L:
            r=q
            L.append(q)
        elif q<=205:
            q=q-1
            if q not in L:
                r=q
                L.append(q)
        elif q<205:
            q=q+1
            if q not in L:
                r=q
                L.append(q)
        print (L)
    if t=='t3':
        q=random.randint(301,310)
        if q not in L:
            r=q
            L.append(q)
        elif q<=305:
            q=q-1
            if q not in L:
                r=q
                L.append(q)
        elif q<305:
            q=q+1
            if q not in L:
                r=q
                L.append(q)
        print (L)
    if t=='t4':
        q=random.randint(401,410)
        if q not in L:
            r=q
            L.append(q)
        elif q<=405:
            q=q-1
            if q not in L:
                r=q
                L.append(q)
        elif q<405:
            q=q+1
            if q not in L:
                r=q
                L.append(q)
        
    if t=='t5':
        q=random.randint(501,510)
        if q not in L:
            r=q
            L.append(q)
        elif q<=505:
            q=q-1
            if q not in L:
                r=q
                L.append(q)
        elif q<505:
            q=q+1
            if q not in L:
                r=q
                L.append(q)
        print (r)
        global rol
        if r in rol:
            r+=1
    msg.showinfo("Room Allocation","Your Room No. is"+' '+str(r))
    fr=open("cust.txt","a")
    fr.write(str(a)+' '+str(b)+' ' +str(d)+' ' +str(e)+ ' '+str(f)+ ' ' +str(g)+ ' ' +str(h)+' '+str(i)+' '+str(r)+'\n')
    fr.close()
    w.destroy()
    win=Tk()
    login(win)
def login(w):
    w.destroy()
    win=Tk()
    win.title("Login ")
    win.geometry('600x401')
    win.config(background="midnight blue")
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:main(win)).place(x=10,y=20)
    Label(win,text="Customer Login",font=('Segoe UI Semibold',22,'bold'),height=1,width=25,bg='gold',fg='black').place(x=100,y=30)
    Label(win,text="Username",font=('Segoe UI Semibold',20,'bold'),bg='gold',fg='black').place(x=50,y=150)
    global u_name
    u_name=Entry(win,font=('Segoe UI Semibold',20,'bold'))
    u_name.place(x=180,y=150)
    Label(win,text="Password",font=('Segoe UI Semibold',20,'bold'),bg='gold',fg='black').place(x=50,y=200)
    global passwd
    passwd=Entry(win,font=('Segoe UI Semibold',20,'bold'),show="*")
    passwd.place(x=170,y=200)
    Button(win,text='Login',font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black',command=lambda:log(win)).place(x=250,y=300)
    def log(w):
        global u_name
        global passwd
        global crlist
        global r
        crlist=[]
        f2=open("custlog.txt","r+")
        lin=f2.readline()
        while lin:
            if u_name==lin[0]:
                tl=int(lin[1])
                tf=int(lin[2])
            lin=f2.readline()
        f2.close()
        fl=open("cust.txt","r+")
        c=0
        refno=' '
        logr=' '
        x=u_name.get()
        lm=fl.readline()
        while lm:
            c+=1
            s=lm.split()
            if x in s[0]:
                refno=str(c)
                logr=s[8]
            lm=fl.readline()
        fl.close()
        rm=str(logr)
        global u
        u=u_name.get()
        p=rm+"_"+"akshay"
        if u_name.get()==u and passwd.get()==p:
            u_name.delete(0,END)
            passwd.delete(0,END)
            msg.showinfo("Login","successfull!")
            f=open("cust.txt",'r')
            n=int(refno)
            d=0
            line=f.readline()
            while line:
                d+=1
                if d==n:
                    crlist=line.split()
                else:
                    line=f.readline()
           
            w.destroy()
            win=Tk()
            checkin(win)
        else:
            msg.showwarning("Login","Invaild! user")
            u_name.delete(0,END)
            passwd.delete(0,END)
    win.mainloop()
def receipt():
    global tf
    global tl
    global rr
    nod=0
    s1=crlist[7].split('.')
    s2=crlist[6].split('.')
    z1=int(s1[0])
    z2=int(s2[0])
    nod=((z1-z2)+1)
    rre=str(rr)
    n=str(nod)
    lb=str(tl)
    fb=str(tf)
    msg.showinfo("Receipt","Please Collect your Receipt (flie=receipt.pdf)")
    os.environ["INVOICE_LANG"] = "en"
    client = Client(crlist[0].capitalize()+'\n'+crlist[2]+'\n'+crlist[3])
    provider = Provider('Akshay Hotels Pte. Ltd.', bank_account='2600420569', bank_code='2010')
    creator = Creator('Jayanth Srinivasan')
    
    invoice = Invoice(client, provider, creator)
    invoice.currency = u"\u20B9"
    invoice.add_item(Item(nod, rr, description="Room Rent",tax=30))
    invoice.add_item(Item(1, lb, description="Laundry", tax=18))
    invoice.add_item(Item(1, fb, description="Food", tax=18))
    invoice.add_item(Item(1, 600, description="Misc.", tax=2))

    pdf = SimpleInvoice(invoice)
    pdf.gen("receipt.pdf", generate_qr_code=True)
def rememp(w):
    w.destroy()
    win=Tk()
    win.title("Remove Employee")
    win.geometry("300x200")
    Lc1=Label(win,text="Employee name",font=('Segoe UI Semibold',15,'bold')).grid(row=2,column=1)
    global E1
    E1=Entry(win,text="Employee name")
    E1.grid(row=2,column=2)
    Lc2=Label(win,text="Category",font=('Segoe UI Semibold',15,'bold')).grid(row=3,column=1)
    global E2
    E2=Entry(win,text="Category")
    E2.grid(row=3,column=2)
    def rem():
        f=open('addemp.txt','r')
        global E1
        na= E1.get()
        global E2
        c= E2.get()
        line=f.readlines()
        for i in line:
            if na in i and c in i:
                line.remove(i)
                f.close()
                break
            f=open('addemp.txt','w')
            for i in line:
                f.write(i)
    Button(win,text="Remove",font=('Segoe UI Semibold',13,'bold'),command=lambda:rem()).grid(row=5,column=1)
    win.mainloop()
def logout(w):
    file=open("room.txt","a")
    global L
    for i in L:
        file.write(str(i)+" ")
    file.close()
    f1=open("custlog.txt","a")
    global tf
    global tl
    global crlist
    f1.write(crlist[0]+" "+str(tl)+" "+str(tf))
    f1.close()
    crlist.clear()
    w.destroy()
    win=Tk()
    main(win)
def addemp(w):
    w.destroy()
    win=Tk()
    win.title("Add Employee")
    win.geometry("300x200")
    lc1=Label(win,text="Employee name",font=('Segoe UI Semibold',15,'bold')).grid(row=2,column=1)
    global e1
    e1=Entry(win,text="Employee name")
    e1.grid(row=2,column=2)
    lc2=Label(win,text="Category",font=('Segoe UI Semibold',15,'bold')).grid(row=3,column=1)
    global e2
    e2=Entry(win,text="Category")
    e2.grid(row=3,column=2)
    lc3=Label(win,text="Salary",font=('Segoe UI Semibold',15,'bold')).grid(row=4,column=1)
    global e3
    e3=Entry(win,text="Salary")
    e3.grid(row=4,column=2)
    def add():
        global e1
        o=e1.get()
        global e2
        s=e2.get()
        global e3
        t=e3.get()
        file=open("addemp.txt","r+")
        file.write(str(o)+" ")
        file.write(str(s)+" ")
        file.write(str(t)+" ")
    b4=Button(win,text="ADD",font=('Segoe UI Semibold',13,'bold'),command=lambda:add()).grid(row=5,column=1)
    win.mainloop()
def showemp(w):
    w.destroy()
    win=Tk()
    win.title("Emplyee")
    win.geometry('600x401')
    fe=open("addemp.txt","r+")
    l=fe.readlines()
    if l!=None:
        lab=''
        for i in l:
            lab+=str(i)+' '+'\n'
        Label(win,text=lab,font=('Segoe UI Semibold',22,'bold')).pack()
    win.mainloop()
def emp(w):
    w.destroy()
    win=Tk()
    win.title("Emplyee")
    win.geometry('600x401')
    win.config(background='midnight blue')
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:admin(win)).place(x=10,y=20)
    Label(win,text='Employee Management',font=('Segoe UI Semibold',22,'bold'),height=1,width=25,bg='white',fg='black').place(x=100,y=30)
    Button(win,text='Add Employee',font=('Segoe UI Semibold',19,'bold'),bg='gold',fg='black',command=lambda:addemp(win)).place(x=173,y=100)
    Button(win,text='Remove Employee',font=('Segoe UI Semibold',19,'bold'),bg='gold',fg='black',command=lambda:rememp(win)).place(x=173,y=200)
    Button(win,text='Show Employee ',font=('Segoe UI Semibold',19,'bold'),bg='gold',fg='black',command=lambda:showemp(win)).place(x=173,y=300)
    win.mainloop()
def inventory(w):
    w.destroy()
    win=Tk()
    win.title("Inventory")
    win.geometry('768x520')
    win.config(background="midnight blue")
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:admin(win)).place(x=10,y=20)
    USERNAME = StringVar()
    PASSWORD = StringVar()
    PRODUCT_NAME = StringVar()
    PRODUCT_PRICE = IntVar()
    PRODUCT_QTY = IntVar()
    SEARCH = StringVar()
    def Database():
        global conn, cursor
        conn = sqlite3.connect("inventory.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT)")
        conn.commit()
    def ShowAddNew():
         global addnewform
         addnewform = Toplevel()
         addnewform.title("Simple Inventory System/Add new")
         addnewform.geometry("600x500")
         AddNewForm()
    def AddNewForm():
        TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
        TopAddNew.pack(side=TOP, pady=20)
        lbl_text = Label(TopAddNew, text="Add New Product", font=('arial', 18), width=600)
        lbl_text.pack(fill=X)
        MidAddNew = Frame(addnewform, width=600)
        MidAddNew.pack(side=TOP, pady=50)
        lbl_productname = Label(MidAddNew, text="Product Name:", font=('arial', 25), bd=10)
        lbl_productname.grid(row=0, sticky=W)
        lbl_qty = Label(MidAddNew, text="Product Quantity:", font=('arial', 25), bd=10)
        lbl_qty.grid(row=1, sticky=W)
        lbl_price = Label(MidAddNew, text="Product Price:", font=('arial', 25), bd=10)
        lbl_price.grid(row=2, sticky=W)
        productname = Entry(MidAddNew, textvariable=PRODUCT_NAME, font=('arial', 25), width=15)
        productname.grid(row=0, column=1)
        productqty = Entry(MidAddNew, textvariable=PRODUCT_QTY, font=('arial', 25), width=15)
        productqty.grid(row=1, column=1)
        productprice = Entry(MidAddNew, textvariable=PRODUCT_PRICE, font=('arial', 25), width=15)
        productprice.grid(row=2, column=1)
        btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNew)
        btn_add.grid(row=3, columnspan=2, pady=20)
    def AddNew():
        Database()
        cursor.execute("INSERT INTO `product` (product_name, product_qty, product_price) VALUES(?, ?, ?)", (str(PRODUCT_NAME.get()), int(PRODUCT_QTY.get()), int(PRODUCT_PRICE.get())))
        conn.commit()
        PRODUCT_NAME.set("")
        PRODUCT_PRICE.set("")
        PRODUCT_QTY.set("")
        cursor.close()
        conn.close()
    def ViewForm():
        global tree
        TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
        TopViewForm.pack(side=TOP, fill=X)
        LeftViewForm = Frame(viewform, width=600)
        LeftViewForm.pack(side=LEFT, fill=Y)
        MidViewForm = Frame(viewform, width=600)
        MidViewForm.pack(side=RIGHT)
        lbl_text = Label(TopViewForm, text="View Products", font=('arial', 18), width=600)
        lbl_text.pack(fill=X)
        lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
        lbl_txtsearch.pack(side=TOP, anchor=W)
        search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
        search.pack(side=TOP,  padx=10, fill=X)
        btn_search = Button(LeftViewForm, text="Search", command=Search)
        btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
        btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
        btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
        btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
        btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        tree = ttk.Treeview(MidViewForm, columns=("ProductID", "Product Name", "Product Qty", "Product Price"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('ProductID', text="ProductID",anchor=W)
        tree.heading('Product Name', text="Product Name",anchor=W)
        tree.heading('Product Qty', text="Product Qty",anchor=W)
        tree.heading('Product Price', text="Product Price",anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=0)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=120)
        tree.column('#4', stretch=NO, minwidth=0, width=120)
        tree.pack()
        DisplayData()
    def DisplayData():
        Database()
        cursor.execute("SELECT * FROM `product`")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
    def Search():
        if SEARCH.get() != "":
            tree.delete(*tree.get_children())
            Database()
            cursor.execute("SELECT * FROM `product` WHERE `product_name` LIKE ?", ('%'+str(SEARCH.get())+'%',))
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
    def Reset():
        tree.delete(*tree.get_children())
        DisplayData()
        SEARCH.set("")
    def Delete():
        if not tree.selection():
            print("ERROR")
        else:
            result = msg.askquestion('Simple Inventory System', 'Are you sure you want to delete this record?', icon="warning")
            if result == 'yes':
                curItem = tree.focus()
                contents =(tree.item(curItem))
                selecteditem = contents['values']
                tree.delete(curItem)
                Database()
                cursor.execute("DELETE FROM `product` WHERE `product_id` = %d" % selecteditem[0])
                conn.commit()
                cursor.close()
                conn.close()
    def ShowView():
        global viewform
        viewform = Toplevel()
        viewform.title("Simple Inventory System/View Product")
        viewform.geometry("600x400")
        ViewForm()
    
    def ShowHome():
        win.withdraw()
        Home()
    Title = Frame(win, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Stock & Inventory", font=('arial', 45))
    lbl_display.pack()
    Button(win,text="Add new Item",font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black',command=lambda:ShowAddNew()).place(x=173,y=100)
    Button(win,text="View Stock",font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black',command=lambda:ShowView()).place(x=173,y=200)

        


    win.mainloop()
def check(w):
    w.destroy()
    win=Tk()
    win.title("Check In")
    win.geometry('1000x616')
    win.config(background="steel blue")
    Label(win,text='Welcome to Akshay Hotels',font=('Segoe UI Semibold',22,'bold'),height=1,width=25,bg='white',fg='black').place(x=300,y=30)
    Label(win,text='Name',font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black').place(x=250,y=80)
    global name
    name=Entry(win,bd=2,font=('Segoe UI Semibold',22,'bold'))
    name.place(x=335,y=80)
    Label(win,text='Age',font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black').place(x=250,y=140)
    global age
    age=Entry(win,bd=2,font=('Segoe UI Semibold',22,'bold'))
    age.place(x=308,y=140)
    Label(win,text='Gender',font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black').place(x=250,y=200)
    global gender
    gender=StringVar()
    Radiobutton(win,text="Male",value='male',variable=gender,command=None).place(x=400,y=210)
    Radiobutton(win,text="Female",value='female',variable=gender,command=None).place(x=500,y=210)
    Label(win,text='Phone no.',font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black').place(x=250,y=250)
    global ph
    ph=Entry(win,bd=2,font=('Segoe UI Semibold',22,'bold'))
    ph.place(x=380,y=250)
    Label(win,text='Email ID',font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black').place(x=250,y=300)
    global emd
    emd=Entry(win,bd=2,font=('Segoe UI Semibold',22,'bold'))
    emd.place(x=365,y=300)
    Label(win,text='Nationality',font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black').place(x=250,y=350)
    global nan
    nan=Entry(win,bd=2,font=('Segoe UI Semibold',22,'bold'))
    nan.place(x=400,y=350)
    Label(win,text='No. of Guests',font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black').place(x=250,y=400)
    global nog
    nog=StringVar()
    Radiobutton(win,text="1",value=1,variable=nog,command=None).place(x=450,y=410)
    Radiobutton(win,text="2",value=2,variable=nog,command=None).place(x=500,y=410)
    Radiobutton(win,text="3",value=3,variable=nog,command=None).place(x=550,y=410)
    Radiobutton(win,text=">3",value=4,variable=nog,command=None).place(x=600,y=410)
    Label(win,text='Check In Date',font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black').place(x=250,y=450)
    global cid
    cid=Entry(win,bd=2,font=('Segoe UI Semibold',22,'bold'))
    cid.place(x=435,y=450)
    Label(win,text='Check Out Date',font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black').place(x=250,y=500)
    global cod
    cod=Entry(win,bd=2,font=('Segoe UI Semibold',22,'bold'))
    cod.place(x=460,y=500)
    Button(win,text="Done",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:chdone(win)).place(x=380,y=550)
    win.mainloop()
def chdone(w):
    global a
    global name
    a= name.get()
    global age
    global b
    b=age.get()
    global gender
    global c
    c=gender.get()
    l=c
    global ph
    global d
    d= ph.get()
    if len(d)!=10:
        msg.showerror("Check In","Invaild Phone No.!!")
    global emd
    global e
    e=emd.get()
    if '@' not in e:
        msg.showerror("Check In","Invaild Email Id!!")
    global nan
    global f
    f=nan.get()
    global nog
    global g
    g=nog.get()
    global cid
    global h
    h=cid.get()
    global cod
    global i
    i=cod.get()
    print(a,b,c,d,e,f,g,h,i)
    name.delete(0,END)
    age.delete(0,END)
    ph.delete(0,END)
    emd.delete(0,END)
    nan.delete(0,END)
    cid.delete(0,END)
    cod.delete(0,END)
    conn=sqlite3.connect('custdetails.db')
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS details (c_name text, c_age integer, c_gender text, c_ph integer, c_emd text, c_nan text, c_nog integer, c_cid text, c_cod text)")
    c.execute(" INSERT INTO details VALUES(:name, :age, :gender, :ph, :emd, :nan, :nog, :cid, :cod)",
              {'name':a,'age':b,'gender':l,'ph':d,'emd':e,'nan':f,'nog':g,'cid':h,'cod':i})
    
    conn.commit()
    conn.close()
    w.destroy()
    win=Tk()
    roomaloca(win)
def showguest(w):
    conn=sqlite3.connect('custdetails.db')
    c=conn.cursor()
    c1=c.execute("SELECT *, oid FROM details")
    recd=c.fetchall()
    print (recd)
    print_recd=' '
    for re in recd:
        print_recd+=str(re)+"\n"
    top=Toplevel()
    top.title("Show Guest")    
    Label(top,text=print_recd).pack()
    conn.commit()
    conn.close()
    top.mainloop()
def welcome(w):
    w.destroy()
    win=Tk()
    win.title("Terms and Conditions")
    win.geometry('1200x760')
    win.config(background="red")
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:main(win)).place(x=10,y=20)
    tnc=StringVar()
    lb=Message(win,font=("Segoe UI Semibold",10),textvariable=tnc,relief=RAISED)
    tnc.set("These General T&Cs and any other applicable specific terms and conditions relevant to the [Promotion], together with any amendments as may be made from time to time, shall form a legal agreement between Akshay Hotels Pte. Ltd. (“AHS”) and you.\n \
Reservation Terms\n The rates quoted are based on your period of stay. Rates are subject to change as a result of changes in your arrival and/or departure dates. Rates quoted are in Indian Rupees. Rate is for the number of adults reserved at point of booking only. \
Additional fees are applicable for each additional adult. Rates do not include any applicable prevailing government taxes at time of occupancy. The rates are subject to 10% Service Charge and prevailing Goods and Services Tax.\nA rate modifier will apply should you decide to stay in a higher room category than the one originally booked. All services not included in the offer package shall be charged separately.\n \
Any extension of stay will be charged to guest based on either the Flexible Rate or any other Packages offered by AHS.\nMaximum of 3 guests per room (minimum one adult; any combination of adults + children not exceeding 3 guests total). A fee of RS.1000 will be charged for each additional adult staying in Deluxe or Premier rooms and a fee of Rs.2200 will be charged for each additional adult staying in the Club/Grand Club room or any suite.\
\nMaximum occupancy varies from selected family rooms and premium suites. Children aged 12 or younger sleep for free in the existing bedding of a shared room with a paying adult. Fees apply should a rollaway bed be required.\n\
A valid credit card is required to secure your reservation. Upon reservation, the credit card will be charged for the amount indicated on the booking confirmation page and email. AHS accepts Visa, MasterCard and, American Express. Debit Cards are not accepted. \n \
Exchange rates are applicable at time of reservation, but are subject to currency fluctuations. Your bill for your stay will be charged at the prevailing exchange rates upon completion of your stay.\
Blackout dates may apply.\
In the event that a guest completes a booking based on a rate that has been incorrectly posted, AHS reserves the right to correct the rate or cancel the reservation at its discretion, and will contact you directly in order to do so.\
This reservation is not transferable. No name change is allowed.\n \
You must be at least 18 years of age to check-in and register for a room. Check-in time is from 3pm onwards and check-out time is by 11am. A valid government issued identification or passport is required at check-in.\
Should you arrive at AHS prior to the normal check-in time, please approach AHS’ Guest Services Desk for assistance in storing your luggage until check-in is available. If arriving early, you are also advised to consider making a reservation for the evening prior to your arrival. \n \
Late check-outs are available on request subject to room availability and occupancy level. Please check with AHS’ Front Desk at least 24 hours prior to your departure on availability of late check-out. A half-day room charge may be incurred for late check-out between 11am to 6pm and a full day room charge may be incurred for late check-out after 6pm.\
A deposit of Rs.2000 is applicable for each night of stay by way of cash payment or credit card. A valid credit card is required upon check-in for incidentals in addition to full payment of room and prevailing government taxes.\
AHS may revise, alter or delete any part of these General T&Cs and terms and conditions of any Promotion at any time without prior notice.\
You shall indemnify and hold AHS harmless in respect of any liability, loss, damage, cost and expense of any nature arising out of, and/or in connection with the acceptance of the reservation by AHS.\
To the extent permitted by law, AHS shall not be liable for any losses, damages, costs or expenses incurred by you as a result of any cancellation of the reservation by AHS.\n\
Personal Data Privacy\n\
I consent to any AHS-Authorised Party collecting, using, storing, and/or disclosing to another AHS-Authorised Party my Data or contacting me via telephone call, text message, email and/or postal mail to:\
(i) administer my hotel stay booking or customer service or my relationship with any AHS-Authorised Party;\
(ii) respond to my requests or communications;\
(iii) conduct surveys or Data profiling and analytics to learn about my hotel stay and preferences;\
(iv) improve guest experience for me and others;\
(v) protect the safety of persons and property;\ (vi) comply with or address any applicable AHS-Authorised Party’s internal policies or contractual obligations, third party requests, and/or law, regulation, guideline, notice or request issued by any Authority; and/or\
(vii) administer any AHS-Authorised Party’s legal, operational, business or development purposes, or any purpose(s) in the prevailing AHS privacy policy. \
I further warrant that all information provided by me in this form is true, accurate and complete.")
    lb.pack()
    Button(win,text="I Agree",font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black',command=lambda:check(win)).place(x=900,y=645)
    Button(win,text="Cancel",font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black',command=lambda:main(win)).place(x=200,y=645)
    win.mainloop()
def mail(w):
    w.destroy()
    win=Tk()
    win.title("mail")
    win.geometry('800x401')
    win.config(background="midnight blue")
    Label(win,text="Reciver'sEmailId",font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=50,y=50)
    global rec
    rec=Entry(win,bd=5,font=('Segoe UI Semibold',22,'bold'))
    rec.place(x=275,y=50)
    Label(win,text="Subject",font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=75,y=125)
    global sub
    sub=Entry(win,bd=5,font=('Segoe UI Semibold',22,'bold'),state=NORMAL)
    sub.place(x=275,y=125)
    Label(win,text="Content",font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=75,y=200)
    global content
    content=ScrolledText(win,height=10,width=30).place(x=275,y=200)
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:otherser(win)).place(x=10,y=20)
    
    Button(win,text='Send',font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black',command=lambda:mailsend()).place(x=600,y=300)
    win.mainloop()
def mailsend():
    
    global content
    message = " "
    msb = MIMEMultipart()
    password = "Akshay@123" 
    msb['From'] = "akshayhotels123@gmail.com" 
    global rec
    msb['To'] = rec.get()
    global sub
    msb['Subject'] = sub.get()
    msb.attach(MIMEText(message, 'plain'))
    try:
        mail = smtplib.SMTP('smtp.gmail.com: 587')
        mail.starttls()
        mail.login(msb['From'], password)
        mail.sendmail(msb['From'], msb['To'], msb.as_string())
        mail.quit()
    except:
        print("Something Went Wrong...Try after sometime")
def taxi(w):
    w.destroy()
    win=Tk()
    win.title("taxi")
    win.geometry('600x401')
    photo=PhotoImage(file='taxi (1).gif')
    Label(win,image=photo).place(x=0,y=0)
    From=StringVar()
    To=StringVar()
    Label(win,text="Pick Up",font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=50,y=50)
    global e1
    e1=Entry(win,bd=5,font=('Segoe UI Semibold',22,'bold'),textvariable=From)
    e1.place(x=155,y=50)
    Label(win,text="Drop",font=('Segoe UI Semibold',22,'bold'),bg='gold',fg='black').place(x=75,y=125)
    global e2
    e2=Entry(win,bd=5,font=('Segoe UI Semibold',22,'bold'))
    e2.place(x=155,y=125)
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:otherser(win)).place(x=10,y=20)
    Button(win,text="Book Now",font=('Segoe UI Semibold',20,'bold'),bg='gold',fg='black',command=lambda:book()).place(x=200,y=200)
    win.mainloop()
def book():
    global e1
    global e2
    f=e1.get()
    t=e2.get()
    con=msg.askokcancel("confrimation","Confrim your ride")
    if con==True:
        top=Toplevel()
        top.title("ride details")
        top.geometry('300x300')
        top.config(background="gold")
        Label(top,text="Your Ride Details",font=('Segoe UI Semibold',22,'bold'),bg='black',fg='gold').place(x=30,y=20)
        Label(top,text="Pick Up at:"+" "+ f,font=('Segoe UI Semibold',20,'bold'),bg='black',fg='gold').place(x=50,y=70)
        Label(top,text="Drop at: "+" "+ t,font=('Segoe UI Semibold',20,'bold'),bg='black',fg='gold').place(x=50,y=115)
        Label(top,text="Booking Time:",font=('Segoe UI Semibold',20,'bold'),bg='black',fg='gold').place(x=20,y=160)
        Button(top,text="Confrim",font=('Segoe UI Semibold',20,'bold'),bg='gold',fg='black',command=lambda:conms()).place(x=50,y=220)
        time1=StringVar()
        time1.set(time.strftime('%H:%M:%S'))
        Label(top,textvariable=time1,font=('Segoe UI Semibold',20,'bold'),bg='gold',fg='black').place(x=200,y=160)
        def conms():
            msg.showinfo("Travel Desk","Your Ride Details has been Shared with Travel Desk \n Please approach them to confrim your booking!")
        top.mainloop()
def tourpac():
    msg.showinfo("Book aTour Package","To Avail This Service Please Contact Receptionist or Call 122")
def orderon():
    ws=urllib. request. urlopen('https://jayanthsrinivasan2.wixsite.com/akshay-hotels')
    ur=ws.geturl()
    webbrowser.open_new(ur)
def feedback(w):
    w.destroy()
    from db import DBConnect
    from listComp import ListComp
    conn = DBConnect()
    win=Tk()
    win.title("feedback")
    win.geometry('600x285')
    win.config(background='#AEB6BF')
    
    labels = ['Full Name:', 'Gender:', 'Comment:']
    for i in range(3):
        Label(win, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)
    BuList = Button(win, text='List Comp.')
    BuList.grid(row=4, column=1)
    BuSubmit = Button(win, text='Submit Now')
    BuSubmit.grid(row=4, column=2)
    fullname = Entry(win, width=40, font=('Arial', 14))
    fullname.grid(row=0, column=1, columnspan=2)
    SpanGender = StringVar()
    Radiobutton(win, text='Male', value='male', variable=SpanGender).grid(row=1, column=1)
    Radiobutton(win, text='Female', value='female', variable=SpanGender).grid(row=1, column=2)
    comment = Text(win, width=35, height=5, font=('Arial', 14))
    comment.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
    def SaveData():
        msg = conn.Add(fullname.get(), SpanGender.get(), comment.get(1.0, 'end'))
        fullname.delete(0, 'end')
        comment.delete(1.0, 'end')
    def ShowList():
        listrequest = ListComp()
    BuSubmit.config(command=SaveData)
    BuList.config(command=ShowList)
    win.mainloop()
def menuback(w):
    r=msg.askyesno("Restaurant","Are You a guest of this Hotel")
    if r==True:
        w.destroy()
        win=Tk()
        res(win)
    else:
        w.destroy()
        win=Tk()
        ngres(win)
def menu(w):
    w.destroy()
    win=Tk()
    win.title("menu")
    win.geometry('975x700')
    win.config(background='brown')
    f1=Frame(win,bd=14,width=1024,height=100,padx=10,relief=SUNKEN,bg='yellow')
    f1.grid(row=1,column=0)
    Label(f1,text="                                                  Our Menu                                                ",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='black').pack()
    f2=Frame(win,bd=14,width=400,height=500,relief=SUNKEN,bg='yellow').place(x=50,y=145)
    Label(f2,text="SOUPS",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=75,y=160)
    Label(f2,text="Cream of Tomato",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=210)
    Label(f2,text="Spicy Veg and Coriander",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=260)
    Label(f2,text="Sweet Corn & Veg",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=310)
    Label(f2,text="Cream of Spinach & mushroo",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=360)
    Label(f2,text="STARTERS",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=75,y=410)
    Label(f2,text="Cheese Corn Ball",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=460)
    Label(f2,text="French Fries",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=510)
    Label(f2,text="Masala Garlic Bread",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=560)
    
    f3=Frame(win,bd=14,width=400,height=500,relief=SUNKEN,bg='yellow').place(x=500,y=145)
    Label(f3,text="Mexican Nanchos",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=160)
    Label(f3,text="Nanchos Veg Supreme",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=210)
    Label(f3,text="TANDOOR STARTERS",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=525,y=260)
    Label(f3,text="Paneer Tikka",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=310)
    Label(f3,text="Veg Seekh Kebab",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=360)
    Label(f3,text="Achari Paneer Tikka",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=410)
    Label(f3,text="Hariyali Paneer Tikka",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=460)
    Label(f3,text="Madrasi Mushroom",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=510)
    Label(f3,text="Dingri Achari Adraki",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=560)
    Button(win,text="Back",font=('Segoe UI Semibold',15,'bold'),bg='white',fg='black',command=lambda:menuback(win)).place(x=75,y=650)
    Button(win,text="Next",font=('Segoe UI Semibold',15,'bold'),bg='white',fg='black',command=lambda:menup1(win)).place(x=825,y=650)
def menup1(w):
    w.destroy()
    win=Tk()
    win.title("menu")
    win.geometry('975x700')
    win.config(background='brown')
    fm=Frame(win,bd=14,width=1024,height=100,padx=10,relief=SUNKEN,bg='yellow')
    fm.grid(row=1,column=0)
    Label(fm,text="                                                  Our Menu                                                ",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='black').pack()
    f4=Frame(win,bd=14,width=400,height=500,relief=SUNKEN,bg='yellow').place(x=50,y=145)
    Label(f4,text="SALADS",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=75,y=160)
    Label(f4,text="Pasta & yoghurt Salad",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=210)
    Label(f4,text="Corn Bean & Pasta Salad ",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=260)
    Label(f4,text="Russian Salad",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=310)
    Label(f4,text="Green Salad",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=360)
    Label(f4,text="QUESADILLAS",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=75,y=410)
    Label(f4,text="Cheese & Bean Quesadilla",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=460)
    Label(f4,text="Cheese & Paneer Quesadilla",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=510)
    Label(f4,text="Cheese & Corn Quesadilla",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=560)
    f5=Frame(win,bd=14,width=400,height=500,relief=SUNKEN,bg='yellow').place(x=500,y=145)
    Label(f5,text="WRAP",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=525,y=160)
    Label(f5,text="Mexican Veg Wrap",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=210)
    Label(f5,text="Paneer&Mushroom Wrap",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=260)
    Label(f5,text="Splender Club Wrap",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=310)
    Label(f5,text="PASTAS",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=525,y=360)
    Label(f5,text="Penne Arabitta",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=410)
    Label(f5,text="Farfalle Pesto Cream Sauce",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=460)
    Label(f5,text="Mexican Pasta Delight",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=510)
    Label(f5,text="Red Sauce Pasta",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=560)
    Button(win,text="Previous",font=('Segoe UI Semibold',15,'bold'),bg='white',fg='black',command=lambda:menu(win)).place(x=75,y=650)
    Button(win,text="Next",font=('Segoe UI Semibold',15,'bold'),bg='white',fg='black',command=lambda:menup2(win)).place(x=825,y=650)

def menup2(w):
    w.destroy()
    win=Tk()
    win.title("menu")
    win.geometry('975x700')
    win.config(background='brown')
    fn=Frame(win,bd=14,width=1024,height=100,padx=10,relief=SUNKEN,bg='yellow')
    fn.grid(row=1,column=0)
    Label(fn,text="                                                  Our Menu                                                ",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='black').pack()
    f6=Frame(win,bd=14,width=400,height=500,relief=SUNKEN,bg='yellow').place(x=50,y=145)
    Label(f6,text="ENCHILADAS",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=75,y=160)
    Label(f6,text="Mexican Bean & Cheese ",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=210)
    Label(f6,text="Spicy Paneer Enchiladas",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=260)
    Label(f6,text="Corn & Cheese Enchiladas",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=310)
    Label(f6,text="SIZZLERS",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=75,y=360)
    Label(f6,text="Italian Sizzler",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=410)
    Label(f6,text="Indian Sizzler",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=460)
    Label(f6,text="Paneer & Corn Sizzler",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=510)
    Label(f6,text="Fricassee of Paneer & Corn",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=560)
    f7=Frame(win,bd=14,width=400,height=500,relief=SUNKEN,bg='yellow').place(x=500,y=145)
    Label(f7,text="SANDWICH",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=525,y=160)
    Label(f7,text="Spicy Paneer Sandwich",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=210)
    Label(f7,text="Texas Veg Sandwich",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=260)
    Label(f7,text="Greek Veg Sandwich",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=310)
    Label(f7,text="Veg Club Sandwich",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=360)
    Label(f7,text="BURGER",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=525,y=410)
    Label(f7,text="Veg Cheese Burger",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=460)
    Label(f7,text="Texas Burger",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=510)
    Label(f7,text="Double Burger",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=560)
    Button(win,text="Previous",font=('Segoe UI Semibold',15,'bold'),bg='white',fg='black',command=lambda:menup1(win)).place(x=75,y=650)
    Button(win,text="Next",font=('Segoe UI Semibold',15,'bold'),bg='white',fg='black',command=lambda:menup3(win)).place(x=825,y=650)
def menup3(w):
    w.destroy()
    win=Tk()
    win.title("menu")
    win.geometry('975x700')
    win.config(background='brown')
    fo=Frame(win,bd=14,width=1024,height=100,padx=10,relief=SUNKEN,bg='yellow')
    fo.grid(row=1,column=0)
    Label(fo,text="                                                  Our Menu                                                ",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='black').pack()
    f8=Frame(win,bd=14,width=400,height=500,relief=SUNKEN,bg='yellow').place(x=50,y=145)
    Label(f8,text="PIZZAS",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=75,y=160)
    Label(f8,text="Mushroom Delight Pizza",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=210)
    Label(f8,text="Veg Jungle Pizza",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=260)
    Label(f8,text="Veg Romantic Pizza",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=310)
    Label(f8,text="Deluxe Veg Pizza",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=360)
    Label(f8,text="INDIAN BREADS",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=75,y=410)
    Label(f8,text="Naan",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=460)
    Label(f8,text="Roti",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=510)
    Label(f8,text="Butter Naan",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=560)
    f9=Frame(win,bd=14,width=400,height=500,relief=SUNKEN,bg='yellow').place(x=500,y=145)
    Label(f9,text="Cheese Garlic Naan",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=160)
    Label(f9,text="Kashmiri Naan",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=210)
    Label(f9,text="Butter Roti",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=260)
    Label(f9,text="Kulcha",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=310)
    Label(f9,text="Paratha",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=360)
    Label(f9,text="INDIAN GRAVY",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=525,y=410)
    Label(f9,text="Dal Makhini",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=460)
    Label(f9,text="Dal Tadka",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=510)
    Label(f9,text="Paneer Butter Masala",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=560)

    Button(win,text="Previous",font=('Segoe UI Semibold',15,'bold'),bg='white',fg='black',command=lambda:menup2(win)).place(x=75,y=650)
    Button(win,text="Next",font=('Segoe UI Semibold',15,'bold'),bg='white',fg='black',command=lambda:menup4(win)).place(x=825,y=650)
def menup4(w):
    w.destroy()
    win=Tk()
    win.title("menu")
    win.geometry('975x700')
    win.config(background='brown')
    fp=Frame(win,bd=14,width=1024,height=100,padx=10,relief=SUNKEN,bg='yellow')
    fp.grid(row=1,column=0)
    Label(fp,text="                                                  Our Menu                                                ",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='black').pack()
    f10=Frame(win,bd=14,width=400,height=500,relief=SUNKEN,bg='yellow').place(x=50,y=145)

    Label(f10,text="Palak Paneer",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=160)
    Label(f10,text="Mushroom Masala",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=210)
    Label(f10,text="Malai Veg Kofta",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=260)
    Label(f10,text="Paneer Lababdar",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=310)
    Label(f10,text="Veg Saagwala",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=360)
    Label(f10,text="INDIAN RICE",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=75,y=410)
    Label(f10,text="Pulav",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=460)
    Label(f10,text="Veg Briyani",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=510)
    Label(f10,text="Ghee Rice",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=560)
    f11=Frame(win,bd=14,width=400,height=500,relief=SUNKEN,bg='yellow').place(x=500,y=145)
    Label(f11,text="Cashew Nut Rice",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=160)
    Label(f11,text="Veg Fried Rice",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=210)
    Label(f11,text="CHINESE",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=525,y=260)
    Label(f11,text="Veg Noodles",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=310)
    Label(f11,text="Sezchuan Noodles",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=360)
    Label(f11,text="Sezchuan Fried Rice",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=410)
    Label(f11,text="Gobi Manchurian",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=460)
    Label(f11,text="Mushroom Manchurian",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=510)
    Label(f11,text="Paneer Manchurian",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=560)

    
    Button(win,text="Previous",font=('Segoe UI Semibold',15,'bold'),bg='white',fg='black',command=lambda:menup3(win)).place(x=75,y=650)
    Button(win,text="Next",font=('Segoe UI Semibold',15,'bold'),bg='white',fg='black',command=lambda:menup5(win)).place(x=825,y=650)
def menup5(w):
    w.destroy()
    win=Tk()
    win.title("menu")
    win.geometry('975x700')
    win.config(background='brown')
    fq=Frame(win,bd=14,width=1024,height=100,padx=10,relief=SUNKEN,bg='yellow')
    fq.grid(row=1,column=0)
    Label(fq,text="                                                  Our Menu                                                ",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='black').pack()
    f12=Frame(win,bd=14,width=400,height=500,relief=SUNKEN,bg='yellow').place(x=50,y=145)
    Label(f12,text="SMOOTHIES",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=75,y=160)
    Label(f12,text="Vanila",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=210)
    Label(f12,text="Stawberry",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=260)
    Label(f12,text="Chocolate",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=310)
    Label(f12,text="Punjabi Lassi",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=360)
    Label(f12,text="Banana Lassi",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=410)
    Label(f12,text="La Summer Rain",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=460)
    Label(f12,text="DESERTS",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=75,y=510)
    Label(f12,text="Gulab Jamun",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=75,y=560)
    f13=Frame(win,bd=14,width=400,height=500,relief=SUNKEN,bg='yellow').place(x=500,y=145)
    Label(f13,text="Gajar Halwa",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=160)
    Label(f13,text="Sizzling Brownie",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=210)
    Label(f13,text="HOT BEVERAGES",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=525,y=260)
    Label(f13,text="Filter Coffee",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=310)
    Label(f13,text="Tea",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=360)
    Label(f13,text="Milk",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=410)
    Label(f13,text="Hot Chocolate",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=460)
    Label(f13,text="ICE CREAM",font=('Segoe UI Semibold',22,'bold'),bg='yellow',fg='brown').place(x=525,y=510)
    Label(f13,text="As per M.R.P",font=('Segoe UI Semibold',20,'bold'),bg='yellow',fg='black').place(x=525,y=560)

    Button(win,text="Previous",font=('Segoe UI Semibold',15,'bold'),bg='white',fg='black',command=lambda:menup4(win)).place(x=75,y=650)

    
  
def rateus(w):
    w.destroy()
    win=Tk()
    win.title("rate us")
    win.geometry('950x768')
    photo=PhotoImage(file='admin.gif')
    Label(win,image=photo).place(x=0,y=0)
    Label(win,text="Welcome,"+crlist[0],font=('Segoe UI Semibold',20,'bold'),height=1,bg='white',fg='black').place(x=710,y=10)
    Label(win,text='Rate Us',font=('Segoe UI Semibold',22,'bold'),height=1,width=10,bg='white',fg='black').place(x=300,y=30)
    Label(win,text='1.Room Services',font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black').place(x=50,y=100)
    Label(win,text='2.Food Quality',font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black').place(x=500,y=100)
    Label(win,text='3.Cleanliness',font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black').place(x=50,y=250)
    Label(win,text='4.Comfort',font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black').place(x=500,y=250)
    Label(win,text='5.Aminities',font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black').place(x=50,y=400)
    Label(win,text='6.Overall Rating',font=('Segoe UI Semibold',22,'bold'),bg='white',fg='black').place(x=500,y=400)
    rat1=StringVar()
    rat2=StringVar()
    rat3=StringVar()
    rat4=StringVar()
    rat5=StringVar()
    rat6=StringVar()
    Radiobutton(win,text="Excellent",value=10,variable=rat1,command=lambda:rate1()).place(x=50,y=150)
    Radiobutton(win,text="Good",value=8,variable=rat1,command=lambda:rate1()).place(x=125,y=150)
    Radiobutton(win,text="Average",value=6,variable=rat1,command=lambda:rate1()).place(x=183,y=150)
    Radiobutton(win,text="Below Average",value=4,variable=rat1,command=lambda:rate1()).place(x=256,y=150)
    Radiobutton(win,text="Poor",value=2,variable=rat1,command=lambda:rate1()).place(x=363,y=150)
    Radiobutton(win,text="Excellent",value=10,variable=rat2,command=lambda:rate2()).place(x=500,y=150)
    Radiobutton(win,text="Good",value=8,variable=rat2,command=lambda:rate2()).place(x=575,y=150)
    Radiobutton(win,text="Average",value=6,variable=rat2,command=lambda:rate2()).place(x=633,y=150)
    Radiobutton(win,text="Below Average",value=4,variable=rat2,command=lambda:rate2()).place(x=706,y=150)
    Radiobutton(win,text="Poor",value=2,variable=rat2,command=lambda:rate2()).place(x=813,y=150)
    Radiobutton(win,text="Excellent",value=10,variable=rat3,command=lambda:rate3()).place(x=50,y=300)
    Radiobutton(win,text="Good",value=8,variable=rat3,command=lambda:rate3()).place(x=125,y=300)
    Radiobutton(win,text="Average",value=6,variable=rat3,command=lambda:rate3()).place(x=183,y=300)
    Radiobutton(win,text="Below Average",value=4,variable=rat3,command=lambda:rate3()).place(x=256,y=300)
    Radiobutton(win,text="Poor",value=2,variable=rat3,command=lambda:rate3()).place(x=363,y=300)
    Radiobutton(win,text="Excellent",value=10,variable=rat4,command=lambda:rate4()).place(x=500,y=300)
    Radiobutton(win,text="Good",value=8,variable=rat4,command=lambda:rate4()).place(x=575,y=300)
    Radiobutton(win,text="Average",value=6,variable=rat4,command=lambda:rate4()).place(x=633,y=300)
    Radiobutton(win,text="Below Average",value=4,variable=rat4,command=lambda:rate4()).place(x=706,y=300)
    Radiobutton(win,text="Poor",value=2,variable=rat4,command=lambda:rate4()).place(x=813,y=300)
    Radiobutton(win,text="Excellent",value=10,variable=rat5,command=lambda:rate5()).place(x=50,y=450)
    Radiobutton(win,text="Good",value=8,variable=rat5,command=lambda:rate5()).place(x=125,y=450)
    Radiobutton(win,text="Average",value=6,variable=rat5,command=lambda:rate5()).place(x=183,y=450)
    Radiobutton(win,text="Below Average",value=4,variable=rat5,command=lambda:rate5()).place(x=256,y=450)
    Radiobutton(win,text="Poor",value=2,variable=rat5,command=lambda:rate5()).place(x=363,y=450)
    Radiobutton(win,text="Excellent",value=10,variable=rat6,command=lambda:rate6()).place(x=500,y=450)
    Radiobutton(win,text="Good",value=8,variable=rat6,command=lambda:rate6()).place(x=575,y=450)
    Radiobutton(win,text="Average",value=6,variable=rat6,command=lambda:rate6()).place(x=633,y=450)
    Radiobutton(win,text="Below Average",value=4,variable=rat6,command=lambda:rate6()).place(x=706,y=450)
    Radiobutton(win,text="Poor",value=2,variable=rat6,command=lambda:rate6()).place(x=813,y=450)
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:checkin(win)).place(x=10,y=20)
    Button(win,text="Leave Us aComment/Feedback",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',height=1,width=25,command=lambda:feedback(win)).place(x=300,y=550)
    def rate1():
        global r1
        r1=rat1.get()
        print("room service rating",r1)
    def rate2():
        global r2
        r2=rat2.get()
        print("food quality rating",r2)
    def rate3():
        global r3
        r3=rat3.get()
        print("cleanliness rating",r3)
    def rate4():
        global r4
        r4=rat4.get()
        print("comfort rating",r4)
    def rate5():
        global r5
        r5=rat5.get()
        print("aminities rating",r5)
    def rate6():
        global r6
        r6=rat6.get()
        print("overall rating:",r6)
    win.mainloop()
def guestman(w):
    w.destroy()
    win=Tk()
    win.title("guest manager")
    win.geometry('600x401')
    win.config(background="midnight blue")
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:admin(win)).place(x=10,y=20)
    
    Label(win,text='Guest Manager',font=('Segoe UI Semibold',22,'bold'),height=1,width=25,bg='gold',fg='black').place(x=100,y=30)
    try:
        Label(win,text="Loged in Guest:"+crlist[0],font=('Segoe UI Semibold',20,'bold'),height=1,bg='white',fg='black').place(x=150,y=250)
        Label(win,text="Room no.:"+crlist[8],font=('Segoe UI Semibold',20,'bold'),height=1,bg='white',fg='black').place(x=150,y=300)
        Button(win,text="Comments/Feedback from Guest",font=('Segoe UI Semibold',20,'bold'),bg='gold',fg='black',command=lambda:feed()).place(x=130,y=180)
        try:
            global r1
            global r2
            global r3
            global r4
            global r5
            global r6
            s=int(r1)+int(r2)+int(r3)+int(r4)+int(r5)+int(r6)
            Button(win,text="Guest Rating Graph",font=('Segoe UI Semibold',20,'bold'),bg='gold',fg='black',command=lambda:graph()).place(x=150,y=100)
            def graph():
                top=Toplevel()
                top.title("graph")
                top.geometry("600x501")
                data={'Rating Categories' : ['Room Services','Food Quality','Cleanliness','Comfort','Aminities','Overall Rating'],
                      'Customer Rating' : [int(r1),int(r2),int(r3),int(r4),int(r5),int(r6)]}
                df=DataFrame(data, columns= ['Rating Categories','Customer Rating'])
                df=df[['Rating Categories','Customer Rating']].groupby('Rating Categories').sum()
                f1=plt.Figure(figsize=(6,6),dpi=100)
                ax1=f1.add_subplot(111)
                bar1=FigureCanvasTkAgg(f1,top)
                bar1.get_tk_widget().pack(side=LEFT,fill=BOTH)
                df.plot(kind='bar',legend=True,ax=ax1)
                ax1.set_title('Rating Categories Vs. Customer Rating')
        except:
            msg.showerror("Guest Manager",crlist[0]+" "+"has not rated")
        def feed():
            from listComp import ListComp
            listrequest = ListComp()
    except:
        msg.showinfo("guestman","NO guest has loged in")
    win.mainloop()
def admin(w):
    w.destroy()
    win=Tk()
    win.title("Admin")
    win.geometry('1024x650')
    photo=PhotoImage(file='admin.gif')
    Label(win,image=photo).place(x=0,y=0)
    Label(win,text='Welcome Admin',font=('Segoe UI Semibold',22,'bold'),height=1,width=25,bg='white',fg='black',command=None).place(x=300,y=30)
    Button(win,text="Show Guest List",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:showguest(win)).place(x=400,y=175)  
    Button(win,text="Stock & Inventory",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:inventory(win)).place(x=390,y=250)
    Button(win,text="Guest Manager",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:guestman(win)).place(x=400,y=325)
    Button(win,text="Employee Management",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:emp(win)).place(x=350,y=400) 
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:main(win)).place(x=10,y=20)
    win.mainloop()
def otherser(w):
    w.destroy()
    win=Tk()
    win.title("other services")
    win.geometry('564x430')
    photo=PhotoImage(file='roomser.gif')
    Label(win,image=photo).place(x=0,y=0)
    Label(win,text="Welcome,"+crlist[0],font=('Segoe UI Semibold',20,'bold'),height=1,bg='white',fg='black').place(x=410,y=10)
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:checkin(win)).place(x=10,y=20)
    Button(win,text="Taxi",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:taxi(win)).place(x=100,y=50)
    Button(win,text="Mail",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:mail(win)).place(x=100,y=125)
    Button(win,text="Book a Tour Package",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:tourpac()).place(x=100,y=200)
    win.mainloop()

def roomcle(w):
    w.destroy()
    win=Tk()
    win.title("cleaning..")
    win.geometry('600x401')
    photo=PhotoImage(file='cleaning.gif')
    Label(win,image=photo).place(x=0,y=0)
    Label(win,text='Cleaning is Under Progress',font=('Segoe UI Semibold',22,'bold'),height=1,bg='white',fg='black').place(x=50,y=50)
    Label(win,text='Time Left:',font=('Segoe UI Semibold',22,'bold'),height=1,bg='white',fg='black').place(x=50,y=100)
    l=Label()
    l.config(bg="yellow")
    l.config(height=1,font=('times',22,'bold'))
    l.place(x=200,y=100)
    for i in range(90,0,-1):
        l["text"]=i
        win.update()
        time.sleep(1)
    l.config(bg='red')
    l.config(fg='white')
    l["text"]="your room is ready!"
    Button(win,text='Done',font=("Segoe UI Semibold",14),height=1,bg='white',fg='black',command=lambda:checkin(win)).place(x=250,y=300)
    Label(win,text='Please Rate Our Service',font=('Segoe UI Semibold',14,'bold'),height=1,bg='white',fg='black').place(x=50,y=350)
    Button(win,text='Rate Us',font=("Segoe UI Semibold",14),height=1,bg='white',fg='black',command=lambda:rateus(win)).place(x=270,y=350)
    win.mainloop()
def roomser(w):
    w.destroy()
    win=Tk()
    win.title("room service")
    win.geometry('564x430')
    photo=PhotoImage(file='roomser.gif')
    Label(win,image=photo).place(x=0,y=0)
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:checkin(win)).place(x=10,y=20)
    Label(win,text='Room Services',font=('Segoe UI Semibold',22,'bold'),height=1,bg='white',fg='black').place(x=180,y=30)
    Label(win,text="Welcome,"+crlist[0],font=('Segoe UI Semibold',20,'bold'),height=1,bg='white',fg='black').place(x=410,y=10)
    Button(win,text="Room Cleaning Service",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:roomcle(win)).place(x=125,y=100)
    Button(win,text="In-Room Dining",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:rmdin(win)).place(x=150,y=175)
    win.mainloop()
    
def ngres(w):
    w.destroy()
    win=Tk()
    win.title("Restaurant")
    win.geometry('1024x650')
    photo=PhotoImage(file='rest.gif')
    Label(win,image=photo).place(x=0,y=0)
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:main(win)).place(x=10,y=20)
    Label(win,text='Welcome to Akshay Restaurants',font=('Segoe UI Semibold',22,'bold'),height=1,width=25,bg='white',fg='black').place(x=280,y=30)
    Button(win,text="Our Menu",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:menu(win)).place(x=375,y=150)
    Button(win,text="Order Online",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:orderon()).place(x=350,y=250)
    win.mainloop()
def res(w):
    w.destroy()
    win=Tk()
    win.title("Restaurant")
    win.geometry('1024x650')
    photo=PhotoImage(file='rest.gif')
    Label(win,image=photo).place(x=0,y=0)
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:main(win)).place(x=10,y=20)
    Label(win,text='Welcome to Akshay Restaurants',font=('Segoe UI Semibold',22,'bold'),height=1,width=25,bg='white',fg='black').place(x=280,y=30)
    Label(win,text="Welcome,"+crlist[0],font=('Segoe UI Semibold',20,'bold'),height=1,bg='white',fg='black').place(x=710,y=10)
    Button(win,text="Our Menu",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:menu(win)).place(x=375,y=150)
    Button(win,text="Order Online",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:orderon()).place(x=350,y=250)
    Button(win,text="Request Room Service",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:rmdin(win)).place(x=300,y=350)
    win.mainloop()


def checkin(w):
    global u
    w.destroy()
    win=Tk()
    win.title("Check In")
    win.geometry('936x557')
    photo=PhotoImage(file='checkmain.gif')
    Label(win,image=photo).place(x=0,y=0)
    Label(win,text='Welcome to Akshay Hotels',font=('Segoe UI Semibold',22,'bold'),height=1,width=25,bg='white',fg='black').place(x=280,y=30)
    Label(win,text="Welcome,"+crlist[0],font=('Segoe UI Semibold',20,'bold'),height=1,bg='white',fg='black').place(x=710,y=10)
    Button(win,text='Back',font=("Script MT Bold",10),bg='white',fg='black',command=lambda:main(win)).place(x=10,y=20)
    Button(win,text="Restaurant",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:res(win)).place(x=400,y=100)
    Button(win,text="Laundry",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:laundry(win)).place(x=410,y=175)
    Button(win,text="Room Services",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:roomser(win)).place(x=375,y=250)
    Button(win,text="Other Services",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:otherser(win)).place(x=375,y=325)
    Button(win,text="Check out",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:checkout1(win)).place(x=415,y=400)
    Button(win,text="Logout",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',height=1,command=lambda:logout(win)).place(x=100,y=475)
    Button(win,text="Rate us",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:rateus(win)).place(x=750,y=475)
    
    win.mainloop()
def main(w):
    w.destroy()
    win=Tk()
    win.title('Akshay')
    win.geometry('1000x516')
    win.config(background='blue')
    photo=PhotoImage(file='projectmain.gif')
    a=Label(win,image=photo)
    a.place(x=0,y=0)
    Label(win,text='Welcome to Akshay Hotels',font=('Segoe UI Semibold',22,'bold'),height=1,width=25,bg='white',fg='black').place(x=300,y=30)
    Button(win,text="Check In",font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',command=lambda:welcome(win)).place(x=240,y=190)
    Button(win,text="Go to Restaurant",bg="white",fg='black',font=('Segoe UI Semibold',20,'bold'),command=lambda:ngres(win)).place(x=620,y=190)
    Button(win,text='Exit',font=('Segoe UI Semibold',20,'bold'),bg='white',fg='black',height=1,command=win.destroy).place(x=475,y=360)
    Button(win,text="Admin",font=('Segoe UI Semibold',20,'bold'),bg='black',fg='white',height=1,command=lambda:loginad(win)).place(x=100,y=450)
    Label(win,text='Already a Guest ? ',font=('Segoe UI Semibold',22,'bold'),height=1,bg='white',fg='black').place(x=450,y=460)
    Button(win,text="Login In",bg="white",fg='black',font=('Segoe UI Semibold',20,'bold'),command=lambda:login(win)).place(x=700,y=450)
    mainloop()
win=Tk()
main(win)


    






