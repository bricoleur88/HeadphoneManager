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
    context = {'headphone_list': qs}
    return render(request, 'main.html', context)

# 신규 헤드폰 정보 등록 (= create)
# main.html에서 헤드폰 등록 form data를 db에 반영
# reverse() : url 하드코딩 필요없게 함 /main/main
def regHeadphone(request):
    name = request.POST['reg_name']
    serial = request.POST['reg_serial']

    qs = HeadphoneMain(hp_model=name, hp_serial=serial, hp_state='사용가능')
    qs.save()     # db 저장

    return HttpResponseRedirect(reverse('main:main'))

# 선택한 헤드폰의 지급하기 페이지로 이동
def provHeadphone(request, pk):
    return render(request, 'provideHeadphone.html')

# 선택한 헤드폰의 반납하기 페이지로 이동
def retHeadphone(request, pk):
    return render(request, 'returnHeadphone.html')
    
