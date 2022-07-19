from django.db import models
import datetime

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    is_teacher = models.BooleanField(default = False)
    is_student = models.BooleanField(default = False)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(
        Student, 
        through='Membership', 
        related_name='sections',
        through_fields=('section', 'student'),
        # blank=True,
    )
    def section_students(self):
        section_students = self.students.all()
        return section_students
    

    def get_memberships(self):
        return Section.students.through.objects.filter(section_id=self.id)

    def __str__(self):
            return self.name


class Membership(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.student.name} -- {self.section.name}'
