from django.shortcuts import render,HttpResponse
def block(request):
    return render(request,"index.html")
def extend(request):
    return render(request,"extend.html")

def home(request):
    return HttpResponse('This is an example of url_name')