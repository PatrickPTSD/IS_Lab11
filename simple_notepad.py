import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt", 
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file:\n{e}")

def save_file():
     file = filedialog.asksaveasfilename(defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
     if file:
        try:
            content = text_area.get(1.0, tk.END)
            with open(file, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")

root = tk.Tk()
root.title("Simple Notepad")
root.geometry("600x400")

text_area = tk.Text(root, font=("Arial", 12))
text_area.pack(fill=tk.BOTH, expand=True)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
