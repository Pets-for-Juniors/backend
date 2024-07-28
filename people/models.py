from django.db import models


# Create your models here.

class CoEditors(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    job_title = models.CharField(max_length=100)
    about_person = models.TextField()
    photo = models.ImageField(upload_to='images/people')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name
