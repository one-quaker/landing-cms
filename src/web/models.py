from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField


class CreatedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PositionMixin(models.Model):
    position = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class Block(PositionMixin, CreatedMixin):
    name = models.CharField(max_length=32)
    position = models.PositiveIntegerField(default=0)
    in_menu = models.BooleanField(default=False)
    content = models.TextField(max_length=2048, default='')

    class Meta:
        ordering = ['position', ]

    def __str__(self):
        return self.name

    @property
    def html_id(self):
        return 'block-{}'.format(self.pk)


class Skill(PositionMixin):
    block = models.ForeignKey('Block', on_delete=models.SET_NULL, related_name='skill_list', blank=True, null=True)
    name = models.CharField(max_length=32)
    icon = models.FileField(upload_to='skill')
    content = models.TextField(max_length=2048, default='')

    class Meta:
        ordering = ['position', ]

    def __str__(self):
        return self.name
