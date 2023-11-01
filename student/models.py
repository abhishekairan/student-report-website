from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def only_int(value: str): 
    if value.isdigit()==False:
        raise ValidationError('Phone Number cannot contain characters')

class Student(models.Model):
    name = models.CharField("Name",max_length=100)
    phone_no = models.CharField("Phone Number",max_length=15 ,validators=[only_int])
    email = models.EmailField("Email",unique=True)
    age = models.IntegerField("Age")
    address = models.TextField("Address")
    course = models.ForeignKey("college.Course",related_name="studentCourse",on_delete=models.SET_NULL,null=True)
    department = models.ForeignKey("college.Department",related_name="studentDepartment",on_delete=models.SET_NULL,null=True)
    image = models.ImageField("Image",null=True,upload_to='student/image/',blank=True)

    
    def __str__(self) -> str:
        return self.name


class Marks(models.Model):
    student_name = models.ForeignKey(Student , on_delete=models.CASCADE)
    subject_name = models.CharField("Subject Name",max_length=50)
    mark = models.IntegerField("Marks Obtained")
    totalMarks = models.IntegerField("Total Marks")

    
    def __str__(self) -> str:
        return self.student_name.name