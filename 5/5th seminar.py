import tkinter as tk
from tkinter import ttk
from first_task_solver import solve_first_task
root = tk.Tk()
class MatrixApp:
    def __init__(self, root, size=7):
        self.root = root
        self.size = size
        self._vars_list = [[0] * (self.size + 1) for i in range(self.size + 1)]
        self.__index_for_name = dict()
        self.build_table()

    def build_table(self):
        for i in range(self.size + 1):
            for j in range(self.size + 1):
                self._vars_list[i][j] = tk.StringVar()
                self.__index_for_name[str(self._vars_list[i][j])] = (i, j)
        for i in range(self.size + 1):
            for j in range(self.size + 1):
                if i == 0 and j == 0:
                    label = tk.Label(self.root, textvariable=self._vars_list[i][j], width=6, borderwidth=0, relief="solid")
                    label.grid(row=0, column=0)
                elif i == 0:
                    label = tk.Label(self.root, textvariable=self._vars_list[i][j], width=6, borderwidth=0, relief="solid", bg="#f0f0f0")
                    self._vars_list[i][j].set(f"П{j}")
                    label.grid(row=i, column=j)
                elif j == 0:
                    label = tk.Label(self.root, textvariable=self._vars_list[i][j], width=6, borderwidth=0, relief="solid", bg="#f0f0f0")
                    self._vars_list[i][j].set(f"П{i}")
                    label.grid(row=i, column=j)
                elif i == j:
                    label = tk.Label(self.root, textvariable=self._vars_list[i][j], width=6, borderwidth=0, relief="solid", bg="#DEDCDC")
                    label.grid(row=i, column=j)
                else:
                    entry = tk.Entry(self.root, width=6, justify="center", textvariable=self._vars_list[i][j])
                    entry.grid(row=i, column=j, padx=1, pady=1)
                    self._vars_list[i][j].trace('w', self.mirror_input)


    def mirror_input(self, var_name, *args):
        i, j = self.__index_for_name[var_name]
        self._vars_list[j][i].set(self._vars_list[i][j].get())

    def get_matrix(self):
        matrix = []
        for i in range(1, self.size + 1):
            row = []
            for j in range(1, self.size + 1):
                value = self._vars_list[i][j].get()
                row.append(value)
            matrix.append(row)
        return matrix

    @property
    def format_for_solving_table(self):
        col_set = "123456789"[:self.size]
        matrix = self.get_matrix()

        c = ''
        for i in range(self.size):
            c += col_set[i]
            for j in range(self.size):
                c += (matrix[i][j] != '') * col_set[j]
            c += ' '
        c = c[:-1]

        return c


class TableApp:
    def __init__(self, root, size=5):
        self.root = root
        self.size = size
        self.entries = []

        self.build_table()

    def build_table(self):
        headers = ["Название пункта", "С какими пунктами связан"]
        for col, text in enumerate(headers):
            label = ttk.Label(self.root, text=text, font=("Arial", 12, "bold"))
            label.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")

        for row in range(1, self.size + 1):
            row_entries = []
            for col in range(2):
                if col == 0: width = 5
                else: width = 15
                entry = ttk.Entry(self.root, width=width)
                entry.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                row_entries.append(entry)
            self.entries.append(row_entries)


    def get_data(self):
        data = []
        for row in self.entries:
            data.append([cell.get() for cell in row])
        return data

    @property
    def format_for_solving_graph(self):
        data = self.get_data()
        for i in range(len(data)):
            data[i][0] = data[i][0].upper()
            data[i][1] = ''.join(sorted([c.upper() for c in data[i][1] if c.isalpha()]))
        data.sort(key = lambda lst: lst[0])
        print(data)
        s = ''
        for i in data:
            s += ''.join(i) + ' '
        s = s[: -1]
        return s

class MainApp:
    def __init__(self, root):
        self.root = root
        self.__entry_var = tk.StringVar()
        self.__entry = ttk.Entry(root, textvariable=self.__entry_var)
        self.__label = ttk.Label(root, text = "Размер квадратной таблицы (цифра)")

        self.__entry_var.trace('w', self.input_indicator)

        self.__length_input_button = ttk.Button(root, text="Ввод", command=self.place_solver, state='disabled')

        self.__label.pack()
        self.__entry.pack()
        self.__length_input_button.pack()

        self.__main_frame = tk.Frame(root)



    def input_indicator(self, *args):
        text = self.__entry_var.get()
        if text in '56789' and len(text) == 1:
            self.__label.config(foreground='green')
            self.__length_input_button.config(state='enabled')
            return 1
        else:
            self.__label.config(foreground='red')
            self.__length_input_button.config(state='disabled')
            return 0


    def place_solver(self):
        for widget in self.__main_frame.winfo_children():
            widget.destroy()
            print(widget)
        size = int(self.__entry_var.get())
        self.size = size

        first_frame = tk.Frame(
            self.__main_frame,
            borderwidth=1,
            relief="solid",
            padx=5,
            pady=5,
        )
        self.mapp = MatrixApp(first_frame, size)

        second_frame = tk.Frame(
            self.__main_frame,
            borderwidth=1,
            relief="solid",
            padx=5,
            pady=5,
        )
        self.tapp = TableApp(second_frame, size)

        first_frame.pack()
        tk.Label(self.__main_frame, text = "Данные с графа:", font = ("Arial", 12, "bold")).pack()
        second_frame.pack()
        self.solve_button = ttk.Button(self.__main_frame, text = "Решить", command = self.full_solve)
        self.solve_button.pack()

        self.__main_frame.pack()

    def full_solve(self):
        try:
            res = solve_first_task(self.tapp.format_for_solving_graph, self.mapp.format_for_solving_table, self.size)
            for i in range(1, self.size + 1):
                self.mapp._vars_list[0][i].set(res[i-1])
                self.mapp._vars_list[i][0].set(res[i-1])
            self.solve_button.config(text = "Таблица заполнена")
        except:
            self.solve_button.config(text = "Решения не найдено, проверьте вводы")

app = MainApp(root=root)

root.mainloop()
