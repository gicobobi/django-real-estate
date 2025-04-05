import uuid  # Importing the uuid module for generating unique identifiers.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone  # Provides support for timezone-aware datetimes.
from django.utils.translation import gettext_lazy as _  # For translating strings.
from .managers import CustomUserManager  # Import the custom manager defined earlier.

# Custom User model inheriting from AbstractBaseUser and PermissionsMixin.
class User(AbstractBaseUser, PermissionsMixin):
    # Primary key using BigAutoField (an auto-incrementing integer) for internal database use.
    pkid = models.BigAutoField(primary_key=True, editable=False)
    
    # A UUID field used as a public identifier for the user, generated automatically.
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    # Unique username field with a maximum length of 255 characters.
    username = models.CharField(verbose_name=_('Username'), max_length=255, unique=True)
    
    # Field to store the user's first name (up to 50 characters).
    first_name = models.CharField(verbose_name=_('First Name'), max_length=50)
    
    # Field to store the user's last name (up to 50 characters).
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50)
    
    # Email field used for authentication, must be unique.
    email = models.EmailField(verbose_name=_('Email Address'), unique=True)
    
    # Boolean field to indicate if the user has staff status (access to admin site).
    is_staff = models.BooleanField(default=False)
    
    # Boolean field indicating if the user account is active.
    is_active = models.BooleanField(default=True)
    
    # Field to record when the user joined, defaults to the current time.
    date_joined = models.DateTimeField(default=timezone.now)

    # Field that Django uses as the unique identifier for authentication.
    USERNAME_FIELD = 'email'
    
    # Additional required fields when creating a user via the createsuperuser command.
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  # Note: Likely intended to be REQUIRED_FIELDS

    # Associate the custom manager with this model.
    objects = CustomUserManager()

    class Meta:
        # Human-readable name for the object, singular and plural.
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    # This method returns the string representation of the user.
    def __str__(self):
        return self.username
    
    # Property to get the user's full name, with proper capitalization.
    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"
    
    # Method to get a short name for the user, here it's simply returning the username.
    def get_shot_name(self):
        return self.username
