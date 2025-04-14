from django.conf import settings  # Import Django settings to access MEDIA_URL and MEDIA_ROOT.
from django.contrib import admin  # Import Django's built-in admin site.
from django.urls import path, include  # Import functions to define URL patterns.
from django.conf.urls.static import static  # Import helper function to serve static and media files during development.

# Define URL patterns for the project.
urlpatterns = [
    # This URL pattern maps 'supersecret/' to the admin site.
    # It means that the Django admin interface will be accessible at the /supersecret/ URL.
    path('supersecret/', admin.site.urls),
]

# Append media file serving configuration for development:
# It takes the MEDIA_URL (the base URL for media files) and serves files from MEDIA_ROOT.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Customize the Django admin site text displayed in the browser.
admin.site.site_header = 'Real State Admin'  # The header of the admin interface.
admin.site.site_title = 'Real Estate Admin Portal'  # The title for the admin pages.
admin.site.index_title = 'Welcome to the Real Estate Portal'  # The title on the admin index page.
