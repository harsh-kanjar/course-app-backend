from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.title

class Instance(models.Model):
    year = models.PositiveIntegerField()
    semester = models.PositiveIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.title} - {self.year} Semester {self.semester}"
