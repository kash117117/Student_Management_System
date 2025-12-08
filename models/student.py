class Student:
    def __init__(self, student_id, name, section):
        self.student_id = student_id
        self.name = name
        self.section = section
        self.enrolled_subjects_count = 0
        # Requirement: Encapsulation - Student owns their records
        self.records = [] 

    def add_record(self, record):
        """Adds a new record to the student's list."""
        self.records.append(record)
        self.enrolled_subjects_count += 1

    def get_record(self, subject_code):
        """Finds a record by subject code."""
        for record in self.records:
            if record.subject_code == subject_code:
                return record
        return None

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Section: {self.section}"
        
    def to_file_format(self):
        return f"{self.student_id}|{self.name}|{self.section}\n"