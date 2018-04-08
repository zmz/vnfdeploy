# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=30)
    u_enname = models.CharField(max_length=30,unique=True,blank=False)
    u_password = models.CharField(max_length=50)
    u_email = models.EmailField(max_length=50)
    u_role = models.IntegerField(default=1)
    u_ctime = models.DateTimeField(auto_now=False, auto_now_add=True)
    u_mtime = models.DateTimeField(auto_now=True, auto_now_add=False)
    u_status = models.BooleanField(default=True)

    # u_role , 1:other,2:leader
    # u_purview , 1:leader,2:other

    def __unicode__(self):
        return str(self.u_id)