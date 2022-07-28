from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria', 30, 'bold') ,text="Restaurant Management System",bg="darkviolet",fg="orange",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria',20, ),text=localtime,fg="black",anchor=W)
lblinfo.grid(row=1,column=0)

#---------------Calculator------------------
text_Input=StringVar()
operator =""

txtdisplay = Entry(f2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
txtdisplay.grid(columnspan=4)

def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    ord.set(randomRef)
    raw_text = u"\u20B9"

    if Punj.get()=='':
        pung=0
    else:
        pung =float(Punj.get())

    if chine.get()=='':
        chini=0
    else:
        chini= float(chine.get())

    if guj.get()=='':
        gujju=0
    else:
        gujju = float(guj.get())

    if rajas.get()=='':
        raja=0
    else:
       raja= float(rajas.get())

    if kathya.get()=='':
        kath=0
    else:
        kath= float(kathya.get())

    if cold.get()=='':
        drinkcold=0
    else:
       drinkcold= float(cold.get())

    pnjprice = pung*100
    chnprice = chini*150
    gjtprice = gujju*120
    rjsprice = raja*70
    ktwprice = kath*80
    drinksprice = drinkcold*50

    dinnercost = raw_text,str('%.2f'% (pnjprice +  chnprice + gjtprice + rjsprice + ktwprice + drinksprice))
    PayTax=((pnjprice +  chnprice + gjtprice + rjsprice +  ktwprice + drinksprice)*0.33)
    Totalcost=(pnjprice +  chnprice + gjtprice + rjsprice  + ktwprice + drinksprice)
    Ser_Charge=((pnjprice +  chnprice + gjtprice + rjsprice + ktwprice + drinksprice)/99)
    Service=raw_text,str('%.2f'% Ser_Charge)
    OverAllCost=raw_text,str( PayTax + Totalcost + Ser_Charge)
    PaidTax=raw_text,str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(dinnercost)
    Tax.set(PaidTax)
    Subtotal.set(dinnercost)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    Punj.set("")
    chine.set("")
    guj.set("")
    rajas.set("")
    kathya.set("")
    cold.set("")
    ord.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Tax.set("")
    cost.set("")



btn7=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="7",bg="black", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="8",bg="black", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="9",bg="black", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="+",bg="black", command=lambda: btnclick("+") )
Addition.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="4",bg="black", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="5",bg="black", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="6",bg="black", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)

Substraction=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="-",bg="black", command=lambda: btnclick("-") )
Substraction.grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="1",bg="black", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="2",bg="black", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="3",bg="black", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)

multiply=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="*",bg="black", command=lambda: btnclick("*") )
multiply.grid(row=4,column=3)
#------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="0",bg="black", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)

btnc=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="c",bg="black", command=clrdisplay)
btnc.grid(row=5,column=1)

btnequal=Button(f2,padx=16,pady=16,bd=4,width = 16, fg="white", font=('ariel', 20 ,'bold'),text="=",bg="black",command=eqals)
btnequal.grid(columnspan=4)

Decimal=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text=".",bg="black", command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=4, fg="white", font=('ariel', 20 ,'bold'),text="/",bg="black", command=lambda: btnclick("/") )
Division.grid(row=5,column=3)
status = Label(f2,font=('aria', 15, 'bold'),bd=2,relief=SUNKEN)
status.grid(row=7,columnspan=3)

#---------------------------------------------------------------------------------------
Punj = StringVar()
chine = StringVar()
guj = StringVar()
rajas = StringVar()
kathya= StringVar()
cold = StringVar()
ord = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
cost = StringVar()


lblmanok = Label(f1, font=('aria' , 16, 'bold'), text="Punjabi", fg="green", bd=10, anchor='w')
lblmanok.grid(row=0, column=0)
txtmanok = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=Punj, bd=6, insertwidth=4, bg="white", justify='left')
txtmanok.grid(row=0, column=1)

lblbaboy = Label(f1, font=('aria' , 16, 'bold'), text="Chinese", fg="green", bd=10, anchor='w')
lblbaboy.grid(row=1, column=0)
txtbaboy = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=chine, bd=6, insertwidth=4, bg="white", justify='left')
txtbaboy.grid(row=1, column=1)


