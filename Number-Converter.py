from tkinter import *
top=Tk()
top.geometry("165x150")
top.title("Number Converter")
top.config(background="gray")

def reset():
    def conv():
        try:
            d=0
            d=int(en1.get())
            a="inp ↓"
            a=var.get()
            b="out ↓"
            b=var1.get()    
        
            if(a=="inp ↓"):
                var2.set("Enter input type")
            elif(b=="out ↓"):
                var2.set("Enter output type")
            
            if(a=='Decimal'):
                if(b=='Decimal'):
                    var2.set(d)
                elif(b=='Binary'):
                    var2.set(bin(d))
                elif(b=='Octal'):
                    var2.set(oct(d))
                elif(b=='Hexadecimal'):
                    var2.set(hex(d))
            elif(a=='Binary'):
                if(b=='Binary'):
                    var2.set(d)
                elif(b=='Decimal'):
                    var2.set(int(d,2))
                elif(b=='Octal'):
                    var2.set(oct(d))
                elif(b=='Hexadecimal'):
                    var2.set(hex(d))
            elif(a=='Octal'):
                if(b=='Octal'):
                    var2.set(d)
                elif(b=='Decimal'):
                    var2.set(int(d,8))
                elif(b=='Binary'):
                    var2.set(bin(d))
                elif(b=='Hexadecimal'):
                    var2.set(hex(d))
            elif(a=='Hexadecimal'):
                if(b=='Hexadecimal'):
                    var2.set(d)
                elif(b=='Decimal'):
                    var2.set(int(d,16))
                elif(b=='Binary'):
                    var2.set(bin(d))
                elif(b=='Octal'):
                    var2.set(oct(d))
        except:
            if(d==0):
                var2.set("Enter Value First")
            else:
                var2.set("Something Went Wrong")
            

    var2=StringVar()

    lb1=Label(text="Enter Value =").place(x=10,y=10)
    en1=Entry(width='6',justify='center')
    en1.place(x=100,y=10)

    btn=Button(text="R",command=reset).place(x=150,y=0)

    var=StringVar(top)
    var.set("inp ↓")

    option=OptionMenu(top, var, "Decimal", "Binary", "Octal", "Hexadecimal")
    option.place(x=10,y=35)

    var1=StringVar(top)
    var1.set("out ↓")

    option=OptionMenu(top, var1, "Decimal", "Binary", "Octal", "Hexadecimal")
    option.place(x=83,y=35)

    btn=Button(text="Convert",command=conv)
    btn.place(x=50,y=72)

    en2=Entry(textvariable=var2,width='25',justify='center').place(x=5,y=99)

reset()
mainloop()
