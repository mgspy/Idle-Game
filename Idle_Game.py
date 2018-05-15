import tkinter
#!/usr/bin/python3

# Start of Idle Clicker Game by Matthieu and Luca
# There might be a few errors. We're kids. Chill out. We still have some work to do.

from tkinter import messagebox
import time

window = tkinter.Tk()
window.title('Idle Clicker Game')

current_clicks = 0

def instructions():
	messagebox.showinfo('Instructions', 'Start by clicking the main button')
	time.sleep(2)
	messagebox.showinfo('Instructions', 'Press the "Add a click" Button to add a click for every other click')
	time.sleep(2)
	messagebox.showinfo('Instructions', 'Press the cursor button to add clicks for you')
	time.sleep(1)
	messagebox.showinfo('Message', 'Have fun!')

def add_click():
	current_clicks = (1 + current_clicks)

def extra_click(number):
	for current_clicks in add_click:
		current_clicks = (current_clicks + number)

def cursor_action():
	while(current_clicks > 0):
		add_click()
		time.sleep(5)

welcome_label = tkinter.Label(window, text='Welcome to the Idle Clicker Game! \n Click the Button to start!')
score_label = tkinter.Label(window, text='Score: '+str(current_clicks))

help_label = tkinter.Label(window, text='Enter For Help')
help_button = tkinter.Button(window, text='Help', command=lambda: instructions())

clicker_button = tkinter.Button(window, text='Click the Button!', command=lambda: add_click())
extra_click = tkinter.Button(window, text='Add a click', command=lambda: extra_click(current_clicks))
cursor = tkinter.Button(window, text='Cursor', command=lambda: cursor_action())

welcome_label.grid(column='2', row='1')
score_label.grid(column='2', row='3')

help_label.grid(column='1', row='4')
help_button.grid(column='2', row='4')

clicker_button.grid(column='2', row='2')
extra_click.grid(column='1', row='2')
cursor.grid(column='3', row='2')

if __name__ == '__main__':
        instructions()
        window.mainloop()
