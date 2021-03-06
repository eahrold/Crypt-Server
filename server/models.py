from django.db import models
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Computer(models.Model):
    recovery_key = models.CharField(max_length=200, verbose_name="Recovery Key")
    serial = models.CharField(max_length=200, verbose_name="Serial Number")
    username = models.CharField(max_length=200, verbose_name="User Name")
    computername = models.CharField(max_length=200, verbose_name="Computer Name")
    last_checkin = models.DateTimeField(blank=True,null=True)
    def __unicode__(self):
        return self.computername
    class Meta:
        ordering = ['serial']
        permissions = (
                    ('can_approve', (u'Can approve requests to see encryption keys')),
                )
                
class Request(models.Model):
    computer = models.ForeignKey(Computer)
    requesting_user = models.ForeignKey(User, related_name='requesting_user')
    approved = models.NullBooleanField(verbose_name="Approved?")
    auth_user = models.ForeignKey(User, null=True, related_name='auth_user')
    reason_for_request = models.TextField()
    reason_for_approval = models.TextField(blank=True,null=True, verbose_name="Approval Notes")
    date_requested = models.DateTimeField(auto_now_add=True)
    date_approved = models.DateTimeField(blank=True,null=True)
    current = models.BooleanField(default=True)