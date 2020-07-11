import re

from django import forms
from app1.models import AddNewClasses,StudentModel

class AddnewclassForm(forms.ModelForm):
    duration=forms.IntegerField(min_value=10)
    price=forms.FloatField(min_value=2000)

    class Meta:
        model=AddNewClasses
        fields='__all__'
        labels={'name':'Subject'}

    def clean_name(self):
        name=self.cleaned_data['name']
#^[a-zA-Z]+(\s[a-zA-Z]+)?$
        res=re.findall(r'^[a-zA-Z]*$',name)
        if res:
            return  name
        else:
            raise forms.ValidationError('Only Alphabets are allowed')
    def clean_faculty(self):
        fac=self.cleaned_data['faculty']
        res=re.findall(r'^[a-zA-Z]*$',fac)
        if res:
            return fac
        else:
            raise forms.ValidationError('Only Alphabets are allowed')


class StudentForm(forms.ModelForm):


    class Meta:
        model=StudentModel
        fields='__all__'



    def clean_stu_name(self):
        st_name=self.cleaned_data['stu_name']
        res=re.findall(r'^[a-zA-Z]*$',st_name)
        if res:
            return st_name
        else:
            raise forms.ValidationError('Only Alphabets are allowed')


