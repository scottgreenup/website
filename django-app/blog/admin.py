from blog import models
from django.contrib import admin


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created_at',
        'updated_at',
        'author'
    ]

    fieldsets = (
        (None, {
            'fields': [
                'title',
                'created_at',
                'updated_at',
                'author',
                'content'
            ],
        }),
        (None, {'fields': []})
    )
