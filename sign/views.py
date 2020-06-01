from django.shortcuts import render, get_object_or_404

# Create your views here.
from app1.models import MeetingApp


def meeting_sign(request):
    return render(request, 'meeting_sign.html')


def sign_action(request):
    name = request.POST.get("name", " ")
    phone = request.POST.get("phone", " ")
    # print(phone)
    result = MeetingApp.objects.filter(mobile=phone, name=name)
    # print(result)
    if not result:
        return render(request, 'meeting_sign.html', {"hint": "姓名或手机号错误！"})
    result = MeetingApp.objects.get(mobile=phone)
    if result.sign == '1':
        return render(request, 'meeting_sign.html', {"hint": "用户已签到！"})
    else:
        MeetingApp.objects.filter(mobile=phone, name=name).update(sign='1')
        return render(request, 'meeting_sign.html', {"hint": "签到成功！"})

# Create your views here.
