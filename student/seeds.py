from faker import Faker
import random
from .models import Student
from college.models import Course,Department,Faculty
from student.models import Marks


fake = Faker()

def createStudent(n=10):
    for a in range(n):
        try:
            student_name = fake.name()
            phoneNo = str(random.randint(1000000000,9999999999))
            student_email = fake.email()
            student_address = fake.address()
            course = random.choice(list(Course.objects.all()))
            deparment = random.choice(list(Department.objects.all()))
            student_age = random.randint(17,21)
            student = Student.objects.create(
                name = student_name,
                phone_no = phoneNo,
                email = student_email,
                age = student_age,
                address = student_address,
                course = course,
                department = deparment,
            )
        except Exception as e:
            print(e)
            break

def createFaculty(n=10):
    for a in range(n):
        try:
            Faculty_name = fake.name()
            phoneNo = str(random.randint(1000000000,9999999999))
            Faculty_email = fake.email()
            Faculty_address = fake.address()
            faculty = Faculty.objects.create(
                name = Faculty_name,
                phone_no = phoneNo,
                email = Faculty_email,
                address = Faculty_address
            )
        except Exception as e:
            print(e)
            break

def addMarks():
    for student in Student.objects.all():
        for subject in ['Java','Python','PHP','C','C++']:
            if list(Marks.objects.filter(student_name = student.id).filter(subject_name = subject)) != []:
                print(Marks.objects.filter(student_name = student.id).filter(subject_name = subject))
                pass
            else:
                try:
                    mark = Marks.objects.create(
                        student_name = student,
                        subject_name = subject,
                        mark = random.randint(1,101),
                        totalMarks = 100
                    )
                except Exception as e:
                    print(e)
                    break