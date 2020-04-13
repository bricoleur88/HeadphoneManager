from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.models import HeadphoneMain
# Create your views here.

# 전체 헤드폰 리스트 렌더링
# 쿼리 날려 DB에서 정보 가져옴
# dict 타입으로 넣어 이 list를 html쪽에서 활용
# context 정보도 넘겨주어 관련 html template refresh
def main(request):
    qs = HeadphoneMain.objects.all()    
    context = {'headphone_list':qs}
    return render(request, 'main.html', context)    

# 신규 헤드폰 정보 등록
# main.html에서 헤드폰 등록 form data를 db에 반영
def regHeadphone(request):
    name = request.POST['reg_name']
    serial = request.POST['reg_serial']
    
    qs = HeadphoneMain(hp_model=name, hp_serial=serial, hp_pDate='2020-01-01', hp_pDetail='신규등록', hp_rDate='2020-01-01', hp_rDetail='신규등록', hp_receiver='None', hp_checker='None', hp_state='사용가능')
    qs.save() # db 저장
    
    return HttpResponseRedirect(reverse('main:main'))

# 헤드폰 지급하기 버튼액션 시 정보수정
# 쿼리스트링을 받아 dict에 value값으로 context에 저장
def proHeadphoneOne(request, serial):
    qs = HeadphoneMain.objects.get(hp_serial = serial)
    context = {'headphone_info': qs}
    return render(request, 'provideHeadphone.html', context)

# 헤드폰 반납하기 버튼액션 시 정보수정
def retHeadphoneOne(request, serial):
    qs = HeadphoneMain.objects.get(hp_serial = serial)
    context = {'headphone_info': qs}
    return render(request, 'returnHeadphone.html', context)

# 헤드폰 정보 갱신 (기존 데이터를 수정한 입력 정보들로 바꾸어 주는 기능)
def modConHeadphone(request):
    serial = request.POST['serial']
    
    hp_qs = HeadphoneMain.objects.get(hp_serial = serial)
    
    hp_qs.hp_model = model
    hp_qs.hp_serial = serial
    hp_qs.hp_pDate = pDate
    hp_qs.hp_pDetail = pDetail
    hp_qs.hp_rDate = rDate
    hp_qs.hp_rDetail = rDetail
    hp_qs.hp_receiver = receiver
    hp_qs.hp_checker = checker
    hp_qs.hp_state = state
        
    hp_qs.save()
    
    return HttpResponseRedirect(reverse('main:main'))