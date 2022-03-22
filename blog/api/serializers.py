
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from blog.models import Blog, Category, Tag, Comment, Subscription
from authentication.api.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'slug'


class TagSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'
        lookup_field = 'slug'


class BlogSerializer(serializers.ModelSerializer):
    # def get_authour(self):
    #     return User.objects.get(self.author)

    url = serializers.CharField(source='get_absolute_url', read_only=True)
    author = UserSerializer()

    class Meta:
        model = Blog
        fields = '__all__'
        lookup_field = 'slug'


# class Child2CommentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Comment
#         fields = '__all__'


class ChildCommentSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # children = serializers.ListSerializer(
    #     child=Child2CommentSerializer()
    # )

    class Meta:
        model = Comment
        fields = '__all__'
        # exclude = ['updated_at']
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    children = serializers.ListField(
        child=ChildCommentSerializer(), allow_empty=True, read_only=True, required=False
    )

    blog = serializers.PrimaryKeyRelatedField(
        required=True, queryset=Blog.objects.all())

    body = serializers.CharField(required=True, error_messages={
        'required': 'You cannot submit an empty comment.',
        'blank': 'You cannot submit an empty comment.',
    })

    parent = serializers.PrimaryKeyRelatedField(
        default=None, queryset=Comment.objects.all(), allow_null=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # exclude = ['updated_at']
        depth = 1
        extra_kwargs = {
            # 'user': {'required': False},
            # 'blog': {'read_only': False},
            'parent': {
                'default': None
            }
        }


class SubscriptionSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(min_length=3, max_length=40, error_messages={
        'required': 'Provided firstname.',
        'blank': 'Provided firstname.',
        'min_length': 'Firstname must have 3 to 40 characters.',
        'max_length': 'Firstname must have 3 to 40 characters.'
    })
    email = serializers.EmailField(validators=[
        UniqueValidator(
            queryset=Subscription.objects.all(),
            message='Email already signed up for subscriptions.'
        )
    ], error_messages={
        'required': 'Provide email.',
        'blank': 'Provide email.',
    })

    class Meta:
        model = Subscription
        fields = '__all__'
