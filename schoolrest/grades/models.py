from django.db import models

# Create your models here.
from schools.models import School
from students.models import Student
from standards.models import Standard
from subjects.models import Subject
from commons.models import createdModel, deletedModel


class Grade(createdModel, deletedModel):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    std_id = models.ForeignKey(Standard, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_date = models.DateTimeField()
