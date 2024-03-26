from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models

admin.site.register(models.CustomUser)


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_cover', 'desc', 'type', 'age_limit')
    list_display_links = ('title', )
    filter_horizontal = ('video', )

    @admin.display(description='Обложка')
    def get_cover(self, obj: models.Movie):
        return mark_safe(f'<img src="{obj.cover.url}" width="100px">')


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('content', )


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_limit')
