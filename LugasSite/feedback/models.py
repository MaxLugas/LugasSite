from django.db import models


class Feedback(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email', max_length=250)
    content = models.TextField('Feedback')
    date = models.DateField('Feedback date')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
