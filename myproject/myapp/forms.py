from django import forms
from . models import *


class LoginForm(forms.ModelForm):
    class Meta:
        model = Store_login
        fields = ['username','email','password']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Store_product
        fields = ['product_name','quantity','amount','delivered','remaining']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Store_employee
        fields =['employee_name','email','address','contactno','salary']