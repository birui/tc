#coding=utf-8
import json
import re
import time
import os,sys
from kz.models import *
from datetime import datetime
from django.contrib import auth
from django.template import loader,Context
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def index(request):
    return render_to_response('tc/index.html')

def base(request):
    return render_to_response('tc/base.html')

def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'tc/home.html', {'post_list' : post_list})

def law(request):  #对应home
    post_list = Article.objects.all()
    return render(request, 'tc/law.html', {'post_list' : post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tc/post.html', {'post' : post})

