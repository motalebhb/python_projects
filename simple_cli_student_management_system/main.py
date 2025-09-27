from university import University
from student import Student

# Create a University object
versity = University("ADUST")

# Ask the user what they want to do
action = input("What do you want to do? (insert/retrieve/update/delete): ").strip().lower()


if action == "insert":
    # Take student information from user
    studentId = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ").strip()
    age = int(input("Enter Student Age: "))

    # Create Student object
    student = Student(studentId, name, age)

    # Add student to university
    versity.addStudent(student)
    print("Student has been inserted successfully.")

elif action == "retrieve":
    # Display all student data
    print("Fetching student records from the database...\n")
    versity.displayInfo()
elif action == "update":
    versity.updateStudentData()
    print("Student has been updated successfully.")
elif action == "delete":
    versity.deleteStudentData()
else:
    # Invalid input
    print("Invalid option. Please type 'insert' or 'retrieve'.")
