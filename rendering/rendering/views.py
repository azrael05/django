from django.shortcuts import render

def stat(request):
    return render(request,"index.html")

def dyna(request,name):
    return render(request,"index.html",{"data":name,"list":["pytohn","java","css"],"table":[{"name":"pradeep","phone":9222},{"name":"devesh","phone":111}]})

def if_else(request):
    data={
        "my_list":[1,2,3,4,5,6]
    }
    return render(request,"if_else.html",data)