from django import forms


class LoginForm(forms.Form):
    """
        登录form 参数验证

        其中参数名称如username必须和html中form表单input的name一致：
            <input name="username" id=...>
    """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
