# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Team,Player

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','t_name','t_info',]
    list_per_page = 4
    search_fields = ['t_name','t_info']

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id','p_name','p_gender','p_info','team_id']
    list_per_page = 3

admin.site.register(Team,TeamAdmin)
admin.site.register(Player,PlayerAdmin)
