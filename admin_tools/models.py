from django.db import models
from teachers.models import Teacher
from django.core.validators import MaxLengthValidator


class Department(models.Model):
    # DEPARTMENT_YEAR = ""
    # DEPARTMENT_YEAR = generate_year()
    name = models.CharField(max_length=255, unique=True)
    code = models.PositiveIntegerField(blank=True, null=True)
    head = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, blank=True, null=True)
    establish_date = models.CharField(max_length=4)

    def dept_code(self):
        if not self.code:
            return ""
        return self.code

    def __str__(self):
        return str(self.name)

    def generate_year():
        collage_first_year = 1962
        current_year = 2020
        l = []
        for i in range(collage_first_year, current_year):
            t = (str(i), str(i))
            l = l.append(t)
        return l



class AcademicSession(models.Model):
    year = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return '{} - {}'.format(self.year, self.year + 1)


class Semester(models.Model):
    number = models.PositiveIntegerField(unique=True)
    guide = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, default=None, null=True, blank=True)

    class Meta:
        ordering = ['number', ]

    def __str__(self):
        if self.number == 1:
            return '1st'
        if self.number == 2:
            return '2nd'
        if self.number == 3:
            return '3rd'
        if 3 < self.number <= 12:
            return '%sth' % self.number


class SemesterCombination(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    batch = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['department', 'semester']
        ordering = ['department', 'semester']

    def __str__(self):
        return '%s %s' % (self.semester, self.department)
