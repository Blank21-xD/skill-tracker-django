from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='General')
    is_learned = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)

    class Meta:

        ordering = ['-id']

    def __str__(self):
        return self.name
