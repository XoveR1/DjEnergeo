from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey('categories.Category')
    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.name

