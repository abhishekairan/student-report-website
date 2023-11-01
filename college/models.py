from django.db import models
from student.models import only_int


# Create your models here.


class Department(models.Model):
    name = models.CharField("Name",max_length=100)
    dean = models.OneToOneField('Faculty',models.SET_NULL,related_name="departmentDean",null=True)
    hod = models.OneToOneField('Faculty',models.SET_NULL,related_name="departmentHOD",null=True)
    
    def __str__(self) -> str:
        return self.name

class Faculty(models.Model):
    name = models.CharField("Name",max_length=100)
    phone_no = models.CharField("Phone Number",max_length=15 ,validators=[only_int])
    email = models.EmailField("Email",unique=True)
    address = models.TextField("Address")
    department = models.ForeignKey("Department",on_delete=models.SET_NULL,null=True)
    image = models.ImageField("Image",null=True,upload_to='college/image/',blank=True)

    
    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    name = models.CharField("Course",max_length=10)
    duration = models.CharField(
        "Duration",
        choices=[
            ("1","1 Year"),
            ("2","2 Year"),
            ("3","3 Year"),
            ("4","4 Year"),
            ("5","5 Year"),
            ("6","6 Year"),
            ("7","7 Year"),
            ("8","8 Year"),
        ],
        max_length=10
    )
    sems = models.CharField(
        "Semisters",
        choices=[
            ("1","1 Sem"),
            ("2","2 Sem"),
            ("3","3 Sem"),
            ("4","4 Sem"),
            ("5","5 Sem"),
            ("6","6 Sem"),
            ("7","7 Sem"),
            ("8","8 Sem"),
            ("9","9 Sem"),
            ("10","10 Sem"),
            ("11","11 Sem"),
            ("12","12 Sem"),
            ("13","13 Sem"),
            ("14","14 Sem"),
            ("15","15 Sem"),
            ("16","16 Sem"),
        ],
        max_length=10
    )
    course_type = models.CharField(
        "Course Type",
        max_length=50,
        choices={
            ("UG","UG"),
            ("PG","PG"),
            ("PHD","PHD")
        }
    )
    fees = models.IntegerField("Fees")

    def __str__(self) -> str:
        return self.name

