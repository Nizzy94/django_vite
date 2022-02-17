from core.settings import BASE_DIR, STATICFILES_DIRS
from django.core.files.images import ImageFile
import os
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from PIL import Image
from django.utils.text import slugify
from blog.models import Blog, Category, Tag
from importlib_metadata import email
from faker.providers import BaseProvider
from faker import Faker
from django.core.management.base import BaseCommand


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
            paragraphs = []
            paragraph = ""
            html = "<div>"

            # print(fake.paragraphs(nb=10))

            for _ in range(5):
                paragraphs.append(fake.paragraph(nb_sentences=20))

            for para in paragraphs:
                html += f"<p>{para}</p><br>"

                # print(paragraph)
            # for par in paragraph:
            #     html += f"<p>{par}</p><br><br>"

            # print(html)

            body = html+"</div>"

            blog = Blog.objects.create(
                category=cat,
                title=title,
                image=img,
                author=author,
                body=body
            )

            blog_tags = fake.random_tags()

            for tag in blog_tags:
                blog.tags.add(tag)

            # self.stdout.write('Adding blogs: %d' % ((blogs_num/50)*100,))
        self.stdout.write(self.style.SUCCESS("Blogs added."))
