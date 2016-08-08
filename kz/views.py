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
