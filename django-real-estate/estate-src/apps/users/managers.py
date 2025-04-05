from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

# Custom manager for handling user creation
class CustomUserManager(BaseUserManager):

    # Helper method to validate email address
    def email_validator(self, email):
        try:
            # Django's built-in email validation function
            validate_email(email)
        except ValidationError:
            # If validation fails, raise a ValueError with an appropriate message
            raise ValueError(_('You must provide a valid email address'))
        
    # Method to create a standard user
    def create_user(self, username, first_name, last_name, email, password, **extra_fields):
        # Ensure the username is provided
        if not username:
            raise ValueError(_('User must submit a username'))
        # Ensure the first name is provided
        if not first_name:
            raise ValueError(_('User must submit a first name'))
        # Ensure the last name is provided
        if not last_name:
            raise ValueError(_('User must submit a last name'))
        
        # Email is required; if provided, normalize and validate it
        if email:
            email = self.normalize_email(email)  # Convert the domain part to lowercase, etc.
            self.email_validator(email)
        else:
            # Raise error if email is missing
            raise ValueError(_('Base User Account: An email address is required'))

        # Create an instance of the user model with the provided fields and any extra fields
        user = self.model (
            username=username, 
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        # Set the user's password (this method hashes the password)
        user.set_password(password)
        # Set default values for staff and superuser status if not provided
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        # Save the user instance to the database using the specified database
        user.save(using=self._db)
        return user
    
    # Method to create a superuser (administrator)
    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):
        # Ensure superuser-specific fields are set to True
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # Validate that is_staff is True for a superuser
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superusers must have is_staff=True'))
        
        # Validate that is_superuser is True for a superuser
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superusers must have is_superuser=True'))
        
        # Ensure a password is provided
        if not password:
            raise ValueError(_('Superusers must have a password'))
        
        # Process and validate email just as in create_user
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('Admin Account: An email address is required'))

        # Create the user by calling create_user with the provided and extra fields
        user = self.create_user(
            username, 
            first_name,
            last_name,
            email,
            password,  # Ensure the password is passed along
            **extra_fields
        )
        # Save the superuser instance
        user.save(using=self._db)
        return user
