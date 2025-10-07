import tkinter as tk
from tkinter import ttk
from logic_counter import logic_table
from itertools import product, permutations
from copy import deepcopy
root = tk.Tk()

root.title("Таблица истинности")
root.geometry("500x500")

class LTableMaker():
    def __init__(self):
        self.tables = []

    def create_table(self):
        if len(self.tables) != 0:
            self.tables[0].pack_forget()
            self.tables.pop()
        expression = log_entry.get()


        table_columns = ('w', 'x', 'y', 'z', 'result')
        table_fill = logic_table(expression)


        table = ttk.Treeview(log_entry.master, columns=table_columns, show="headings", height=len(table_fill))

        for col in table_columns:
            table.heading(col, text=col)
            table.column(col, width=50)

        for string in table_fill:
            table.insert("", "end", values=string)

        table.pack()
        self.tables.append(table)



class LogEntryBlock(ttk.Entry):
    def __init__(self, master, *args, **kwargs):
        self.var = tk.StringVar()
        kwargs["textvariable"] = self.var

        super().__init__(master, *args, **kwargs)

        self.__label_var = tk.StringVar()
        self.__label = ttk.Label(self.master, textvariable=self.__label_var)
        self.var.trace("w", self.validate_input)
        self.__enter = ttk.Button(self.master, text="Составить логическую таблицу", command=LTableMaker().create_table, state="disabled")


    def validate_input(self, *args):
        self.__enter.config(state="disabled")
        text = self.var.get()
        text = text.replace('≡', ' == ').replace('→', ' <= ').replace('¬', ' 1- ')
        text = text.replace('∧', ' and ').replace('∨', ' or ').replace(' ', '')
        text = text.replace('  ', ' ')
        self.var.set(text)


        without_brackets = text.replace('(', ' ').replace(')', ' ')

        val_list = without_brackets.split(' ')

        for elem in val_list:
            if not (elem in ('w', 'x', 'y', 'z', 'and', 'or', '<=', 'not', '==', '', '1-')):
                self.__label_var.set("Могут присутствовать только: 'and', 'or', '<=', '==', 'not' '(', ')', 'w', 'x', 'y', 'z', '1-'"
                                     "\nВсе операции и символы(кроме скобок) нужно разделить пробелами")
                self.__label.config(foreground='red')
                return 0
        if not ('w' in val_list and 'x' in val_list and 'y' in val_list and 'z' in val_list):
            self.__label_var.set("Обязаны присутствовать символы: 'w', 'x', 'y', 'z'")
            self.__label.config(foreground='red')
            return 0
        try:
            w, x, y, z = 1, 1, 1, 1
            eval(text)
        except:
            self.__label_var.set("Проверьте корректность расстановки скобок, вычислимость")
            self.__label.config(foreground='red')
            return 0

        self.__label_var.set("Ввод корректен и готов к расчёту")
        self.__label.config(foreground='green')

        self.__enter.config(state="enabled")

        ts_button_var.set("Решить")
        return 1


    def pack(self, **kwargs):
        super().pack(**kwargs)

        self.__label.pack(**kwargs)
        self.__enter.pack(**kwargs)

class TableSolver():
    def __init__(self, master):
        self.master = master
        self.widgets_list = [[0] * 5 for i in range(5)]
        self.vars_list = [[0] * 5 for i in range(5)]

        for i in range(5):
            for j in range(5):
                self.vars_list[i][j] = tk.StringVar()
        self.vars_list[0][0].set("Пер. 1")
        self.vars_list[0][1].set("Пер. 2")
        self.vars_list[0][2].set("Пер. 3")
        self.vars_list[0][3].set("Пер. 4")
        self.vars_list[0][4].set("Функция")

        for i in range(4): self.vars_list[1][i].set('?')
        self.vars_list[1][4].set('F')

        for j in range(5):
            self.widgets_list[0][j] = ttk.Label(master, textvariable = self.vars_list[0][j], width=10)
            self.widgets_list[1][j] = ttk.Label(master, textvariable = self.vars_list[1][j], width=10)

        for i in range(2, 5):
            for j in range(5):
                self.widgets_list[i][j] = ttk.Entry(master, width=10, textvariable=self.vars_list[i][j])
                self.vars_list[i][j].trace('w', self.val_input)

    def val_input(self, *args):
        for i in range(2, 5):
            for j in range(5):
                if self.widgets_list[i][j].get() not in ('1', '0', ''):
                    self.vars_list[i][j].set('')

    def solve_process(self):
        args_table = [[''] * 4 for i in range(3)]
        func_table = [0] * 3
        x_cnt = 0
        for i in range(2, 5):
            for j in range(4):
                elem = self.widgets_list[i][j].get()
                if elem == '':
                    args_table[i - 2][j] = 'x'
                    x_cnt += 1
                elif elem == '0':
                    args_table[i - 2][j] = 0
                elif elem == '1':
                    args_table[i - 2][j] = 1

        for i in range(2, 5):
            func_table[i - 2] = int(self.widgets_list[i][4].get())

        product_lst = []
        for i in product([0, 1], repeat=x_cnt):
            product_lst.append(i)

        def f(x, y, w, z):
            return eval(log_entry.var.get())

        for prod in product_lst:
            test_table = deepcopy(args_table)
            index = 0
            for i in range(3):
                for j in range(4):
                    if test_table[i][j] == 'x':
                        test_table[i][j] = prod[index]
                        index += 1
            for i in range(len(test_table)): test_table[i] = tuple(test_table[i])

            if len(test_table) == len(set(test_table)):
                for p in permutations('xywz'):
                    if [f(**dict(zip(p, i))) for i in test_table] == func_table:
                        for i in range(4):
                            self.vars_list[1][i].set(p[i])
                            for i in range(3):
                                for j in range(4):
                                    if args_table[i][j] == 'x':
                                        self.vars_list[i + 2][j].set(str(test_table[i][j]))
    def solve(self):
        if not (log_entry.validate_input()):
            ts_button_var.set("Введите логическое выражение в специальное поле поле")
            return
        try:
            self.solve_process()
        except: ts_button_var.set("Введённых в таблицу данных недостаточно для решения")



    def pack(self):
        for i in range(0, 5):
            for j in range(5):
                self.widgets_list[i][j].grid(row=i, column=j)



first_frame = tk.Frame(
        root,
        borderwidth=1,
        relief="solid",
        padx=5,
        pady=5,
    )
log_entry = LogEntryBlock(first_frame, width=54)
log_entry.pack()
first_frame.pack()


second_frame = tk.Frame(
        root,
        borderwidth=1,
        relief="solid",
        padx=5,
        pady=5,
    )
table_solver = TableSolver(second_frame)
ts_button_var = tk.StringVar()
ts_button_var.set("Решить")
ts_button = ttk.Button(second_frame, textvariable=ts_button_var, command=table_solver.solve)
table_solver.pack()
ts_button.grid(row = 5, column = 0, columnspan = 5)
second_frame.pack()


root.mainloop()