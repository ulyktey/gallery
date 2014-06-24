from django.contrib import admin
# Import the UserProfile model individually.
from models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'website', 'admin_image')

admin.site.register(UserProfile, UserProfileAdmin)
