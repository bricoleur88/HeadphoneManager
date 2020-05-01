from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from hisdata.models import HeadphoneHistory    # hisdata app DB import

# Create your views here.

# 헤드폰 지급/반납 이력 hisdata에 백업 (검색용)
# provide, returnheadphone.html에서 헤드폰 등록 form data를 db에 추가
def regHeadphone(request):
    name = request.POST['hist_name']
    serial = request.POST['hist_serial']
    pDate = request.POST['hist_pDate']
    pDetail = request.POST['hist_pDetail']
    rDate = request.POST['hist_rDate']
    rDetail = request.POST['hist_Detail']
    receiver = request.POST['hist_receiver']
    checker = request.POST['hist_checker']
    state = request.POST['hist_state']
    

    qs = HeadphoneHistory(hh_model=name, hh_serial=serial, hh_pDate=pDate, hh_pDetail=pDetail, hh_rDate=rDate, hh_rDetail=rDetail, hh_reciever=receiver, hh_checker=checker, hh_state=state)
    qs.save()     # db 저장.. 까지만..
    

# 전체 헤드폰 이력 렌더링
# HeadphoneHistory db 조회
# 검색에 ALL 입력할 경우 전체 조회
# 검색에 지정 serial 입력할 경우 일부 조회
def hisall(request):
    
    search = request.POST['search_serial']
    
    if search == ALL:
        qs = HeadphoneHistory.objects.all()
        context = {'headphone_history': qs}
        return render(request, 'history.html', context)
    else:
        qs = HeadphoneHistory.objects.filter(hh_serial = serial)
        context = {'headphone_historyone': qs}
        return render(request, 'histroy.html', context)
    


