import django_tables2 as tables
from apps.api.models import Material

class MaterialTable(tables.Table):
    class Meta:
        model = Material