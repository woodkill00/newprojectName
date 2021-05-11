from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile
from django.forms import TextInput, Textarea

# Register your models here.

class UserAdminConfig(UserAdmin):
    model = CustomUser
    # readonly_fields = ('id', 'date_joined', 'last_login')
    search_fields = ('email', 'username', 'first_name', 'last_name',)
    list_filter = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_organizer')

    # ordering = ('-start_date', 'username', 'email',)
    ordering = ('email',)
    # ordering = ('email',)
    list_display = ('email', 'username', 'first_name', 'last_name',
                    'is_active', 'is_staff', 'start_date')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_customer','is_staff', 'is_active', 'is_organizer')}),
        # ('Personal', {'fields': ('about',)}),
    )
    # formfield_overrides = {
    #     CustomUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    # }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(CustomUser, UserAdminConfig)
admin.site.register(UserProfile)
# admin.site.register(User, UserAdmin)
