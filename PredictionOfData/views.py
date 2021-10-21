from django.shortcuts import render,redirect
from django.conf import settings
import datetime
from .models import userMaster
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from io import StringIO,BytesIO
import base64
from openpyxl import Workbook
import xlsxwriter
try:
    from io import BytesIO as IO # for modern python
except ImportError:
    from io import StringIO as IO # for legacy python



from django.http import HttpResponse


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
def FileUploded(request):
	if request.method=="POST":
		file = request.FILES['uplodedFile']
		data = pd.read_excel(file)
		concatData = pd.concat([data,data])
		
		excel_file = IO()
		
		xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')
		concatData.to_excel(xlwriter, 'sheetname')
		xlwriter.save()
		xlwriter.close()
		excel_file.seek(0)
		response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
		response['Content-Disposition'] = 'attachment; filename=myfile.xlsx'
		


		temp = data.plot(x="COL1", y=["COL2","COL3","COL2"])
		buffer = BytesIO()
		plt.savefig(buffer,format='png')
		buffer.seek(0)
		image_png= buffer.getvalue()
		graph = base64.b64encode(image_png)
		graph = graph.decode('utf-8')
		buffer.close()
		# plt.show()
		return render(request,'ViewGraph.html',{'graph':graph,'concatData':concatData})
	else:
		return render(request,'Dashboard.html')

def download(request):
	if request.method == 'POST':
		Data = request.POST['data']
		print(Data)
		return HttpResponse("its work")
	else:
		pass
	
	
def LogOut(request):
	try:
		del request.session['admin_email']
		return redirect('index')
	except:
		return redirect('index')