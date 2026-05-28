import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

def clear():
    calc.delete(0, 'end')
    calc.insert (0,0)

def calculate():
    value = calc.get()
    if value [-1] in '+-*/':
        value += value [:-1]
    calc.delete(0, 'end')
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        error_message = CTkMessagebox(
            win,
            title='Внимание!',
            message='Нужны только цифры. Вы ввели другие символы!'
        )
        calc.insert(0,0)
    except ZeroDivisionError:
        error_message = CTkMessagebox(
            win,
            title='Внимание!',
            message='На ноль делить нельзя!'
        )
        calc.insert(0,0)

def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, 'end')
    calc.insert(0, value + digit)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, 'end')
    calc.insert(0, value + operation)

def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()

ctk.set_appearance_mode("dark")
win = ctk.CTk()
win.title('Калькулятор')
win.bind ('<Key>', press_key)
win.geometry('300x340+600+300')
win.resizable(False, False)

calc = ctk.CTkEntry(
    win, justify='right', font=('Arial', 30),
    width=15, height = 50
)
calc.insert(0, '0')
calc.grid(
    row=0, column=0, columnspan=4,
    stick='we', padx=5
)

GRID_PARAMS = {
    'sticky': 'wens',
    'padx': 5,
    'pady': 5
}

BTN_PARAMS = {
    'fg_color': '#333333',
    'hover_color': '#262626',
    'font': ('Arial', 13)
}

button_data = [
    ('0', 4, 0, lambda: add_digit('0')),
    ('1', 1, 0, lambda: add_digit('1')),
    ('2', 1, 1, lambda: add_digit('2')),
    ('3', 1, 2, lambda: add_digit('3')),
    ('4', 2, 0, lambda: add_digit('4')),
    ('5', 2, 1, lambda: add_digit('5')),
    ('6', 2, 2, lambda: add_digit('6')),
    ('7', 3, 0, lambda: add_digit('7')),
    ('8', 3, 1, lambda: add_digit('8')),
    ('9', 3, 2, lambda: add_digit('9')),
    ('+', 1, 3, lambda: add_operation('+')),
    ('-', 2, 3, lambda: add_operation('-')),
    ('*', 3, 3, lambda: add_operation('*')),
    ('/', 4, 3, lambda: add_operation('/')),
    ('C', 4, 1, clear),
    ('=', 4, 2, calculate)
]

for text, row, column, command in button_data:
    button = ctk.CTkButton(
        win,
        **BTN_PARAMS,
        text=text,
        command=command
    )

    button.grid(
        row=row,
        column=column,
        **GRID_PARAMS
    )

grid_types = {
    'column': win.grid_columnconfigure,
    'row': win.grid_rowconfigure
}

grid_data = [
    ('column', 0), ('column', 1), ('column', 2), ('column', 3),
    ('row', 1), ('row', 2), ('row', 3), ('row', 4)
]

for grid_type, value in grid_data:
    configure = grid_types[grid_type]
    configure(value, weight=1)

win.mainloop()