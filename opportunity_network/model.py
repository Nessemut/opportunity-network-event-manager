from django.db import models


class Event(models.Model):
    id = models.AutoField(name='rowid', primary_key=True)
    title = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=64)
    # TODO: state of published

    class Meta:
        db_table = "event"


class EventSubscription(models.Model):
    id = models.AutoField(name='rowid', primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=64)
    email = models.CharField(blank=False, max_length=64)
    comment = models.CharField(max_length=512)

    class Meta:
        db_table = "subscription"
