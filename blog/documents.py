from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Blog


@registry.register_document
class BlogDocument(Document):

    tags = fields.ObjectField(properties={
        # 'id': fields.IntegerField(),
        'name': fields.TextField(),
    })
    category = fields.ObjectField(properties={
        # 'id': fields.IntegerField(),
        'name': fields.TextField(),
    })
    body = fields.TextField()

    class Index:
        # Name of the Elasticsearch index
        name = 'blogs'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    # body = fields.TextField(attr="body_to_str")

    class Django:
        model = Blog  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'id',
            'title',
        ]
