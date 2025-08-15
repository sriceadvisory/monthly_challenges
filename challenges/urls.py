from django.urls import path
from . import views  # Import views from the current app directory

# URL ROUTING CONFIGURATION
# This list defines all the URL patterns for the monthly challenges app
# Django matches URLs from top to bottom, so order matters!
urlpatterns = [
    # PATTERN 1: ROOT/HOME URL - matches empty string after app prefix
    # Example: /challenges/ (if app is mounted at /challenges/)
    # Maps to: views.home function
    # Purpose: Shows navigation menu with all 12 months
    path("", views.home),
    
    # PATTERN 2: NUMERIC MONTH URL - matches integers
    # Example: /challenges/1/, /challenges/12/, etc.
    # <int:month> captures the number and passes it as 'month' parameter
    # Maps to: views.monthly_challenge_by_number function
    # Purpose: Redirects numeric months (1-12) to proper month name URLs
    # Note: No 'name' parameter means this URL can't be reversed by name
    path("<int:month>", views.monthly_challenge_by_number),
    
    # PATTERN 3: NAMED MONTH URL - matches any string
    # Example: /challenges/january/, /challenges/february/, etc.
    # <str:month> captures the string and passes it as 'month' parameter
    # Maps to: views.monthly_challenge function
    # name="month_challenge" allows reverse URL lookup in templates/views
    # Purpose: Displays the actual challenge content for a specific month
    # IMPORTANT: This must come AFTER the <int:month> pattern to avoid conflicts
    path("<str:month>", views.monthly_challenge, name="month_challenge"),
]

# URL PATTERN MATCHING LOGIC:
# 1. Empty string "" -> home view (navigation menu)
# 2. Pure numbers like "1" -> monthly_challenge_by_number (redirects to month name)
# 3. Text strings like "january" -> monthly_challenge (shows actual challenge)
#
# The order is crucial because Django stops at the first match.
# If <str:month> came before <int:month>, numbers would be caught as strings!