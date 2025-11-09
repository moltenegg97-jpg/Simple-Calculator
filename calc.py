import tkinter as tk
from tkinter import *
from tkinter import ttk


some_number=''

def enter_number(letter, last_number): #выводит знаки на дисплей
    global some_number

    if len(last_number) == 0:
        print ('выполняю ф1')
        print(f"Текст кнопки: {letter}")
        print(f"Last number before:{last_number}")
        some_number=last_number+letter
        last_number=some_number
        NumberText.set(some_number)
        print(f"some number:{some_number}")
        print(f"Last number after:{last_number}")
    elif last_number[0] == '0':
        print ('выполняю ф2')
        print(f"Текст кнопки: {letter}")
        print(f"Last number before:{last_number}")
        some_number=letter
        last_number=some_number
        NumberText.set(some_number)
        print(f"some number:{some_number}")
        print(f"Last number after:{last_number}")

    elif last_number[0] != '0' and len(last_number) != 0 and len(last_number) <2:
        print ('выполняю ф3')
        print(f"Текст кнопки: {letter}")
        print(f"Last number before:{last_number}")
        some_number=last_number+letter
        last_number=some_number
        NumberText.set(some_number)
        print(f"some number:{some_number}")
        print(f"Last number after:{last_number}")
    elif len(last_number) >= 2:
        print ('больше 2')
        if last_number[-2] == '+' and last_number[-1] == '0':
            print ('выполняю ф4')
            print(f"Последний символ: {last_number[-1]}")
            print(f"Текст кнопки: {letter}")
            print(f"Last number before:{last_number}")
            print(f"last_number -1: {last_number[:-1]}")
            some_number=last_number[:-1]+letter
            last_number=some_number
            NumberText.set(some_number)
            print(f"some number:{some_number}")
            print(f"Last number after:{last_number}")
        elif last_number[0] != '0' and len(last_number) != 0 and (last_number[-2] != '+' or last_number[-2] != '0'):
            print ('выполняю ф3.5')
            print(f"Текст кнопки: {letter}")
            print(f"Last number before:{last_number}")
            some_number=last_number+letter
            last_number=some_number
            NumberText.set(some_number)
            print(f"some number:{some_number}")
            print(f"Last number after:{last_number}")
    return 

def clear_number(): #очищает строку дисплей
    global some_number
    some_number=''
    NumberText.set(some_number)
    print (f"some number {some_number}")
    return

def calculate(letter): #высчитывает мат.формулу на дисплее
    global some_number

    

    # first_char = letter[0] #для того чтобы убрать 0 в начале строки, но не работает
    # special_letter=letter[1]

    # i=0
    # while i<len(letter):
    #     if letter[i] == '0': 
    #         print ('0 is detected')

    #         if first_char == '0' :
    #             for j in range(len(letter)):
    #                 print (f'print letter[i] {letter[i]}')
    #                 if letter[j] == '0': 
    #                     continue
    #                 else: 
    #                     notazero=j 
    #                     print (f'not a zero {notazero}')
    #                     letter=letter[notazero:]
    #                     print (f'letter after deleted zeros {letter}')
    #                     break
    # i+=1    


    some_number=f'{eval(letter)}' #eval -функция расчета строки
    NumberText.set(some_number)
    return


window=tk.Tk() #создает окно window
window.title('main window') #прописывает окну Имя main window
#window.geometry('300x300') #задает размеры окна прописываются как строка высотахширина+смещение по х+смещение по y

mainframe=ttk.Frame(window, padding=(3, 3, 3, 3))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

frame1=ttk.Frame(mainframe) #разделил остновной фрейм на два дочерних чтобы кнопки и дисплей были в разных grid'ах
frame1.grid(column=1, row=1, sticky=NSEW)
frame2=ttk.Frame(mainframe)
frame2.grid(column=1, row=2, sticky=NSEW)

NumberText = StringVar() #переменная которая хранит значение строки и выводиться на экран
NumberText.set("Нажмите кнопку")




display = StringVar()
display = ttk.Entry(frame1, width=30, textvariable=NumberText)
display.grid(column=2, row=1, sticky=(NSEW))


ttk.Label(frame1, textvariable=NumberText).grid(column=1, row=1, sticky=N)


ttk.Button(frame2, text='1',command=lambda: enter_number('1', some_number)).grid(column=1, row=7, sticky=NSEW) #в команде необходимо писать lambda: что это я хз но без неё эта функция не работает
ttk.Button(frame2, text='2',command=lambda: enter_number('2', some_number)).grid(column=2, row=7, sticky=NSEW) #кнопки цифр от 0 до 9
ttk.Button(frame2, text='3',command=lambda: enter_number('3', some_number)).grid(column=3, row=7, sticky=NSEW)

ttk.Button(frame2, text='4',command=lambda: enter_number('4', some_number)).grid(column=1, row=6, sticky=NSEW)
ttk.Button(frame2, text='5',command=lambda: enter_number('5', some_number)).grid(column=2, row=6, sticky=NSEW)
ttk.Button(frame2, text='6',command=lambda: enter_number('6', some_number)).grid(column=3, row=6, sticky=NSEW)

ttk.Button(frame2, text='7',command=lambda: enter_number('7', some_number)).grid(column=1, row=5, sticky=NSEW)
ttk.Button(frame2, text='8',command=lambda: enter_number('8', some_number)).grid(column=2, row=5, sticky=NSEW)
ttk.Button(frame2, text='9',command=lambda: enter_number('9', some_number)).grid(column=3, row=5, sticky=NSEW)

ttk.Button(frame2, text='.',command=lambda: enter_number('.', some_number)).grid(column=1, row=8, sticky=NSEW)

ttk.Button(frame2, text='0', command=lambda: enter_number('0', some_number)).grid(column=2, row=8, sticky=NSEW)
ttk.Button(frame2, text='clear', command=lambda: clear_number()).grid(column=3, row=8, sticky=NSEW)  #кнопка =

ttk.Button(frame2, text='+', command=lambda: enter_number('+', some_number)).grid(column=4,row=8, sticky=NSEW) #кнопки +,-,/,*
ttk.Button(frame2, text='-', command=lambda: enter_number('-', some_number)).grid(column=4,row=7, sticky=NSEW)
ttk.Button(frame2, text='*', command=lambda: enter_number('*', some_number)).grid(column=4,row=6, sticky=NSEW)
ttk.Button(frame2, text='/', command=lambda: enter_number('/', some_number)).grid(column=4,row=5, sticky=NSEW)

ttk.Button(frame2, text='=', command=lambda: calculate(some_number)).grid(column=4,row=9, sticky=NSEW) #кнопка =

window.mainloop()