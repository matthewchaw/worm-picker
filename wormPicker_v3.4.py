"""
Worm picker v3

01/24/22
Utilize modified model-view-controller framework

view-controller

use classes

Icon Created with BioRender.com
"""
from os import path 
import tkinter as tk
from tkinter import ttk
import datetime
from pandastable import Table
import csv
import pandas as pd 
from tkcalendar import DateEntry
from ttkthemes import ThemedStyle


####### CLASSES #######

### PAGE 1: Entry ###

class Page1(ttk.Frame):
	''' 
	Class called by main controller window
	Purpose: Allow user to input strains to database by
	giving any number or combination of attributes as they 
	relate to C. elegans experiments in Shroff Lab.
	'''
	def __init__(self, parent, controller):
		ttk.Frame.__init__(self, parent)
		self.parent = parent
		self.controller = controller 

		self.addWin = ttk.Frame(self.parent) #Width has no effect
		self.addWin.grid(sticky='nesw')
		self.parent.add(self.addWin, text='Add new strain', sticky='nesw')
		#self.addWin.grid_columnconfigure(0, weight=1)


		self.addBox = ttk.LabelFrame(self.addWin, text='Strain Variables', style = 'Header.TLabelframe')
		self.addBox.grid(column=0, sticky = 'nw', padx=20, pady=0)
		self.addBox.grid_columnconfigure(0, weight=1)
		self.addBox.grid_rowconfigure(7, weight  = 1)

		self.eventLogFrame = ttk.LabelFrame(self.addWin, text = 'Event Log')#, background='cyan')
		self.eventLogFrame.grid(column = 1, row = 0, sticky = 'nw')
		self.eventLogFrame.grid_columnconfigure(1, weight=1)

		self.eventLog = tk.Text(self.eventLogFrame, background = self.controller.themeColor)#) #Inside frame
		self.eventLog.grid(sticky = 'nesw')
		self.eventLog.grid_columnconfigure(0, weight=1)


		### Variables
		self.strainvar = StrainClass(self.addBox, self.controller, 0) #self.controller is a downstream reference to ControllerWin
		self.typevar = TypeClass(self.addBox, self.controller, 1) 
		self.constructsvar = ConstructsClass(self.addBox, self.controller, 2) 
		self.statusvar = StatusClass(self.addBox, self.controller, 3) 
		self.pickDatevar = PickDateClass(self.addBox, self.controller, 4)
		self.pickEvery =  PickEveryClass(self.addBox, self.controller, 5)
		self.numPlatesvar = NumPlatesClass(self.addBox, self.controller, 6)
		self.locationvar = LocationClass(self.addBox, self.controller, 7)
		self.notesvar = NotesClass(self.addBox, self.controller, 8)
		### Getting
		self.enterButton = ttk.Button(self.addBox, text = 'Enter', width=25, command = (lambda:self.controller.enterData())) 

		self.enterButton.grid(columnspan = 2, row=9, column=0, pady=5, padx=5) 
class StrainClass(ttk.Frame):#var=self.strain
	'''
	Class called by page 1
	Purpose: create entrybox and label for 
	strain name
	'''
	def __init__(self, addBox, controller, addBoxRow):

		ttk.Frame.__init__(self, addBox)
		self.controller = controller
		self.addBox = addBox 

		ttk.Label(self.addBox, text='Strain Name').grid(row = addBoxRow, sticky='w', pady=5)
		self.strain = ttk.Entry(self.addBox)
		self.strain.grid(row=addBoxRow, column=1, sticky='w', padx=5)
class TypeClass(ttk.Frame):#var=self.strainTypeVar
	'''
	Class called by page 1
	Purpose: Create optionmenu for 'strain type' variables
	and label for box
	'''
	def __init__(self, addBox, controller, addBoxRow):

		ttk.Frame.__init__(self, addBox)
		self.controller = controller
		self.addBox = addBox

		
		
		self.No = tk.IntVar()
		self.In = tk.IntVar()
		self.Ar = tk.IntVar()
		self.Hs = tk.IntVar()
		self.Ma = tk.IntVar()

		self.strainTypesDict = {'None': self.No, 'Integrated': self.In, 'Array':self.Ar, 'Heat shock':self.Hs, 'Males':self.Ma}

		ttk.Label(self.addBox, text= 'Type').grid(row = addBoxRow, sticky= 'nw', pady=5)
		self.checkFrame = ttk.Frame(self.addBox)
		self.checkFrame.grid(row=addBoxRow, column = 1, sticky='w', pady=5)

		self.NoCheck = ttk.Checkbutton(self.checkFrame, text = 'None', variable = self.No ).grid(row = 0, sticky='w')
		self.InCheck = ttk.Checkbutton(self.checkFrame, text = 'Integrated', variable = self.In ).grid(row = 1, sticky='w')
		self.ArCheck = ttk.Checkbutton(self.checkFrame, text = 'Array', variable = self.Ar).grid(row = 2, sticky='w')
		self.HsCheck = ttk.Checkbutton(self.checkFrame, text = 'Heat Shock', variable = self.Hs).grid(row =3, sticky='w')
		self.MaCheck = ttk.Checkbutton(self.checkFrame, text = 'Males', variable = self.Ma).grid(row = 4, sticky='w')

		#self.strainTypeVar = tk.StringVar(self.addBox)
		#self.strainTypeVar.set(self.strainTypesls[0]) # default value
		#self.typeMenu = tk.OptionMenu(self.addBox, self.strainTypeVar, *self.strainTypesls)
		#self.typeMenu.grid(row=1, column=1, sticky='w', padx=5)
class ConstructsClass(ttk.Frame):#var=self.constructs
	'''
	Class called by page 1
	Purpose: Create entry box for constructs and labels
	Dependent on user to know and input necessary constructs
	'''
	def __init__(self, addBox, controller, addBoxRow):

		ttk.Frame.__init__(self, addBox)
		self.controller = controller
		self.addBox = addBox

		ttk.Label(self.addBox, text= 'Construct').grid(row= addBoxRow, sticky= 'w', pady=5)
		self.constructs = ttk.Entry(self.addBox) 
		self.constructs.grid(row=addBoxRow, column=1, sticky='w', padx=5)
