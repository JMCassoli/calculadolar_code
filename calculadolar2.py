from cProfile import label
from tkinter import *
from bs4 import BeautifulSoup
import requests

url ='https://dolarhoy.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


#dolar compra
dc = soup.find_all('div', class_='val')

dolar = 0
dolar_compra = 0
dolar_venta = 0
valores = list()
count=0
for i in dc:
    if count <= 1:
        valores.append(i.text)
    else: break
    count+=1

count = 0
for i in valores:
    if count==0:
        print('dolar compra = '+ i)
        dolar_compra=int(i.replace("$",""))
        count+=1
    else:
        print('dolar venta = '+ i)
        dolar_venta=int(i.replace("$",""))
        dolar = int(i.replace("$",""))
        


    



# CALCULADOLAR

root = Tk()

root.title("Calculadolar")
root.geometry("330x460")
root.resizable(True, True)

calculate_done = False


# Display
display = Entry(root , font=("Minion Pro Med", 36) , justify=RIGHT , bd=4 , width=10 )
display.grid(row= 0 , column= 0, columnspan=4 , sticky= N+S+E+W)

index = 0

# Info
Label(root, font=("Minion Pro bld", 13) , text=("DOLAR BLUE :") , justify=LEFT ).grid(row=6 , rowspan=1 , column= 0 , columnspan= 3)
cambio = Label(root, font=("Minion Pro bld", 11) , text=("CAMBIO : ") , justify=LEFT ).grid(row=6 , rowspan=1 , column= 3 , columnspan= 3)
dolarCompra = Label(root , font=("Minion Pro Med", 12) , text=("COMPRA = $" + str(dolar_compra)) , justify= LEFT)
dolarCompra.grid(row=7 , rowspan=1, column= 0 , columnspan=3)
dolarVenta = Label(root , font=("Minion Pro Med", 12) , text=("VENTA = $" + str(dolar_venta)) , justify=LEFT)
dolarVenta.grid(row=8 , rowspan=1, column= 0 , columnspan=3)
dolarPromedio = Label(root , font=("Minion Pro Med", 12) , text=("PROMEDIO = $" + (str((dolar_compra +  dolar_venta)/2 ) ) ) )
dolarPromedio.grid(row=9 , rowspan=1, column= 0 , columnspan=3)

# Functions
def get_numbers(n):
    global index
    global calculate_done
    if calculate_done:
        clear_display()
        calculate_done = False
    display.insert(index, n)
    index += 1
    

def get_operations(n):
    global index

def clear_display():
    display.delete(0, END)

def print(text):
    clear_display()
    display.insert(0, text)    

def calculate(t):
    global calculate_done
    display_state = display.get()
    input = int(display_state)
    if (t==0):
        result = input * dolar
        print(result)
        calculate_done = True
    else:
        result = input / dolar
        print(result)
        calculate_done = True

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        print(display_new_state)

def change_type(type):
    global dolar
    global tipo_cambio
    global cambio

    if(type == 0):
        dolar=dolar_compra
        tipo_cambio= "compra"
        change_color(type)
    elif(type == 1):
        dolar=dolar_venta
        tipo_cambio= "venta"
        change_color(type)
    elif(type == 2):
        dolar= (dolar_compra + dolar_venta)/2
        tipo_cambio= "promed"
        change_color(type)



def change_color(color):
    global btn_c
    global btn_v
    global btn_p
    
    if color==0:
        btn_c = Button(root, text = "COMPRA" , command=lambda:change_type(0), font=("Minion Pro Med", 12) , bg="green" , fg='White').grid(row = 7 , column=3 , sticky=N+S+E+W)
        btn_v = Button(root, text = "VENTA" , command=lambda:change_type(1), font=("Minion Pro Med", 12)).grid(row = 8 , column=3 , sticky=N+S+E+W)
        btn_p = Button(root, text = "PROMEDIO" , command=lambda:change_type(2), font=("Minion Pro Med", 12)).grid(row = 9 , column=3 , sticky=N+S+E+W)
    elif color == 1:
        btn_c = Button(root, text = "COMPRA" , command=lambda:change_type(0), font=("Minion Pro Med", 12)).grid(row = 7 , column=3 , sticky=N+S+E+W)
        btn_v = Button(root, text = "VENTA" , command=lambda:change_type(1), font=("Minion Pro Med", 12) , bg="green" , fg='White').grid(row = 8 , column=3 , sticky=N+S+E+W)
        btn_p = Button(root, text = "PROMEDIO" , command=lambda:change_type(2), font=("Minion Pro Med", 12)).grid(row = 9 , column=3 , sticky=N+S+E+W)
    elif color == 2:
        btn_c = Button(root, text = "COMPRA" , command=lambda:change_type(0), font=("Minion Pro Med", 12)).grid(row = 7 , column=3 , sticky=N+S+E+W)
        btn_v = Button(root, text = "VENTA" , command=lambda:change_type(1), font=("Minion Pro Med", 12)).grid(row = 8 , column=3 , sticky=N+S+E+W)
        btn_p = Button(root, text = "PROMEDIO" , command=lambda:change_type(2), font=("Minion Pro Med", 12) , bg="green" , fg='White').grid(row = 9 , column=3 , sticky=N+S+E+W)
        


