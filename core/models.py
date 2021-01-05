from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()
    """ Meta class등록 후 abstract = True로 하면 db에는 저장되지 않는다 """

    class Meta:
        abstract = True