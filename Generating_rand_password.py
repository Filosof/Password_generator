from tkinter import *
from random import *
class window:
    #--------------------
    def __init__(self,master):
        self.root = master
        self.root.geometry('300x205+200+200')
        self.root.title('Генератор паролів')
        self.root.minsize(300,205)
        self.root.maxsize(300,205)
        #--------------------Текстове поле
        self.my_text1 = Text(self.root,width=30,height=2,font = 'arail 22')
        self.my_text1['selectforeground'] = 'red'
        self.my_text2 = Text(self.root,width=10,height=1,font = 'arail 16')
        self.my_text2.insert('0.0',4)
        #--------------------Button`s
        self.my_button1 = Button(self.root,text = 'Генерувати!',width ='40',height = '2')
        self.my_button2 = Button(self.root,text = 'В буфер!')
        #--------------------checkbuttons
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        check1 = Checkbutton(self.root,text="Цифри",variable=var1,onvalue="1",offvalue="0")
        check2 = Checkbutton(self.root,text="Літери(нижній регістр)",variable=var2,onvalue="1",offvalue="0")
        check3 = Checkbutton(self.root,text="Літери(верхній регістр)",variable=var3,onvalue="1",offvalue="0")
        check4 = Checkbutton(self.root,text="Спец.символи",variable=var4,onvalue="1",offvalue="0")
        #----------Функція для обробки події(обов"язково після буттонів і чек боксів і в конструкторі)
        def but_click(event):
            len_password=IntVar()
            len_password=self.my_text2.get(1.0,END)
            len_password = int(len_password)
            '''
            Методом get(), в качестве аргументов указываются номера строки и символа,
            с которых надо брать, и номера строки и символа, до которых надо брать текст.
            Если до конца, то пишется ключевое слово END.
            Приклад: x = text_field.get(1.0, END)
            '''
            self.my_text1.delete('0.0',END)
            ch_1 = var1.get()
            ch_2 = var2.get()
            ch_3 = var3.get()
            ch_4 = var4.get()
            str = ''
            numbers = '1234567890'
            lines = 'qwertyuiopasdfghjklzxcvbnm'
            upper_lines = lines.upper()
            special_char = '`+-*/!@#$%^&*()[]|\.,'
            if ch_1==1:
                str+=numbers
            if ch_2==1:
                str+=lines
            if ch_3==1:
                str+=upper_lines
            if ch_4==1:
                str+=special_char
            #----Сам алгоритм!!! МОЖЛИВО НЕЕФЕКТИВНИЙ!
            rezult_list = sample(str,len_password)
            rezult_str =''
            for i in rezult_list:
                rezult_str+=i
            self.my_text1.insert('0.0',rezult_str)
            #print('Ось ваш пароль: '+ rezult_str)
            #-----------Бінд першої клавіші
        self.my_button1.bind('<Button-1>',but_click)
        
        #--------------------Запаковка і отрісовка
        self.my_text1.place(x='0',y='0')
        self.my_text2.place(x='170',y='75')
        self.my_button1.place(x='5',y='160')
        self.my_button2.place(x='170',y='100')
        check1.place(x='1',y='70')
        check2.place(x='1',y='90')
        check3.place(x='1',y='110')
        check4.place(x='1',y='130')
        self.root.mainloop()
        #---------Тут закінчився конструктор
    
    
        #---Функції для Button`s
    
        
        
        
        
#---------------------------------------

root = Tk()
window(root)
