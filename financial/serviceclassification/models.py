from __future__ import unicode_literals
import datetime
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

class Serviceclassification(models.Model):
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=250)
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
        ('C', 'Cancelled'),
        ('O', 'Posted'),
        ('P', 'Printed'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    enterby = models.ForeignKey(User, default=1, related_name='serviceclassification_enter')
    enterdate = models.DateTimeField(auto_now_add=True)
    modifyby = models.ForeignKey(User, default=1, related_name='serviceclassification_modify')
    modifydate = models.DateTimeField(auto_now_add=True)
    isdeleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'serviceclassification'
        ordering = ['-pk']
        permissions = (("view_serviceclassification", "Can view serviceclassification"),)

    def get_absolute_url(self):
        return reverse('serviceclassification:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.code

    def __unicode__(self):
        return self.code

    def status_verbose(self):
        return dict(Serviceclassification.STATUS_CHOICES)[self.status]
