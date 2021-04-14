import tkinter as tk
from tkinter import *
import sqlite3

def quiz():
	login.destroy()
	global quiz
	quiz = Tk()
	quizCanvas = Canvas(quiz, width=720, height=440, bg="black")
	quizCanvas.pack()
	quizFrame = Frame(quizCanvas, bg="white")
	quizFrame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
	header = Label(quizFrame, text="Welcome to Quizz App", bg="white", fg="black")
	header.place(relx=0.4, rely=0.07)
	quiz.mainloop()

def loginPage(userData):
	global login
	signup.destroy()
	login = Tk()
	loginCanvas = Canvas(login, width=720, height=440, bg="blue")
	loginCanvas.pack()
	loginFrame = Frame(loginCanvas, bg="white")
	loginFrame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
	header = Label(loginFrame, text="LogIn Page", bg="white", fg="black")
	header.place(relx=0.4, rely=0.07)
	
	# Username
	unlabel = Label(loginFrame, text="Username: ", bg="white", fg="black")
	unlabel.place(relx=0.1, rely=0.2)
	unEntry = Entry(loginFrame)
	unEntry.place(relx=0.3, rely=0.2)
	# Password
	pwdLabel = Label(loginFrame, text="Password: ", bg="white", fg="black")
	pwdLabel.place(relx=0.1, rely=0.3)
	pwdEntry = Entry(loginFrame, show="*")
	pwdEntry.place(relx=0.3, rely=0.3)
	def verifyUser():
		for fn, un, pw in userData:
			if un == unEntry.get() and pw == pwdEntry.get(): quiz()
		errorLabel = Label(loginFrame, text="Invalid Username and Password!", bg="white", fg="red")
		errorLabel.place(relx=0.1, rely=0.7)
	
	loginButton = Button(loginFrame, text="Login", activebackground="blue", bg="green", command=verifyUser)
	loginButton.place(relx=0.1, rely=0.5)
	
	login.mainloop()

def signUp():
	global signup
	root.destroy()
	signup = Tk()
	signupCanvas = Canvas(signup, width=720, height=440, bg="blue")
	signupCanvas.pack()
	signupFrame = Frame(signupCanvas, bg="white")
	signupFrame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
	header = Label(signupFrame, text="Sign Up Page", bg="white", fg="black")
	header.place(relx=0.4, rely=0.07)

	# Full Name
	fnlabel = Label(signupFrame, text="Full Name: ", bg="white", fg="black")
	fnlabel.place(relx=0.1, rely=0.2)
	fnEntry = Entry(signupFrame)
	fnEntry.place(relx=0.3, rely=0.2)
		
	# Username
	unlabel = Label(signupFrame, text="Username: ", bg="white", fg="black")
	unlabel.place(relx=0.1, rely=0.3)
	unEntry = Entry(signupFrame)
	unEntry.place(relx=0.3, rely=0.3)
	# Password
	pwdLabel = Label(signupFrame, text="Password: ", bg="white", fg="black")
	pwdLabel.place(relx=0.1, rely=0.4)
	pwdEntry = Entry(signupFrame, show="*")
	pwdEntry.place(relx=0.3, rely=0.4)
	
	# adding User to DB
	def addUser():
		full_name = fnEntry.get()
		username = unEntry.get()
		pwd = pwdEntry.get() 
		conn = sqlite3.connect('quiz.db')
		cursor = conn.cursor()
		cursor.execute('CREATE TABLE IF NOT EXISTS user(FULLNAME text, USERNAME text, PASSWORD text)')
		cursor.execute('INSERT INTO user VALUES(?,?,?)',( full_name, username, pwd))
		conn.commit()
		cursor.execute('SELECT * FROM user')
		userData = cursor.fetchall()
		conn.close()
		goToLogin()
	
	signButton = Button(signupFrame, text="SignUp", activebackground="blue", bg="green", command=addUser)
	signButton.place(relx=0.1, rely=0.6)
	loginLabel = Label(signupFrame, text="Already have an Account", bg="white", fg="black")
	loginLabel.place(relx=0.1, rely=0.75)
	loginButton = Button(signupFrame, text="Click Here", activebackground="blue", bg="green", command=goToLogin)
	loginButton.place(relx=0.1, rely=0.80)
	signup.mainloop()

def goToLogin():
	conn = sqlite3.connect('quiz.db')
	cursor = conn.cursor()
	cursor.execute('SELECT * from user')
	userData = cursor.fetchall()
	conn.close()
	loginPage(userData)

def start_app():
	global root
	root = Tk()
	frame = Frame(root, bg="white")
	frame.pack()
	regButton = Button(frame, text="Start", activebackground="blue", bg="green", command=signUp)
	regButton.pack( side = LEFT)
	root.mainloop()
	
if __name__ == "__main__":
	start_app()
	
