from django import forms
from .models import Budget

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ["month", "year", "amount"]

    def clean(self):
        cleaned_data = super().clean()
        user = self.instance.user or self.initial.get("user")
        month = cleaned_data.get("month")
        year = cleaned_data.get("year")

        if user and month and year:
            exists = Budget.objects.filter(user=user, month=month, year=year).exclude(pk=self.instance.pk).exists()
            if exists:
                raise forms.ValidationError("You already created a budget for this month.")
        return cleaned_data
