from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from headphones.models import Headphone

# Create your views here.
def regHeadphone(request):
    return render(request, 'headphones/registerHeadphone.html') # 요 html을 넘기기로 함.. html 만들어야함.

def regConHeadphone(request): # form에서 넘긴 데이터를 받아 record 생성
    name = request.POST['name']
    serial = request.POST['serial']
    
    qs = Headphone(h_name=name, h_serial=serial) #query string 생성, memory에 데이터 올림
    qs.save() # db 저장
    
    return HttpResponseRedirect(reverse('headphones:readheadphoneAll')) # 이제 readheadphoneAll url pattern 만들어야함..

#실제 등록된 모든 유저 보여줌
def readHeadphoneAll(request): 
    qs = Headphone.objects.all()    # query 날려서 db에서 정보 가져와야함
    context = {'headphone_list':qs} # dict type으로 넣어줌 (이 리스트를 html쪽에서 활용)
    return render(request, 'headphones/readHeadphones.html', context) # context 정보도 넘겨주기로 하고.이제 html template 만들어야 함