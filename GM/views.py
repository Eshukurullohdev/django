from django.shortcuts import render
from .models import Blog, Stories

from django.utils import timezone


def index(request):
    now = timezone.now()
    threeDaysBefore = now - timezone.timedelta(days=3)
    current_month = now.strftime("%B")  
    current_day = now.strftime("%A")
    blogs = Blog.objects.filter(is_main=False)
    stori = Stories.objects.all()
    asosiy_blog = Blog.objects.filter(is_main=True).first()
    news = None
    if request.GET.get("filter") == 'trending':
        news = Blog.objects.filter(views__gte=1000).order_by("-date_posted")
    if request.GET.get("filter") == 'latest':
        news = Blog.objects.filter(date_posted__gte=threeDaysBefore).order_by("-date_posted")

    context = {
        "blogs": blogs,
        "asosiy_blog": asosiy_blog,
        "news": news,
        "current_month": current_month,
        "current_day": current_day,
        'stori': stori
    }
    return render(request, 'home.html', context)

# [1, 2, 3, 4]
# [4] --> 4

# lte -- less than -- dan kam
# gte -- greater than -- dan katta