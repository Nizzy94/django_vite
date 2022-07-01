
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from ckeditor.fields import RichTextField

from blog.managers import CommentManager


class Category(models.Model):
    icon = models.CharField(max_length=255, default="nothing")
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta():
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:blogs_cat", kwargs={"category": self.slug})


class Tag(models.Model):
    # icon = models.CharField(max_length=255, default="nothing")
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta():
        verbose_name_plural = 'Tags'

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:blogs_by_tag", kwargs={"tag": self.slug})


class Blog(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True)
    excerpt = models.CharField(max_length=150)
    image = models.ImageField(upload_to="blog_images/%Y/%m/%d")
    tags = models.ManyToManyField(Tag, related_name='blogs')
    body = RichTextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, related_name="blogs", on_delete=CASCADE)
    author = models.ForeignKey(User, related_name="blogs", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    # def body_to_str(self):
    #     return self.body

    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"blog_slug": self.slug, "category": self.category.slug})

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            # print(self.image.path)
            # print(self.image.name)

            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.point(lambda i: i * 2)
                img.save(self.image.path)
        # super().save(*args, **kwargs)


class Comment(models.Model):
    objects = CommentManager()

    blog = models.ForeignKey(
        Blog, related_name="comments", on_delete=CASCADE)

    user = models.ForeignKey(User, related_name="comments", on_delete=CASCADE)
    parent = models.ForeignKey(
        "self", related_name="child_comments", on_delete=CASCADE, null=True)

    body = models.TextField()
    edited = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def username(self):
        return self.user.username

    def children(self):
        return self.child_comments.all()

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("blog:blog_detail", kwargs={"blog_slug": self.slug, "category": self.category.slug})

    def __str__(self) -> str:
        return 'Comment by: %s' % self.username()


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name
