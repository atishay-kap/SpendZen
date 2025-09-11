from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncDay
from django.utils.timezone import now
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.expenses.models import Expense
from apps.budgets.models import Budget


@login_required
def dashboard_view(request):
    return render(request, "analytics/dashboard.html")


@login_required
def expenses_by_category(request):
    data = (
        Expense.objects.filter(user=request.user)
        .values("category__name")
        .annotate(total=Sum("amount"))
        .order_by("-total")
    )
    return JsonResponse(list(data), safe=False)


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


@login_required
def daily_cumulative_expenses(request):
    today = now().date()
    qs = (
        Expense.objects.filter(
            user=request.user,
            date__year=today.year,
            date__month=today.month,
        )
        .annotate(day=TruncDay("date"))
        .values("day")
        .annotate(total=Sum("amount"))
        .order_by("day")
    )

    # build cumulative sum
    cumulative = []
    running = 0
    for row in qs:
        running += row["total"]
        cumulative.append({"day": row["day"], "total": running})

    return JsonResponse(cumulative, safe=False)

def current_month_budgets(request):
    today=now().date()
    budgets = Budget.objects.filter(
        user=request.user , year=today.year , month = today.month
        )
    
    if not budgets.exists():
        budgets = Budget.objects.filter(user=request.user).order_by("-year","-month")[:1]
    
    data = []
    for b in budgets:
        remaining = b.amount - b.spent
        data.append({
            "amount": float(b.amount),
            "spent": float(b.spent),
            "remaining": float(remaining),
            "overspent": remaining < 0,
            "month": b.month,
            "year": b.year,
        })
        
    return JsonResponse(data , safe=False)