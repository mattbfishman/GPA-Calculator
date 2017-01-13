from Tkinter import *
import ttk

gradeDict = {'A' : 4.0,
				'A-' : 3.7,
				'B+': 3.3,
				'B': 3.0,
				'B-': 2.7,
				'C+': 2.3,
				'C': 2.0,
				'C-': 1.7,
				'D+': 1.3,
				'D': 1.0,
				'F': 0.0}

def calculateGPA():
	loop = 0
	gpa = 0
	creditCount = 0
	while(loop <=5):
		grade = StringVar 
		grade = globals()['gradeBox%s' % loop].get()
		credit = StringVar
		credit = globals()['creditBox%s' % loop].get()
		if(grade != '--' and credit != '--'):
			gpa = gpa + (float(gradeDict[grade]) * int(credit))
			creditCount = int(credit) + creditCount
		loop +=1
	gpaValue = gpa/creditCount
	var.set("GPA: " + str(round(gpaValue, 2)))

root = Tk()
root.wm_title("GPA Calculator")
root.resizable(False, False)

sumbitFrame = Frame(root)
sumbitFrame.pack(side=TOP)


count = 0
gpaValue = '0.00'

while(count <= 5):
	globals()['grade%s' % count] = StringVar()
	globals()['gradeLabel%s' % count] = Label(sumbitFrame, textvariable=globals()['grade%s' % count])
	globals()['grade%s' % count].set("Grade: ")
	globals()['gradeLabel%s' % count].grid(row=count, column=1, sticky="w")

	globals()['value%s' % count]  = StringVar()
	globals()['gradeBox%s' % count] = ttk.Combobox(sumbitFrame, textvariable=globals()['value%s' % count])
	globals()['gradeBox%s' % count]['values'] = ('--', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F')
	globals()['gradeBox%s' % count].current(0)
	globals()['gradeBox%s' % count].grid(row=count, column=2, sticky="w")

	globals()['credit%s' % count] = StringVar()
	globals()['creditLabel%s' % count] = Label(sumbitFrame, textvariable=globals()['credit%s' % count])
	globals()['credit%s' % count].set("Credits: ")
	globals()['creditLabel%s' % count].grid(row=count, column=3, sticky="w")

	globals()['creditVal%s' % count]  = StringVar()
	globals()['creditBox%s' % count] = ttk.Combobox(sumbitFrame, textvariable=globals()['creditVal%s' % count])
	globals()['creditBox%s' % count]['values'] = ('--', '1', '2', '3', '4', '5', '6')
	globals()['creditBox%s' % count].current(0)
	globals()['creditBox%s' % count].grid(row=count, column=4, sticky="w")

	count+=1

calulateFrame = Frame(root)
calulateFrame.pack(side=BOTTOM)

var = StringVar()
label = Label(calulateFrame, textvariable=var)
var.set("GPA: " + gpaValue )
label.grid(row=6, column=2, sticky="w")

calculate = Button(calulateFrame, text="Calculate", width=10, command= lambda: calculateGPA())
calculate.grid(row=6, column=1, sticky="w")

mainloop()

