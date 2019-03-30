# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render,redirect
from models import Team,Player

# Create your views here.
def index(request):
    return render(request,'demo/index.html')

def add_t(request):
    if request.method=='POST':
        t_name = request.POST.get('t_name')
        t_info = request.POST.get('t_info')
        tname_list = Team.objects.filter(t_name=t_name)
        if len(tname_list) == 0:
            Team.objects.create(
                t_name = t_name,
                t_info = t_info
            )
            return redirect('/show_team/')
        else:
            msg = '队名不能重复!'
            return  render(request,'demo/add_t.html',locals())
    else:
        return render(request,'demo/add_t.html')

def show_team(request):
    all_team = Team.objects.all()
    return render(request,'demo/show_team.html',locals())

def update_t(request,team_id):
    if request.method=='POST':
        t_name = request.POST.get('t_name')
        t_info = request.POST.get('t_info')
        tname_list = Team.objects.filter(t_name=t_name)
        if len(tname_list) == 0:
            Team.objects.filter(id=team_id).update(
                t_name = t_name,
                t_info = t_info
            )
            return redirect('/show_team/')
        else:
            msg = '队名不能重复!'
            return render(request, 'demo/add_t.html', locals())
    else:
        teams = Team.objects.get(id=team_id)
        return render(request,'demo/update_t.html',locals())

def delete_t(request,team_id):
    Team.objects.filter(id=team_id).delete()
    return redirect('/show_team/')

def add_p(request,team_id):
    if request.method=='POST':
        p_name = request.POST.get('p_name')
        p_gender = request.POST.get('p_gender')
        p_info = request.POST.get('p_info')
        Player.objects.create(
            p_name = p_name,
            p_gender = p_gender,
            p_info = p_info,
            team_id = team_id
        )
        path = '/show_p/'+str(team_id)+'/'
        return redirect(path)
    else:
        return render(request,'demo/add_p.html')

def show_p(request,team_id):
    all_player = Player.objects.filter(team_id=team_id)
    return render(request,'demo/show_p.html',locals())

def update_p(request,p_id):
    if request.method=='POST':
        p_name = request.POST.get('p_name')
        p_gender = request.POST.get('p_gender')
        p_info = request.POST.get('p_info')
        player = Player.objects.get(id = p_id)
        team_id = player.team.id
        Player.objects.filter(id=p_id).update(
            p_name = p_name,
            p_gender = p_gender,
            p_info = p_info,
            team_id = player.team.id
        )
        path = '/show_p/'+str(team_id)+'/'
        return redirect(path)
    else:
        player = Player.objects.get(id = p_id)
        return render(request,'demo/update_p.html',locals())

def delete_p(request,p_id):
    player = Player.objects.get(id=p_id)
    team_id = player.team.id
    path = '/show_p/' + str(team_id) + '/'
    Player.objects.filter(id = p_id).delete()
    return redirect(path)
