from django.shortcuts import render
from django.http import HttpResponse
from login.models import StudentModels
from seat.models import seat
from seat.models import orderrecord
import json
import traceback
from django.http import HttpResponseRedirect
from django.conf import settings
def index(request):
    return HttpResponse(render(request,'index.html'))
def checkin(request):
    if request.method=='POST':
        print('checkin')
        settings.COUNT = 0
        id=request.POST['stuid']
        password=request.POST['mima']
        check=StudentModels.objects.filter(stuid=id,mm=password)
        if check:
            request.session['password']=password
            stu=StudentModels.objects.get(stuid=id,mm=password)
            request.session['stuid']=stu.stuid
            stuid1 = request.session.get('stuid')         
            result='登录成功'
            return render(request,'personal information.html',{"stuname":json.dumps(stu.name)})
        else:
            result='登录失败'
        return HttpResponse(result)
    elif request.method=='GET':
        if request.session['stuid']:
            stuid=request.session['stuid']
            stu=StudentModels.objects.get(stuid=stuid)
            
            return render(request,'personal information.html',{"stuname":json.dumps(stu.name)})
        else:
            return HttpResponse(render(request,'index.html'))

def logout(request):
    if request.method=='GET':
        if request.session['stuid']:
            del request.session['stuid']
            del request.session['password']

        return HttpResponse(render(request,'index.html'))


# Create your views here.
