from django.contrib import admin

from .models import Block, Skill, TeamMember



class BlockAdmin(admin.ModelAdmin):
    model = Block

    list_display = ('name', 'created_at', 'position', 'in_menu')
    list_filter = ('name', 'created_at', )


admin.site.register(Block, BlockAdmin)
admin.site.register(Skill)
admin.site.register(TeamMember)
