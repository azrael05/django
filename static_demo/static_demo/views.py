from django.shortcuts import render

def static_render(request):
    return render(request,"index.html")