import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from functools import partial
import config as cfg


class MainView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color='#262626')

        self.entry = ctk.CTkEntry(
            self, **cfg.ENTRY_PARAMS
        )
        self.entry.grid(**cfg.ENTRY_GRID)
        self.entry.insert(0, '0')
        self.entry.bind('<Key>', controller.transfer_data)

        for value, row, column in cfg.BTN_DATA:
            button = ctk.CTkButton(
                self,
                text=value,
                command=partial(controller.transfer_data, value),
                **cfg.BTN_PARAMS
            )
            button.grid(row=row, column=column, **cfg.BTN_GRID)

        for column in range(4):
            self.grid_columnconfigure(column, weight=1)
        for row in range(1, 5):
            self.grid_rowconfigure(row, weight=1)

    def show_result(self, value):
        self.entry.delete(0, 'end')
        self.entry.insert(0, str(value))
        self.entry.focus()

    def show_error(self, status):
        error_message = CTkMessagebox(
            app,
            message=cfg.ERROR_MESSAGES[status],
            **cfg.MSG_PARAMS
        )
        self.wait_window(error_message)
        self.entry.delete(0, 'end')
        self.entry.insert(0, '0')
        self.entry.focus()


class MainLogic:
    def __init__(self):
        self.value = '0'

    def calculate(self, user_input):
        is_keyboard = hasattr(user_input, 'char')

        if is_keyboard:
            event = user_input
            user_input = event.char

            if event.keysym == 'Backspace' or user_input == '\x08':
                if len(self.value) <= 1:
                    self.value = '0'
                else:
                    self.value = self.value[:-1]
                return self.value

            if user_input == '\r':
                user_input  = '='

            if user_input not in '0123456789+-*/=':
                return self.value

        if user_input == 'C':
            self.value = '0'
            return self.value

        if user_input == '=':
            if not self.value or self.value == '0':
                return self.value

            if self.value[-1] in '+-*/':
                self.value += self.value[:-1]

            try:
                self.value = str(eval(self.value))
            except (NameError, SyntaxError):
                self.value = '0'
                return 'not_digit'
            except ZeroDivisionError:
                self.value = '0'
                return 'zero_division'
            return self.value

        if user_input in '+-*/':
            if not self.value:
                return self.value

            if self.value[-1] in '+-*/':
                self.value = self.value[:-1]
            elif any(op in self.value for op in '+-*/'):
                try:
                    self.value = str(eval(self.value))
                except ZeroDivisionError:
                    self.value = '0'
                    return 'zero_division'
                except Exception:
                    self.value = '0'

            self.value = self.value + user_input
            return self.value

        if self.value == '0':
            self.value = ''

        self.value = self.value + str(user_input)

        return self.value


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Калькулятор')
        self.geometry('300x340+1000+500')
        self.resizable(False, False)
        self.attributes('-alpha', 0.9)

        self.view = MainView(self, self)
        self.view.pack(fill="both", expand=True)
        self.logic = MainLogic()

    def transfer_data(self, user_input):
        result = self.logic.calculate(user_input)
        if result in ('not_digit', 'zero_division'):
            self.view.show_error(result)
            return 'break'
        self.view.show_result(result)
        return 'break'


if __name__ == '__main__':
    app = MainApp()
    app.mainloop()



