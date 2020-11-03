from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl.connections import connections
from wagtail.search import index

from .models import Employee
from .models import Company

connections.create_connection(hosts=['localhost'])


@registry.register_document
class EmployeeDocument(Document):
    class Index:
        name = 'employees'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Employee

        fields = [
            'first_name',
            'last_name',
            'email',
            #index.RelatedFields('company_name'),
            'salary',
            'currency',
            'pan',
            'gender',
            'marital_status',
            'address_1',
            'address_2',
            'city',
            'state',
            'pin_code',
            'country',
        ]

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True

        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False

        # Paginate the django queryset used to populate the index with the specified size
        # (by default it uses the database driver's default setting)
        queryset_pagination = 5000
