from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category','amount','description','date','payment_method']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }