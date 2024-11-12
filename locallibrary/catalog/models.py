from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.student_id})"

class Course(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    subject = models.CharField(max_length=100)
    course_number = models.IntegerField()
    num_of_credits = models.IntegerField()
    professor = models.CharField(max_length=100)
    seats_remaining = models.IntegerField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name="courses", blank=True)

    def __str__(self):
        return f"{self.subject} {self.course_number} - {self.professor}"