class StatusClass(ttk.Frame):#var=self.status
	'''
	Class called by page 1
	Purpose: create option menu for 
	experimental statuses and respective labels
	''' 
	def __init__(self, addBox, controller, addBoxRow): 
		ttk.Frame.__init__(self, addBox)
		self.controller = controller
		self.addBox = addBox 

		

		self.No = tk.IntVar()
		self.Ma = tk.IntVar()
		self.Im = tk.IntVar()
		self.St = tk.IntVar()
		self.Sc = tk.IntVar()
		self.Li = tk.IntVar()
		self.Ct = tk.IntVar()

		self.statusDict = {'None':self.No, 'Maintaining':self.Ma, 'Imaged':self.Im, 'Crossing':self.St, 
							'Screening':self.Sc, 'Lineaging':self.Li, 'Current tracking':self.Ct}

		ttk.Label(self.addBox, text= 'Experimental Status').grid(row=addBoxRow, sticky='nw', pady=5)
		self.checkFrame = ttk.Frame(self.addBox)

		self.checkFrame.grid(row = addBoxRow, column = 1, sticky = 'w')
		self.NoCheck = ttk.Checkbutton(self.checkFrame, text = 'None', variable = self.No ).grid(row = 0, sticky='w')
		self.MaCheck = ttk.Checkbutton(self.checkFrame, text = 'Maintaining', variable = self.Ma ).grid(row = 1, sticky='w')
		self.ImCheck = ttk.Checkbutton(self.checkFrame, text = 'Imaged', variable = self.Im ).grid(row = 2, sticky='w')
		self.StCheck = ttk.Checkbutton(self.checkFrame, text = 'Crossing', variable = self.St ).grid(row = 3, sticky='w')
		self.ScCheck = ttk.Checkbutton(self.checkFrame, text = 'Screening', variable = self.Sc ).grid(row = 4, sticky='w')
		self.LiCheck = ttk.Checkbutton(self.checkFrame, text = 'Lineaging', variable = self.Li ).grid(row = 5, sticky='w')
		self.CtCheck = ttk.Checkbutton(self.checkFrame, text = 'Currently tracking', variable = self.Ct ).grid(row = 6, sticky='w')

		
		#self.status = tk.StringVar(self.addBox)
		#self.status.set(self.statusls[0]) # default value
		#self.statusMenu = tk.OptionMenu(self.addBox, self.status, *self.statusls)
		#self.statusMenu.grid(row=3, column=1, sticky='w', padx=5)
class PickDateClass(ttk.Frame):
	'''
	Class created by page 1
	Purpose: Allows user to select the day last picked. 
	Note: Date defaults to today first, then the last date selected 
	for following entries.
	'''
	def __init__(self, addBox, controller, addBoxRow):
		ttk.Frame.__init__(self, addBox)
		self.addBox = addBox
		self.controller = controller 

		self.lastPick = tk.StringVar()

		self.pickLabel = ttk.Label(self.addBox, text = 'Last Day Picked:')
		self.pickLabel.grid(row = addBoxRow, column =0 , sticky = 'w')

		self.date = DateEntry(self.addBox,selectmode='day', textvariable = self.lastPick, date_pattern = 'yyyy-MM-dd')
		self.date.grid(row=addBoxRow,column=1,pady=5, sticky = 'w')
class PickEveryClass(ttk.Frame):
	'''
	Class created by page 1
	Purpose: Allows user to specify how often a given strain must be maintained
	Units: Days
	'''
	def __init__(self, addBox, controller, addBoxRow):
		self.addBox = addBox
		self.controller = controller 
		self.every = tk.StringVar(self.addBox)
		self.everyOptions = []
		for i in range(0,15):
			self.everyOptions.append(int(i))
		self.every.set(self.everyOptions[3])

		ttk.Label(self.addBox, text = 'Maintain every').grid(row =addBoxRow, column = 0, sticky = 'nw', pady=5)
		
		self.pickEveryMiniFrame = ttk.Frame(self.addBox)
		self.pickEveryMiniFrame.grid(row = addBoxRow, column = 1, sticky='nw', pady=5)

		self.everyMenu = ttk.OptionMenu(self.pickEveryMiniFrame, self.every, *self.everyOptions).grid(row=0, column=0,sticky='nw')
		ttk.Label(self.pickEveryMiniFrame, text = 'day(s)').grid(row=0, column = 1, sticky='nw')
class NumPlatesClass(ttk.Frame):
	'''
	Class created by page 1
	Purpose: Allow user to specify nuber of plates that are routinely maintained. 
	'''
	def __init__(self, addBox, controller, addBoxRow):
		self.addBox = addBox
		self.controller = controller 
		self.numPlates = tk.StringVar(self.addBox)
		self.numPlatesOptions = []
		for i in range(0,20):
			self.numPlatesOptions.append(int(i))
		self.numPlates.set(self.numPlatesOptions[1])

		ttk.Label(self.addBox, text = 'Number of Plates').grid(row = addBoxRow, column = 0, sticky = 'nw', pady=5)
		
		self.numPlatesMiniFrame = ttk.Frame(self.addBox)
		self.numPlatesMiniFrame.grid(row = addBoxRow, column = 1, sticky='nw', pady=5)

		self.numPlatesMenu = ttk.OptionMenu(self.numPlatesMiniFrame, self.numPlates, *self.numPlatesOptions).grid(row=0, column=0,sticky='nw')
		ttk.Label(self.numPlatesMiniFrame, text = 'plate(s)').grid(row=0, column = 1, sticky='nw')
class LocationClass(ttk.Frame):
	def __init__(self, addBox, controller, addBoxRow): #addBox == parent
		ttk.Frame.__init__(self, addBox)
		self.controller = controller
		self.addBox = addBox
		ttk.Label(self.addBox, text = 'Location').grid(row=addBoxRow, sticky='w', pady=5)
		self.location = ttk.Entry(self.addBox)
		self.location.grid(row=addBoxRow, column=1, sticky='w', padx=5)
