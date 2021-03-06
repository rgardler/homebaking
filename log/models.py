from django.db import models

class Log(models.Model):
  event_type = models.CharField(max_length=24)
  description = models.CharField(max_length=250)
  def __str__(self):
      return self.description

class Event(models.Model):
  log = models.ForeignKey(Log)
  time = models.DateTimeField('Event Time')
  data = models.CharField(max_length=250)
  def __str__(self):
      return self.data
