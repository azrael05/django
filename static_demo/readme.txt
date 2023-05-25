add STATICFILES_DIRS = [
    BASE_DIR,"static"
]
in the settings
for loading in html use {% load static%} at the top
and for each source "{% static 'the path' %}"


For header and footer
Create two seperat files for header.html and footer.html
To call these form other pages we use {% include "<file name>"%} at the top and bottom for header and footer respectively 
But remember to use {% load static %} for each files which have the tag