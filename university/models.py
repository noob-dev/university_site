from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='faculties')

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='groups')

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255)
    department = models.ManyToManyField(Department, blank=True, related_name='subjects')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, help_text='+998(99) 999-99-99')
    email = models.EmailField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE, related_name='teachers')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='teachers')
    # Teachers in school maybe manytomany, but professional teachers gonna be masters of one subject, so foreignkey

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, help_text='+998(99) 999-99-99')
    email = models.EmailField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='students')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name='students')
