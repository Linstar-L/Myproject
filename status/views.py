from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from newuser.models import NewUser
from testapp.models import MyProfile


def user_status(request):
    return render(request, 'user_status.html')


def status_action(request):
    phone = request.POST.get("phone", " ")
    print(phone)
    result = MyProfile.objects.filter(mobile=phone)
    print(result)
    if not result:
        return render(request, 'user_status.html', {"hint": "手机号错误！"})
    result = MyProfile.objects.get(mobile=phone).user
    if result.is_active:
        return render(request, 'user_status.html', {"hint": "会员申请已通过！"})
    else:
        return render(request, 'user_status.html', {"hint": "会员申请尚未通过！"})
