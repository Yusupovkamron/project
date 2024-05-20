import uuid
from django.db.models import TextChoices


class Choices(object):
    class MastersStatic(TextChoices):
        DRAFT = 'df,', 'Draft'
        PUBLISHED = 'pb', 'Published'