# signup_app/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import csv
import os

# Path to the CSV file
STUDENTS_FILE = os.path.join(os.path.dirname(__file__), 'students.csv')

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        student_id = f"S{str(os.urandom(4).hex())}"

        # Check if username exists by reading CSV file
        if os.path.exists(STUDENTS_FILE):
            with open(STUDENTS_FILE, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['username'] == username:
                        return JsonResponse({'message': 'Username already exists!'}, status=400)

        # Write data to CSV file
        with open(STUDENTS_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Write header if file is empty
            if file.tell() == 0:
                writer.writerow(['fullName', 'email', 'username', 'password', 'studentID', 'courseList', 'numberOfCredits', 'gpa'])
            writer.writerow([full_name, email, username, password, student_id, '[]', 0, 0.0])

        # Redirect to login page (replace with your actual login URL)
        return redirect('/login/')  # Redirect to login page after signup

    return JsonResponse({'message': 'Invalid request'}, status=405)