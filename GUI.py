import tkinter as tk
import tkinter.filedialog as fd


win = tk.Tk()
win.title("la mia prima GUI in python")
win.rowconfigure(0, weight=1)
win.columnconfigure(0, weight=1)


def do_quit():
    win.quit()


def do_open():
    path = fd.askopenfilename(title='Scegli un file',
                              filetypes=[('text', '*.txt'), ('python', '*.py'),
                                        ('all', '*.*')])
    if len(path) > 0:
        txt.delete('1.0', 'end')
        with open(path, 'U') as f:
            txt.insert('1.0', f.read())


def do_saveas():
    path = fd.asksaveasfilename(title='Dove Salvare')
    if len(path) > 0:
        with open(path, 'w') as f:
            f.write(txt.get('1.0', 'end'))


txt = tk.Text(win)
txt.grid(sticky="nsew")

mb = tk.Menu(win)     # Crea la barra del menu (vuota)
win.config(menu=mb)   # e la aggiunge alla finestra
fm = tk.Menu(mb)                 # Crea il menù File
fm.add_command(label='Open...', command=do_open)  # e vi aggiunge la voce Open
fm.add_separator()               # una linea di separazione
fm.add_command(label="Salva file", command=do_saveas)
fm.add_command(label='Quit', command=do_quit)     # infine, la voce Quit
mb.add_cascade(label='File', menu=fm)   # Aggiunge il menù file nella barra
tk.mainloop()
