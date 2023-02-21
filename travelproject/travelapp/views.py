from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
# Create your views here.
def demo(request):
    obj1=Place.objects.all()
    obj2=Team.objects.all()
    return render(request,"index.html",{'result1':obj1, 'result2':obj2})

# def values(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     div=x/y
#     mul=x*y
#
#     return render(request, "about.html", {'result1':add, 'result2':sub, 'result3':div, 'result4': mul})






# def subtraction(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res1=x-y
#     return render(request, "about.html", {'result': res1})
#
# def division(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res2=x/y
#     return render(request, "about.html", {'result': res2})
# def multiplication(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res3=x*y
#
#     return render(request,"about.html",{'result':res3})
#

#
# def contact(request):
#     return HttpResponse('hello am contact')