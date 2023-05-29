------------------------------Static Folder
add STATICFILES_DIRS = [
    BASE_DIR,"static"
]
in the settings
for loading in html use {% load static%} at the top
and for each source "{% static 'the path' %}"


--------------------------------For header and footer
Create two seperat files for header.html and footer.html
To call these form other pages we use {% include "<file name>"%} at the top and bottom for header and footer respectively 
But remember to use {% load static %} for each files which have the tag

---------------------------------For extends
Able to insert a block of data into a webpage 
Create  a base html where data from block is inserted wnad inlcude the header and footer files, betweeen them insert a target block
{% block <block_name>%}
<content>
{% endblock %}

Now if you want to add data from another html to this in that html write
{% extends <block_html_name>.html%}
{% block block_name %}
<content>
{% endblock}

So now we can use the block_name.html to create webpages for our other webpages by simplying extending their content.



----------------------------------Url templates
in the url.py assign name for the Path by adding arg name
now if you want to link to this path you can use href={% url '<name>' %}
