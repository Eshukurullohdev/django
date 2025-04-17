from django.shortcuts import render
from .models import Blog, Stories
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required(login_url='login')
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

from django.shortcuts import render, redirect
from .forms import UserInfoForm

def collect_user_info(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            with open('user_data.txt', 'a', encoding='utf-8') as f:
                f.write(f"{data['first_name']} {data['last_name']} - {data['phone_number']}\n")
            return redirect('success')
    else:
        form = UserInfoForm()
    return render(request, 'user_info_form.html', {'form': form})