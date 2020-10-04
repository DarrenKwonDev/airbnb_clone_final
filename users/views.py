from django.shortcuts import render
from django.views import View
from . import forms

# Create your views here.
class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)

        # is_valid() : clean()을 전부 통과하면 True 반환
        if form.is_valid():
            # clean()에서 return한 data를 확인할 수 있습니다.
            print(form.cleaned_data)

        return render(request, "users/login.html", {"form": form})


def login_view(request):
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass