import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from main import tab5


class RowList:
    def __init__(self):
        self.items = []

    def __iter__(self):
        for item in self.items:
            yield item

    def __len__(self):
        return len(self.items)

    def append(self, *args):
        for i in args:
            self.items.append(i)


class DeleteCommand:

    def __init__(self):
        self.items = []

    def __iter__(self):
        for item in self.items:
            yield item

    def __len__(self):
        return len(self.items)

    def append(self, item):
        self.items.append(item)


class ToDo(Frame):

    i = 0

    def __init__(self, master=None, datafile=None, *args):
        super().__init__(master)
        self.datafile = datafile
        self.pack()
        self.rows = RowList()
        self.deleted = DeleteCommand()
        self.buildWindow()

    def buildWindow(self):
        """
        This method is called to create all widgets, place them in the GUI, and
        define the event handlers for the application
        """
        self.master.title("To-Do App")
        self.master.resizable(0, 0)
        self.master.geometry("730x800")

        default_frame = ttk.Frame(self.master, width=800, height=800)
        default_frame.pack()

        def undo_delete_handler():
            if len(self.deleted) > 0:
                last_undo = self.deleted.items[-1]
                last_undo[0].pack()
                for i in range(1, 4):
                    last_undo[i].grid()

        undo_delete = ttk.Button(
            default_frame, text="Undo Delete", command=undo_delete_handler)
        undo_delete.pack()

        def delete_todo_handler(indx):
            for lst in self.rows.items:
                if indx in lst:
                    self.deleted.append(lst)
                    try:
                        for j in lst:
                            j.grid_remove()
                    except Exception:
                        pass
                    finally:
                        text_entry_field.focus()

        def edit_todo_handler(textfield, button):
            def save_edit():
                textfield.configure(state="disabled")
                button.configure(text="❌")
                text_entry_field.focus()
            textfield.configure(state="normal")
            textfield.focus()
            button.configure(text="Done", command=save_edit)

        def add_todo(widget):

            user_text = widget.get()

            if len(user_text) <= 90 and len(user_text) > 0:
                indx = ToDo.i
                todo_frame = ttk.Frame(default_frame, width=800)
                todo_frame.pack()
                edit_button = ttk.Button(
                    todo_frame, text="Edit", command=lambda: edit_todo_handler(text_field, delete_button))
                edit_button.grid(row=1, column=0)
                text_field = ttk.Entry(todo_frame, width=95)
                text_field.grid(row=1, column=1)
                text_field.insert("end", user_text)
                delete_button = ttk.Button(
                    todo_frame, text="❌", command=lambda: delete_todo_handler(indx))
                delete_button.grid(row=1, column=3)
                text_field.configure(state="disabled")

                self.rows.append(
                    [todo_frame, edit_button, text_field, delete_button, indx])

                widget.delete("0", "end")

                ToDo.i += 1

            elif len(user_text) > 70:
                messagebox.showinfo(title="To-Do App",
                                    message="Maximum characters allowed is 70")

        text_entry_field = ttk.Entry(default_frame, width=120)
        text_entry_field.pack()
        text_entry_field.focus()
        text_entry_field.bind("<Return>",
                              lambda e: add_todo(text_entry_field))


def main():
    root = Tk()
    APP = ToDo(master=tab5)
    root.mainloop()


if __name__ == "__main__":
    main()