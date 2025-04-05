from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUseAdmin  # Import Django's default UserAdmin to extend its functionality.
from django.utils.translation import gettext_lazy as _  # For translating labels.
from .forms import CustomUserChangeForm, CustomUserCreationForm  # Custom forms for user creation and modification.
from .models import User  # Import the custom user model.

# Custom admin class for managing the User model in the Django admin interface.
class UserAdmin(BaseUseAdmin):
    ordering = ['email']  # Order the user list by email.
    
    # Specify the forms to be used in the admin interface.
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    
    model = User  # Associate this admin class with the custom User model.
    
    # Define the fields to display in the list view of the admin interface.
    list_display = ['pkid', 'id', 'email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active']
    
    # Specify which fields should be clickable to navigate to the detail page.
    list_display_links = ['id', 'email']
    
    # Add filters to the right sidebar of the admin list view to filter by these fields.
    list_filter = ['email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active']
    
    # Grouping of fields on the user detail page.
    fieldsets = (
        (
            _('Login Credentials'),  # Section header, translated.
            {
                'fields': ('email', 'password',)  # Fields related to login credentials.
            },
        ),
        (
            _('Personal Information'),
            {
                'fields': ('username', 'first_name', 'last_name')  # Personal information fields.
            },
        ),
        (
            _('Pemissions and Groups'),
            {
                # Fields related to user permissions.
                'fields': ('is_active', 'is_staff', 'is_superuse', 'groups', 'user_permissions')
            },
        ),
        (
            _('Important Dates'),
            {
                'fields': ('last_login', 'date_joined')  # Important dates associated with the user.
            },
        ),
    )
    
    # Define the layout of the fields when creating a new user from the admin.
    add_fieldsets = (
        (
            None, 
            {
                'classes': ('wide',),  # CSS classes to style the form.
                # Fields required when adding a new user.
                'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',),
            },
        )
    )
    
    # Define which fields are searchable in the admin interface.
    search_fields = ['email', 'username', 'first_name', 'last_name']

# Register the custom User model along with the customized admin class.
admin.site.register(User, UserAdmin)
