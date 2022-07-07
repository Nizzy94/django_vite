

from django.contrib import admin
from PIL import Image
# import core.settings.settings
from .models import Blog, Category, Subscription, Tag
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core import mail


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]
    # list_filter = ["category"]
    date_hierarchy = "created_at"
    exclude = ["created_at", "updated_at"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]
    # list_filter = ["category"]
    date_hierarchy = "created_at"
    exclude = ["created_at", "updated_at"]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("name",)}
    list_display = ["first_name", "email"]
    # list_filter = ["category"]
    date_hierarchy = "created_at"
    exclude = ["created_at", "updated_at"]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "author"]
    list_filter = ["category", "tags"]
    date_hierarchy = "created_at"
    exclude = ["created_at", "updated_at", 'slug']

    def save_model(self, request, obj, form, change):
        print({
            # 'req': request.POST.get(),
            'obj': obj,
            'form':  form,
            'change': change
        })

        if not change:
            obj.author = request.user
            obj.save()

            post = Blog.objects.get(id=obj.id)

            subscribers = Subscription.objects.all()

            if subscribers.count() > 0:
                emails = []
                connection = mail.get_connection()
                connection.open()
                # sub_list = [sub.email for sub in subscribers]
                plaintext_template = get_template('blog/emails/newpost.txt')
                html_template = get_template('blog/emails/newpost.html')
                # subject, from_email, to = 'Subscription to newsletter', 'from@example.com', [
                #     sub.email for sub in subscribers]
                for subscriber in subscribers:
                    subject, from_email, to = 'There is a new post on %s' % settings.SITE_NAME, 'from@example.com', [
                        subscriber.email]
                    d = {
                        'first_name': subscriber.first_name,
                        'title': post.title,
                        'excerpt': post.excerpt,
                        'site_name': settings.SITE_NAME,
                        'post_link': "%s%s" % (settings.SITE_ORIGIN, post.get_absolute_url()),
                    }
                    text_content = plaintext_template.render(d)
                    html_content = html_template.render(d)
                    msg = mail.EmailMultiAlternatives(
                        subject, text_content, from_email, to)

                    msg.attach_alternative(html_content, "text/html")
                    # msg.send()
                    emails.append(msg)

                connection.send_messages(emails)
                connection.close()

        super(BlogAdmin, self).save_model(request, obj, form, change)
