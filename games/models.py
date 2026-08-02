from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    metacritic_score = models.IntegerField(null=True, blank=True)
    background_image = models.URLField(blank=True)
    genres = models.ManyToManyField('categories.Category', related_name='games')
    developers = models.ManyToManyField('developers.Developer', related_name='games')
    platforms = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
