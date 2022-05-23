import tkinter as tk
import tkinter.ttk as ttk
from matplotlib import pyplot as plt

import mainMenu

window = tk.Tk()
window.geometry('540x325')
window.configure(bg='#39383e')

mainMenu.titleScreen()

tk.mainloop()