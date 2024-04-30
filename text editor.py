import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files","*.txt"),("All File","*.*")]
    )
    if not filepath:
        return
    text.delete(1.0,tk.END)
    with open(filepath,'r') as f:
        txt = f.read()
        text.insert(tk.END,txt)
    window.title(f"Text Editor by keshav - {filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text files","*.txt"),("All types","*.*")]
    )

    if not filepath:
        return
    
    with open(filepath,'w') as d:
        txt = text.get(1.0,tk.END)
        d.write(txt)
    window.title("Text Editor by Keshav - {filepath}")


window = tk.Tk()
window.title("Text Editor by keshav")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


text = tk.Text(window)
frame_btn = tk.Frame(window,relief=tk.RAISED,bd=2)

frame_btn.grid(row=0,column=0,sticky="ns")
text.grid(row=0,column=1,sticky="nsew")

btn_open = tk.Button(frame_btn,text="Open",command = open_file)
btn_saveAs = tk.Button(frame_btn,text="Save As..",command=save_file)

btn_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_saveAs.grid(row=1,column=0,sticky="ew",padx=5)

window.mainloop()
