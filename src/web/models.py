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
    menu_name = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    in_menu = models.BooleanField(default=False)
    content = models.TextField(max_length=2048, default='')

    class Meta:
        ordering = ['position', ]

    def __str__(self):
        return self.name

    @property
    def html_id(self):
        return self.name.replace(' ', '-').lower()


class Skill(PositionMixin):
    block = models.ForeignKey('Block', on_delete=models.SET_NULL, related_name='skill_list', blank=True, null=True)
    name = models.CharField(max_length=32)
    icon = models.FileField(upload_to='skill')
    text = models.TextField(max_length=2048, default='')

    class Meta:
        ordering = ['position', ]

    def __str__(self):
        return self.name

    @property
    def icon_is_svg(self):
        is_svg = False
        try:
            is_svg = self.icon.name.lower().split('.')[-1] == 'svg'
        except Exception as e:
            print(e)
        return is_svg


class TeamMember(PositionMixin):
    block = models.ForeignKey('Block', on_delete=models.SET_NULL, related_name='team_list', blank=True, null=True)
    name = models.CharField(max_length=32)
    photo = models.ImageField(upload_to='team')
    text = models.TextField(max_length=2048, default='')

    class Meta:
        ordering = ['position', ]

    def __str__(self):
        return self.name
