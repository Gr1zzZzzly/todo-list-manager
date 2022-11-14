from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    def __str__(self):
        return f"{self.content} {self.done}"
