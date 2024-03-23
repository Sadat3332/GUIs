from tkinter import *
from tkinter import ttk

import numpy as np


class Calculator:
    def __init__(self,root):
        self.root = root
        self.root.resizable(False,False)
        

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both",expand= True)

        self.calculator_frame = Frame(self.notebook)
        self.notebook.add(self.calculator_frame,text="Calculator")
        self.matrix_calculator_frame = Frame(self.notebook)
        self.notebook.add(self.matrix_calculator_frame,text="Matrix Calculator")

        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

        self.create_calculator()
        self.create_matrix_calculator()
    

    def create_calculator(self):

        def button_click(char):
            current = entry.get()
            entry.delete(0, END)
            entry.insert(0, current + str(char))

        def clear():
            entry.delete(0, END)

        def equal():
            try:
                result = eval(entry.get())
                entry.delete(0, END)
                entry.insert(0, str(result))
            except Exception as e:
                entry.delete(0, END)
                entry.insert(0, "Error")


        entry = Entry(self.calculator_frame, width=35, borderwidth=5,font={'size':20})
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            button = Button(self.calculator_frame, text=text, padx=50, pady=20,
                            command=lambda t=text: button_click(t))
            button.grid(row=row, column=column)

        clear_button = Button(self.calculator_frame, text='Clear', padx=95, pady=20, command=clear)
        clear_button.grid(row=5, column=0, columnspan=2)

        equal_button = Button(self.calculator_frame, text='Calculate', padx=85, pady=20, command=equal)
        equal_button.grid(row=5, column=2, columnspan=2)


    def create_matrix_calculator(self):
        self.dimensions = ttk.Combobox(self.matrix_calculator_frame, values=[2, 3, 4, 5])
        self.dimensions.set("2")
        self.dimensions.grid(row=0, column=0, padx=10, pady=10)
        self.dimensions.bind("<<ComboboxSelected>>", self.create_matrices)

        mat_frame_row  = 2
        self.matrix_frame1 = Frame(self.matrix_calculator_frame)
        self.matrix_frame1.grid(row=mat_frame_row, column=0, padx=10, pady=10)



        self.matrix_frame2 = Frame(self.matrix_calculator_frame)
        self.matrix_frame2.grid(row=mat_frame_row, column=1, padx=10, pady=10)

        self.res_frame = Frame(self.matrix_calculator_frame)
        self.res_frame.grid(row=mat_frame_row,column=2,padx=10,pady=10)

        self.operation = ttk.Combobox(self.matrix_calculator_frame, values=["Add", "Subtract", "Multiply"])
        self.operation.set("Add")
        self.operation.grid(row=3, column=0, padx=5, pady=10)

        self.calculate_button = Button(self.matrix_calculator_frame, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=1, padx=20, pady=10)

    def create_matrices(self, event=None):
        self.clear_matrix_frames()
        mat1_label = Label(self.matrix_frame1,text="Matrix 1")
        mat1_label.grid(row=0,column=0, columnspan=self.dimensions.get())
        mat2_label = Label(self.matrix_frame2,text="Matrix 2")
        mat2_label.grid(row=0,column=0, columnspan=self.dimensions.get())
        dimension = int(self.dimensions.get())
        self.entries1 = []
        self.entries2 = []
        for i in range(1,dimension+1):
            row_entries1 = []
            row_entries2 = []
            for j in range(dimension):
                entry1 = Entry(self.matrix_frame1, width=5)
                entry2 = Entry(self.matrix_frame2, width=5)
                entry1.grid(row=i, column=j, padx=5, pady=5)
                entry2.grid(row=i, column=j, padx=5, pady=5)
                row_entries1.append(entry1)
                row_entries2.append(entry2)
            self.entries1.append(row_entries1)
            self.entries2.append(row_entries2)


    def print_result(self,result):

        dimension = int(self.dimensions.get())
        self.clear_result_frame()
        res_label = Label(self.res_frame,text="Result")
        res_label.grid(row=0,column=0, columnspan=self.dimensions.get())
        self.result = []
        for i in range(1,dimension+1):
            row_result = []
            for j in range(dimension):
                res = Entry(self.res_frame, width=5)
                res.insert(0,result[i-1][j])
                res.config(state='disabled')
                res.grid(row=i, column=j, padx=5, pady=5)

                row_result.append(res)
            self.result.append(row_result)

    def get_matrices(self):
        dimension = int(self.dimensions.get())
        matrix1 = []
        matrix2 = []
        for i in range(dimension):
            row1 = []
            row2 = []
            for j in range(dimension):
                value1 = self.entries1[i][j].get()
                value2 = self.entries2[i][j].get()
                
                try:
                    row1.append(float(value1))
                except ValueError:
                    row1.append(0) 
                try:
                    row2.append(float(value2))
                except ValueError:
                    row2.append(0)            
            matrix1.append(row1)
            matrix2.append(row2)
        return matrix1, matrix2

    def calculate(self):
        matrix1, matrix2 = self.get_matrices()
        mat1 = np.array(matrix1)
        mat2 = np.array(matrix2)
        operation = str(self.operation.get())
        if operation == 'Add':
            res = mat1+mat2

        elif operation == 'Subtract':
            res = mat1-mat2
        
        elif operation == 'Multiply':
            res = mat1@mat2
        
        self.print_result(res)
        
        # print(matrix1,matrix2)

    def clear_matrix_frames(self):
        for widget in self.matrix_frame1.winfo_children():
            widget.destroy()
        for widget in self.matrix_frame2.winfo_children():
            widget.destroy()    
    def clear_result_frame(self):
        for widget in self.res_frame.winfo_children():
            widget.destroy()   
    def button_add(self, num):
        curr = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, str(curr) + str(num))

    def on_tab_change(self,event):
        current_tab = self.notebook.tab(self.notebook.select(), "text")
        if current_tab == "Calculator":
            self.root.geometry("460x420")
        elif current_tab == "Matrix Calculator":
            self.root.geometry("710x350")


if __name__ == "__main__":
    root = Tk()
    run = Calculator(root)
    root.mainloop()