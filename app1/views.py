from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def test(request):
    return HttpResponse("测试页面")

def myview(request):
    print("..........................")
    return render(request, 'test.html')
