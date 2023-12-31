from __future__ import unicode_literals
import datetime
from django.core.urlresolvers import reverse
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Departmentbudget(models.Model):
    year = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2100), \
        MinValueValidator(1980)])
    department = models.ForeignKey('department.Department', \
        related_name='department_departmentbudget_id')
    unit = models.ForeignKey('unit.Unit', related_name='unit_departmentbudget_id')
    chartofaccount = models.ForeignKey('chartofaccount.Chartofaccount', \
        related_name='chartofaccount_departmentbudget_id')
    remarks = models.CharField(max_length=255, blank=True, null=True)
    formula = models.CharField(max_length=255, blank=True, null=True)
    method = models.CharField(max_length=255, blank=True, null=True)
    mjan = models.DecimalField(default=0.00, null=True, blank=True, \
        decimal_places=2, max_digits=18)
    mfeb = models.DecimalField(default=0.00, null=True, blank=True, \
        decimal_places=2, max_digits=18)
    mmar = models.DecimalField(default=0.00, null=True, blank=True, \
        decimal_places=2, max_digits=18)
    mapr = models.DecimalField(default=0.00, null=True, blank=True, \
        decimal_places=2, max_digits=18)
    mmay = models.DecimalField(default=0.00, null=True, blank=True, \
        decimal_places=2, max_digits=18)
    mjun = models.DecimalField(default=0.00, null=True, blank=True, \
        decimal_places=2, max_digits=18)
    mjul = models.DecimalField(default=0.00, null=True, blank=True, \
        decimal_places=2, max_digits=18)
    maug = models.DecimalField(default=0.00, null=True, blank=True, \
        decimal_places=2, max_digits=18)
    msep = models.DecimalField(default=0.00, null=True, blank=True, \
        decimal_places=2, max_digits=18)
    moct = models.DecimalField(default=0.00, null=True, blank=True, \
        decimal_places=2, max_digits=18)
    mnov = models.DecimalField(default=0.00, null=True, blank=True, \
        decimal_places=2, max_digits=18)
    mdec = models.DecimalField(default=0.00, null=True, blank=True, \
        decimal_places=2, max_digits=18)
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
        ('C', 'Cancelled'),
        ('O', 'Posted'),
        ('P', 'Printed'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    enterby = models.ForeignKey(User, default=1, related_name='departmentbudget_enter')
    enterdate = models.DateTimeField(auto_now_add=True)
    modifyby = models.ForeignKey(User, default=1, related_name='departmentbudget_modify')
    modifydate = models.DateTimeField(auto_now_add=True)
    isdeleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'departmentbudget'
        ordering = ['-pk']
        permissions = (("view_departmentbudget", "Can view departmentbudget"),)
        unique_together = (('year', 'department', 'unit', 'chartofaccount'),)

    def get_absolute_url(self):
        return reverse('departmentbudget:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return unicode(self.pk)

    def __unicode__(self):
        return unicode(self.pk)

    def status_verbose(self):
        return dict(Departmentbudget.STATUS_CHOICES)[self.status]
