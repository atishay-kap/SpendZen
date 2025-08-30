from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncDay
from django.utils.timezone import now
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.expenses.models import Expense


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
