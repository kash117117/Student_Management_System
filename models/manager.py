import os
from models.student import Student
from models.subject import Subject
from models.record import Record

class SystemManager: #this is the main manager class that handles all operations by utilizing other classes such as Student, Subject, and Record
    def __init__(self):
        self.students = []
        self.subjects = []
        
        self.DATA_DIR = "data" #this is the directory where all text files will be stored
        self.FILE_STUDENTS = os.path.join(self.DATA_DIR, "students.txt") #in this section, file paths for students, subjects, records, and enrollments are defined
        self.FILE_SUBJECTS = os.path.join(self.DATA_DIR, "subjects.txt")
        self.FILE_RECORDS = os.path.join(self.DATA_DIR, "records.txt")
        self.FILE_ENROLLMENTS = os.path.join(self.DATA_DIR, "enrollments.txt")


        if not os.path.exists(self.DATA_DIR):
            os.makedirs(self.DATA_DIR)

        self.load_data()

    def load_data(self): #this loads data from student, subject, and record text files into the system
        if os.path.exists(self.FILE_STUDENTS):
            with open(self.FILE_STUDENTS, "r") as f:
                for line in f:
                    if line.strip():
                        parts = line.strip().split("|") #using a | delimiter to separate data
                        if len(parts) >= 3:
                            self.students.append(Student(parts[0], parts[1], parts[2]))
        
        if os.path.exists(self.FILE_SUBJECTS):
            with open(self.FILE_SUBJECTS, "r") as f:
                for line in f:
                    if line.strip():
                        parts = line.strip().split("|")
                        if len(parts) >= 3:
                            self.subjects.append(Subject(parts[0], parts[1], int(parts[2])))

        if os.path.exists(self.FILE_RECORDS):
            with open(self.FILE_RECORDS, "r") as f:
                for line in f:
                    if line.strip():
                        parts = line.strip().split("|") 
                        if len(parts) >= 4:
                            s_id = parts[0]
                            subject_code = parts[1]
                            
                            student = self.find_student(s_id)
                            if student:
                                rec = Record(subject_code)
                                
                                if parts[2]: 
                                    grade_list = parts[2].split(",")
                                    rec.grades = [float(g) for g in grade_list]
                                
                                att_parts = parts[3].split(",")
                                if len(att_parts) == 2:
                                    rec.attended_classes = int(att_parts[0])
                                    rec.total_classes = int(att_parts[1])
                                
                                student.add_record(rec)
                            
        print("Data loaded successfully.")

    def save_data(self): #this section saves data in the text files for students, subjects, records, and enrollments
        """Saves all lists to text files."""
        with open(self.FILE_STUDENTS, "w") as f:
            for s in self.students:
                f.write(s.to_file_format())
        with open(self.FILE_SUBJECTS, "w") as f:
            for sub in self.subjects:
                f.write(sub.to_file_format())
        with open(self.FILE_RECORDS, "w") as f:
            for s in self.students:
                for r in s.records:
                    f.write(f"{s.student_id}|{r.to_file_format()}\n")
        with open(self.FILE_ENROLLMENTS, "w") as f:
            for s in self.students:
                for r in s.records:
                    f.write(f"{s.student_id}|{r.subject_code}\n")
        
        print("\n>> All data saved to 'data/' folder.")

    def find_student(self, student_id): #this function finds a student by their ID
        for s in self.students:
            if s.student_id == student_id: #if the student ID matches the input 
                return s
        return None

    def find_subject(self, subject_code): #finds a subject by its code
        for s in self.subjects:
            if s.subject_code == subject_code: #if subject code matches then input code
                return s
        return None

    def add_student(self):
        print("\n--- Add New Student ---")
        
        s_id = input("Enter Student ID: ").strip()
        if not s_id:
            print("Error: Student ID cannot be empty.")
            return
        if self.find_student(s_id):
            print("Error: Student ID already exists.")
            return

        name = input("Enter Name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            return

        section = input("Enter Section: ").strip()
        if not section:
            print("Error: Section cannot be empty.")
            return

        self.students.append(Student(s_id, name, section))
        print(f"Student '{name}' added successfully!")

    def add_subject(self): #subject must be alphanumeric
        print("\n--- Add New Subject ---")
        code = input("Enter Subject Code (Must contain Letters & Numbers): ").strip()
        
        if not code.isalnum():
            print("Error: Subject Code must be alphanumeric (no symbols).")
            return
        
        has_letter = any(c.isalpha() for c in code)
        has_number = any(c.isdigit() for c in code)
        
        if not (has_letter and has_number):
            print("Error: Invalid Format. Code must have BOTH letters and numbers (e.g. CS101).")
            return

        if self.find_subject(code):
            print("Error: Subject Code already exists.")
            return
            
        name = input("Enter Subject Name: ").strip()
        
        try:
            credits = int(input("Enter Credit Hours: ").strip())
            self.subjects.append(Subject(code, name, credits))
            print(f"Subject '{name}' added successfully!")
        except ValueError:
            print("Error: Credit hours must be a number.")

    def view_all_students(self):
        print("\n--- List of All Students ---")
        if not self.students:
            print("No students found.")
        else:
            for s in self.students:
                print(s)

    
    def enroll_student(self): #enrolls a student in a subject based on student ID and subject code
        print("\n--- Enroll Student ---")
        s_id = input("Enter Student ID: ").strip()
        student = self.find_student(s_id)
        if not student:
            print("Error: Student not found.")
            return

        code = input("Enter Subject Code: ").strip()
        if not self.find_subject(code):
            print("Error: Subject not found.")
            return

        if student.get_record(code):
            print("Error: Student is already enrolled in this subject.")
            return

        new_record = Record(code)
        student.add_record(new_record)
        print("Student enrolled successfully!")

    def add_grade(self):
        print("\n--- Add Grade ---")
        s_id = input("Enter Student ID: ").strip()
        student = self.find_student(s_id)
        if not student:
            print("Error: Student not found.")
            return
            
        code = input("Enter Subject Code: ").strip()
        record = student.get_record(code)
        
        if not record:
            print("Error: No enrollment record found for this student/subject.")
            return

        try:
            grade = float(input("Enter Grade (0-100): ").strip())
            
        
            if grade < 0 or grade > 100: #ensures grade is between 0 and 100
                print("Error: Grade must be between 0 and 100.")
                return
            

            record.add_grade(grade)
            print(f"Grade {grade} added successfully.")
        except ValueError:
            print("Error: Grade must be a number.")

    def mark_attendance(self):
        print("\n--- Mark Attendance ---")
        s_id = input("Enter Student ID: ").strip()
        student = self.find_student(s_id)
        if not student:
            print("Error: Student not found.")
            return

        code = input("Enter Subject Code: ").strip()
        record = student.get_record(code)

        if not record:
            print("Error: No enrollment record found.")
            return
        
        status = input("Is student present? (y/n): ").strip().lower()
        if status == 'y':
            record.mark_attendance(True)
            print("Marked as Present.")
        elif status == 'n':
            record.mark_attendance(False)
            print("Marked as Absent.")
        else:
            print("Invalid input. Use 'y' for present or 'n' for absent.")

    def view_student_report(self):
        print("\n" + "="*50)
        print("                 STUDENT REPORT                  ")
        print("="*50)
        
        s_id = input("Enter Student ID: ").strip()
        student = self.find_student(s_id)
        
        if not student:
            print("Error: Student not found.")
            return

        print(f"\n[ STUDENT DETAILS ]")
        print(f"Name:    {student.name}")
        print(f"ID:      {student.student_id}")
        print(f"Section: {student.section}")
        print("-" * 50)
        
        if not student.records:
            print("No enrolled subjects found.")
            print("=" * 50)
            return

        total_average = 0
        subject_count = 0
        
        print(f"{'CODE':<10} | {'SUBJECT':<15} | {'AVG GRADE':<10} | {'ATTENDANCE':<10}")
        print("-" * 50)

        for r in student.records:
            subject = self.find_subject(r.subject_code)
            subj_name = subject.subject_name if subject else "Unknown"
            
            avg = r.get_average_grade()
            att_pct = r.get_attendance_percentage()
            
            print(f"{r.subject_code:<10} | {subj_name:<15} | {avg:<10.1f} | {att_pct:<9.1f}%")
            
            total_average += avg
            subject_count += 1

        print("-" * 50)
        
        overall_gpa = total_average / subject_count if subject_count > 0 else 0.0 #calculates overall GPA based on average grades and subject count
        
        print(f"\n[ OVERALL PERFORMANCE SNAPSHOT ]")
        print(f"Total Subjects: {subject_count}")
        print(f"Overall Average: {overall_gpa:.2f}")
        
        if overall_gpa >= 80:
            status = "Excellent"
        elif overall_gpa >= 60:
            status = "Good"
        elif overall_gpa >= 50:
            status = "Average"
        else:
            status = "Needs Improvement"
        print(f"Performance Status: {status}")
        print("=" * 50)