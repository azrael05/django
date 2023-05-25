add STATICFILES_DIRS = [
    BASE_DIR,"static"
]
in the settings
for loading in html use {% load static%} at the top
and for each source "{% static 'the path' %}"