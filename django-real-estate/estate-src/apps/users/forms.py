from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User  # Import the custom user model from the same app

# Custom form for creating a new user.
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # Specify the model this form will work with.
        model = User
        # Define the fields to include in the user creation form.
        fields = ['email', 'username', 'first_name', 'last_name']
        # Assign a CSS class name for form errors (this can be used in the templates for styling error messages).
        error_class = 'error'

# Custom form for updating an existing user.
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        # Specify the model for which the change form applies.
        model = User
        # Define the fields to include in the user change form.
        fields = ['email', 'username', 'first_name', 'last_name']
        # Assign the same CSS class for errors, ensuring consistency in error styling.
        error_class = 'error'
