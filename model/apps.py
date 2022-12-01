from datetime import timedelta, datetime
from decimal import Decimal

from django.conf import settings
from django.db.models import Count
from django.views.decorators.cache import never_cache
from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
    menu = (
        ParentItem('Products', children=[
            ChildItem(model='custom_model.book'),
            ChildItem(model='custom_model.category'),
            ChildItem(model='custom_model.discount'),
        ]),
    )
