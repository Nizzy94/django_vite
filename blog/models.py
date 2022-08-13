
import base64
import django.core.files.images
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.db import models
from django.utils.text import slugify
from django.core.files.images import ImageFile

import boto3
import hashlib
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.conf import settings
from blog.managers import CommentManager
from django.core.files.storage import default_storage as storage

import io
# from core.settings.dev_settings import (AWS_S3_ACCESS_KEY_ID, AWS_S3_SECRET_ACCESS_KEY,
#                                         AWS_STORAGE_BUCKET_NAME)


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


# def process_image(instance, filename):
#     print('instance: ', instance)
#     print('filename: ', filename)

#     img = Image.open(filename)

#     print(img.size)


class Blog(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True)
    excerpt = models.CharField(max_length=150)
    image = models.ImageField(upload_to="blog_images/%Y/%m/%d")
    # image = models.ImageField(upload_to=process_image)
    tags = models.ManyToManyField(Tag, related_name='blogs')
    body = RichTextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, related_name="blogs", on_delete=CASCADE)
    author = models.ForeignKey(User, related_name="blogs", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"blog_slug": self.slug, "category": self.category.slug})

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        self.updated_at = timezone.now()

        super(Blog, self).save(*args, **kwargs)
        # m = Image.open(self.image)

        # print(self.image)

        # if self.image:
        # m = storage.open(self.image.name)
        # obj_location = 'media/%s' % self.image.name

        # # img = Image.open(self.image)
        # session = boto3.Session()

        # s3_session = session.client(
        #     "s3", aws_access_key_id=settings.AWS_S3_ACCESS_KEY_ID,
        #     aws_secret_access_key=settings.AWS_S3_SECRET_ACCESS_KEY
        # )

        # img = Image.open(self.image)

        # if img.height > 200 or img.width > 200:
        #     output_size = (200, 200)
        #     img = img.convert('RGB')
        #     img = img.resize(output_size)
        #     print(img.size)

        # img = img.thumbnail(output_size)
        # img.point(lambda i: i * 2)

        # sfile = io.BytesIO()
        # self.image = img.save(sfile, format='JPEG')

        # path_list = self.image.name.split("/")[:-1]
        # img_name = self.image.name.split("/")[-1]
        # new_path = "/".join(path_list)

        # print('img path: ', self.image.name.split("/")[:-1])

        # value = sfile.getvalue()
        # buffer = sfile.getbuffer()

        # img.save(self.image.name)
        # md = hashlib.md5(value).digest()
        # img_md5 = base64.b64encode(md).decode('utf-8')

        # storage.save(f'{new_path}/{img}', img)

        # storage.save(new_path, ImageFile(img, img_name))

        # storage.save(im)
        # s3_session.put_object(
        #     ContentMD5=img_md5,
        #     Body=value,
        #     Bucket=settings.AWS_STORAGE_BUCKET_NAME,
        #     Key='media/%s/%s' % (new_path, value)
        # )


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
