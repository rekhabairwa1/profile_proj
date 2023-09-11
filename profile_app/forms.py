from django import forms

class my_form(forms.Form):
    name = forms.CharField()
    father_name = forms.CharField()
    mother_name = forms.CharField()
    email = forms.CharField()
    roll_no = forms.IntegerField()
    stream = forms.CharField()
    address = forms.CharField()
    state = forms.CharField()
    city = forms.CharField()
    pin_code = forms.CharField()
    gender = forms.CharField()
    mobile_no = forms.IntegerField()
    image = forms.ImageField()
    description = forms.CharField()