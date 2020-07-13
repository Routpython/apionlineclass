import re

from django import forms
from app1.models import AddNewClasses,StudentModel
def validate_name(name):
    res=re.findall(r'^[a-zA-Z]*$', name)
    if res:
        return name
    else:
        raise forms.ValidationError('Only Alphabets are allowed')

class AddnewclassForm(forms.ModelForm):
    duration=forms.IntegerField(min_value=10)
    price=forms.FloatField(min_value=2000)
    date=forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model=AddNewClasses
        fields='__all__'
        labels={'name':'Subject'}

    def clean_faculty(self):
        fac=self.cleaned_data['faculty']
        res=validate_name(fac)
        return res

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'

    def clean_stu_name(self):
        st_name=self.cleaned_data['stu_name']
        validate_name(st_name)

