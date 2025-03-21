from django.db import models

# Create your models here.
class Question(models.Model):
    CATEGORY_CHOISES = [
        ('math', 'Mathematics'),
        ('verbal', 'Verbal Reasoning'),
        ('spatial', 'Spatial Ability')
    ]

    text = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOISES)
    difficulty = models.IntegerField(default=1)

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text