import uuid
from django.db import models


class ArticleCategory(models.Model):
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name_plural = 'ArticleCategories'

    def __str__(self):
        return f'{self.name}'



class Article(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    name = models.CharField(max_length=100)

    description = models.TextField()

    content = models.TextField(default='')

    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return f'({self.category}) {self.name}'