class Record:
    def __init__(self, subject_code):
        self.subject_code = subject_code
        self.grades = []
        self.attended_classes = 0
        self.total_classes = 0

    def add_grade(self, grade):
        self.grades.append(grade)

    def mark_attendance(self, is_present):
        self.total_classes += 1
        if is_present:
            self.attended_classes += 1

    def get_average_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_attendance_percentage(self):
        if self.total_classes == 0:
            return 0.0
        return (self.attended_classes / self.total_classes) * 100

    def to_file_format(self):
        """
        Returns only the record data. 
        Manager will handle prepending the student_id when saving.
        """
        grades_str = ",".join(map(str, self.grades))
        return f"{self.subject_code}|{grades_str}|{self.attended_classes},{self.total_classes}"