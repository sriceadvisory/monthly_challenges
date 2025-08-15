from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# CHALLENGE DATA: Dictionary storing predefined monthly challenges
# Each key is a month name (lowercase), value is the challenge description
# This could eventually be moved to a database model for better scalability
monthly_challenges = {
    "january": "Eat no meat from 9am - 9pm",
    "february": "Walk for 20 minutes a day",
    "march": "Wake up at 5am",
    "april": "Let's learn Django",
    "may": "Eat no meat from 9am - 9pm",
    "june": "Wake up at 5am",
    "july": "Walk for 20 minutes a day",
    "august": "Eat no meat from 9am - 9pm",
    "september": "Walk for 20 minutes a day",
    "october": "Wake up at 5am",
    "november": "Walk for 20 minutes a day",
    "december": "Eat no meat from 9am - 9pm",
}

# VIEW 1: HOME PAGE - Creates navigation menu for all months
def home(request):
    """
    Displays a homepage with links to all 12 monthly challenges.
    Dynamically generates HTML list with clickable month names.
    Each link uses Django's URL reversing for clean, maintainable URLs.
    """
    list_items = ""  # String to build HTML list items
    months = list(monthly_challenges.keys())  # Get all month names as list

    # Loop through each month and create clickable list item
    for month in months:
        capitalized_month = month.capitalize()  # Format month name for display
        # Use Django's reverse() to generate URL based on URL pattern name
        month_path = reverse("month_challenge", args=[month])
        # Build HTML list item with link
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

    # Wrap all list items in <ul> tags and return as HTTP response
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

# VIEW 2: MONTH BY NUMBER - Redirects numeric month (1-12) to month name
def monthly_challenge_by_number(request, month):
    """
    Handles URLs like /challenges/1/ or /challenges/12/
    Converts month number to month name and redirects to proper URL.
    This creates user-friendly URLs while maintaining flexibility.
    """
    months = list(monthly_challenges.keys())  # Get list of month names
    
    # Validate month number is within valid range (1-12)
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    # Convert month number to month name (subtract 1 for zero-indexing)
    forward_month = months[month - 1]
    
    # Generate proper URL for the month name and redirect
    forward_path = reverse("month_challenge", args=[forward_month])
    return HttpResponseRedirect(forward_path)

# VIEW 3: MONTHLY CHALLENGE - Displays specific month's challenge
def monthly_challenge(request, month):
    """
    Displays the challenge for a specific month.
    Handles both valid months and invalid month names gracefully.
    Returns formatted HTML response with the challenge text.
    """
    try:
        # Look up challenge text for the requested month
        challenge_text = monthly_challenges[month]
        # Format challenge as HTML heading and return
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except KeyError:
        # Handle case where month name doesn't exist in our dictionary
        return HttpResponseNotFound("This month is not supported")