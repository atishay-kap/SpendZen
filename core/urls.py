from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("apps.users.urls")),
    path("expenses/",include("apps.expenses.urls")),
    path("analytics/",include("apps.analytics.urls")),
    path("budgets/",include("apps.budgets.urls"))
]
