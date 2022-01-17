from django.shortcuts import render


def blog(request):
    return render(request, "blog/blog.html")


def blog_cat(request, slug):
    print(slug)
    return render(request, "blog/blog.html")
