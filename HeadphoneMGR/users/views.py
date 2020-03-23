from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.models import User

# Create your views here.
def regUser(request):
    return render(request, 'users/registerUser.html') # 요 html을 넘기기로 함.. 해당 html 만들어야함.

def regConUser(request): # form에서 넘긴 데이터를 받아 record 생성
    name = request.POST['name']
    division = request.POST['division']
    
    qs = User(u_name=name, u_division=division) #query string 생성, memory에 데이터 올림
    qs.save() # db 저장
    
    return HttpResponseRedirect(reverse('users:userAll')) # 이제 userAll url pattern 만들어야함..

#실제 등록된 모든 유저 보여줌
def readUserAll(request): 
    qs = User.objects.all()    # query 날려서 db에서 정보 가져와야함
    context = {'user_list':qs} # dict type으로 넣어줌 (이 리스트를 html쪽에서 활용)
    return render(request, 'users/readUsers.html', context) # context 정보도 넘겨주기로 하고.이제 html template 만들어야 함