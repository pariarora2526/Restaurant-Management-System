from tkinter import*
from tkinter import filedialog,messagebox
import time
def reset():
    textreceipt.delete(1.0,END)
    e_burger.set('0')
    e_pizza.set('0')
    e_fries.set('0')
    e_momos.set('0')
    e_noodles.set('0')
    e_soup.set('0')
    e_tacos.set('0')
    e_pasta.set('0')

    e_coke.set('0')
    e_sprite.set('0')
    e_orangejuice.set('0')
    e_mojito.set('0')
    e_faluda.set('0')
    e_oreoshake.set('0')
    e_jaljeera.set('0')
    e_coffee.set('0')

    e_gulabjamun.set('0')
    e_icecream.set('0')
    e_jalebi.set('0')
    e_donut.set('0')
    e_brownie.set('0')
    e_waffle.set('0')
    e_pastry.set('0')
    e_rabri.set('0')
    
    textburger.config(state=DISABLED)
    textpizza.config(state=DISABLED)
    textfries.config(state=DISABLED)
    textmomos.config(state=DISABLED)
    textnoodles.config(state=DISABLED)
    textsoup.config(state=DISABLED)
    texttacos.config(state=DISABLED)
    textpasta.config(state=DISABLED)
    
    textcoke.config(state=DISABLED)
    textsprite.config(state=DISABLED)
    textorangejuice.config(state=DISABLED)
    textmojito.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textoreoshake.config(state=DISABLED)
    textjaljeera.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    
    textgulabjamun.config(state=DISABLED)
    texticecream.config(state=DISABLED)
    textjalebi.config(state=DISABLED)
    textdonut.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textwaffle.config(state=DISABLED)
    textpastry.config(state=DISABLED)
    textrabri.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)

    costofdrinksvar.set('')
    costoffoodvar.set('')
    costofsweetsvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')

def menu():
    
    root2=Toplevel()

    root2.title("Menu")
    root2.config(bg='red4')
    root2.geometry('850x350+50+50')#w*h distance from x and y axis
    root2.resizable(0,0)
    
    nameLabel=Label(root2,text='YUMMY IN THE TUMMY!!',font=('Britannic Bold',35,'bold underline'),bg='red4',fg='white')
    nameLabel.pack()

    nameLabel1=Label(root2,text='Menu',font=('Algerian',25,'bold underline'),bg='red4',fg='white')
    nameLabel1.pack()
    
    textarea=Text(root2,font=('arial',12,'bold'),bg='light grey',bd=3,width=800,height=350)
    textarea.pack(pady=5)

    textarea.insert(END, f'Food \t\t Cost of food \t\t Drinks \t\t Cost of drinks \t\t Sweets \t\t Cost of sweets\n\n')
    textarea.insert(END, f'Burger \t\t Rs50 \t\t Coke \t\t Rs49 \t\t Gulabjamun \t\t Rs99\n')
    textarea.insert(END, f'Pizza \t\t Rs200 \t\t Sprite \t\t Rs49 \t\t Icecream \t\t Rs49\n')
    textarea.insert(END, f'Fries \t\t Rs99 \t\t Orange juice \t\t Rs89 \t\t Jalebi \t\t Rs59\n')
    textarea.insert(END, f'Momos \t\t Rs100 \t\t Mojito \t\t Rs149  \t\t Donut \t\t Rs149\n')
    textarea.insert(END, f'Noodles \t\t Rs80 \t\t Faluda \t\t Rs100 \t\t Brownie \t\t Rs199\n')
    textarea.insert(END, f'Soup \t\t Rs99 \t\t Oreo shake \t\t Rs80 \t\t Waffle \t\t Rs100\n')
    textarea.insert(END, f'Tacos \t\t Rs199 \t\t Jaljeera \t\t Rs50 \t\t Pastry \t\t Rs49\n')
    textarea.insert(END, f'Pasta \t\t Rs100 \t\t Coffee \t\t Rs45 \t\t Rabri \t\t Rs65\n')
    

    
    root2.mainloop()
def save():
    if textreceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:
            bill_data=textreceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is Succesfully Saved')
    