lblhipon = Label(f1, font=('aria' , 16, 'bold'), text="Gujarati", fg="green", bd=10, anchor='w')
lblhipon.grid(row=2, column=0)
txthipon = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=guj, bd=6, insertwidth=4, bg="white", justify='left')
txthipon.grid(row=2, column=1)

lblkarikari = Label(f1, font=('aria' , 16, 'bold'), text="Rajasthani", fg="green", bd=10, anchor='w')
lblkarikari.grid(row=3, column=0)
txtkarikari = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=rajas, bd=6, insertwidth=4, bg="white", justify='left')
txtkarikari.grid(row=3, column=1)

lblpaksiw = Label(f1, font=('aria' , 16, 'bold'), text="Kathyawadi", fg="green", bd=10, anchor='w')
lblpaksiw.grid(row=4, column=0)
txtpaksiw = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=kathya, bd=6, insertwidth=4, bg="white", justify='left')
txtpaksiw.grid(row=4, column=1)


lblmountaindew = Label(f1, font=('aria' , 16, 'bold'), text="Drinks", fg="green", bd=10, anchor='w')
lblmountaindew.grid(row=5, column=0)
txtmountaindew = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=cold, bd=6, insertwidth=4, bg="white", justify='left')
txtmountaindew.grid(row=5, column=1)

#--------------------------------------------------------------------------------------
lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="red",bd=10,anchor='w')
lblreference.grid(row=0,column=2)
txtreference = Entry(f1, font=('ariel' ,16,'bold'), textvariable=ord, bd=6, insertwidth=4, bg="white", justify='left')
txtreference.grid(row=0,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",fg="red",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="white" ,justify='left')
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="red",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="white" ,justify='left')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="red",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="white" ,justify='left')
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="red",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="white" ,justify='left')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="red",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="white" ,justify='left')
txtTotal.grid(row=5,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="grey",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="grey",command=reset)
btnreset.grid(row=7, column=2)

#btnreview=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="REVIEW", bg="grey",command=review)
#btnreview.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=qexit)
btnexit.grid(row=7, column=4)

