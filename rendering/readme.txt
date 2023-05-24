add templates folder in settings

for rendering we need to use django.shortcut import render

render(request,<path of html>, <other data in dict format if exists>) --> Here key will connect data value to html


for for loop use use { % for i in j %}
for varibles use {{var name}}
for args of for loop use {{forloop.counter, forloop.revcounter0}}
for ending use {% endfor%}

for dictionary we use var.attribute