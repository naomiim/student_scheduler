from datetime import datetime

class Course:
    def __init__(self, start_time: datetime, end_time: datetime, subject: str, course_number: int, num_of_credits: int, professor: str, seats_remaining: int, location: str, description: str):
        self.start_time = start_time
        self.end_time = end_time
        self.subject = subject
        self.course_number = course_number
        self.num_of_credits = num_of_credits
        self.professor = professor
        self.seats_remaining = seats_remaining
        self.location = location
        self.description = description

    def __str__(self):
        return (f"{self.subject} {self.course_number} - {self.description}\n"
                f"Credits: {self.num_of_credits}\n"
                f"Professor: {self.professor}\n"
                f"Time: {self.start_time.strftime('%H:%M')} to {self.end_time.strftime('%H:%M')}\n"
                f"Location: {self.location}\n"
                f"Seats Remaining: {self.seats_remaining}")