class NotesClass(ttk.Frame): #var=self.notes
	'''
	Class created by page 1
	Purpose: Allows user to list notes about the strain.
	'''
	def __init__(self, addBox, controller, addBoxRow): #addBox == parent
		ttk.Frame.__init__(self, addBox)
		self.controller = controller
		self.addBox = addBox
		ttk.Label(self.addBox, text = 'Notes').grid(row=addBoxRow, sticky='w', pady=5)
		self.notes = ttk.Entry(self.addBox)
		self.notes.grid(row=addBoxRow, column=1, sticky='w', padx=5)
### PAGE 2: View Database ###
class Page2(ttk.Frame):
	'''
	Window created by controller window and anchored in notebook frame
	Purpose: Give user an interface to view and edit preveiously 
	added strains in the database. 
	Uses Pandas Table module, allowing for intuitive interaction with dataframe objects
	'''
	def __init__(self, parent, controller):
		ttk.Frame.__init__(self, parent)

		self.parent = parent 
		self.controller = controller
		self.Page2Frame = ttk.Frame(self.parent)
		self.Page2Frame.grid()
		self.Page2Frame.grid_columnconfigure(0, weight=1)
		self.parent.add(self.Page2Frame, text = 'View database strains') #Add tab to NB

		self.dataWin = DataView(self.Page2Frame, self.controller)
 
class DataView(ttk.Frame):
	''' 
	Class called by page 2 class that uses PandasTable
	to map data to an interactive table visualization
	uses getData class from main controller window.
	Data is limited on what is passed through by getData.
	'''
	def __init__(self, parent, controller):
		ttk.Frame.__init__(self, parent)
		self.controller = controller
		self.parent = parent
		self.viewWindow = ttk.Frame(self.parent)
		#self.viewWindow.grid(sticky='nesw')
		#self.viewWindow.grid_columnconfigure(0, weight=1)
		self.viewWindow.pack(fill = 'both', expand=True)
		self.df = self.controller.getData() 
		#print('DataView:', id(self.df), type(self.df))

		self.table = self.pt = Table(self.viewWindow, dataframe = self.df)
		self.pt.show()


	def refresh(self): #To fully refresh, the csv would need to be saved, closed, then opened again and
						# loaded into the table via self.pt.model.df = pd.read_csv('WormStrainsData.csv')
						# Then redrawn again. Shouldn't really be necessary unless multiple users at same time. 
		self.pt.redraw()

### PAGE 3: To-Do ###

class Page3(ttk.Frame):
	'''
	Page called by main controller window. Anchored in the notebook frame.
	Purpose: Display strains that are in need of attention based on 
	days since last picked and maintenance frequency
	'''
	def __init__(self, parent, controller):
		ttk.Frame.__init__(self, parent)
		self.parent = parent 
		self.controller = controller

		self.toDoWin = ttk.Frame(self.parent)
		self.toDoWin.grid(sticky='nesw')
		self.toDoWin.grid_columnconfigure(0, weight=1)
		self.toDoWin.grid_rowconfigure(0, weight=1)
		self.parent.add(self.toDoWin, text='To-Do List', sticky='nesw')


		self.pickBox = ttk.Frame(self.toDoWin, height = 0.85*self.controller.rootHeight, 
												width = 0.6*self.controller.rootWidth)

		self.rightFrame = ttk.Frame(self.toDoWin, height = 0.85*self.controller.rootHeight,
													width = 0.4*self.controller.rootWidth)
		self.eventLogFrame = ttk.LabelFrame(self.rightFrame, text = 'Event Log', style = 'Header.TLabelframe')
		
		self.pickBox.grid(column = 0, row = 0, padx=5, pady = 5, sticky = 'nesw')
		self.pickBox.grid_rowconfigure(0, weight=1)
		self.pickBox.grid_columnconfigure(0, weight=1)
		self.pickBox.grid_propagate(False)
		
		self.rightFrame.grid(column = 1, row = 0, padx=5, pady = 5, sticky = 'nesw')
		self.rightFrame.grid_rowconfigure(0, weight=1)
		self.rightFrame.grid_columnconfigure(0, weight=1)
		self.rightFrame.grid_propagate(False)

		self.eventLogFrame.grid(row = 0, padx=5, pady = 5,sticky = 'nesw')
		self.eventLogFrame.grid_columnconfigure(0, weight = 1)
		self.eventLogFrame.grid_rowconfigure(0, weight = 1)
		self.eventLogFrame.grid_propagate(False)
		

		self.eventLog = tk.Text(self.eventLogFrame, height = 20, background = self.controller.themeColor)#) #Inside frame
		self.eventLog.grid(padx=5, pady = 5,sticky = 'nesw')

		self.childPickFrame = pickList(self.pickBox, self.controller)

		self.weeklyPickFrame = WeeklyPick(self.rightFrame, self.controller)

	def writeTaskEventLog(self, msg):
		
		numlines = int(self.eventLog.index('end - 1 line').split('.')[0])
		self.eventLog['state'] = 'normal'
		if numlines==24:
			self.eventLog.delete(1.0, 2.0)
		if self.eventLog.index('end-1c')!='1.0':
			self.eventLog.insert('end', '\n')
		self.eventLog.insert('end', msg)
		self.eventLog['state'] = 'disabled'

