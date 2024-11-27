from django.http import JsonResponse
from course import Course
from datetime import datetime

def search_courses(request):
    if request.method == 'POST':
        try:
            # Extract course data from request 
            course_data = request.POST.getlist('courses', [])

            # Create object from request data
            courses = [
                Course(
                    start_time=datetime.strptime(course['start_time'], "%H:%M"),
                    end_time=datetime.strptime(course['end_time'], "%H:%M"),
                    subject=course['subject'],
                    course_number=int(course['course_number']),
                    num_of_credits=int(course['num_credits']),
                    professor=course['professor'],
                    seats_remaining=int(course['seats_remaining']),
                    location=course['location'],
                    description=course['description']
                )
                for course in course_data
            ]

            # Extract filtering parameters
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            professor = request.POST.get('professor')
            course_number = request.POST.get('course_number')
            subject = request.POST.get('subject')
            num_credits = request.POST.get('num_credits')
            location = request.POST.get('location')

            # Apply filters to the courses
            if start_time:
                start_time_dt = datetime.strptime(start_time, "%H:%M")
                courses = [c for c in courses if c.start_time >= start_time_dt]
            if end_time:
                end_time_dt = datetime.strptime(end_time, "%H:%M")
                courses = [c for c in courses if c.end_time <= end_time_dt]
            if professor:
                courses = [c for c in courses if professor.lower() in c.professor.lower()]
            if course_number:
                courses = [c for c in courses if c.course_number == int(course_number)]
            if subject:
                courses = [c for c in courses if subject.lower() in c.subject.lower()]
            if num_credits:
                courses = [c for c in courses if c.num_of_credits == int(num_credits)]
            if location:
                courses = [c for c in courses if location.lower() in c.location.lower()]

            # Serialize filtered courses to dictionaries
            serialized_courses = [
                {
                    "start_time": course.start_time.strftime("%H:%M"),
                    "end_time": course.end_time.strftime("%H:%M"),
                    "subject": course.subject,
                    "course_number": course.course_number,
                    "num_of_credits": course.num_of_credits,
                    "professor": course.professor,
                    "seats_remaining": course.seats_remaining,
                    "location": course.location,
                    "description": course.description,
                }
                for course in courses
            ]

            return JsonResponse({"courses": serialized_courses}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"message": "Invalid request"}, status=405)
