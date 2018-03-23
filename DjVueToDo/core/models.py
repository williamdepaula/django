from django.db import models
from django.core.validators import MinValueValidator

class Todo(models.Model):

	title = models.CharField(max_length=200)
	checked = models.BooleanField(default=False)
	pomodoros = models.IntegerField(default=0, validators=[MinValueValidator(0)])

	def __str__(self):
		return self.title
