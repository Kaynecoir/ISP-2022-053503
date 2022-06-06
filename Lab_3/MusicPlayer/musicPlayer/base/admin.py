from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Track, Genre, Listener, UserProfile


# Register your models here.
class UserInline(admin.StackedInline):
    model = Listener
    can_delete = False
    verbose_name_plural = 'Inform'


class UserAdmin(UserAdmin):
    inlines = (UserInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Track)
admin.site.register(Genre)