def receipt():
    global billnumber,date
    if costoffoodvar.get() != '' or costofsweetsvar.get() != '' or costofdrinksvar.get() != '':
        textreceipt.delete(1.0,END)
 #  x=random.randint(100,10000)
        max1="1"
        filehandle=open("receipt.txt","r")
        a=filehandle.read()
        for i in range(len(a)):
            if a[i]>max1:
                max1=a[i]
        filehandle.close()
        filehandle=open("receipt.txt","a")
        max1=int(max1)
        filehandle.write(str(max1+1))
        filehandle.close()
        billnumber='BILL'+str(max1)
        date=time.strftime('%d/%m/%Y')
        textreceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textreceipt.insert(END,'*********************************************************************\n')
        textreceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
        textreceipt.insert(END,'*********************************************************************\n')
        if e_burger.get()!='0':
                textreceipt.insert(END,f'Burger\t\t\t{int(e_burger.get())*50}\n\n')
        if e_pizza.get()!='0':
                textreceipt.insert(END,f'Pizza\t\t\t{int(e_pizza.get())*200}\n\n')
        if e_fries.get()!='0':
                textreceipt.insert(END,f'Fries\t\t\t{int(e_fries.get())*99}\n\n')
        if e_momos.get()!='0':
                textreceipt.insert(END,f'Momos\t\t\t{int(e_momos.get())*100}\n\n')
        if e_noodles.get()!='0':
                textreceipt.insert(END,f'Noodles\t\t\t{int(e_noodles.get())*80}\n\n')
        if e_soup.get()!='0':
                textreceipt.insert(END,f'Soup\t\t\t{int(e_soup.get())*99}\n\n')
        if e_tacos.get()!='0':
                textreceipt.insert(END,f'Tacos\t\t\t{int(e_tacos.get())*199}\n\n')
        if e_pasta.get()!='0':
                textreceipt.insert(END,f'Pasta\t\t\t{int(e_pasta.get())*100}\n\n')
        if e_coke.get()!='0':
                textreceipt.insert(END,f'Coke\t\t\t{int(e_coke.get())*49}\n\n')
        if e_sprite.get()!='0':
                textreceipt.insert(END,f'Sprite\t\t\t{int(e_sprite.get())*49}\n\n')
        if e_orangejuice.get()!='0':
                textreceipt.insert(END,f'Orangejuice\t\t\t{int(e_orangejuice.get())*89}\n\n')
        if e_mojito.get()!='0':
                textreceipt.insert(END,f'Mojito\t\t\t{int(e_mojito.get())*149}\n\n')
        if e_faluda.get()!='0':
                textreceipt.insert(END,f'Faluda\t\t\t{int(e_faluda.get())*100}\n\n')
        if e_oreoshake.get()!='0':
                textreceipt.insert(END,f'Oreoshake\t\t\t{int(e_oreoshake.get())*80}\n\n')
        if e_jaljeera.get()!='0':
                textreceipt.insert(END,f'Jaljeera\t\t\t{int(e_jaljeera.get())*50}\n\n')
        if e_coffee.get()!='0':
                textreceipt.insert(END,f'Coffee\t\t\t{int(e_coffee.get())*45}\n\n')
        if e_gulabjamun.get()!='0':
                textreceipt.insert(END,f'Gulabjamun\t\t\t{int(e_gulabjamun.get())*99}\n\n')
        if e_icecream.get()!='0':
                textreceipt.insert(END,f'IceCream\t\t\t{int(e_icecream.get())*49}\n\n')
        if e_jalebi.get()!='0':
                textreceipt.insert(END,f'Jalebi\t\t\t{int(e_jalebi.get())*59}\n\n')
        if e_donut.get()!='0':
                textreceipt.insert(END,f'Donut\t\t\t{int(e_donut.get())*149}\n\n')
        if e_brownie.get()!='0':
                textreceipt.insert(END,f'brownie\t\t\t{int(e_brownie.get())*199}\n\n')
        if e_waffle.get()!='0':
                textreceipt.insert(END,f'Waffle\t\t\t{int(e_waffle.get())*100}\n\n')
        if e_pastry.get()!='0':
                textreceipt.insert(END,f'Pastry\t\t\t{int(e_pastry.get())*49}\n\n')
        if e_rabri.get()!='0':
                textreceipt.insert(END,f'Rabri\t\t\t{int(e_rabri.get())*65}\n\n')
                
        textreceipt.insert(END,'*********************************************************************\n')       
        if costoffoodvar.get()!='0 Rs':
                textreceipt.insert(END,f'Cost of food\t\t\t{priceoffood}Rs\n\n')
        if costofdrinksvar.get()!='0 Rs':
                textreceipt.insert(END,f'Cost of drinks\t\t\t{priceofdrinks}Rs\n\n')
        if costofsweetsvar.get()!='0 Rs':
                textreceipt.insert(END,f'Cost of sweets\t\t\t{priceofsweets}Rs\n\n')
        textreceipt.insert(END,f'Sub Total\t\t\t{subtotal}Rs\n\n')
        textreceipt.insert(END,f'Service Tax\t\t\t{39}Rs\n\n')
        textreceipt.insert(END,f'Total Cost\t\t\t{subtotal+50}Rs\n\n')
        
        textreceipt.insert(END,'*********************************************************************\n')
    else:
        messagebox.showerror('Error','No Item Is selected')
       
      
