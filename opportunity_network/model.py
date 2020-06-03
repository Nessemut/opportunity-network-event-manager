from django.db import models


class Event(models.Model):
    id = models.AutoField(name='rowid', primary_key=True)
    title = models.CharField()
    description = models.TextField()
    date = models.DateField()
    author = models.CharField()
    # TODO: state of published

    class Meta:
        db_table = "event"


class EventSubscription(models.Model):
    id = models.AutoField(name='rowid', primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(blank=False)
    email = models.CharField(blank=False)
    comment = models.CharField()

    class Meta:
        db_table = "subscription"
