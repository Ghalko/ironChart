from Tkinter import *

class Example(Frame):
	"""docstring for Example"""
	def __init__(self, master):
		self.f = Frame.__init__(self, master)
		self.master = master
		menubar = Menu(self.f)
		# create a pulldown menu, and add it to the menu bar
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="Exit", command=self.exit)
		menubar.add_cascade(label="File", menu=filemenu)
		menubar.add_command(label='Toggle', command=None)
		self.master.config(menu=menubar)
		
	def exit(self):
		pass

class IronChart(Frame):
	"""The canvas for the chart"""
	def __init__(self, master, *args, **kwargs):
		self.f = Frame.__init__(self, master, **kwargs)

if __name__ == '__main__':
	root = Tk()
	app = Example(root)
	app.mainloop()