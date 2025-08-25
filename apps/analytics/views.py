from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from apps.expenses.models import Expense
from django.db.models import Sum
from django.db.models.functions import TruncMonth


@login_required
def dashboard_view(request):
    return render(request , "analytics/dashboard.html")

@login_required
def expenses_by_category(request):
    data = (
        Expense.objects.filter(user=request.user)
        .values("category__name")
        .annotate(total=Sum("amount"))
        .order_by("-total")
    )
    return JsonResponse(list(data) , safe=False)

@login_required
def expenses_by_month(request):
    data = (
        Expense.objects.filter(user=request.user)
        .annotate(month=TruncMonth("date"))
        .values("month")
        .annotate(total=Sum("amount"))
        .order_by("month")
    )
    return JsonResponse(list(data), safe=False)
