from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=False)
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


class Tee(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'{ self.hole.course }_{ self.hole.number }_{ self.description }'

    class Meta:
        ordering = ['hole']


class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f'{ self.description }'

    class Meta:
        ordering = ['updated']


class Round(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    round_number = models.IntegerField()

    def __str__(self):
        return f'{ self.event }_round_{ self.round_number }'

    class Meta:
        ordering = ['updated']


class Score(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    tee = models.ForeignKey(Tee, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f'{ self.round }_{ self.player }_{ self.tee }_{ self.score }'

    class Meta:
        ordering = ['updated']