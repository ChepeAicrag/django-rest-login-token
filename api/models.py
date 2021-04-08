from django.db import models

# Create your models here.

class Person(models.Model):

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100, verbose_name = 'Name')
    last_name = models.CharField(max_length = 200, verbose_name = 'Last name')

    def __str__(self):
        return self.name
        #return '{0}, {1}'.format(self.last_name, self.name)