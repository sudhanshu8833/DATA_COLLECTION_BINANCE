
import logging
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.contrib import messages
import threading
from datamanagement.models import strategy
import random
import string
from .models import strategy

logger = logging.getLogger('dev_log')

def extract(request):
    logger.info("CALLED")

