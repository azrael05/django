add templates folder in settings

for rendering we need to use django.shortcut import render

render(request,<path of html>, <other data in dict format if exists>) --> Here key will connect data value to html


for for loop use use { % for i in j %}
for varibles use {{var name}}
for args of for loop use {{forloop.counter, forloop.revcounter0}}
for ending use {% endfor%}

for dictionary we use var.attribute

for if else we use {% if condition sign value %}
all must be sepeated by space eg i <= 2 need to be used not i<=2 
for ending if loop we use {% endif %}

for if else 
{% if statement %}
    things that would happen if true
{% else %}
    THINGS FOR ELSE statement
{% endif %}