def Totalcost():
    global priceoffood,priceofdrinks,priceofsweets,subtotal
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0:
        item1=int(e_burger.get())#whatever the quantity user has selected will come here
        item2=int(e_pizza.get())
        item3=int(e_fries.get())
        item4=int(e_momos.get())
        item5=int(e_noodles.get())
        item6=int(e_soup.get())
        item7=int(e_tacos.get())
        item8=int(e_pasta.get())
        
        item9=int(e_coke.get())
        item10=int(e_sprite.get())
        item11=int(e_orangejuice.get())
        item12=int(e_mojito.get())
        item13=int(e_faluda.get())
        item14=int(e_oreoshake.get())
        item15=int(e_jaljeera.get())
        item16=int(e_coffee.get())
        
        item17=int(e_gulabjamun.get())
        item18=int(e_icecream.get())
        item19=int(e_jalebi.get())
        item20=int(e_donut.get())
        item21=int(e_brownie.get())
        item22=int(e_waffle.get())
        item23=int(e_pastry.get())
        item24=int(e_rabri.get())
        
        priceoffood=(item1*50)+(item2*200)+(item3*99)+(item4*100)+(item5*80)+(item6*99)+(item7*199)+(item8*100)

        priceofdrinks=(item9*49)+(item10*49)+(item11*89)+(item12*149)+(item13*100)+(item14*80)+(item15*50)+(item16*45)

        priceofsweets=(item17*99)+(item18*49)+(item19*59)+(item20*149)+(item21*199)+(item22*100)+(item23*49)+(item24*65)

        costoffoodvar.set(str(priceoffood)+' Rs')
        costofdrinksvar.set(str(priceofdrinks)+' Rs')
        costofsweetsvar.set(str(priceofsweets)+' Rs')

        subtotal=priceoffood+priceofdrinks+priceofsweets
        subtotalvar.set(str(subtotal) +' Rs')
        servicetaxvar.set('39 Rs')
        total=subtotal+39
        totalcostvar.set(str(total)+' Rs')
    else:
        messagebox.showerror('Error','No Item Is selected')
def burger():
    if var1.get()==1:
        textburger.config(state=NORMAL)#to update its state from disabled
        textburger.delete(0,END)#to delete all the previous entries it contains
        textburger.focus()#to make the cursor blink
    else:
        textburger.config(state=DISABLED)
        e_burger.set('0')

def pizza():
    if var2.get()==1:
        textpizza.config(state=NORMAL)
        textpizza.delete(0,END)
        textpizza.focus()
    else:
        textpizza.config(state=DISABLED)
        e_pizza.set('0')

def fries():
    if var3.get()==1:
        textfries.config(state=NORMAL)
        textfries.delete(0,END)
        textfries.focus()
    else:
        textfries.config(state=DISABLED)
        e_fries.set('0')