def review():
    roo = Tk()
    roo.geometry("600x400+0+0")
    roo.title("Review")
    fr = Frame(roo, width=900, height=700, relief=SUNKEN)
    fr.pack(side=LEFT)

    if Punj.get() == '':
        punj_text='0'
    else:
        punj_text=Punj.get()

    if chine.get() == '':
        chine_text='0'
    else:
        chine_text=chine.get()

    if guj.get() == '':
        guj_text='0'
    else:
        guj_text=guj.get()

    if rajas.get() == '':
        rajas_text='0'
    else:
        rajas_text=rajas.get()

    if kathya.get() == '':
        kathya_text='0'
    else:
        kathya_text=kathya.get()

    if cold.get() == '':
        cold_text='0'
    else:
        cold_text=cold.get()



    lblmanok_1 = Label(fr, font=('aria', 16, 'bold'), text="Items : ", fg="blue", bd=10, anchor='w')
    lblmanok_1.grid(row=0, column=0)
    lblmanok_price = Label(fr, font=('aria', 16, 'bold'), text="Quantity", fg="blue", bd=10, anchor='w')
    lblmanok_price.grid(row=0, column=1)
    lblmanok_price = Label(fr, font=('aria', 16, 'bold'), text="Price", fg="blue", bd=10, anchor='w')
    lblmanok_price.grid(row=0, column=2)

    lblmanok_1 = Label(fr, font=('aria', 16, 'bold'), text="Punjabi : ", fg="brown", bd=10, anchor='w')
    lblmanok_1.grid(row=1, column=0)
    lblmanok_price = Label(fr, font=('aria', 16, 'bold'), text=punj_text, fg="black", bd=10, anchor='w')
    lblmanok_price.grid(row=1, column=1)
    lblmanok_price = Label(fr, font=('aria', 16, 'bold'), text=int(punj_text)*100, fg="black", bd=10, anchor='w')
    lblmanok_price.grid(row=1, column=2)

    lblbaboy = Label(fr, font=('aria', 16, 'bold'), text="Chinese : ", fg="brown", bd=10, anchor='w')
    lblbaboy.grid(row=2, column=0)
    lblbaboy = Label(fr, font=('aria', 16, 'bold'), text=chine_text, fg="black", bd=10, anchor='w')
    lblbaboy.grid(row=2, column=1)
    lblbaboy = Label(fr, font=('aria', 16, 'bold'), text=int(chine_text)*150, fg="black", bd=10, anchor='w')
    lblbaboy.grid(row=2, column=2)

    lblhipon = Label(fr, font=('aria', 16, 'bold'), text="Gujarati : ", fg="brown", bd=10, anchor='w')
    lblhipon.grid(row=3, column=0)
    lblhipon = Label(fr, font=('aria', 16, 'bold'), text=guj_text, fg="black", bd=10, anchor='w')
    lblhipon.grid(row=3, column=1)
    lblhipon = Label(fr, font=('aria', 16, 'bold'), text=int(guj_text)*120, fg="black", bd=10, anchor='w')
    lblhipon.grid(row=3, column=2)

    lblkarikari = Label(fr, font=('aria', 16, 'bold'), text="Rajasthani : ", fg="brown", bd=10, anchor='w')
    lblkarikari.grid(row=4, column=0)
    lblkarikari = Label(fr, font=('aria', 16, 'bold'), text=rajas_text, fg="black", bd=10, anchor='w')
    lblkarikari.grid(row=4, column=1)
    lblkarikari = Label(fr, font=('aria', 16, 'bold'), text=int(rajas_text)*70, fg="black", bd=10, anchor='w')
    lblkarikari.grid(row=4, column=2)

    lblpaksiw = Label(fr, font=('aria', 16, 'bold'), text="Kathyawadi : ", fg="brown", bd=10, anchor='w')
    lblpaksiw.grid(row=5, column=0)
    lblpaksiw = Label(fr, font=('aria', 16, 'bold'), text=kathya_text, fg="black", bd=10, anchor='w')
    lblpaksiw.grid(row=5, column=1)
    lblpaksiw = Label(fr, font=('aria', 16, 'bold'), text=int(kathya_text)*80, fg="black", bd=10, anchor='w')
    lblpaksiw.grid(row=5, column=2)

    lblmountaindew = Label(fr, font=('aria', 16, 'bold'), text="Drinks", fg="brown", bd=10, anchor='w')
    lblmountaindew.grid(row=6, column=0)
    lblmountaindew = Label(fr, font=('aria', 16, 'bold'), text=cold_text, fg="black", bd=10, anchor='w')
    lblmountaindew.grid(row=6, column=1)
    lblmountaindew = Label(fr, font=('aria', 16, 'bold'), text=int(cold_text)*50, fg="black", bd=10, anchor='w')
    lblmountaindew.grid(row=6, column=2)

    roo.mainloop()

btnreview = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="REVIEW",bg="lightgreen", command=review)
btnreview.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Products", bg="darkblue", fg="white", bd=5)
    lblrestaurant.grid(row=0, column=0)
    lblrestaurant = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblrestaurant.grid(row=0, column=2)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="PRICE",bg="darkblue", fg="white", anchor=W)
    lblrestaurant.grid(row=0, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Punjabi", fg="brown", anchor=W)
    lblrestaurant.grid(row=1, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="100", fg="purple", anchor=W)
    lblrestaurant.grid(row=1, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Chinese", fg="brown", anchor=W)
    lblrestaurant.grid(row=2, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="150", fg="purple", anchor=W)
    lblrestaurant.grid(row=2, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Gujarati", fg="brown", anchor=W)
    lblrestaurant.grid(row=3, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="120", fg="purple", anchor=W)
    lblrestaurant.grid(row=3, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Rajasthani", fg="brown", anchor=W)
    lblrestaurant.grid(row=4, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="70", fg="purple", anchor=W)
    lblrestaurant.grid(row=4, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Kathyawadi", fg="brown", anchor=W)
    lblrestaurant.grid(row=5, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="80", fg="purple", anchor=W)
    lblrestaurant.grid(row=5, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="brown", anchor=W)
    lblrestaurant.grid(row=6, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="50", fg="purple", anchor=W)
    lblrestaurant.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="lightgreen",command=price)
btnprice.grid(row=7, column=0)

root.mainloop()