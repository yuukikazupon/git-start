from django import forms
from .models import Profile,Keijiban

class KeijibanForm(forms.ModelForm) :
    class Meta :
        model = Keijiban
        fields = "__all__"

class CreateForm(forms.ModelForm):
    class Meta :
        model = Keijiban
        fields = ["toukou","image","created_at"]

class ProfileForm(forms.ModelForm):
    class Meta :
        model = Profile
        fields = ["username","age","sex","address","icon"]
