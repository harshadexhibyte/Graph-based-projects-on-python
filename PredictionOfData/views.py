from django.shortcuts import render,redirect
from django.conf import settings
# import datetime
# from .models import adminUser
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt 
from django.http import HttpResponse


def index(request):
	return render(request,'index.html')