class WeeklyPick(ttk.Frame):
	def __init__(self, parent, controller):
		ttk.Frame.__init__(self, parent)
		self.parent = parent
		self.controller = controller

		self.weeklyPickFrame = ttk.LabelFrame(self.parent, text = 'Weekly Outlook', style = 'Header.TLabelframe')
		self.weeklyPickFrame.grid(row = 1, padx=5, pady = 5,sticky = 'nesw')

		weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
		self.weekdayidx = {}
		#self.weekdaycount = []
		todaywd = datetime.datetime.today().weekday()
		for i in range(todaywd,todaywd+7): #Creates respective list starting at today, ending 6 days from now
			if (i+1) >7:				   #Puts days in order starting with today
				self.weekdayidx[i-7] = 0
			else:
				self.weekdayidx[i] = 0

		self.countsFrame = ttk.Frame(self.weeklyPickFrame)
		self.countsFrame.grid(column = 0, sticky = 'w')
		self.getDayCounts() #Gets weekly counts and overdue count
		myrow = 0
		for key in self.weekdayidx:
			myrow += 1
			if key == 'Overdue':
				ttk.Label(self.countsFrame, text = 'Overdue:').grid(column = 0, row = myrow, sticky = 'e')
				ttk.Label(self.countsFrame, text = self.weekdayidx[key]).grid(column = 1, row = myrow, sticky = 'w')
			else:
				#Day label
				ttk.Label(self.countsFrame, text = weekdays[key]+':').grid(column = 0, row = myrow, sticky = 'e')
				#print(weekdays[key], self.weekdayidx[key])
				
				#Count label
				ttk.Label(self.countsFrame, text = self.weekdayidx[key]).grid(column = 1, row = myrow, sticky = 'w')

		total = 0
		for key in self.weekdayidx:
			total += self.weekdayidx[key]

		self.totalLabel = ttk.Label(self.countsFrame, text = 'Total plates this week: {}'.format(total))
		self.totalLabel.grid(column = 0, columnspan = 2, row = len(self.weekdayidx)+1, sticky = 's', pady = 4)

	def getDayCounts(self):
		self.df = self.controller.viewPage.dataWin.pt.model.df
		self.df.apply(lambda row: (self.calcCounts(row['Remind Date'])), axis=1)

	def calcCounts(self, remindDate):

		self.maxDay = (datetime.datetime.today() + datetime.timedelta(weeks=1)).replace(hour = 0, minute = 0, second = 0, microsecond = 0)
		self.minDay = datetime.datetime.today().replace(hour = 0, minute = 0, second = 0, microsecond = 0)
		dt = self.controller.getDatetime(remindDate)
		if  dt > self.maxDay:
			pass 
		elif dt < self.minDay:
			if 'Overdue' not in self.weekdayidx:
				self.weekdayidx['Overdue'] = 0
				self.weekdayidx['Overdue'] += 1
			else:
				self.weekdayidx['Overdue'] += 1
			
		else:
			self.weekdayidx[dt.weekday()] += 1

