#!/usr/bin/env python3
'''
Simple example Tkinter
'''

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.CreateWidgets()

    def CreateWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()


app = Application()
app.master.title("Sample Application")
app.mainloop()
