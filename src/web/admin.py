from django.contrib import admin

from .models import Block, Skill, TeamMember


class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 1


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    model = Block

    list_display = ('name', 'created_at', 'position', 'in_menu')
    list_filter = ('name', 'created_at')

    inlines = []
    skill_inline = [SkillInline, ]
    team_inline = [TeamMemberInline, ]

    def get_inline_instances(self, request, obj=None):
        inline_instances = []
        if not obj:
            return inline_instances

        if obj.skill_list.all():
            inlines = self.skill_inline
        elif obj.team_list.all():
            inlines = self.team_inline
        else:
            inlines = self.inlines

        for inline_class in inlines:
            inline = inline_class(self.model, self.admin_site)
            inline_instances.append(inline)
        return inline_instances


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'icon', 'block')
    list_filter = ('block', )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'photo', 'block')
    list_filter = ('block', )
