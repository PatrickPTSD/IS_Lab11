import tkinter as tk
def click(button):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current+button)

def equal():
    try:
        rezultat=eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(rezultat))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Eroare")

def dell():#delete
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

entry= tk.Entry(root, width=20, font=('Arial',20), borderwidth=2, relief='ridge',justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons =[
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for i, line in enumerate(buttons):
    for j, text in enumerate(line):
        if text == '=':
            tk.Button(root, text=text, width=5, height=2, font=('Arial',14), command=equal).grid(row=i+1, column=j)
        else:
            tk.Button(root, text=text, width=5, height=2, font=('Arial',14), command=lambda t=text: click(t)).grid(row=i+1, column=j)
    
tk.Button(root, text="C", width=5, height=2, font=('Arial',14), command=dell).grid(row=5, column=0, columnspan=4, sticky='we')

root.mainloop()