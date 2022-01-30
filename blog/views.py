from django.shortcuts import render


def blogs(request):
    return render(request, "blog/blog.html")


def blogs_by_tag(request, tag):
    return render(request, "blog/blog.html")


def blogs_cat(request, category):
    print(category)
    return render(request, "blog/blog.html")


def blog(request, category, blog_slug):
    print(category, blog_slug)
    return render(request, "blog/blog_detail.html")
