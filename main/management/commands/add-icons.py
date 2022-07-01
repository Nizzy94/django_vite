from django.core.management.base import BaseCommand
from main.models import SocialIcon

# import faker.providers


class Command(BaseCommand):

    def handle(self, *args, **options):

        # data = {
        #     'google': 'https://cdn.cdnlogo.com/logos/g/35/google-icon.svg',
        #     'github': 'https://cdn.cdnlogo.com/logos/g/69/github-icon.svg',
        #     'facebook': 'https://cdn.cdnlogo.com/logos/f/83/facebook.svg',
        #     'twitter': 'https://cdn.cdnlogo.com/logos/t/45/twitter.svg',
        #     'linkedin': 'https://cdn.cdnlogo.com/logos/l/66/linkedin-icon.svg',
        # }

        data = [
            {
                'provider': 'google',
                'icon': 'https://cdn.cdnlogo.com/logos/g/35/google-icon.svg'
            },
            {
                'provider': 'github',
                'icon': 'https://cdn.cdnlogo.com/logos/g/69/github-icon.svg'
            },
            {
                'provider': 'facebook',
                'icon': 'https://cdn.cdnlogo.com/logos/f/83/facebook.svg'
            },
            {
                'provider': 'twitter',
                'icon': 'https://cdn.cdnlogo.com/logos/t/45/twitter.svg'
            },
            {
                'provider': 'linkedin',
                'icon': 'https://cdn.cdnlogo.com/logos/l/66/linkedin-icon.svg'
            },
        ]

        self.stdout.write(self.style.NOTICE("Adding social icons..."))

        for provider in data:
            SocialIcon.objects.create(
                provider=provider['provider'],
                icon=provider['icon']
            )

        self.stdout.write(self.style.SUCCESS("Social Icons added."))
