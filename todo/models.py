from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(default=None)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    class Meta:
        ordering = ["done", "created_at"]

    def __str__(self):
        return f"{self.content} {self.done}"
