from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from . forms import (
    RegistrationForm,
    UserAdminChangeForm,
    UserAdminCreationForm
)


User = get_user_model()


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    
    list_display = ['email', 'admin']
    list_filter = ['admin']
    fieldsets = (
        (None, {'fields': (
            'email',
            'username',
            'password',
            )
        }),
        ('Personal Info', {'fields':()}),
        ('Permissions', {'fields': ('admin',)})
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username',
                       'password','password_2') 
        }),
    )
    filter_horizontal = ()
    
    
    


admin.site.register(User, UserAdmin)
    