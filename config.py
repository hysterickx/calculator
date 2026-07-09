COLOR_DARK = '#0d0a0c'

BTN_PARAMS = {
    'fg_color': '#333333',
    'hover_color': '#262626',
    'font': ('Arial', 13)
}

BTN_GRID = {
    'sticky': 'wens',
    'padx': 5,
    'pady': 5
}

ENTRY_PARAMS = {
    'justify': 'right',
    'font': ('Arial', 30),
    'height': 50
}

ENTRY_GRID = {
    'row': 0,
    'column': 0,
    'columnspan': 4,
    'stick': 'we',
    'padx': 5
}

BTN_DATA = [
    ('0', 4, 0), ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('7', 3, 0),
    ('8', 3, 1), ('9', 3, 2), ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3), ('C', 4, 1), ('=', 4, 2)
]

WRONG_ERROR_TXT = {
    'title': 'Внимание!',
    'message': 'Нужны только цифры. Вы ввели другие символы!'
}

ZERO_ERROR_TXT = {
    'title': 'Внимание!',
    'message': 'На ноль делить нельзя!'
}

