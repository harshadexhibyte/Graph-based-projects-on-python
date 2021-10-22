from django.shortcuts import render,redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import datetime
from .models import userMaster
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import json
from django.http import HttpResponse
from django.http import JsonResponse
from io import StringIO,BytesIO
import base64
from openpyxl import Workbook
import xlsxwriter
try:
    from io import BytesIO as IO # for modern python
except ImportError:
    from io import StringIO as IO # for legacy python




def index(request):
	return render(request,'index.html')
def Dashboard(request):
	if request.method == 'POST':
		try:
			admin_user=userMaster.objects.get(email=request.POST['admin_email'],password=request.POST['admin_password'])
			request.session['admin_email']=admin_user.email
			return render(request,'Dashboard.html')
		except Exception as e:
			print(e)
			FailedMsg="Incorrect Email or Password"
			return render(request,'index.html',{'FailedMsg':FailedMsg})
	else:
		return render(request,'Dashboard.html')
def UserProfile(request):
	user = userMaster.objects.get(email=request.session['admin_email'])
	return render(request,'UserProfile.html',{'user':user})
def FileUploded(request):
	if request.method=="POST":
		numerical1 = int(request.POST['numerical1'])
		numerical2 = int(request.POST['numerical2'])
		numerical3 = int(request.POST['numerical3'])
		multiply = int(request.POST['multiply'])
		subscription = int(request.POST['subscription'])
		file = request.FILES['uplodedFile']

		print(file,numerical1,numerical2,numerical3,multiply,subscription)


		data = pd.read_excel(file)
		concatData = pd.concat([data,data])

		print(data)
		data["COL1"] = (numerical1 * numerical2 * numerical3) + data["COL1"]
		data["COL2"] = multiply * data["COL2"]
		data["COL3"] = subscription + data["COL3"]
		print(data)

		
		excel_file = IO()
		xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')
		val = data.to_excel(xlwriter, 'sheetname')
		xlwriter.save()
		xlwriter.close()
		excel_file.seek(0)
		print(xlwriter)
		
		# response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
		# response['Content-Disposition'] = 'attachment; filename=myfile.xlsx'
		# return response

		temp = data.plot(x="COL1", y=["COL2","COL3","COL2"])
		buffer = BytesIO()
		plt.savefig(buffer,format='png')
		buffer.seek(0)
		image_png= buffer.getvalue()
		graph = base64.b64encode(image_png)
		graph = graph.decode('utf-8')
		buffer.close()
		# plt.show()
		return render(request,'ViewGraph.html',{'graph':graph})
	else:
		return render(request,'Dashboard.html')

@csrf_exempt
def Download(request):
	if request.method == 'POST':
		# return JsonResponse({"success":True})
		pass
	else:
		pass
	
def LogOut(request):
	try:
		del request.session['admin_email']
		return redirect('index')
	except:
		return redirect('index')