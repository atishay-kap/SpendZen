from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Budget
from .forms import BudgetForm

@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user).order_by('-year','-month')
    return render(request , 'budgets/budget_list.html', {'budgets':budgets})

@login_required
def budget_create(request):
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            try:
                budget.save()
                messages.success(request, "Budget created successfully!")
                return redirect("budgets:budget_list")
            except Exception:
                # This will catch unique_together duplicates
                form.add_error(None, "You already have a budget for this month.")
    else:
        form = BudgetForm()
    return render(request, "budgets/budget_form.html", {"form": form})

@login_required
def budget_detail(request , id):
    budget = get_object_or_404(Budget , id=id , user=request.user)
    return render(request , "budgets/budget_detail.html" , {"budget":budget})

@login_required
def budget_edit(request, id):
    budget = get_object_or_404(Budget, id=id, user=request.user)
    if request.method == "POST":
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Budget updated successfully!")
                return redirect("budgets:budget_detail", id=budget.id)
            except Exception:
                form.add_error(None, "Another budget for this month already exists.")
    else:
        form = BudgetForm(instance=budget)
    return render(request, "budgets/budget_form.html", {"form": form})


@login_required
def budget_delete(request , id):
    budget = get_object_or_404(Budget , id=id , user=request.user)
    if request.method=="POST":
        budget.delete()
        messages.success(request , "Budget Deleted Successfully!!")
        return redirect("budgets:budget_list")
    return render(request, "budgets/budget_confirm_delete.html", {"budget": budget})

from django.utils.timezone import now
@login_required
def current_month_budgets(request):
    today = now()
    budgets = Budget.objects.filter(user=request.user, month = today.month , year = today.year)
    
    data = [
        {
            "id": b.id,
            "month": b.month,
            "month_display": b.get_month_display(),
            "year": b.year,
            "amount": float(b.amount),
            "spent": float(b.spent),
            "remaining": float(b.remaining),
            "overspent": b.overspent,
        }
        for b in budgets
    ]
    return JsonResponse(data , safe=False)