from django.contrib import admin

from User.models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['name', 'phone', 'email']
