# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Team(models.Model):
    t_name = models.CharField('队名',max_length=22)
    t_info = models.TextField('简介',max_length=4220)
    class Meta:
        verbose_name = '球队'
        verbose_name_plural = verbose_name

class Player(models.Model):
    p_name = models.CharField('姓名',max_length=22)
    p_gender = models.CharField('性别',max_length=10,choices=(('nan', '男'),('nv', '女')),default='nan')
    p_info = models.TextField('简介',max_length=2000)
    team = models.ForeignKey(Team)
    class Meta:
        verbose_name = '球员'
        verbose_name_plural = verbose_name