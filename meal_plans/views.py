from django.shortcuts import render

def index(request):
    """식단 관리 홈페이지"""
    return render(request, 'meal_plans/index.html')
