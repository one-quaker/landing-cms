from django.db import models


class CreatedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Block(CreatedMixin):
    name = models.CharField(max_length=32)
    position = models.PositiveIntegerField(default=0)
    in_menu = models.BooleanField(default=False)
    content = models.TextField(max_length=2048, default='')

    class Meta:
        ordering = ['position', ]

    def __str__(self):
        return self.name