class pickList(ttk.Frame):
	'''
	Inner frame structure for to-do list
	Called by page 3 class
	Purpose: Creates nested frame structure that serves as the backbone of 
	the to-do list page.
	Contains template for pick box, descriptions, and interactor buttons. 
	'''
	def __init__(self, parent, controller):
		ttk.Frame.__init__(self, parent)
		self.parent = parent
		self.controller = controller

		self.refineddf = self.refine()
		self.names = self.refineddf['Name'].tolist()
		self.namesVar = tk.StringVar(value = self.names)

		self.pickListFrame = ttk.Frame(self.parent)
		self.pickListFrame.grid(column = 0, sticky = 'nesw')
		self.pickListFrame.grid_columnconfigure(2, weight = 1)
		self.pickListFrame.grid_propagate(False)
		self.pickListFrame.grid_columnconfigure(4, weight = 1)
		self.pickListFrame.grid_rowconfigure(0, weight = 1)

		self.pickListBox = tk.Listbox(self.pickListFrame, height = 10, width = 30, listvariable = self.namesVar, font = (10), selectmode = 'browse', background = self.controller.themeColor)
		self.pickListBox.grid(column = 0, row = 0, sticky = 'nsw', padx=(25,0), pady = (10,0))
		self.pickListBox.bind('<<ListboxSelect>>', lambda a: self.descriptions())

		self.vscroll = ttk.Scrollbar(self.pickListFrame, orient= 'vertical', command = self.pickListBox.yview)
		self.vscroll.grid(column = 1, row = 0, sticky = 'nws', padx=(0,15))
		self.pickListBox['yscrollcommand'] = self.vscroll.set

		#self.descboxborder.grid_columnconfigure(0, weight = 1)
		self.descbox = ttk.LabelFrame(self.pickListFrame, text = 'Description', width = 0.5*self.controller.rootWidth, style = 'Header.TLabelframe')
		self.descbox.grid(column = 2, row = 0, sticky = 'nesw', pady=(5,0))
		self.descbox.grid_columnconfigure(1, weight = 1)




		self.dsmsg = tk.StringVar() #Days since last pick
		self.mfmsg = tk.StringVar() #Picking frequency
		self.dpmsg = tk.StringVar() #date picked
		self.stmsg = tk.StringVar() #strain type
		self.comsg = tk.StringVar() #constructs
		self.exmsg = tk.StringVar() #experimental status
		self.npmsg = tk.StringVar() #Number of plates
		self.lomsg = tk.StringVar() #location
		self.nomsg = tk.StringVar() #notes

		self.dstitle = ttk.Label(self.descbox, text = 'Days Since Last Pick:')
		self.mftitle = ttk.Label(self.descbox, text = 'Maintenance Frequency (Days):')
		self.dptitle = ttk.Label(self.descbox, text = 'Last Date Picked:' )
		self.sttitle = ttk.Label(self.descbox, text = 'Strain Type:')
		self.cotitle = ttk.Label(self.descbox, text = 'Constructs:')
		self.extitle = ttk.Label(self.descbox, text = 'Experimental Status:')
		self.nptitle = ttk.Label(self.descbox, text = 'Number of Plates:')
		self.lotitle = ttk.Label(self.descbox, text = 'Location')
		self.notitle = ttk.Label(self.descbox, text = 'Notes:')

		self.dsdesc = ttk.Label(self.descbox, textvariable = self.dsmsg, wraplength = 175, justify = 'left')
		self.mfdesc = ttk.Label(self.descbox, textvariable = self.mfmsg, wraplength = 175, justify = 'left')
		self.dpdesc = ttk.Label(self.descbox, textvariable = self.dpmsg, wraplength = 175, justify = 'left')
		self.stdesc = ttk.Label(self.descbox, textvariable = self.stmsg, wraplength = 175, justify = 'left')
		self.codesc = ttk.Label(self.descbox, textvariable = self.comsg, wraplength = 175, justify = 'left')
		self.exdesc = ttk.Label(self.descbox, textvariable = self.exmsg, wraplength = 175, justify = 'left')
		self.npdesc = ttk.Label(self.descbox, textvariable = self.npmsg, wraplength = 175, justify = 'left')
		self.lodesc = ttk.Label(self.descbox, textvariable = self.lomsg, wraplength = 175, justify = 'left')
		self.nodesc = ttk.Label(self.descbox, textvariable = self.nomsg, wraplength = 175, justify = 'left')

		self.titles = [self.dstitle, self.mftitle, self.dptitle, self.sttitle, self.cotitle,
						self.extitle, self.nptitle, self.lotitle, self.notitle]
		self.descs = [self.dsdesc, self.mfdesc, self.dpdesc, self.stdesc, self.codesc,
						self.exdesc, self.npdesc, self.lodesc, self.nodesc]

		for i in range(len(self.titles)):
			self.titles[i].grid(row = i, column = 0, sticky = 'ne', pady = 5)
			self.descs[i].grid(row = i, column = 1, sticky = 'nw', pady = 5)


		self.dsmsg.set('')
		self.mfmsg.set('')
		self.dpmsg.set('')
		self.stmsg.set('')
		self.comsg.set('')
		self.exmsg.set('')
		self.npmsg.set('')
		self.lomsg.set('')
		self.nomsg.set('')

		self.snoozeorpick = SnoozePickButtons(self.descbox, self.controller)

	def descriptions(self):

		self.idxs = self.controller.toDoPage.childPickFrame.pickListBox.curselection()
		if len(self.idxs) == 1:

			self.idx = int(self.idxs[0])
			
			self.dsmsg.set(self.refineddf['Days Since'].values[self.idx])
			self.mfmsg.set(self.refineddf['Maintenance Frequency'].values[self.idx])
			self.dpmsg.set(self.refineddf['Date Picked'].values[self.idx])
			self.stmsg.set(self.refineddf['Strain Type'].values[self.idx])
			self.comsg.set(self.refineddf['Constructs'].values[self.idx])
			self.exmsg.set(self.refineddf['Experimental Status'].values[self.idx])
			self.npmsg.set(self.refineddf['Number of Plates'].values[self.idx])
			self.lomsg.set(self.refineddf['Location'].values[self.idx])
			self.nomsg.set(self.refineddf['Notes'].values[self.idx])

		self.controller.toDoPage.childPickFrame.snoozeorpick.snoozeVar.set('Snooze')

	def refine(self):

		"""refine df"""
		self.df2 = self.controller.getStrains() #temporary dataframe
		self.df2.dropna(subset = ['Date Picked'], axis = 0, inplace = True) #If no date picked, then drop it in temp file
		self.df2['Today'] = datetime.datetime.today()
		self.df2['Days Since'] = self.df2.apply(lambda row: (self.calcDaysSince(row['Today'], row['Date Picked'])).days, axis=1)

		self.df2['Ready'] = self.df2.apply(lambda row: (self.calcDaysUntil(row['Today'], row['Remind Date'])), axis = 1)

		pd.to_timedelta(self.df2['Maintenance Frequency'], unit = 'days')

		#self.df2 = self.df2[self.df2['Days Since'] >= self.df2['Maintenance Frequency']]	#Strains where days since is greater than

		self.df2 = self.df2[self.df2['Ready'] == True]

		""" Splitting DFs between old and current. """
		self.df2Old = self.df2[self.df2['Days Since'] > 30]

		self.df2 = self.df2[self.df2['Days Since'] <=30]

		"""Sorting Current and adding old to it after"""
		self.df2.sort_values(['Days Since'], ascending = False, inplace = True)
		self.df2 = self.df2.append(self.df2Old)
		self.df2.drop(labels= ['Date Added','Today'], axis = 1, inplace = True)
		self.df2.fillna('None', inplace = True)

		return self.df2

	def calcDaysSince(self, todayDate, datePicked):
		datePicked = str(datePicked)
		daysSince = todayDate - self.controller.getDatetime(datePicked)
		return daysSince

	def calcDaysUntil(self, todayDate, remindDate):
		#Return boolean if remind date is today?
		remindDate = str(remindDate)
		daysUntil = self.controller.getDatetime(remindDate) - todayDate

		if daysUntil.days < 0: #If daysuntil has passed or is 0
			return True
		else:
			return False

