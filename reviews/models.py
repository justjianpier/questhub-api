from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    game = models.ForeignKey(
        'games.Game',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    comment = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        contraints = [
            models.UniqueConstraint(fields=['user', 'game'], name='unique_user_game')
        ]
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.user.username} - {self.game.name} ({self.rating})"