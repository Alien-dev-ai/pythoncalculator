import thinker as tk

def click_button(value):
    current=entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current+value)

def clear_entry():
    entry.delete(0,tk.END)

def calculate():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    except Exception:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")

root = tk.tk()
root.title("Alien calculator")
root.goemetry("300*400")
root.resizable(False,False)

entry = tk.Entry(root,width=20,font=("Arial",18),borderwidth=2,relief="solid",justify="right")
entry.pack(pady=10)

buttons =[
    ("7","8","9","/"),
    ("6","5","4","*"),
    ("3","2","1","-"),
    ("0",".","=","+")
]

for row_values in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True,fill="both")
    for value in row_values:
        if value =="=":
            btn=tk.Button(frame,text=value,font=("Arial",16),height=2,width=6,command=lambda val=value:click_button(val))
            btn.pack(side="left",expand=True,fill="both")

clear_btn = tk.Button(root,text="Clear",font=("Arial",16),height=2,width=26,command=clear_entry)
clear_btn.pack(pady=5)

root.mainloop()