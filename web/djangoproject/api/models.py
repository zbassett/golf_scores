from django.db import models

class Course(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True, default='')
    number_of_holes = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Hole(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.IntegerField()
    par = models.IntegerField()
    handicap = models.IntegerField(null=True)

    def __str__(self):
        return f'{ self.course }_{ self.number }'

    class Meta:
        ordering = ['number']