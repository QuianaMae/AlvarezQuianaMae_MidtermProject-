from django.db import models
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, default='Pending')

    def save(self, *args, **kwargs):
        if self.due_date < timezone.now().date():
            self.status = 'Completed'
        else:
            self.status = 'Pending'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title