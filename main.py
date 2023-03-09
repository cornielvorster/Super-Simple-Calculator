#main screen, containing buttons, form and display
from tkinter import *

expression = ""

#displaying
def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)


def equalpress():
    try:
        global expression

        total = str(eval(expression))

        equation.set(total)

        expression = ""

    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    window = Tk()
    
    window.title('Calculator')
    
    window.configure(bg=("Blue"))

    window.geometry("350x125")

    equation = StringVar()
   
    
    
    txtfld=Entry(window, textvariable=equation)
    #entry

    txtfld.grid(columnspan=4, ipadx=70)

        

    #button 0
    btn1=Button(window, text="0", fg='grey', height=1, width= 7,
                command=lambda: press(0))
    btn1.grid(row=5, column=2)

    ############################
    #button 1
    btn1=Button(window, text="1", fg='grey', height=1, width= 7,
                command=lambda: press(1))
    btn1.grid(row=4, column=1)

    #button 2
    btn2=Button(window, text="2", fg='grey', height=1, width= 7,
                command=lambda: press(2))
    btn2.grid(row=4, column=2)

    #button 3
    btn3=Button(window, text="3", fg='grey', height=1, width= 7,
                command=lambda: press(3))
    btn3.grid(row=4, column=3)
    ################
    #button 4
    btn4=Button(window, text="4", fg='grey', height=1, width= 7,
                command=lambda: press(4))
    btn4.grid(row=3, column=1)

    #button 5
    btn5=Button(window, text="5", fg='grey', height=1, width= 7,
                command=lambda: press(5))
    btn5.grid(row=3, column=2)

    #button 6
    btn6=Button(window, text="6", fg='grey', height=1, width= 7,
                command=lambda: press(6))
    btn6.grid(row=3, column=3)
    ##################
    #button 7
    btn7=Button(window, text="7", fg='grey', height=1, width= 7,
                command=lambda: press(7))
    btn7.grid(row=2, column=1)

    #button 8
    btn8=Button(window, text="8", fg='grey', height=1, width= 7,
                command=lambda: press(8))
    btn8.grid(row=2, column=2)

    #button 9
    btn9=Button(window, text="9", fg='grey', height=1, width= 7,
                command=lambda: press(9))
    btn9.grid(row=2, column=3)
    #################
    

    #button +
    btnPlus = Button(window, text="+ ", fg='grey', height=1, width=7,
                     command=lambda: press('+'))
    btnPlus.grid(row=2, column=4)

    #button /
    btnDivide=Button(window, text="/", fg='grey', height=1, width=7,
                     command=lambda: press('/'))
    btnDivide.grid(row=3, column=4)

    #button -
    btn9=Button(window, text="-", fg='grey', height=1, width=7,
                     command=lambda: press('-'))
    btn9.grid(row=4, column=4)

    #button *
    btn9=Button(window, text="x", fg='grey', height=1, width=7,
                     command=lambda: press("*"))
    btn9.grid(row=5, column=4)


    clear = Button(window, text='Clear', fg='black', bg='red',
                command=clear, height=1, width=7)
    clear.grid(row=5, column=1)
    
    #button =
    btnEqual = Button(window, text="=", fg='grey',
                command= equalpress, height=1, width= 7)
    btnEqual.grid(row=5, column=3)

    Decimal= Button(window, text='.', fg='black',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=5, column=2)
    
    window.mainloop()
    



    





