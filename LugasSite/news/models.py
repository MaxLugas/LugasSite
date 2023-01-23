from django.db import models


class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    content = models.TextField('Content')
    date = models.DateField('Date of publication', auto_now_add=True)
    link = models.URLField('Link to GitHub', default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = "News"
