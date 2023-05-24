from django.http import HttpResponse

def hello(request):
    return HttpResponse("The process was successful")

def string(request,name):
    return HttpResponse("Hello"+name+"\n This is string")

def inte(request,name):
    return HttpResponse("Hello"+str(name)+"\n This is integer")

def slug(request,name):
    return HttpResponse("Hello"+name+"\n This is a slug")

def unknown(request,name):
    return HttpResponse("Hello"+str(type(name))+"This can accept amything")