def momos():
    if var4.get()==1:
        textmomos.config(state=NORMAL)
        textmomos.delete(0,END)
        textmomos.focus()
    else:
        textmomos.config(state=DISABLED)
        e_momos.set('0')

def noodles():
    if var5.get()==1:
        textnoodles.config(state=NORMAL)
        textnoodles.delete(0,END)
        textnoodles.focus()
    else:
        textnoodles.config(state=DISABLED)
        e_noodles.set('0')

def soup():
    if var6.get()==1:
        textsoup.config(state=NORMAL)
        textsoup.delete(0,END)
        textsoup.focus()
    else:
        textsoup.config(state=DISABLED)
        e_soup.set('0')

def tacos():
    if var7.get()==1:
        texttacos.config(state=NORMAL)
        texttacos.delete(0,END)
        texttacos.focus()
    else:
        texttacos.config(state=DISABLED)
        e_tacos.set('0')

def pasta():
    if var8.get()==1:
        textpasta.config(state=NORMAL)
        textpasta.delete(0,END)
        textpasta.focus()
    else:
        textpasta.config(state=DISABLED)
        e_pasta.set('0')


def coke():
    if var9.get()==1:
        textcoke.config(state=NORMAL)
        textcoke.delete(0,END)
        textcoke.focus()
    else:
        textcoke.config(state=DISABLED)
        e_coke.set('0')

def sprite():
    if var10.get()==1:
        textsprite.config(state=NORMAL)
        textsprite.delete(0,END)
        textsprite.focus()
    else:
        textsprite.config(state=DISABLED)
        e_sprite.set('0')

def orangejuice():
    if var11.get()==1:
        textorangejuice.config(state=NORMAL)
        textorangejuice.delete(0,END)
        textorangejuice.focus()
    else:
        textorangejuice.config(state=DISABLED)
        e_orangejuice.set('0')

def mojito():
    if var12.get()==1:
        textmojito.config(state=NORMAL)
        textmojito.delete(0,END)
        textmojito.focus()
    else:
        textmojito.config(state=DISABLED)
        e_mojito.set('0')

def faluda():
    if var13.get()==1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0,END)
        textfaluda.focus()
    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')


def oreoshake():
    if var14.get()==1:
        textoreoshake.config(state=NORMAL)
        textoreoshake.delete(0,END)
        textoreoshake.focus()
    else:
        textoreoshake.config(state=DISABLED)
        e_oreoshake.set('0')


def jaljeera():
    if var15.get()==1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.delete(0,END)
        textjaljeera.focus()
    else:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')

def coffee():
    if var16.get()==1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0,END)
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')

def gulabjamun():
    if var17.get()==1:
        textgulabjamun.config(state=NORMAL)
        textgulabjamun.delete(0,END)
        textgulabjamun.focus()
    else:
        textgulabjamun.config(state=DISABLED)
        e_gulabjamun.set('0')

def icecream():
    if var18.get()==1:
        texticecream.config(state=NORMAL)
        texticecream.delete(0,END)
        texticecream.focus()
    else:
        texticecream.config(state=DISABLED)
        e_icecream.set('0')

def jalebi():
    if var19.get()==1:
        textjalebi.config(state=NORMAL)
        textjalebi.delete(0,END)
        textjalebi.focus()
    else:
        textjalebi.config(state=DISABLED)
        e_jalebi.set('0')

def donut():
    if var20.get()==1:
        textdonut.config(state=NORMAL)
        textdonut.delete(0,END)
        textdonut.focus()
    else:
        textdonut.config(state=DISABLED)
        e_donut.set('0')

def brownie():
    if var21.get()==1:
        textbrownie.config(state=NORMAL)
        textbrownie.delete(0,END)
        textbrownie.focus()
    else:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')

def waffle():
    if var22.get()==1:
        textwaffle.config(state=NORMAL)
        textwaffle.delete(0,END)
        textwaffle.focus()
    else:
        textwaffle.config(state=DISABLED)
        e_waffle.set('0')

