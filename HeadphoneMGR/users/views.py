from django.shortcuts import render

# Create your views here.
def regUser(request):
    return render(request, 'users/registerUser.html') # 요 html을 넘기기로 함.. 해당 html 만들어야함.