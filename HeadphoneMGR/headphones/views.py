from django.shortcuts import render

# Create your views here.
def regHeadphone(request):
    return render(request, 'headphones/registerHeadphone.html') # 요 html을 넘기기로 함.. html 만들어야함.