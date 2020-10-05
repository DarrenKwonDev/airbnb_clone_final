from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
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
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))

        return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect(reverse("core:home"))