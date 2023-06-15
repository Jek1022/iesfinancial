from __future__ import unicode_literals
import datetime
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Ccc(models.Model):
    IMPORT_STATUS_CHOICES = (
        ('F', 'Failed'),
        ('S', 'Success'),
        ('P', 'Posted'),
    )
    importstatus = models.CharField(max_length=1, choices=IMPORT_STATUS_CHOICES, default='S')
    enterby = models.ForeignKey(User, default=1, related_name='ccc_enter')
    enterdate = models.DateTimeField(auto_now_add=True)
    modifyby = models.ForeignKey(User, default=1, related_name='ccc_modify')
    modifydate = models.DateTimeField(auto_now_add=True)
    isdeleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'ccc'
        ordering = ['-pk']
        permissions = (
            ("view_ccc", "Can view ccc"),
            ("tag_ccc", "Can tag ccc")
        )

    def get_absolute_url(self):
        return reverse('ccc:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.code

    def __unicode__(self):
        return self.code

    def status_verbose(self):
        return dict(Ccc.IMPORT_STATUS_CHOICES)[self.status]