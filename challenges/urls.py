from django.urls import path
from . import views  # Import views from the current app directory

# URL ROUTING CONFIGURATION
# This list defines all the URL patterns for the monthly challenges app
# Django matches URLs from top to bottom, so order matters!
urlpatterns = [
    path("", views.home, name="index"),
    path("<int:month>/", views.monthly_challenge_by_number, name="month_by_number"),
    path("<str:month>/", views.monthly_challenge, name="month_challenge"),
]


# URL PATTERN MATCHING LOGIC:
# 1. Empty string "" -> home view (navigation menu)
# 2. Pure numbers like "1" -> monthly_challenge_by_number (redirects to month name)
# 3. Text strings like "january" -> monthly_challenge (shows actual challenge)
#
# The order is crucial because Django stops at the first match.
# If <str:month> came before <int:month>, numbers would be caught as strings!