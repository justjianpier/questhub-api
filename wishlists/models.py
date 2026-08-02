from django.db import models
from django.conf import settings

class Wishlist(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='wishlist'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Wishlist de {self.user.username}"

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(
        Wishlist,
        on_delete=models.CASCADE,
        related_name='items'
    )
    game = models.ForeignKey(
        'game.Game',
        on_delete=models.CASCADE
    )
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['wishlist', 'game'], name='unique_wishlist_game')
        ]
    
    def __str__(self):
        return f"{self.wishlist.user.username} - {self.game.name}"