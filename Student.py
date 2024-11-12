import random
from course import Course

class Student:
    #Student constructor
    def __init__(self, password: str, full_name: str, email: str, course_list=None, number_of_credits=0, gpa=0.0):
        self.password = password
        self.full_name = full_name
        self.email = email
        self.student_id = self.generateStudentId()
        self.course_list = course_list if course_list is not None else []
        self.number_of_credits = number_of_credits
        self.gpa = gpa
    
    # Generates student ID, called in the student constructor
    @staticmethod
    def generateStudentId():
        return f"S{random.randint(10000, 99999)}"

    # Adds course to course list after signing up
    def addCourse(self, course: Course):
        self.class_list.append(course)
        self.number_of_credits += course.credits

    # allows for updating of gpa outside of object
    def updateGPA(self, new_gpa):
        self.gpa = new_gpa
    
    # formatting for print statements
    def __str__(self):
        courses = ", ".join([course.course_name for course in self.class_list])
        return (f"Student ID: {self.student_id}\n"
                f"Name: {self.full_name}\n"
                f"Email: {self.email}\n"
                f"Number of Credits: {self.number_of_credits}\n"
                f"GPA: {self.gpa}\n"
                f"Courses: {courses}")