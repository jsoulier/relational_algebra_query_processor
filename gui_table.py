import tkinter
import tkinter.ttk as ttk

class GUITable(ttk.Frame):
    ''''''

    def __init__(self, master, table):
        ''''''
        super().__init__(master)

        # Add columns
        for x, column in enumerate(table.columns):
            label = ttk.Label(self, text=column)
            label.grid(row=0, column=x)

        # Underline columns
        separator = ttk.Separator(self, orient=tkinter.HORIZONTAL)
        separator.grid(row=1, column=0, sticky=tkinter.EW, columnspan=len(table.columns))

        # Add rows
        for y, row in enumerate(table.rows):
            for x, column in enumerate(row):
                label = ttk.Label(self, text=column)
                label.grid(row=y+2, column=x)

        self.grid(row=0, column=0, sticky=tkinter.NSEW)
