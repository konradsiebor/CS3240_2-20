from django import forms


class CreateForm(forms.Form):
    image1 = forms.ImageField()
    title = forms.CharField()
    organization = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    description = forms.CharField()
    category = forms.CharField()
    goal = forms.DecimalField()
    length = forms.IntegerField()
