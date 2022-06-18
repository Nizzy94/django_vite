from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "main/home.html")


def about(request):
    return render(request, "main/about.html")


@login_required
def contact(request):
    return render(request, "main/contact.html")
