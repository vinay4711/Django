from django import forms
from .models import Mobile


class mobForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = "__all__"


class Vinay_form(forms.Form):
    Firstname= forms.CharField(label="Enter first name",max_length=50)
    lastname  = forms.CharField(label="Enter last name", max_length = 100)
    Email_id  =   forms.EmailField( label="Enter Email id",max_length = 20)
    Email_Mobile = forms.IntegerField(label="Enter Mobile Number")
    #Email_Mobile = forms.ImageField(label="Please Upload the Image")
    File_filed  =    forms.FileField()