# Numeric Buttons
Button(root, text = "1" , command=lambda:get_numbers(1) , font=("Minion Pro Med",24)).grid(row = 2 , column=0 , sticky=N+S+E+W , ipadx=10)
Button(root, text = "2" , command=lambda:get_numbers(2), font=("Minion Pro Med", 24)).grid(row = 2 , column=1 , sticky=N+S+E+W , ipadx=10)
Button(root, text = "3" , command=lambda:get_numbers(3), font=("Minion Pro Med", 24)).grid(row = 2 , column=2 , sticky=N+S+E+W , ipadx=10)
Button(root, text = "4" , command=lambda:get_numbers(4), font=("Minion Pro Med", 24)).grid(row = 3 , column=0 , sticky=N+S+E+W , ipadx=10)
Button(root, text = "5" , command=lambda:get_numbers(5), font=("Minion Pro Med", 24)).grid(row = 3 , column=1 , sticky=N+S+E+W , ipadx=10)
Button(root, text = "6" , command=lambda:get_numbers(6), font=("Minion Pro Med", 24)).grid(row = 3 , column=2 , sticky=N+S+E+W , ipadx=10)
Button(root, text = "7" , command=lambda:get_numbers(7), font=("Minion Pro Med", 24)).grid(row = 4 , column=0 , sticky=N+S+E+W , ipadx=10)
Button(root, text = "8" , command=lambda:get_numbers(8), font=("Minion Pro Med", 24)).grid(row = 4 , column=1 , sticky=N+S+E+W , ipadx=10)
Button(root, text = "9" , command=lambda:get_numbers(9), font=("Minion Pro Med", 24)).grid(row = 4 , column=2 , sticky=N+S+E+W , ipadx=10)
Button(root, text = "0" , command=lambda:get_numbers(0), font=("Minion Pro Med", 16)).grid(row = 5 , column=0 , sticky=N+S+E+W, columnspan="3" , ipadx=5 , ipady=10)

# Operation buttons
Button(root, text = "⮪", font=("Minion Pro Med", 24) , command = undo).grid(row = 2 , column=3 , sticky=N+S+E+W)
Button(root, text = "PES 🡆 DOL" , command=lambda:calculate(1), font=("Minion Pro Med", 14) , bg="#588152").grid(row = 3 , column=3 , sticky=N+S+E+W)
Button(root, text = "DOL 🡆 PES" , command=lambda:calculate(0), font=("Minion Pro Med", 14) , bg="#487ba3").grid(row = 4 , column=3 , sticky=N+S+E+W)
Button(root, text = "AC" , command=lambda: clear_display(), font=("Minion Pro Med", 16)).grid(row = 5 , column=3 , sticky=N+S+E+W)
btn_c = Button(root, text = "COMPRA" , command=lambda:change_type(0), font=("Minion Pro Med", 12)).grid(row = 7 , column=3 , sticky=N+S+E+W)
btn_v = Button(root, text = "VENTA" , command=lambda:change_type(1), font=("Minion Pro Med", 12) , bg="green" , fg='White').grid(row = 8 , column=3 , sticky=N+S+E+W)
btn_p = Button(root, text = "PROMEDIO" , command=lambda:change_type(2), font=("Minion Pro Med", 12)).grid(row = 9 , column=3 , sticky=N+S+E+W)

root.mainloop()