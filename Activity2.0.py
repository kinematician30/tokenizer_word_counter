import os
import time
import datetime

file_name = "class_attendance"

class_attendance = []
time_in = []

with open(f"{file_name}.txt", 'w+') as file:
	# write the date and time the file was created
	file.write(f"Class Attendance for "
			   f"{datetime.datetime.now()}\n")

	# iterating to ass the student name in the empty list.
	while True:
		name = input("What is your name:")
		timer = time.strftime("%H:%M:%S", time.localtime())
		time.sleep(2)
		if name == "quit":
			break
		else:
			class_attendance.append(name)
			time_in.append(timer)
			continue

	# Iterating to add the student names in the text file
	for n, name, t in zip(range(1, len(class_attendance)+1),
					   class_attendance, time_in):
		file.writelines(f'{n} - {name} at {t}.\n')

	file.write(f"File Saved at: {os.getcwd()}")