class SnoozePickButtons(ttk.Frame):
	'''
	Class called by pickList class in page 3.
	Contains buttons to control interactors with the to-do list
	'''
	def __init__(self, parent, controller):
		ttk.Frame.__init__(self, parent)
		self.parent = parent
		self.controller = controller 
		self.pt = self.controller.viewPage.dataWin.pt
		#print('SnoozePickButtons:', id(self.pt.model.df), type(self.pt.model.df))

		self.buttonFrame = ttk.Frame(self.parent)
		self.buttonFrame.grid(row = 10, column = 0, columnspan=2, sticky = 'w')

		self.pickedButton = ttk.Button(self.buttonFrame, text = 'Mark as Picked', width = 13, command = lambda: self.pickedRemind())

		self.snoozeList = ['Snooze', '1 Day', '2 Days', '3 Days', '4 Days']
		self.snoozeVar = tk.StringVar()

		self.snoozeVar.set(self.snoozeList[0])
		self.snoozeMenu = ttk.OptionMenu(self.buttonFrame, self.snoozeVar, *self.snoozeList, command = lambda x: self.showSnoozeButton())
		self.deleteButton = ttk.Button(self.buttonFrame, text = 'Delete Strain', width = 13, command = lambda: self.deleteRemind())

		self.pickedButton.grid(row=0, pady=5,padx=(10,15), sticky = 'nw')
		self.snoozeMenu.config(width = 10)
		self.snoozeMenu.grid(row=1, pady=5, padx=(9,0), sticky = 'nw')
		self.deleteButton.grid(row = 2, pady=5, padx=(10,0), sticky = 'nw')
	def showSnoozeButton(self):
		self.snoozeButton = ttk.Button(self.buttonFrame, text = 'Confirm Snooze', width = 13, command = lambda: self.snoozeRemind())
		self.snoozeButton.grid(row=1, column = 1, pady=5, sticky = 'nw')
	
	def pickedRemind(self):
		#Set the pick date and remind date, change days since, save to csv
		#Delete strain from the listbox self.controller.toDoPage.childPickFrame.snoozeorpick.snoozeVar.set('Snooze')
		self.refineddf = self.controller.toDoPage.childPickFrame.refineddf
		self.idxs = self.controller.toDoPage.childPickFrame.pickListBox.curselection()
		if len(self.idxs) == 1:
			self.idx = int(self.idxs[0])

			self.strainName = self.controller.toDoPage.childPickFrame.names[self.idx]
			self.rowNum = self.pt.model.df.index[self.pt.model.df['Name'] == self.strainName].to_list()[0]

			self.newDatePicked = datetime.date.today()
			self.newDateRemind = self.newDatePicked + datetime.timedelta(days = int(self.pt.model.df.at[self.rowNum,'Maintenance Frequency']))
			#print(self.newDateRemind)
			self.pt.model.df.at[self.rowNum,'Date Picked'] = self.newDatePicked
			self.pt.model.df.at[self.rowNum,'Remind Date'] = self.newDateRemind
			#print('pickedRemind:', id(self.pt.model.df), type(self.pt.model.df))
			self.pt.redraw()

			#self.controller.viewPage.dataWin.refresh()
			#self.controller.saveDatabase() #save to csv
			self.controller.toDoPage.writeTaskEventLog(msg = str(datetime.datetime.now().replace(microsecond = 0, second = 0))+': {} Marked as Picked'.format(self.strainName))

			self.controller.toDoPage.childPickFrame.pickListBox.delete(self.idx)
			self.controller.toDoPage.childPickFrame.names.remove(self.strainName)
			self.refineddf.drop(self.refineddf.index[self.refineddf['Name'] == self.strainName], inplace = True)

	def snoozeRemind(self):
		#Keep the old pick date, set new remind date, keep days since save to csv
		#Delete strain from the listbox
		self.refineddf = self.controller.toDoPage.childPickFrame.refineddf
		if self.snoozeVar.get() == 'Snooze':
			return
		self.idxs = self.controller.toDoPage.childPickFrame.pickListBox.curselection()
		if len(self.idxs) == 1:
			self.idx = int(self.idxs[0])

			self.strainName = self.controller.toDoPage.childPickFrame.names[self.idx]
			self.rowNum = self.pt.model.df.index[self.pt.model.df['Name'] == self.strainName].to_list()[0]

			self.newDateRemind = datetime.date.today() + datetime.timedelta(days = int(self.snoozeVar.get()[:1]))
			self.pt.model.df.at[self.rowNum,'Remind Date'] = self.newDateRemind
			#print('snoozeRemind:', id(self.pt.model.df), type(self.pt.model.df))
			self.pt.redraw()
			#self.controller.viewPage.dataWin.refresh()
			#self.controller.saveDatabase() #save to csv
			self.controller.toDoPage.writeTaskEventLog(msg = str(datetime.datetime.now().replace(microsecond = 0, second = 0))+': {} Snoozed for {}'.format(self.strainName, self.snoozeVar.get()))

			self.controller.toDoPage.childPickFrame.pickListBox.delete(self.idx)
			self.controller.toDoPage.childPickFrame.names.remove(self.strainName)
			self.refineddf.drop(self.refineddf.index[self.refineddf['Name'] == self.strainName], inplace = True)

	def deleteRemind(self):

		self.refineddf = self.controller.toDoPage.childPickFrame.refineddf

		self.idxs = self.controller.toDoPage.childPickFrame.pickListBox.curselection()
		if len(self.idxs) == 1:
			self.idx = int(self.idxs[0])

			self.strainName = self.controller.toDoPage.childPickFrame.names[self.idx]
			self.rowNum = self.pt.model.df.index[self.pt.model.df['Name'] == self.strainName].to_list()[0]

			self.pt.model.df.drop(self.refineddf.index[self.refineddf['Name'] == self.strainName], inplace = True)
			#print('deleteRemind:', id(self.pt.model.df), type(self.pt.model.df))
			self.pt.redraw()
			#self.controller.saveDatabase() #save to csv
			self.controller.toDoPage.writeTaskEventLog(msg = str(datetime.datetime.now().replace(microsecond = 0, second = 0))+': {} Deleted from database'.format(self.strainName))

			self.controller.toDoPage.childPickFrame.pickListBox.delete(self.idx)
			self.controller.toDoPage.childPickFrame.names.remove(self.strainName)
			self.refineddf.drop(self.refineddf.index[self.refineddf['Name'] == self.strainName], inplace = True)

###### MENU BAR ########