def pastry():
    if var23.get()==1:
        textpastry.config(state=NORMAL)
        textpastry.delete(0,END)
        textpastry.focus()
    else:
        textpastry.config(state=DISABLED)
        e_pastry.set('0')

def rabri():
    if var24.get()==1:
        textrabri.config(state=NORMAL)
        textrabri.delete(0,END)
        textrabri.focus()
    else:
        textrabri.config(state=DISABLED)
        e_rabri.set('0')
        


root=Tk()#the object on which we will be doing the work
root.state=('zoomed')
root.title("Restaurant Management System")
root.configure(background='Slate Gray4')
root.resizable(0,0)


Tops=Frame(root,bg='black',bd=5,pady=5,relief=RIDGE)#bd stands for border,relief is for styling
Tops.pack(side=TOP)#so that we can see this frame on the TOP side

lbltitle=Label(Tops,font=('chiller',60,'bold'),text='YUMMY IN THE TUMMY!!',bd=21,bg='ghost white',
               fg='Slate Gray4',justify=CENTER)
lbltitle.grid(row=0,column=0)

rightframe=Frame(root,bg='light grey', bd=3, relief=RIDGE)
rightframe.pack(side=RIGHT)#to align the side

calculatorframe=Frame(rightframe,bg='light grey', bd=3, relief=RIDGE)
calculatorframe.pack(side=TOP)

Receiptframe=Frame(rightframe,bd=10,relief=RIDGE)
Receiptframe.pack()

Buttonframe=Frame(rightframe,bg='light grey', bd=3, relief=RIDGE)
Buttonframe.pack(side=BOTTOM)
                                  
Menuframe=Frame(root,bg='light grey',bd=10,relief=RIDGE)
Menuframe.pack(side=LEFT)
                 
Costframe=Frame(Menuframe,bg='light grey',bd=10,relief=RIDGE)
Costframe.pack(side=BOTTOM)
                 
Foodframe1=LabelFrame(Menuframe,text='FOOD',font=('Chiller',25,'bold'),bg='light grey',bd=10)
Foodframe1.pack(side=LEFT)

Foodframe2=LabelFrame(Menuframe,text='DRINKS',font=('Chiller',25,'bold'),bg='light grey',bd=10)
Foodframe2.pack(side=LEFT)

Foodframe3=LabelFrame(Menuframe,text='SWEETS',font=('Chiller',25,'bold'),bg='light grey',bd=10)
Foodframe3.pack(side=LEFT)


#VARIABLES
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()

e_burger=StringVar()
e_pizza=StringVar()
e_fries=StringVar()
e_momos=StringVar()
e_noodles=StringVar()
e_soup=StringVar()
e_tacos=StringVar()
e_pasta=StringVar()

e_coke=StringVar()
e_sprite=StringVar()
e_orangejuice=StringVar()
e_mojito=StringVar()
e_faluda=StringVar()
e_oreoshake=StringVar()
e_jaljeera=StringVar()
e_coffee=StringVar()

e_gulabjamun=StringVar()
e_icecream=StringVar()
e_jalebi=StringVar()
e_donut=StringVar()
e_brownie=StringVar()
e_waffle=StringVar()
e_pastry=StringVar()
e_rabri=StringVar()

#setting the initial value of the entry field as zero:
e_burger.set('0')
e_pizza.set('0')
e_fries.set('0')
e_momos.set('0')
e_noodles.set('0')
e_soup.set('0')
e_tacos.set('0')
e_pasta.set('0')

e_coke.set('0')
e_sprite.set('0')
e_orangejuice.set('0')
e_mojito.set('0')
e_faluda.set('0')
e_oreoshake.set('0')
e_jaljeera.set('0')
e_coffee.set('0')

e_gulabjamun.set('0')
e_icecream.set('0')
e_jalebi.set('0')
e_donut.set('0')
e_brownie.set('0')
e_waffle.set('0')
e_pastry.set('0')
e_rabri.set('0')


costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofsweetsvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()



