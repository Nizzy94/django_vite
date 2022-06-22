from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"] = forms.CharField(
            required=True, min_length=3, max_length=15)
        self.fields["last_name"] = forms.CharField(
            required=True, min_length=3, max_length=15)
        # self.fields["district"] = forms.CharField(required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        return user
