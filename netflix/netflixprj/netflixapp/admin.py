from django.contrib import admin
from .models import Movie, Profile, Video, CustomUser

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'type', 'age_limit')
    search_fields = ('title', 'description')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_limit')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title',)

# If needed, register CustomUser
admin.site.register(CustomUser)