from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True, null=True, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        if self.parent:
            return f"{self.parent} --> {self.name}"
        return self.name