#FOOD 1
burger=Checkbutton(Foodframe1,text='BURGER\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var1,bg='light grey',command=burger).grid(row=0,sticky=W)
#sticky is used over here to provide alignment
pizza=Checkbutton(Foodframe1,text='PIZZA\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var2,bg='light grey',command=pizza).grid(row=1,sticky=W)

fries=Checkbutton(Foodframe1,text='FRIES\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var3,bg='light grey',command=fries).grid(row=2,sticky=W)

momos=Checkbutton(Foodframe1,text='MOMOS\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var4,bg='light grey',command=momos).grid(row=3,sticky=W)

noodles=Checkbutton(Foodframe1,text='NOODLES\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var5,bg='light grey',command=noodles).grid(row=4,sticky=W)

soup=Checkbutton(Foodframe1,text='SOUP\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var6,bg='light grey',command=soup).grid(row=5,sticky=W)

tacos=Checkbutton(Foodframe1,text='TACOS\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var7,bg='light grey',command=tacos).grid(row=6,sticky=W)

pasta=Checkbutton(Foodframe1,text='PASTA\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var8,bg='light grey',command=pasta).grid(row=7,sticky=W)
#taking entries

textburger=Entry(Foodframe1,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_burger)
textburger.grid(row=0,column=1)

textpizza=Entry(Foodframe1,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_pizza)
textpizza.grid(row=1,column=1)

textfries=Entry(Foodframe1,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_fries)
textfries.grid(row=2,column=1)

textmomos=Entry(Foodframe1,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_momos)
textmomos.grid(row=3,column=1)

textnoodles=Entry(Foodframe1,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_noodles)
textnoodles.grid(row=4,column=1)

textsoup=Entry(Foodframe1,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_soup)
textsoup.grid(row=5,column=1)

texttacos=Entry(Foodframe1,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_tacos)
texttacos.grid(row=6,column=1)

textpasta=Entry(Foodframe1,font=('arial',18,'bold'),width=5,  state=DISABLED, textvariable=e_pasta)
textpasta.grid(row=7,column=1)


#FOOD 2
coke=Checkbutton(Foodframe2,text='COKE\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var9,bg='light grey',command=coke).grid(row=0,sticky=W)

sprite=Checkbutton(Foodframe2,text='SPRITE\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var10,bg='light grey',command=sprite).grid(row=1,sticky=W)

orangejuice=Checkbutton(Foodframe2,text='ORANGE JUICE\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var11,bg='light grey',command=orangejuice).grid(row=2,sticky=W)

mojito=Checkbutton(Foodframe2,text='MOJITO\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var12,bg='light grey',command=mojito).grid(row=3,sticky=W)

faluda=Checkbutton(Foodframe2,text='FALUDA\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var13,bg='light grey',command=faluda).grid(row=4,sticky=W)

oreoshake=Checkbutton(Foodframe2,text='ORESHAKE\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var14,bg='light grey',command=oreoshake).grid(row=5,sticky=W)

jaljeera=Checkbutton(Foodframe2,text='JALJEERA\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var15,bg='light grey',command=jaljeera).grid(row=6,sticky=W)

coffee=Checkbutton(Foodframe2,text='COFFEE\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var16,bg='light grey',command=coffee).grid(row=7,sticky=W)

#entries for drinks
textcoke=Entry(Foodframe2,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_coke)
textcoke.grid(row=0,column=1)

textsprite=Entry(Foodframe2,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_sprite)
textsprite.grid(row=1,column=1)

textorangejuice=Entry(Foodframe2,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_orangejuice)
textorangejuice.grid(row=2,column=1)

textmojito=Entry(Foodframe2,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_mojito)
textmojito.grid(row=3,column=1)

textfaluda=Entry(Foodframe2,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_faluda)
textfaluda.grid(row=4,column=1)

textoreoshake=Entry(Foodframe2,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_oreoshake)
textoreoshake.grid(row=5,column=1)

textjaljeera=Entry(Foodframe2,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_jaljeera)
textjaljeera.grid(row=6,column=1)

textcoffee=Entry(Foodframe2,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=7,column=1)

#SWEETS

gulabjamun=Checkbutton(Foodframe3,text='GULAB JAMUN\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var17,bg='light grey',command=gulabjamun).grid(row=0,sticky=W)

icecream=Checkbutton(Foodframe3,text='ICE CREAM\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var18,bg='light grey',command=icecream).grid(row=1,sticky=W)

jalebi=Checkbutton(Foodframe3,text='JALEBI\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var19,bg='light grey',command=jalebi).grid(row=2,sticky=W)

donut=Checkbutton(Foodframe3,text='DONUT\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var20,bg='light grey',command=donut).grid(row=3,sticky=W)

brownie=Checkbutton(Foodframe3,text='BROWNIE\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var21,bg='light grey',command=brownie).grid(row=4,sticky=W)

waffle=Checkbutton(Foodframe3,text='WAFFLE\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var22,bg='light grey',command=waffle).grid(row=5,sticky=W)

pastry=Checkbutton(Foodframe3,text='PASTRY\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var23,bg='light grey',command=pastry).grid(row=6,sticky=W)

rabri=Checkbutton(Foodframe3,text='RABRI\t',font=('arial',18,'bold'),onvalue=1,offvalue=0,
                   variable=var24,bg='light grey',command=rabri).grid(row=7,sticky=W)

#entries for sweets
textgulabjamun=Entry(Foodframe3,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_gulabjamun)
textgulabjamun.grid(row=0,column=1)

texticecream=Entry(Foodframe3,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_icecream)
texticecream.grid(row=1,column=1)

textjalebi=Entry(Foodframe3,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_jalebi)
textjalebi.grid(row=2,column=1)

textdonut=Entry(Foodframe3,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_donut)
textdonut.grid(row=3,column=1)

textbrownie=Entry(Foodframe3,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_brownie)
textbrownie.grid(row=4,column=1)

textwaffle=Entry(Foodframe3,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_waffle)
textwaffle.grid(row=5,column=1)

textpastry=Entry(Foodframe3,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_pastry)
textpastry.grid(row=6,column=1)

textrabri=Entry(Foodframe3,font=('arial',18,'bold'),width=5,state=DISABLED, textvariable=e_rabri)
textrabri.grid(row=7,column=1)


#making the cost frame and taking entries in it
costoffood=Label(Costframe,text='Cost of food',font=('arial',18,'bold'),bg='light grey')
costoffood.grid(row=0,column=0)

textoffood=Entry(Costframe,font=('arial',18,'bold'),width=22,textvariable=costoffoodvar)
textoffood.grid(row=0,column=1,padx=26)#padx is used to provide correct spacing

costofdrinks=Label(Costframe,text='Cost of drinks',font=('arial',18,'bold'),bg='light grey')
costofdrinks.grid(row=1,column=0)

textofdrinks=Entry(Costframe,font=('arial',18,'bold'),width=22,textvariable=costofdrinksvar)
textofdrinks.grid(row=1,column=1,padx=26)

costofsweets=Label(Costframe,text='Cost of sweets',font=('arial',18,'bold'),bg='light grey')
costofsweets.grid(row=2,column=0)

textofsweets=Entry(Costframe,font=('arial',18,'bold'),width=22,textvariable=costofsweetsvar)
textofsweets.grid(row=2,column=1,padx=26)

subtotal=Label(Costframe,text='Subtotal',font=('arial',18,'bold'),bg='light grey')
subtotal.grid(row=0,column=2)

textofsubtotal=Entry(Costframe,font=('arial',18,'bold'),width=22,textvariable=subtotalvar)
textofsubtotal.grid(row=0,column=3,padx=26)

servicetax=Label(Costframe,text='Service tax',font=('arial',18,'bold'),bg='light grey')
servicetax.grid(row=1,column=2)

textofservicetax=Entry(Costframe,font=('arial',18,'bold'),width=22,textvariable=servicetaxvar)
textofservicetax.grid(row=1,column=3,padx=26)

total=Label(Costframe,text='Total',font=('arial',18,'bold'),bg='light grey')
total.grid(row=2,column=2)

textoftotal=Entry(Costframe,font=('arial',18,'bold'),width=22,textvariable=totalcostvar)
textoftotal.grid(row=2,column=3,padx=26)

buttontotal=Button(Buttonframe,text='Total',font=('arial',18,'bold'),bg='light grey',command=Totalcost)
buttontotal.grid(row=0,column=0)

buttonreceipt=Button(Buttonframe,text='Receipt',font=('arial',18,'bold'),bg='light grey',command=receipt)
buttonreceipt.grid(row=0,column=1)

buttonsave=Button(Buttonframe,text='Save',font=('arial',18,'bold'),bg='light grey',command=save)
buttonsave.grid(row=0,column=2)

buttonmenu=Button(Buttonframe,text='Menu',font=('arial',18,'bold'),bg='light grey',command=menu)
buttonmenu.grid(row=0,column=3)

buttonreset=Button(Buttonframe,text='Reset',font=('arial',18,'bold'),bg='light grey',command=reset)
buttonreset.grid(row=0,column=4)

#text receipt
textreceipt=Text(Receiptframe,font=('arial',12,'bold'),bd=3,width=46,height=12)
textreceipt.grid(row=0,column=0)

#calculator
operator=' '
def buttonclick(numbers):
        global operator
        operator=operator+numbers
        calculatorfield.delete(0,END)
        calculatorfield.insert(END,operator)

def clear():
        global operator
        operator=' '
        calculatorfield.delete(0,END)

def answer():
        global operator
        result=str(eval(operator))#eval operates
        calculatorfield.delete(0,END)
        calculatorfield.insert(0,result)
        operator=''

calculatorfield=Entry(calculatorframe,font=('arial',16,'bold'),width=35,bd=6)
calculatorfield.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorframe,text='7',font=('arial',12,'bold'),fg='yellow',bg='Slate Gray4',bd=6,width=9,command=lambda:buttonclick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorframe,text='8',font=('arial',12,'bold'),fg='yellow',bg='Slate Gray4',bd=6,width=9,command=lambda:buttonclick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorframe,text='9',font=('arial',12,'bold'),fg='yellow',bg='Slate Gray4',bd=6,width=9,command=lambda:buttonclick('9'))
button9.grid(row=1,column=2)

buttonplus=Button(calculatorframe,text='+',font=('arial',12,'bold'),fg='yellow',bg='Slate Gray4',bd=6,width=9,command=lambda:buttonclick('+'))
buttonplus.grid(row=1,column=3)

button4=Button(calculatorframe,text='4',font=('arial',12,'bold'),fg='yellow',bg='Slate Gray4',bd=6,width=9,command=lambda:buttonclick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorframe,text='5',font=('arial',12,'bold'),fg='red4',bg='white',bd=6,width=9,command=lambda:buttonclick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorframe,text='6',font=('arial',12,'bold'),fg='red4',bg='white',bd=6,width=9,command=lambda:buttonclick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorframe,text='-',font=('arial',12,'bold'),fg='yellow',bg='Slate Gray4',bd=6,width=9,command=lambda:buttonclick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorframe,text='1',font=('arial',12,'bold'),fg='yellow',bg='Slate Gray4',bd=6,width=9,command=lambda:buttonclick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorframe,text='2',font=('arial',12,'bold'),fg='red4',bg='white',bd=6,width=9,command=lambda:buttonclick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorframe,text='3',font=('arial',12,'bold'),fg='red4',bg='white',bd=6,width=9,command=lambda:buttonclick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorframe,text='*',font=('arial',12,'bold'),fg='yellow',bg='Slate Gray4',bd=6,width=9,command=lambda:buttonclick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorframe,text='Ans',font=('arial',12,'bold'),fg='yellow',bg='Slate Gray4',bd=6,width=9,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorframe,text='Clear',font=('arial',12,'bold'),fg='yellow',bg='Slate Gray4',bd=6,width=9,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorframe,text='0',font=('arial',12,'bold'),fg='yellow',bg='Slate Gray4',bd=6,width=9,command=lambda:buttonclick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorframe,text='/',font=('arial',12,'bold'),fg='yellow',bg='Slate Gray4',bd=6,width=9,command=lambda:buttonclick('/'))
buttonDiv.grid(row=4,column=3)
root.mainloop()
