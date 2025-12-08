This text file will serve as a guide on how to navigate through the Student Management System (SMS)

1. Directory Tree

student_management_system/ 
├── main.py 
├── models/ 
│   ├── student.py 
│   ├── subject.py 
│   ├── record.py 
│   └── manager.py 
├── data/ 
│   ├── students.txt 
│   ├── subjects.txt 
│   ├── enrollments.txt 
│   └── records.txt        
└── README.md 
└── .gitignore.txt

2. How to run the SMS program

a. Open the main.py file or CMD Terminal
b. If using the terminal, open the program using cd path/to/student_management_system
c. Run the application python main.py

3. Features implemented

a. Student management: Adds new students. System will also check for duplicate IDs or for empty inputs.
b. Subject management: Adds new subjects. System ensure that subject code is alphanumeric.
c. Enrollment management: Enrolls students in subjects and automatically creates a record.
d. Grading management: Adds numerical grades ranged from (0-100). The program will not accept negative numbers or numbers greater than 100.
e. Attendance management: Marks attendance as either Present or Absent and calculates attendance percentage.
f. Reporting system: Generates a detailed text-based performance files:
	i. Students list
	ii. Enrollments list
	iii. Subjects offered list
	iv. Records list

4. How data is stored

All of the data is stored in the data/ directory using plain text files.
The following are the text files with the structure of the contents:
a. students.txt: student ID|name|section
b. subjects.txt: subject code|subject name|credit hours
c. records.txt:  student ID|course ID|grades|attendance
d. enrollments.txt: student ID|subject code

5. Summary of classes
a. Student: Holds arguments for student ID, name, section
b. Subject: Holds arguments for subject code, subject name, subject credit hours.
c. Record: Holds the performance data for a single subject, including grades, averages grades and attendance.
d. SystemManager: Handles file loading and data saving, user input data validation, and Enrolling, Grading, Reporting students and their respective subjects.

