import re
import PySimpleGUI as sg


layout = [[sg.Text(key='result', font=('Helvetica', 14), size=(15, 1))],
          [sg.Input(key='input')],      
          [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
          [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
          [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-')],
          [sg.Button('0'), sg.Button('.'), sg.Button('='), sg.Button('+')],
          [sg.Button('Clear'), sg.Button('Exit')]
          ]     

window = sg.Window('My Calculator', layout, default_button_element_size=(5,2), auto_size_buttons=False )     

def error(msg):
     window['result'].update(msg)

#Logics
def validate(expression):
    #should not starts and endswith with * or /
    if expression.startswith(('*', '/')) or  expression.endswith(('*', '/')):
        error('Invalid Expression')
        return False
    
    if expression.endswith('/0'):
        error("can't divide with 0")
        return False

    #operator should come only once in the expression
    count = 0
    for x in '+-*/':
        count = count + expression.count(x)
    if count <= 1:
        return True
    else: 
        error('Invalid operation')
        return False


def add(a, b):
    return a + b

def sub(a, b): 
    return a - b

def mult(a,b):
    return a * b

def divide(a,b):
    return a / b


OPERATIONS = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': divide
}

def evaluate(a, op , b):
    if op in '+-*/':
        method = OPERATIONS[op] 
        result =  method(float(a),float(b))

        #convert to .xx
        result = str("%0.2f" % result)

        #convert X.0 to X (float to int)
        if '.0' in result:
            result  =  str(int(float(result)))

        return result
    else:
       error('Invalid Operation') 


op = None
# The Event Loop
while True:
    result = ''
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Clear':
        result = ''        

    elif event in '1234567890.+-/*':
        result = values['input'] #old value       
        result += event
        if event in '+-/*':
            op = event
    elif event == '=':
        result = values['input']

        if validate(result):
            exp = result.split(op)
            if len(exp) == 2:
                result= evaluate(exp[0], op, exp[1])

            window['result'].update(result)
    window['input'].update(result)
        

