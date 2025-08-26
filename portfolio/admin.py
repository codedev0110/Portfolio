from django.contrib import admin
from .models import Project, Experience, Profile

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'featured', 'created_at')
    list_filter = ('featured', 'created_at')
    search_fields = ('title', 'technologies')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'type', 'start_date', 'current')
    list_filter = ('type', 'current')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')