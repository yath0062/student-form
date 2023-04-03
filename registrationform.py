from tkinter import *
from PIL import ImageTk, Image
import sqlite3
import tkinter.messagebox

root = Tk()
root.geometry("500x650")
root.maxsize(580, 650)
root.minsize(580, 650)

# conn = sqlite3.connect("company.db")
# c = conn.cursor()
# c.execute("Create Table person(name Text, age INT, gen Text)")
# conn.commit()
# conn.close()

# Open a connection to the database
conn = sqlite3.connect('company.db')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='person'")
table_exists = c.fetchone()

if not table_exists:
    c.execute('''CREATE TABLE person
                 (name TEXT, age INTEGER, gen Text)''')
    print("Table 'person' created successfully.")
else:
    print("Table 'person' already exists.")

conn.commit()
conn.close()


def action():
	name = e1.get()
	age = e2.get()
	gen = gender.get()

	conn = sqlite3.connect("company.db")
	c = conn.cursor()
	c.execute("INSERT INTO person VALUES('"+name+"', "+age+", '"+gen+"')")
	tkinter.messagebox.showinfo("Information", "YOUR DATA HAS BEEN SAVED!!")
	conn.commit()
	conn.close()

	# print(name)
	# print(age)
	# print(gen)

def next():
 	nx = Tk()
 	nx.geometry("500x650")
 	nx.maxsize(580, 650)
 	nx.minsize(580, 650)
 	nx.title("Student Registration Records")

 	label = Label(nx, text = "Student Registration Records", font = "time 20 bold", bg = "blue", fg = "white", padx = 17, pady = 20)
 	label.grid(row = 0, column = 0, columnspan = 20)

 	p1 = Label(nx, text = "Name", font = "time 15 bold")
 	p1.grid(row = 1, column = 0, padx = 10, pady = 10)

 	p2 = Label(nx, text = "Age", font = "time 15 bold")
 	p2.grid(row = 1, column = 1, padx = 10, pady = 10)

 	p3 = Label(nx, text = "Gender", font = "time 15 bold")
 	p3.grid(row = 1, column = 2, padx = 10, pady = 10)

 	conn = sqlite3.connect("company.db")
 	c = conn.cursor()
 	c.execute("SELECT * FROM person")
 	r = c.fetchall()

 	num = 2
 	for i in r:

 		name = Label(nx, text = i[0], font = "time 12 bold", fg = "blue")
 		name.grid(row = num, column = 0, padx = 10, pady = 10)

 		age = Label(nx, text = i[1], font = "time 12 bold", fg = "blue")
 		age.grid(row = num, column = 1, padx = 10, pady = 10)

 		gender = Label(nx, text = i[2], font = "time 12 bold", fg = "blue")
 		gender.grid(row = num, column = 2, padx = 10, pady = 10)

 		num = num + 1
 	conn.commit()
 	conn.close()

img = Image.open("1.png")
img = img.resize((100,100))

my = ImageTk.PhotoImage(img)
label = Label(image = my)
label.place(x = 200, y = 10)

l1 = Label(root, text ="student Registration Panel", font = "time 20 bold")
l1.place(x = 75, y = 120)

l2 = Label(root, text = "Enter Name", font = "time 15 bold")
l2.place(x = 30, y = 220)

e1 = Entry(root, width = 30, bd = 3)
e1.place(x = 260, y = 220)

l3 = Label(root, text = "Enter Age", font = "time 15 bold")
l3.place(x = 30, y = 280)

e2 = Entry(root, width = 30, bd = 3)
e2.place(x = 260, y = 280)

l4 = Label(root, text = "Select Your Gender", font = "time 15 bold")
l4.place(x = 30, y = 340)

gender = StringVar()
g1 = Radiobutton(root, text = "Male", variable = gender, value = "Male", font = "time 15")
g1.select()
g1.place(x = 260, y = 340)
g2 = Radiobutton(root, text = "Female", variable = gender, value = "Female", font = "time 15")
g2.place(x = 360, y = 340)
g2.deselect()

button = Button(root, text = "Submit", fg = "white", bg = "blue", font = "time 15 bold", width = "34", command = action)
button.place(x = 32, y = 500)

button2 = Button(root, text = "Show", fg = "white", bg = "red", font = "time 15 bold", width = "16", command = next )
button2.place(x = 32, y = 570)


button3 = Button(root, text = "Exit", fg = "white", bg = "red", font = "time 15 bold", width = "16", command = root.quit)
button3.place(x = 248, y = 570)

root.mainloop()
