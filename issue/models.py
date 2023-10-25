from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ChartData(models.Model):
    value1 = models.IntegerField(default=0)
    value2 = models.IntegerField(default=0)
    value3 = models.IntegerField(default=0)
    value4 = models.IntegerField(default=0)
    value5 = models.IntegerField(default=0)
    value6 = models.IntegerField(default=0)
    value7 = models.IntegerField(default=0)
    value8 = models.IntegerField(default=0)
    value9 = models.IntegerField(default=0)
    value10 = models.IntegerField(default=0)
    value11 = models.IntegerField(default=0)
    value12 = models.IntegerField(default=0)
    value13 = models.IntegerField(default=0)
    value14 = models.IntegerField(default=0)
    value15 = models.IntegerField(default=0)
    value16 = models.IntegerField(default=0)

    VOTE_CHOICES = [
        ('vote01', 'Vote01'),
        ('vote02', 'Vote02'),
    ]

    vote_type = models.CharField(max_length=10, choices=VOTE_CHOICES)
    category = models.CharField(max_length=10, null=True, blank=True)
    data = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chart_data', null=True, blank=True)

    def __str__(self):
        return f'Vote Type: {self.vote_type}, Value1: {self.value1}, Value2: {self.value2}'