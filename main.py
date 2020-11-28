import contextlib
import tkinter as tk
import os
from tkinter import *
from tkinter.filedialog import FileDialog


def main():
    def file():
        def save_path():
            temp_path = open("default_path.txt", "w")
            temp_path.write(path.get())
            temp_path.close()
            temp_path = open("default_path.txt", "r")
            print(temp_path.readline(100))
            return

        try:
            set_location = open("default_path.txt", "r").readline()
        except:
            set_location = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\')
            default_path = open("default_path.txt", "w")
            default_path.write(set_location)
            default_path.close()
        set_default_path = tk.Tk(className=" Set Default Path")
        set_default_path.geometry("320x30")
        set_default_path.focus_force()
        path_name = Label(set_default_path, text="Path:")
        path = Entry(set_default_path, width=40)
        path_save = Button(set_default_path, text="Save", command=save_path)
        path.insert(0, set_location)
        path_name.grid(column=1, row=0, pady=2)
        path.grid(column=2, row=0, pady=2)
        path_save.grid(column=3, row=0, pady=2, padx=2)

    def clear():
        text.delete("1.0", "end")
        return

    def non_over_write(complete_path, save_path, over_write_window):
        print("chose not to overwrite")
        i = 1
        while os.path.exists(complete_path):
            complete_path = os.path.join(save_path, file_name.get() + "(" + str(i) + ").txt")
            i = i + 1
        over_write_window.destroy()
        return

    def over_write(over_write_window):
        print("overwrite in progress")
        over_write_window.destroy()
        return

    def save(self):
        print("testing save")
        save_path = open("default_path.txt", "r").readline()
        complete_path = os.path.join(save_path, file_name.get() + ".txt")
        if os.path.exists(complete_path):
            over_write_window = tk.Tk(className=" Alert")
            over_write_window.geometry("170x50")
            over_write_window.focus_force()
            over_write_btn = Button(over_write_window, text="Overwrite [F1]", command=lambda: over_write(over_write_window))
            non_overwrite_btn = Button(over_write_window, text="New [F2]", command=lambda: non_over_write(complete_path, save_path, over_write_window))
            over_write_label = Label(over_write_window, text="Do you want to overwrite?")
            over_write_label.grid(column=0, row=0, columnspan=2, padx=5)
            over_write_btn.grid(column=0, row=1, pady=2, padx=5)
            non_overwrite_btn.grid(column=1, row=1, pady=2, padx=5)
        new_file = open(complete_path, "w")
        new_file.write(text.get("1.0", "end"))
        return

    root = tk.Tk(className=" Note Maker")
    root.geometry("505x350")
    label = Label(root, text="Note Maker")
    file_label = Label(root, text="File Name: ")
    file_name = Entry(root, width=40)
    txt_label = Label(root, text=".txt")
    text = Text(root, width=60, height=15)
    file_path_btn = tk.Button(root, text="Set Default Path [F3]", command=file)
    clear_btn = tk.Button(root, text="Clear [F2]", command=clear)
    save_btn = tk.Button(root, text="Save [F1]", command=save)
    root.bind('<F1>', save)

    label.grid(column=3, row=0)
    file_label.grid(column=2, row=1)
    file_name.grid(column=3, row=1)
    file_name.focus_set()
    txt_label.grid(column=4, row=1)
    file_path_btn.grid(column=5, row=1)
    text.grid(column=1, row=2, columnspan=10, rowspan=10, padx=10, pady=10)
    save_btn.grid(column=3, row=12)
    clear_btn.grid(column=3, row=12, columnspan=10)
    root.mainloop()


main()
