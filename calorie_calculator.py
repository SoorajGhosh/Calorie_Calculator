from tkinter import *

class Root(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		
		self.title('Calorie Calculator')
		container = Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		
		self.frames ={}
		self.geometry('300x300') 
		self.maxsize(300,300)

		for F in (StartPage,):
			frame = F(container,self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky = "nsew")
			
		self.show_frame(StartPage)
		
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
		

class StartPage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		
		self.cb_gm = DoubleVar()
		self.pt_gm = DoubleVar()
		self.ft_gm = DoubleVar()
		
		
		cb_ent = Entry(self, textvariable = self.cb_gm)
		ft_ent = Entry(self, textvariable = self.ft_gm)
		pt_ent = Entry(self, textvariable = self.pt_gm)
		
		cb_lbl = Label(self, text = "Grams of Carbs")
		ft_lbl = Label(self, text = "Grams of Fat")
		pt_lbl = Label(self, text = "Grams of Protien")
		
		clr_lbl = Label(self, text = "Calories in Meal")
		self.calories = Label(self, text = "")
		
		calc_btn = Button(self, text = "Calculate Calories", command = self.calc_calr)
		clear_btn = Button(self, text = "Clear All", command = self.clr_all)
		ext_btn = Button(self, text = "Exit", command = controller.destroy)
		
		
		cb_lbl.grid(row = 0, column = 0, padx = 10, pady = 10)
		ft_lbl.grid(row = 1, column = 0, padx = 10, pady = 10)
		pt_lbl.grid(row = 2, column = 0, padx = 10, pady = 10)
		
		cb_ent.grid(row = 0, column = 1, padx = 10, pady = 10)
		ft_ent.grid(row = 1, column = 1, padx = 10, pady = 10)
		pt_ent.grid(row = 2, column = 1, padx = 10, pady = 10)
		
		calc_btn.grid(row = 3, columnspan = 2, padx = 10, pady = 10)
		
		clr_lbl.grid(row = 4, column = 0, padx = 10, pady = 10)
		self.calories.grid(row = 4, column = 1, padx = 10, pady = 10)
		
		clear_btn.grid(row = 5, column = 0, padx = 10, pady = 10)
		ext_btn.grid(row = 5, column = 1, padx = 10, pady = 10)
		
		
	def calc_calr(self):
		tot_carb = self.cb_gm.get()*4
		tot_fat = self.ft_gm.get()*9
		tot_prot = self.pt_gm.get()*4
		tot_calr = str(tot_carb + tot_fat + tot_prot)
		self.calories['text'] = tot_calr
	
	def clr_all(self):
		self.cb_gm.set(0.0)
		self.ft_gm.set(0.0)
		self.pt_gm.set(0.0)
		self.calories['text'] = ''
	
app = Root()
app.mainloop()		
	














