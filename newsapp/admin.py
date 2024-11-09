from django.contrib import admin
from .models import News, Category


# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ("title","description","image")
    search_fields = (["image"])
    readonly_fields = (["slug"])

admin.site.register(News, NewsAdmin)
admin.site.register(Category)