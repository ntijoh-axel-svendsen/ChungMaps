from django.db import models
from django.contrib.auth.models import User


class MinecraftBlock(models.Model):
    name = models.CharField(max_length=100)
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    dimension = models.CharField(max_length=100)
    metadata = models.JSONField(null=True, blank=True)
    lastModified = models.DateTimeField(auto_now=True, blank=True)
    lastModifiedBy = models.ForeignKey(User, related_name='scanned_blocks', limit_choices_to={'groups__name': "MapScanners"}, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['x', 'y', 'z', 'dimension'], name='unique_block'),
        ]

    def __str__(self):
        return f"{self.name} at ({self.x}, {self.y}, {self.z}) in {self.dimension}"