class MenuBar():
	'''
	Menu bar appears at the top of window.
	Options given are: ABOUT, SAVE, REFRESH, EXIT
	'''
	def __init__(self, parent, controller):

		self.parent = parent 
		self.controller = controller 
		self.menubar = tk.Menu(parent)

		self.fileMenu = tk.Menu(self.menubar, tearoff = 0)
		self.helpMenu = tk.Menu(self.menubar, tearoff = 0)
		self.howToMenu = tk.Menu(self.helpMenu, tearoff = 0)
		self.menubar.add_cascade(label = 'File', menu = self.fileMenu)
		self.menubar.add_cascade(label = 'Help', menu = self.helpMenu)

		
		self.fileMenu.add_command(label = 'Save Database', command = lambda:self.SaveDBComm())
		self.fileMenu.add_command(label = 'Refresh', command = lambda:self.RefreshComm())
		self.fileMenu.add_separator()
		self.fileMenu.add_command(label = 'Exit', command = lambda:self.ExitComm())

		self.helpMenu.add_command(label = 'About', command = lambda:self.AboutComm())
		self.helpMenu.add_cascade(label = 'How to', menu = self.howToMenu)

		self.howToMenu.add_command(label = 'Add Strains', command = lambda: self.addHowTo())
		self.howToMenu.add_command(label = 'View and Edit Strains', command = lambda: self.viewHowTo())
		self.howToMenu.add_command(label = 'View To-Do List', command = lambda: self.toDoHowTo())

		self.parent.config(menu = self.menubar)

	def AboutComm(self):
		tk.messagebox.showinfo('Worm Picker', 'Worm Picker is a fun program.')

	def addHowTo(self):
		msg = ('Type strain information into each textbox and make corresponding selections for attributes such as construct or'+
				'intended location.\nWhen ready, click Enter to input the information into the database.')
		tk.messagebox.showinfo('Worm Picker',msg)
	def viewHowTo(self):
		msg = ('Use the view database tab to see all strains. This tab works similar to an excel file in that pre-existing cells can be changed or mutated.'+
				'\nThough be sure to save your work using the save button in Menu --> File --> Save Database') 
		tk.messagebox.showinfo('Worm Picker', msg)
	def toDoHowTo(self):
		msg = ('If a strain is ready to be picked, it wil show up in the to-do list tab along with any other data about it. Strains are deemed ready to be picked when' +
				'the time since the strain was last picked has surpassed the picking frequency. Use the buttons to clear a strain from the list.'+
				'\nMarking as picked will reset the days since picked while snooze will specify a number of days until you are again reminded.') 
		tk.messagebox.showinfo('Worm Picker', msg)
	
	def SaveDBComm(self):
		self.controller.saveDatabase()
		tk.messagebox.showinfo('Worm Picker', 'Data Saved!')

	def RefreshComm(self):
		#self.controller.viewPage.dataWin.redraw()
		self.df = self.controller.viewPage.dataWin.pt.model.df
		self.df['Date Picked'] = self.df['Date Picked'].apply(lambda x: self.controller.getDatetime(x).date())

		self.df['Remind Date'] = self.df.apply(lambda row: (self.executeRefresh(row['Date Picked'], row['Maintenance Frequency'])), axis = 1)
		self.controller.viewPage.dataWin.pt.redraw()
		self.controller.saveDatabase()

		

	
	def executeRefresh(self, datePicked, maintFreq):
		datePickeddt = self.controller.getDatetime(datePicked)
		newDateRemind = datePickeddt + datetime.timedelta(days = int(maintFreq))
		newDateRemind = newDateRemind.date() 

		return newDateRemind
		

		#Reset Date remind
	def ExitComm(self):
		self.controller.parent.destroy()

		
###### CONTROLLER ######

