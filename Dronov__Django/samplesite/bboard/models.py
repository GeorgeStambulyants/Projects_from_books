from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Product')
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    price = models.FloatField(null=True, blank=True, verbose_name='Price')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Publish date')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubric')

    class Meta:
        verbose_name_plural = 'Declarations'
        verbose_name = 'Declaration'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Name')

    class Meta:
        verbose_name_plural = 'Rubrics'
        verbose_name = 'Rubric'
        ordering = ['name']

    def __str__(self):
        return self.name
