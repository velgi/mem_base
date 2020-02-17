from django.contrib import admin 
# Register your models here.

from .models import Tags, Memes
from django.utils.safestring import mark_safe

#admin.site.register(Tags)
#admin.site.register(Memes)

@admin.register(Memes)
class MemesAdmin(admin.ModelAdmin):
    list_display = ('image_miniature','name', 'display_tags', 'slug',)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ["image_miniature"]
    
    def image_miniature(self, obj):
        return mark_safe('<img src="{url}" width="100" height="100" />'.format(
            url = obj.meme_image.url,
            )
    )
   

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)
