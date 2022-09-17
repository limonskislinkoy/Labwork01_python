from tkinter import *

window = Tk()
window.geometry('500x550')
window.resizable(False, False)
window.config(bg = '#fff')
window.title('Calculator')


def calculate(operation):
    global fm

    try:
        if (((fm[-1]).isdigit())==False and
                (operation=='x^y' or operation=='x^2' or
                 operation=='-' or operation=='+' or operation=='*'
                 or operation=='/' or operation=='.' or operation=='√x'
                 or fm[-1] == operation)):
            fm = fm[:((len(fm))-1)]
    except: pass

    if operation == 'C': fm = ''
    elif operation == 'del': fm = fm[0: -1]
    elif operation == 'x^2':
        if fm != '':
            fm = str((eval(fm)) ** 2)
    elif operation == 'x^y': 
        if fm != '':
            fm = str(fm+'^')
    elif operation == '1/x':
        if ('+' in fm or '-' in fm or '*' in fm or '/' in fm or '^' in fm or fm[-1]=='.') and fm != '':
            operation = ''
        elif fm != '0' and fm != '':
            fm = str(1 / (eval(fm)))
        if fm == '0':
            fm = 'Ошибка. Деление на ноль'
    elif operation == '.':
        if '.' not in fm:
            fm = fm + '.'
    elif operation == '+/-':
        try:
            if fm[0]!='-':
                fm = '-'+fm
            else: fm = fm[1:]
        except: pass
    elif operation == '√x':
        if fm[0] == '-' and fm != '':
            fm = 'Ошибка. Корень из отрицательного'
        elif fm != '': fm = str(eval(fm)**0.5)
    elif operation == '=':
        if '/0' in fm and not '/0.' in fm:
            operation = ''
            fm = 'Ошибка. Деление на ноль'
        elif fm[-1]=='+' or fm[-1]=='-' or fm[-1]=='/' or fm[-1]=='*' or fm[-1]=='^':
            operation = ''
        else:
            fm = fm.replace('^', '**')
            fm = str(eval(fm))
    else:
        if fm == '0':
            fm = ''

        fm += operation
    label_text.config(text = str(fm))

fm = '0'
label_text = Label(text=fm, font=('Times New Roman', 20, 'bold'),
                   bg='white', fg='black')
label_text.place(x=18, y=50)

bts = ['del', 'C', 'x^y', '√x',
       'x^2', '1/x', '+', '-',
       '1', '2', '3', '*',
       '4', '5', '6', '/',
       '7', '8', '9', '=',
       '+/-', '0', '.']

x = 18
y = 120
for bt in bts:
    get_label = lambda x=bt: calculate(x)
    if bt == '=':
        Button(text=bt, bg='gray', font=('Times New Roman', 20),
               command=get_label).place(x=x, y=y, width=115, height=139)
    else:
        Button(text=bt, bg='gray', font=('Times New Roman', 20),
               command=get_label).place(x=x, y=y, width=115, height=69)
    x += 117
    if x > 400:
        x = 18
        y += 70


window.mainloop()
