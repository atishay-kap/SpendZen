from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Budget
from .forms import BudgetForm

@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user).order_by('-year','-month')
    return render(request , 'budgets/budget_list.html', {'budgets':budgets})

@login_required
def budget_create(request):
    if request.method=="POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            messages.success(request , "Budget Created Successfully!!")
            return redirect("budgets:budget_list")
    else:
        form = BudgetForm
    return render(request , "budgets/budget_form.html" , {"form":form})

@login_required
def budget_detail(request , id):
    budget = get_object_or_404(Budget , id=id , user=request.user)
    return render(request , "budgets/budget_detail.html" , {"budget":budget})

@login_required
def budget_edit(request , id):
    budget = get_object_or_404(Budget , id=id , user=request.user)
    if request.method=="POST":
        form = BudgetForm(request.POST , intance=budget)
        if form.is_valid():
            form.save()
            messages.success(request , "Budget Updated Successfully!!")
            return redirect("budgets:budget_list")
    else:
        form = BudgetForm(instance=Budget)
    return render(request , "budgets/budget_form.html" , {"form":form})


@login_required
def budget_delete(request , id):
    budget = get_object_or_404(Budget , id=id , user=request.user)
    if request.method=="POST":
        budget.delete()
        messages.success(request , "Budget Deleted Successfully!!")
        return redirect("budgets:budget_list")
    return render(request, "budgets/budget_confirm_delete.html", {"budget": budget})
