from django.contrib import admin
from django.urls import path, re_path, include

app_name = 'meal_plans'

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'', include(('meal_plans.urls', 'meal_plans'),
        namespace = 'meal_plans')),
]
