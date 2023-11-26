from django.contrib import admin
from .models import artist, album
# Register your models here.

@admin.register(artist)
class artistAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'username')
    search_fields = ('name',)


@admin.register(album)
class albumAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    search_fields = ('name',)