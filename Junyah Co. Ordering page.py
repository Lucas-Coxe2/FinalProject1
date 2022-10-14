from cProfile import label
from cgitb import text
import cmd
from multiprocessing.sharedctypes import Value
from sqlite3 import Row
from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from tkinter import font
from tkinter.font import BOLD
from tkinter.tix import COLUMN
from turtle import back, width

root = Tk()
root.geometry("1350x650+0+0")
root.title("Junyah Industries Ordering")
root.configure(background='green')

def Exit():
    qExit = messagebox.askyesno("Junyah Industries", "Are you sure you want to leave your order")
    if qExit > 0:
        root.destroy()
        return
def reset():
    CustomerName.set("")
    CustomerEmail.set("")
    CustomerPhone.set("")
    DateOfOrder.set("")
    TimeOfOrder.set("")
    Tax.set("")
    SubTotal.set("")






Tops=Frame(root,width=1350, height=50,bd= 16, relief="raise")
Tops.pack(side=TOP)


LF = Frame(root, width=700, height = 650, bd=16, relief="raise")
LF.pack(side=LEFT)

RF = Frame(root, width=600, height=650, bd=16, relief="raise")
RF.pack(side=RIGHT)

Tops.configure(background='black')
LF.configure(background='black')
RF.configure(background='black')


LeftInsideLF = Frame(LF, width=700, height=100, bd=8, relief="raise")
LeftInsideLF.pack(side=TOP)
LeftInsideFLF = Frame(LF, width=700, height=400, bd=8, relief="raise")
LeftInsideFLF.pack(side=LEFT)

RightInsideLF = Frame(RF, width=604, height=200, bd = 8, relief="raise")
RightInsideLF.pack(side=TOP)
RightInsideFLF = Frame(RF, width=306, height=400, bd = 8, relief="raise")
RightInsideFLF.pack(side=LEFT)
RightInsideRF = Frame(RF, width=300, height=400, bd = 8, relief="raise")
RightInsideRF.pack(side=RIGHT)

#Top Left Frame

CustomerName = label(LeftInsideLF,font=('arial',14,'bold'), text="Customer Name",
                    fg="black", bd=10, anchor = "w")
CustomerName.grid(row = 0, colum = 0)

txtCustomerName = Entry(LeftInsideLF, font=('arial',14,'bold'), bd = 20, width=43, bg="white",
                        justify='left', textvariable= CustomerName) 
txtCustomerName.grid(row=0, column=1)



CustomerPhone = label(LeftInsideLF,font=('arial',14,'bold'), text="Customer Phone #",
                    fg="black", bd=10, anchor = "w")
CustomerPhone.grid(row = 1, colum = 0)

txtCustomerPhone = Entry(LeftInsideLF, font=('arial',14,'bold'), bd = 20, width=43, bg="white",
                        justify='left', textvariable= CustomerPhone) 
txtCustomerPhone.grid(row=1, column=1)



CustomerEmail = label(LeftInsideLF,font=('arial',14,'bold'), text="Customer Email",
                    fg="black", bd=10, anchor = "w")
CustomerEmail.grid(row = 2, colum = 0)

txtCustomerEmail = Entry(LeftInsideLF, font=('arial',14,'bold'), bd = 20, width=43, bg="white",
                        justify='left', textvariable= CustomerEmail) 
txtCustomerEmail.grid(row=2, column=1)


#Top Right Frame
DateOfOrder = label(RightInsideLF, font=('arial',14,'bold'), text="Date of Order",
                    fg="black", bd=10, anchor = "w")
DateOfOrder.grid(row=0, column=0)
txtDateOfOrder = Entry(RightInsideLF, font=('arial',12,'bold'), bd = 20, width=43, bg="white",
                        justify='left', textvariable= DateOfOrder) 
txtDateOfOrder.grid(row=0, column=1)


TimeOfOrder = label(RightInsideLF, font=('arial',12,'bold'), text="Time of Order",
                    fg="black", bd=10, anchor = "w")
TimeOfOrder.grid(row=1, column=0)
txtTimeOfOrder = Entry(RightInsideLF, font=('arial',12,'bold'), bd = 20, width=43, bg="white",
                        justify='left', textvariable= DateOfOrder) 
txtTimeOfOrder.grid(row=1, column=1)


CustomerReference = label(RightInsideLF, font=('arial',12,'bold'), text="Customer Reference",
                    fg="black", bd=10, anchor = "w")
CustomerReference.grid(row=2, column=0)
txtCustomerReference = Entry(RightInsideLF, font=('arial',12,'bold'), bd = 20, width=43, bg="white",
                        justify='left', textvariable= DateOfOrder) 
txtCustomerReference.grid(row=3, column=1)



#Right Frame
Naming = Label(Tops, font=('arial', 50, 'bold'), text="   Junyah Industries   ", bd=10, anchor='w')
Naming.grid(row=0, column=0)

MethodOfPayment = Label(RightInsideFLF, font=('arial', 12, 'bold'), text="Method of Payment",
                        fg="black", bd=16,anchor="w")
MethodOfPayment.grid(row=0, column=0)

