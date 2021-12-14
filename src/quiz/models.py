from django.db import models

class Question(models.Model):
    body                = models.CharField(max_length=400)
    correctAns          = models.BooleanField(default=True)

    def __str__(self):
        return self.body