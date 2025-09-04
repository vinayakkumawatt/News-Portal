from django.contrib import admin

from .models import Categories,News,Comment

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

class NewsAdmin(admin.ModelAdmin):
    list_display = ['heading','date','category','photo']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'comment']


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)