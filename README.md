# worm-picker
A simple app designed for experimental element organization in C. elegans labs. Originally designed for Shroff Lab at NIH/NIBIB
Optimized for Windows Operating Systems. 

worm-notifications.py will NOT run on a non-Windows system. 

____________________________________________________________
# What is a worm-picker?

Worm picker is a simple desktop app built on Python's tkinter module. This app allows the user to keep track of up to thousands of C. elegans experimental strains. Capabilities include: 
1. Adding strains to your database
2. Viewing acute status and information on current strains
3. Determining daily and weekly tasks pertaining to maintenance
4. Notifying users and their team about daily strains to pick, maintain, or experiment.

# Installation

**Modules**

- os (Pre-installed with python)

- tkinter (Pre-installed with python)

- datetime (Pre-installed with python)

- csv

- pandastable

- pandas (Pre-installed with python) 

- tkcalendar 

- pause

- plyer


To install modules: 
1. Navigate to command line (Powershell/Anaconda Prompt on windows or Terminal on Mac OSX)

2. Type: 'pip install [module name here]'



____________________________________________________________
# Usage

To use this package, 

1.	Open the Wormpicker program (wormPickerV2.1.py)
	
    a.	Navigate to the local directory and run ‘python wormPickerV2.1.py’
	
    b. 	Use the File tab for options such as 'Save', 'Refresh', and 'Exit'
	
    c. 	Use the Help tab for options such as 'About' and 'How to' to learn more about the features
		and usage of wormPicker. 
	
2.	To run the notification app (notipick.py) in the background. (Only works on Windows OS)
    a.	Navigate to the local directory and run ‘pythonw.exe .\worm_notifications.py

3.	To close the notification app, open task manager, select python, and ‘end task’
