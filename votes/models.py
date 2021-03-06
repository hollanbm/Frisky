from django.db import models


class Vote(models.Model):
    label = models.CharField(max_length=200, db_index=True, unique=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'Votes for {self.label}'
