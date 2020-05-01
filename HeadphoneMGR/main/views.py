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

# 1. 선택한 헤드폰의 지급하기 페이지로 이동 
# 2. POST로 들어왔으면, DB 수정하는것으로 보고 if문 타서 DB반영 후 refresh
def provHeadphone(request, pk):
    qs = HeadphoneMain.objects.get(pk=pk)
    
    if request.method == "POST":
        qs.hp_pDate = request.POST['p_date']
        qs.hp_pDetail = request.POST['p_detail']
        qs.hp_receiver = request.POST['receiver']
        qs.hp_checker = request.POST['checker']
        qs.hp_state = request.POST['state']
        qs.save()
        return HttpResponseRedirect(reverse('main:main'))
    
    context = {'provide': qs}
    return render(request, 'provideHeadphone.html', context)

# 1.선택한 헤드폰의 반납하기 페이지로 이동
# 2.POST로 들어왔으면, DB 수정으로 판단하여 main refresh 할 수 있도록
def retHeadphone(request, pk):
    qs = HeadphoneMain.objects.get(pk=pk)
    
    if request.method == "POST":
        qs.hp_rDate = request.POST['r_date']
        qs.hp_rDetail = request.POST['r_detail']
        qs.hp_receiver = request.POST['receiver']
        qs.hp_checker = request.POST['checker']
        qs.hp_state = request.POST['state']
        qs.save()
        return HttpResponseRedirect(reverse('main:main'))
    
    context = {'return': qs}    
    return render(request, 'returnHeadphone.html', context)

# 사용불가 헤드폰 재활성
def changeState(request, pk):
    qs = HeadphoneMain.objects.get(pk=pk)
    qs.hp_state = '사용가능'
    qs.save()
    return HttpResponseRedirect(reverse('main:main'))

# 사용불가 헤드폰 삭제
def delete(request, pk):
    qs = HeadphoneMain.objects.get(pk=pk)
    qs.delete()
    return HttpResponseRedirect(reverse('main:main'))

    
    
    

