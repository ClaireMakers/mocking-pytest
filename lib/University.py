class University:
    def __init__(self):
        self.subjects_offered = ["English", "French", "Computer Science"]
        self.students_list = []
    
    def admit_student(self, student):
        for subject in self.subjects_offered:
            if student.get_subject() == subject:
                student.accepted_in_uni()
                self.students_list.append(student)

#It's often good practice to abstract this kind of function - it checks something, then you can re-run it a few different times if needed.
    def check_subject_is_on_list(self, major): 
        for subject in self.subjects_offered: 
            if subject == major: 
                return True

        return False

    def update_student_subject(self, student_to_update, major):
        #Hre, it's quite readable - you can see what this function is checking for based on its name, and that it returns a boolean. 
        if self.check_subject_is_on_list(major):
            for student in self.students_list: 
                if student == student_to_update:
                    student.update_subject(major) 