class ControllerWin(ttk.Frame): 
	'''
	Main controller window called by main(). 
	Also contains multiple functions that affect other classes.
	Creates the notebook frame which the app is anchored in,
	grids three subclasses (arbitrarily named page 1-3).
	Pages are referenced in order of appearance. 
	Menubar created last, which gives options to save, refresh, or exit
	'''
	def __init__(self, parent):

		ttk.Frame.__init__(self, parent)
		self.parent = parent #parent is the root)

		self.rootWidth = 1500
		self.rootHeight = 1000
		self.rootFontSize = 11
		self.rootFont = 'Roboto'
		self.bgColor = 'white'
		self.fgColor = 'black'
		self.themeColor = 'white'##FCDFFC'
		self.parent.geometry('{}x{}'.format(self.rootWidth, self.rootHeight))
		self.parent.resizable(0,0)
		self.style = ThemedStyle(self.parent)
		#self.style.set_theme('breeze')
		#self.style = ttk.Style(parent)
		self.style.theme_use('vista') # *xpnative, winnative, *vista, classic, clam, alt
		self.style.configure('TFrame')
		self.style.configure('TLabelFrame')
		self.style.configure('TButton', font = (self.rootFont, self.rootFontSize))
		self.style.configure('TCheckbutton', font = (self.rootFont, self.rootFontSize))
		self.style.configure('TCombobox', font = (self.rootFont, self.rootFontSize))
		self.style.configure('TEntry', font = (self.rootFont, self.rootFontSize))
		self.style.configure('TLabel', font = (self.rootFont, self.rootFontSize))
		self.style.configure('Header.TLabelframe.Label', font = (self.rootFont, self.rootFontSize+1, 'bold'))
		self.style.configure('TMenuButton', font = (self.rootFont, self.rootFontSize))
		self.style.configure('TNotebook', font = (self.rootFont, self.rootFontSize))
		self.style.configure('Horizontal.TScrollbar', font = (self.rootFont, self.rootFontSize))#, font=('Helvetica', 12))
		self.style.configure('Vertical.TScrollbar')#, font=('Helvetica', 12))#




		self.leftFrame = tk.Frame(self.parent)
		self.leftFrame.grid(column = 0, sticky='nesw')
		self.leftFrame.grid_columnconfigure(0, weight=1)
		self.leftFrame.grid_rowconfigure(0, weight=1)

		self.notebook = ttk.Notebook(self.leftFrame) 
		self.notebook.grid(column = 0,sticky = 'nesw')
		self.notebook.grid_columnconfigure(0, weight=1)
		self.notebook.grid_rowconfigure(0, weight = 1)

		self.viewPage = Page2(self.notebook, self)
		self.entryPage = Page1(self.notebook, self) #Self is the first reference of the omnipotent controller(win)
		self.toDoPage = Page3(self.notebook, self)

		menubar = MenuBar(self.parent, self)

		self.entryMsg = ''
		self.writeEventLog(self.entryMsg)

	def writeEventLog(self, msg):
		
		numlines = int(self.entryPage.eventLog.index('end - 1 line').split('.')[0])
		self.entryPage.eventLog['state'] = 'normal'
		if numlines==24:
			self.entryPage.eventLog.delete(1.0, 2.0)
		if self.entryPage.eventLog.index('end-1c')!='1.0':
			self.entryPage.eventLog.insert('end', '\n')
		self.entryPage.eventLog.insert('end', msg)
		self.entryPage.eventLog['state'] = 'disabled'

	def enterData(self):


		self.strainEntry = 	self.entryPage.strainvar.strain.get()

		if self.strainEntry == None or self.strainEntry == '':

			logMsg = '{}: No strain entered. Data will not be saved.'.format(datetime.datetime.now().replace(second=0, microsecond=0))
			self.writeEventLog(logMsg)
			return

		else:
			self.pickDateEntry = 	self.entryPage.pickDatevar.lastPick.get()
			self.constructEntry = 	self.entryPage.constructsvar.constructs.get()
			self.pickEveryEntry = 	self.entryPage.pickEvery.every.get()
			self.numPlatesEntry = 	self.entryPage.numPlatesvar.numPlates.get()
			self.locationEntry = 	self.entryPage.locationvar.location.get()
			self.notesEntry = 		self.entryPage.notesvar.notes.get()

			typeDict = self.entryPage.typevar.strainTypesDict
			typeEntry = ''
			for key in typeDict:
				boolean = typeDict.get(key).get() #1 = checked, 0 = unchecked
				if boolean == 1:
					if len(typeEntry) > 1: #already word in entry
						typeEntry = typeEntry + ', ' + key
						
					else: #Nothing in string yet
						typeEntry = str(key)
				typeDict.get(key).set(0)

			statusDict= self.entryPage.statusvar.statusDict
			statusEntry = ''
			for key in statusDict:
				boolean = statusDict.get(key).get() #1 = checked, 0 = unchecked
				if boolean == 1:
					if len(statusEntry) > 1: #already word in entry
						statusEntry = statusEntry + ', ' + key
					else: #Nothing in string yet
						statusEntry = str(key)
				else:
					continue
				statusDict.get(key).set(0)


			confirmMsg = 'Add {} to database?\n(Type: {}, Construct: {}, Status: {}'.format(
																							self.strainEntry, 
																							typeEntry, 
																							self.constructEntry, 
																							statusEntry
																							) #For pop up message
			#Create remind date from date picked and maint. freq. 

			try: 
				self.datepicked = datetime.datetime.strptime(self.pickDateEntry, '%m-%d-%Y')

			except ValueError:
				try: 
					self.datepicked = datetime.datetime.strptime(self.pickDateEntry, '%d-%m-%Y')
				except ValueError:
					try:
						self.datepicked = datetime.datetime.strptime(self.pickDateEntry, '%Y-%m-%d')
					except ValueError:
						pass 
			self.remindDateEntry = self.datepicked + datetime.timedelta(days = int(self.pickEveryEntry))
			self.remindDateEntry = self.remindDateEntry.date()


			dataRow = {'Name': self.strainEntry,
					 	'Date Picked': self.pickDateEntry,
						'Date Added': datetime.date.today(),
						'Strain Type': typeEntry,
						'Constructs': self.constructEntry,
						'Experimental Status': statusEntry,
						'Maintenance Frequency':self.pickEveryEntry,
						'Number of Plates': int(self.numPlatesEntry),
						'Location':self.locationEntry,
						'Notes': self.notesEntry,
						'Remind Date': self.remindDateEntry
					}

			self.addRowtoTable(dataRow)
			self.saveDatabase()

			logMsg = '{}: Saved {} to database'.format(datetime.datetime.now().replace(second=0, microsecond=0), self.strainEntry)

			self.writeEventLog(logMsg) #Write message to appear in log

			self.entryPage.strainvar.strain.delete(0, tk.END)
			self.entryPage.locationvar.location.delete(0, tk.END)
			self.entryPage.constructsvar.constructs.delete(0, tk.END)
			self.entryPage.pickEvery.every.set(self.entryPage.pickEvery.everyOptions[3])
			self.entryPage.numPlatesvar.numPlates.set(self.entryPage.numPlatesvar.numPlatesOptions[1])
			self.entryPage.notesvar.notes.delete(0, tk.END)

	def addRowtoTable(self, row):
		self.viewPage.dataWin.pt.model.df = self.viewPage.dataWin.pt.model.df.append(row, ignore_index = True)
		self.viewPage.dataWin.pt.redraw()

	def getData(self):
		self.data = pd.read_csv('WormStrainsData.csv')
		#print('getData:', id(self.data), type(self.data))
		return self.data

	def getDatetime(self, date):
		date = str(date)
		try:
			dtobject = datetime.datetime.strptime(date, '%Y-%m-%d')

		except ValueError:
			try:
				dtobject = datetime.datetime.strptime(date, '%Y/%m/%d')
			except ValueError:
				try:
					dtobject = datetime.datetime.strptime(date, '%m-%d-%Y')
				except ValueError:
					try:
						dtobject = datetime.datetime.strptime(date, '%m/%d/%Y')
					except ValueError:
						try:
							dtobject = datetime.datetime.strptime(date, '%d-%m-%Y')
						except ValueError:
							try:
								dtobject = datetime.datetime.strptime(date, '%d/%m/%Y')
							except ValueError:
								return None
		return dtobject

	def getStrains(self):
		#Scrape strains that are 'pertinent' from local dataframe, located in the viewWin.
		#return shallow copy
		self.it = self.viewPage.dataWin.pt.model.df.copy(deep = False)
		#print('getStrains:', id(self.it), type(self.it))
		return self.it

	def saveDatabase(self):

		self.viewPage.dataWin.pt.model.df.to_csv('WormStrainsData.csv', index = False)

##### END OF CLASSES #####

def initDB():
	
	if path.exists('WormStrainsData.csv') == False:
		msg = 'Creating database'
		fields = ['Name', 'Date Picked', 'Date Added', 'Strain Type', 'Constructs', 'Experimental Status', 'Maintenance Frequency', 'Number of Plates', 'Location', 'Notes', 'Remind Date']
		blankrow = ['Example Strain', '2022-01-01', '2022-01-01', 'Array', 'olaEX3847', 'Crossing', '3', '2', 'Incubator 1, shelf 2', 'Delete this row', '2022-01-04']

		with open('WormStrainsData.csv', 'w') as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerow(fields)
			csvwriter.writerow(blankrow)
			csvfile.close()

		return msg
	else:
		msg = 'Welcome!'
		return msg


def main():
	initDB()
	root = tk.Tk()
	icon = tk.PhotoImage(file = 'icon.png')
	root.iconphoto(True, icon)
	root.title('Worm Picker V3.0-VISTA')
	root.grid_columnconfigure(0, weight = 1)
	ControllerWin(root)
	root.mainloop()


main()