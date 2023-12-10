import webbrowser
import time
import os
from tkinter import messagebox

sito = input("cosa vuoi vedere? \n")
url = ("http://www."+sito+".it")
webbrowser.open(url)
time.sleep(5)
messagebox.showinfo("chiusura", "Chiudo il browser...")
os.system("killall 'chrome'")
