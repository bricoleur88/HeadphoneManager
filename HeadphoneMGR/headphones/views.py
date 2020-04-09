from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from headphones.models import Headphone

# Create your views here.

# 헤드폰 등록
# 이거 정의하고 html을 넘기기로 함 html 만들어야함
def regHeadphone(request):
    return render(request, 'headphones/registerHeadphone.html')


# form에서 넘긴 데이터를 받아 record 생성
# query string 생성, memory에 데이터 올림
# 정의 하고 readheadphoneAll url pattern 만들어야함
def regConHeadphone(request): 
    name = request.POST['name']
    serial = request.POST['serial']
    
    qs = Headphone(h_name=name, h_serial=serial) 
    qs.save() # db 저장
    
    return HttpResponseRedirect(reverse('headphones:readheadphoneAll')) 


# 등록된 헤드폰 목록 렌더링
# query 날려서 db에서 정보 가져와야함
# dict type으로 넣어줌 (이 리스트를 html쪽에서 활용)
# context 정보도 넘겨주기로 하고.이제 html template 만들어야 함
def readHeadphoneAll(request): 
    qs = Headphone.objects.all()    
    context = {'headphone_list':qs} 
    return render(request, 'headphones/readHeadphones.html', context)

# 헤드폰 정보 보기
def detHeadphone(request, name):
    qs = Headphone.objects.get(h_name = name)
    context = {'headphone_info': qs}
    return render(request, 'headphones/detailHeadphone.html', context)

# 헤드폰 정보 수정
def readHeadphoneOne(request, name):
    qs = Headphone.objects.get(h_name = name)
    context = {'headphone_info': qs}
    return render(request, 'headphones/modifyHeadphone.html', context)

# 헤드폰 정보 갱신 (기존 데이터를 수정한 입력 정보들로 바꾸어 주는 기능)
def modConHeadphone(request):
    name = request.POST['name']
    serial = request.POST['serial']
    
    h_qs = Headphone.objects.get(h_name = name)
    
    h_qs.h_name = name
    h_qs.h_serial = serial
    
    h_qs.save()
    
    return HttpResponseRedirect(reverse('headphones:readheadphoneAll'))

# 헤드폰 정보 삭제
def delConHeadphone(request, name):
    qs = Headphone.objects.get(h_name = name)
    qs.delete()
    
    return HttpResponseRedirect(reverse('headphones:readheadphoneAll'))
    