import uuid
import hashlib
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ChallengeCategory(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField()

    class Meta:
        verbose_name_plural = 'ChallengeCategories'

    def __str__(self):
        return f'{self.name}'


class Challenge(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField(max_length=100)

    description = models.TextField()

    category = models.ForeignKey(ChallengeCategory, on_delete=models.CASCADE, related_name='challenges')

    points = models.IntegerField()

    difficulty = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        default=1
    )

    flag = models.CharField(max_length=32, blank=True, editable=False)


    def save(self, *args, **kwargs):
        if not self.flag:
            random_value = uuid.uuid4()
            self.flag = hashlib.md5(str(random_value).encode()).hexdigest()
        
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.name} ({self.points} points)'
    