from django.contrib import admin
from .models import Profile, Activity

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration_minutes', 'timestamp')
    list_filter = ('activity_type',)
    search_fields = ('user__username', 'notes')
