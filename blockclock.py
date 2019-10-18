from tkinter import *
import sys
import subprocess as sp

def tick():
	blocks = sp.getoutput(' bitcoin-cli getblockchaininfo | grep blocks | cut -c 13-18')
	clock.config(text= blocks)
	clock.after(6150, tick)
root = Tk()
root.title("Block Clock")
clock = Label(root, font = ("helvetica", 100, "bold"), bg= "orange")
clock.grid(row=0, column=1)
tick()
root.mainloop()

