from base64 import decode
from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers import BaseProvider
from importlib_metadata import email
from blog.models import Blog, Category, Tag
from django.utils.text import slugify
from PIL import Image
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import os
from django.core.files.images import ImageFile

from core.settings import BASE_DIR, STATICFILES_DIRS


CATEGORIES = [
    'Entertainment',
    'Sports',
    'Education',
    'Politics',
    'Health',
]
TAGS = [
    'Laravel',
    'Python',
    'Php',
    'django',
    'Football',
    'Basketball',
    'Tennis',
    'Schools',
    'Colleges',
    'Parties',
    'Medicine',
]

# IMG_DIR = BASE_DIR / '../unicart_django/unicart_market/static/images/ecommerce-images/JPEG'
IMG_DIR = BASE_DIR / 'static/JPEG'


class Provider(BaseProvider):
    def categories(self):
        return self.random_element(CATEGORIES)

    def tags(self):
        return self.random_element(TAGS)

    def random_author(self):
        authors = User.objects.all()
        return self.random_element(authors)

    def random_tags(self):
        tags = Tag.objects.all()
        return self.random_elements(tags)

    def random_category(self):
        cats = Category.objects.all()
        return self.random_element(cats)

    def save_image(self):

        img_list = os.listdir(IMG_DIR)
        return self.random_element(img_list)


class Command(BaseCommand):
    help = 'Seed database'

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(Provider)

        not_super_user = User.objects.exclude(is_superuser=True)
        if not_super_user.count() > 0:
            not_super_user.delete()

        self.stdout.write(self.style.NOTICE("Adding users..."))
        for _ in range(5):

            User.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                username=fake.profile()['username'],
                password=make_password('mandeladela')
            )

        self.stdout.write(self.style.SUCCESS("Users added."))

        self.stdout.write(self.style.NOTICE("Adding categories..."))

        for _ in range(len(CATEGORIES)):
            name = fake.unique.categories()
            # print(name)
            Category.objects.get_or_create(
                slug=slugify(
                    name, allow_unicode=True
                ),
                defaults={'name': name},
            )

        self.stdout.write(self.style.SUCCESS("Categories added."))

        self.stdout.write(self.style.NOTICE("Adding tags..."))
        for _ in range(len(TAGS)):
            name = fake.unique.tags()
            Tag.objects.get_or_create(
                slug=slugify(
                    name, allow_unicode=True
                ),
                defaults={'name': name},
            )

        self.stdout.write(self.style.SUCCESS("Tags added."))

        blogs = Blog.objects.all()

        self.stdout.write(self.style.NOTICE("Deleting blogs..."))
        blogs.delete()
        self.stdout.write(self.style.SUCCESS("Blogs deleted."))

        # blogs_num = 0
        self.stdout.write(self.style.NOTICE("Adding blogs..."))

        for _ in range(500):
            image_name = fake.save_image()

            img_obj = open(IMG_DIR / image_name, 'rb')

            img = ImageFile(img_obj, name=image_name)

            cat = fake.random_category()
            title = fake.sentence(nb_words=10)
            author = fake.random_author()
            body = fake.paragraphs(nb=10)

            blog = Blog.objects.create(
                category=cat,
                title=title,
                image=img,
                author=author,
                body=body
            )

            # print(blog.image.path)

            blog_tags = fake.random_tags()

            for tag in blog_tags:
                blog.tags.add(tag)

            # blogs_num += 1

            # self.stdout.write('Adding blogs: %d' % ((blogs_num/50)*100,))
        self.stdout.write(self.style.SUCCESS("Blogs added."))
