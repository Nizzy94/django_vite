
from django.conf import settings
from blog.models import Comment
# from core.settings.settings import BASE_DIR, STATICFILES_DIRS
from django.core.files.images import ImageFile
import os
import boto3
import io
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# from PIL import Image
from django.utils.text import slugify
from blog.models import Blog, Category, Tag
# from importlib_metadata import email
from faker.providers import BaseProvider
from faker import Faker
from django.core.management.base import BaseCommand
# from django.core.files.storage import default_storage as storage

# from django.conf import settings
# from core.storages import MediaStorage


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

IMG_LIST = [
    "brown-shopping-bags-5956.jpg",
    "background-bags-black-cardboard-346748.jpg",
    "blue-master-card-on-denim-pocket-164571.jpg",
    "classic-clothes-commerce-fashion-298863.jpg",
    "ecommerce-2140604_1920.jpg",
    "smile-2072908_1920.jpg",
    "woman-1030895_1920.jpg",
    "woman-3040029_1920.jpg",
    "woman-in-brown-and-gray-t-shirt-sitting-on-brown-wooden-949670.jpg"
]


def downloadDirectoryFroms3(self, bucketName, remoteDirectoryName):

    s3_resource = boto3.resource(
        's3',
        aws_access_key_id=settings.AWS_S3_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_S3_SECRET_ACCESS_KEY
    )
    bucket = s3_resource.Bucket(bucketName)

    el = self.random_element(IMG_LIST)
    path = 'media/%s/%s' % (remoteDirectoryName, el)
    obj = bucket.Object(path)

    return {'stream': obj.get(), 'path': path}


# IMG_DIR = BASE_DIR / 'static/JPEG'
IMG_DIR = 'JPEG'


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

    def random_comment(self, blog):

        comments = blog.comments.filter(parent=None)
        if comments.count() < 1:
            # print('com count less than one')
            return None

        rand_com = self.random_element(comments)
        rand_com_or_null = self.random_element([rand_com, None])
        # print('add rand or null:', rand_com_or_null)
        return rand_com_or_null

    def save_image(self):
        file = downloadDirectoryFroms3(
            self,
            settings.AWS_STORAGE_BUCKET_NAME, IMG_DIR
        )

        return file

    # def save_image(self):
    #     downloadDirectoryFroms3(
    #         settings.AWS_STORAGE_BUCKET_NAME, 'JPEG')

    #     img_list = os.listdir(IMG_DIR)
    #     return self.random_element(img_list)


class Command(BaseCommand):
    help = 'Seed database'

    def seed_comments(self, fake):
        comments = Comment.objects.all()

        if comments.count() > 0:
            comments.delete()

        self.stdout.write(self.style.NOTICE("Adding comments..."))
        # print('before blogs')
        blogs = Blog.objects.all()

        # print('before blogs loops')
        for blog in blogs:
            # print('before range loops')
            for _ in range(10):
                # print('in range loops')

                Comment.objects.create(
                    blog=blog,
                    user=fake.random_author(),
                    parent=fake.random_comment(blog),
                    body=fake.sentence(nb_words=20),
                )

        self.stdout.write(self.style.SUCCESS("Comments added."))

    def add_arguments(self, parser):

        parser.add_argument(
            '--comments', '-c',
            action='store_true',
            help='Add only comments to database',
        )
        parser.add_argument(
            '-a', '--all',
            action='store_true',
            help='Add all to database',
        )

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(Provider)

        not_super_user = User.objects.exclude(is_superuser=True)

        if kwargs['comments']:
            self.seed_comments(fake)

        if kwargs['all']:
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

            for _ in range(100):
                # image_name = fake.save_image()
                res = fake.save_image()
                image_name = res['path'].split("/")[-1]
                stream = res['stream']

                # img_obj = Image.open(res['stream'])
                # print(img_obj.path)
                # img = img_obj.save(res['path'])

                img_obj = stream['Body']
                # img_obj = open(IMG_DIR / image_name, 'rb')
                print(res['path'].split("/")[-1])

                img = ImageFile(img_obj, name=image_name)
                # img = ImageFile(img_obj, name=image_name)

                cat = fake.random_category()
                title = fake.text(max_nb_chars=50)
                # excerpt = fake.sentence(nb_words=15)
                author = fake.random_author()
                paragraphs = []
                excerpts = []
                html = "<div>"

                # print(fake.paragraphs(nb=10))
                excerpt = html+f"<p>{fake.text(max_nb_chars=130)}</p></div>"

                for _ in range(5):
                    paragraphs.append(fake.paragraph(nb_sentences=20))

                for para in paragraphs:
                    html += f"<p>{para}</p><br>"

                body = html+"</div>"

                blog = Blog.objects.create(
                    category=cat,
                    title=title,
                    excerpt=excerpt,
                    image=img,
                    author=author,
                    body=body
                )

                blog_tags = fake.random_tags()

                for tag in blog_tags:
                    blog.tags.add(tag)

                # self.stdout.write('Adding blogs: %d' % ((blogs_num/50)*100,))
            self.stdout.write(self.style.SUCCESS("Blogs added."))

            self.seed_comments(fake)