cmdMethodOfPayment=ttk.Combobox(RightInsideFLF,font=('arial',10,'bold'))
cmdMethodOfPayment['Value'] = 'Cash','Debit Card','Visa Card', 'Master Card'
cmdMethodOfPayment.grid(row=0,column=1)

Discount = Label(RightInsideFLF, font=('arial',12,'bold'), text="Discount", fg="black", bd=16, anchor = 'w')
Discount.grid(row = 1, column=0)
txtDiscount = Entry(RightInsideFLF, font=('arial',12,'bold'), bd = 16, width = 18,
                    bg="white", justify= 'left', textvariable=Discount)
txtDiscount.grid(row=1, column=1)


Tax = Label(RightInsideFLF, font=('arial',12,'bold'), text="Discount", fg="black", bd=16, anchor = 'w')
Tax.grid(row = 2, column=0)

txtTax = Entry(RightInsideFLF, font=('arial',12,'bold'), bd = 16, width = 18,
                    bg="white", justify= 'left', textvariable=Tax)
txtTax.grid(row=2,column=1)


SubTotal = Label(RightInsideFLF, font=('arial',12,'bold'), text="Discount", fg="black", bd=16, anchor = 'w')
SubTotal.grid(row = 3, column=0)

txtSubTotal = Entry(RightInsideFLF, font=('arial',12,'bold'), bd = 16, width = 18,
                    bg="white", justify= 'left', textvariable=SubTotal)
txtSubTotal.grid(row=3,column=1)

#Bottom Left Frame

ItemOrder = label(LeftInsideFLF, font =('arial', 14, 'bold'), text = "Item Order", fg = "black", bd = 20)
ItemOrder.grid(row = 0, colum = 0)
ItemQuantity = label(LeftInsideFLF,font =('arial', 14, 'bold'), text = "Item Order", fg = "black", bd = 10)
ItemQuantity.grid(row = 0, colum = 1)
CostOfItem = label(LeftInsideFLF, font =('arial', 14, 'bold'), text = "Item Order", fg = "black", bd = 20)
CostOfItem.grid(row = 0, colum = 3)
#==================================
TShirt = label(LeftInsideFLF, font =('arial', 14, 'bold'), text = "Item Order", fg = "black", bd = 20)
TShirt.grid(row = 1, colum = 0)
Hoodie = label(LeftInsideFLF, font =('arial', 14, 'bold'), text = "Item Order", fg = "black", bd = 20)
Hoodie.grid(row = 2, colum = 0)
LongSleeve = label(LeftInsideFLF, font =('arial', 14, 'bold'), text = "Item Order", fg = "black", bd = 20)
LongSleeve.grid(row = 3, colum = 0)
#==================================
QuantityTShirt =(400)
QuantityHoodie =(400)
QuantityLongSleeve =(250)
#==================================
txtQuantityTShirt = Entry(LeftInsideFLF, font =('arial', 12, 'bold'), bd =20, width=16,
                          bg = "white", justify='left', textvariable = QuantityTShirt)
txtQuantityTShirt.grid(row=1,colum=1)

txtQuantityHoodie = Entry(LeftInsideFLF, font =('arial', 12, 'bold'), bd =20, width=16,
                          bg = "white", justify='left', textvariable = QuantityHoodie)
txtQuantityHoodie.grid(row=2,colum=1)

txtQuantityLongSleeve = Entry(LeftInsideFLF, font =('arial', 12, 'bold'), bd =20, width=16,
                          bg = "white", justify='left', textvariable = QuantityLongSleeve)
txtQuantityLongSleeve.grid(row=3,colum=1)
#========================================
CostTShirt = ()
CostHoodie =()
CostLongSleeve = ()
#=========================================

txtCostTShirt = Entry(LeftInsideFLF, font =('arial', 12, 'bold'), bd =20, width=16,
                          bg = "white", justify='left', textvariable = CostTShirt)
txtCostTShirt.grid(row=1,colum=2)

txtCostHoodie = Entry(LeftInsideFLF, font =('arial', 12, 'bold'), bd =20, width=16,
                          bg = "white", justify='left', textvariable = CostHoodie)
txtCostHoodie.grid(row=2,colum=2)

txtCostLongSleeve = Entry(LeftInsideFLF, font =('arial', 12, 'bold'), bd =20, width=16,
                          bg = "white", justify='left', textvariable = CostLongSleeve)
txtCostLongSleeve.grid(row=1,colum=2)




#Right Frame Buttons
btnCost = Button(RightInsideRF, paddy=8,bd=8,fg="black",font=('arial',16,'bold'), width=11,
                text="Total Cost", bg="white").grid(row=0,column=0)
btnReset = Button(RightInsideRF, paddy=8,bd=8,fg="black",font=('arial',16,'bold'), width=11,
                text="Reset", bg="white", command=reset).grid(row=1,column=0)
btnOrderReference = Button(RightInsideRF, paddy=8,bd=8,fg="black",font=('arial',16,'bold'), width=11,
                text="Order Reference", bg="white").grid(row=2,column=0)
btnExit = Button(RightInsideRF, paddy=8,bd=8,fg="black",font=('arial',16,'bold'), width=11,
                text="Exit", bg="white",command=Exit).grid(row=3,column=0)








root.mainloop()