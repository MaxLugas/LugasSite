from django.db import models


class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    content = models.TextField('Content')
    date = models.DateField('Date of publication', auto_now_add=True)
    file = models.FileField(upload_to='', max_length=250, null=True, default=None, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = "News"
