from django import forms
from . import models


class LoginForm(forms.Form):

    # passwordField는 없습니다
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # 필드 간의 관계 등 다른 validation을 위해서는 clean함수를 사용하자.
    # clean_[필드명] 꼴이 verbose하다고 생각하면 clena으로 한 방에 통합해도 된다.
    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return password
            else:
                # clean 메서드를 사용할 시 어느 필드에서 오류가 났는지 add_error에서 명시해줄 것
                self.add_error("password", forms.ValidationError("password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))
