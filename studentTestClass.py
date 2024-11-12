import unittest
from Student import Student
from course import Course
from datetime import time

class TestStudent(unittest.TestCase):

    def setUp(self):
        # Set up some sample data for testing
        start1 = time(10,30)
        end1 = time(12,30)
        start2 = time(1,30)
        end2 = time(3,30)
        self.student = Student("password123", "John Doe", "johndoe@example.com")
        self.course1 = Course(start1, end1, "Math", 101, 3, "Mr. Man", 20, "Math Wing", "Introduction to Mathmatics")
        self.course2 = Course(start2, end2, "Science", 102, 3, "Mr. Man", 20, "Science Wing", "Introduction to Science")

    def test_initialization(self):
        # Test the initialization of Student object
        self.assertEqual(self.student.password, "password123")
        self.assertEqual(self.student.full_name, "John Doe")
        self.assertEqual(self.student.email, "johndoe@example.com")
        self.assertIsInstance(self.student.student_id, str)
        self.assertEqual(len(self.student.student_id), 6)
        self.assertEqual(self.student.course_list, [])
        self.assertEqual(self.student.number_of_credits, 0)
        self.assertEqual(self.student.gpa, 0.0)
        print("test_initialize_method: Success")

    def test_generate_student_id(self):
        # Test that student ID is generated in correct format
        student_id = self.student.student_id
        self.assertTrue(student_id.startswith("S"))
        self.assertTrue(student_id[1:].isdigit())
        self.assertEqual(len(student_id), 6)
        print("test_id_method: Success")

    def test_add_course(self):
        # Test adding a course to the student's course list
        self.student.addCourse(self.course1)
        self.assertIn(self.course1, self.student.course_list)
        self.assertEqual(self.student.number_of_credits, 3)
        
        # Add another course and check the number of credits
        self.student.addCourse(self.course2)
        self.assertIn(self.course2, self.student.course_list)
        self.assertEqual(self.student.number_of_credits, 6)
        print("test_add_course_method: Success")

    def test_update_gpa(self):
        # Test updating the student's GPA
        self.student.updateGPA(3.5)
        self.assertEqual(self.student.gpa, 3.5)
        
        # Update GPA again and verify
        self.student.updateGPA(3.8)
        self.assertEqual(self.student.gpa, 3.8)
        print("test_gpa_method: Success")

    def test_student_str_method(self):
        # Test the string representation of the student object
        self.student.addCourse(self.course1)
        self.student.addCourse(self.course2)
        expected_output = (f"Student ID: {self.student.student_id}\n"
                           f"Name: {self.student.full_name}\n"
                           f"Email: {self.student.email}\n"
                           f"Number of Credits: {self.student.number_of_credits}\n"
                           f"GPA: {self.student.gpa}\n"
                           f"Courses: {self.course1.subject} {self.course1.course_number}, {self.course2.subject} {self.course2.course_number}")
        self.assertEqual(str(self.student), expected_output)
        print("test_student_str_method: Success")

    def test_course_str_method(self):
        # Test the string representation of the Course object
        expected_output = (
            "Math 101 - Introduction to Mathmatics\n"
            "Credits: 3\n"
            "Professor: Mr. Man\n"
            "Time: 10:30 to 12:30\n"
            "Location: Math Wing\n"
            "Seats Remaining: 20"
        )
        self.assertEqual(str(self.course1), expected_output)
        print("test_course_str_method: Success")

if __name__ == '__main__':
    unittest.main()
