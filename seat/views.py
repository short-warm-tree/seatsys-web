from django.shortcuts import render
import json
import random
import traceback
import time
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from seat.models import seat
from seat.models import orderrecord
from django.http import  JsonResponse
from login.models import StudentModels

from django.conf import settings
def showfreeseat(request):
    freecount1=freecount2=freecount3=freecount4=freecount5=count1=count2=count3=count4=count5=0
    for freeseat1 in seat.objects.filter(seatlevel='1'):
        count1=count1+1
        if freeseat1.seatstatus=='1':
           freecount1=freecount1+1
    for freeseat2 in seat.objects.filter(seatlevel='2'):
        count2=count2+1
        if freeseat2.seatstatus=='1':
           freecount2=freecount2+1
    for freeseat3 in seat.objects.filter(seatlevel='3'):
        count3=count3+1
        if freeseat3.seatstatus=='1':
           freecount3=freecount3+1
    for freeseat4 in seat.objects.filter(seatlevel='4'):
        count4=count4+1
        if freeseat4.seatstatus=='1':
           freecount4=freecount4+1
    for freeseat5 in seat.objects.filter(seatlevel='5'):
        count5=count5+1
        if freeseat5.seatstatus=='1':
           freecount5=freecount5+1
    return render(request,'layer(3).html',{"freefloorone":json.dumps(freecount1),"freefloortwo":json.dumps(freecount2),"freefloorthree":json.dumps(freecount3),"freefloorfour":json.dumps(freecount4),"freefloorfive":json.dumps(freecount5),"floorone":count1,"floortwo":count2,"floorthree":count3,"floorfour":count4,"floorfive":count5})

def showseat(request):
    return render(request,'seatinfo.html')


def leave(request):
    return render(request,'leave(3).html')

def seatinfo(request):

    seatlevel = request.GET.get('seatlevel')  # 取楼层号(get)
    empty_objs = seat.objects.filter(seatstatus='1', seatlevel=seatlevel)
    empty_ids = []  # 利用循环将seatid从每个对象里取出来
    for obj in empty_objs:
        empty_ids.append(obj.seatid)

    ordered_objs = seat.objects.filter(seatstatus='2', seatlevel=seatlevel)
    ordered_ids = []  # 利用循环将seatid从每个对象里取出来
    for obj in ordered_objs:
        ordered_ids.append(obj.seatid)

    using_objs = seat.objects.filter(seatstatus='3', seatlevel=seatlevel)
    using_ids = []  # 利用循环将seatid从每个对象里取出来
    for obj in using_objs:
        using_ids.append(obj.seatid)

    left_objs = seat.objects.filter(seatstatus='4', seatlevel=seatlevel)
    left_ids = []  # 利用循环将seatid从每个对象里取出来
    for obj in left_objs:
        left_ids.append(obj.seatid)



    return render(request, '%syuyue.html'%(seatlevel), {
        'empty_ids': json.dumps(empty_ids),
        'ordered_ids': json.dumps(ordered_ids),
        'using_ids': json.dumps(using_ids),
        'left_ids': json.dumps(left_ids),
    })


# 以下是预定系统的代码


# 基本预约函数：传入参数，创建预约记录，返回成功与否
#@csrf_exempt
def order(request):
    print("1")
    
    stu_id=request.session.get('stuid')  # 参数2是测试用，实装用None
    print(stu_id)
    if StudentModels.objects.filter(stuid=stu_id).filter(condition=True): #一人只能预约一个位置

        return JsonResponse({'result': '您有预约过或正在使用的座位'}, safe=False)
    else:

        seatid = request.POST['seatid']
        print(seatid)
        print(type(seatid))
        fromminute = request.POST['fromminute']
        fromhour = request.POST['fromhour']
        fromtime = fromminute + ':' + fromhour
        timelong = request.POST['timelong']
        print(type(fromtime))
        print(fromtime)


        # 参数2是测试用，实装用None
        orderid = str(int(time.strftime("%Y%m%d%H%M%S")) + random.randint(0, 10))  # 时间戳作为id，随机数防止同时请求
        print(stu_id)
        print(orderid)

        try:
            stuobj = StudentModels.objects.get(stuid = stu_id)
            #name = stuobj.name
            #print(name)
            seatobj = seat.objects.get(seatid=seatid)
            orderrecord.objects.create(orderid=orderid, seat=seatobj, fromtime=fromtime,
                                       timelong=timelong, student=stuobj,orderstatus = '2'
                                       )
            stuobj.condition = True
            stuobj.save()
            seatobj.seatstatus = '3'
            seatobj.save()
            request.session['seatid']=seatid
            return JsonResponse({'result':'预约成功'},safe=False)
        except:
            traceback.print_exc()  # 打印报错
            return JsonResponse({'result':'failed'},safe=False)


def signout(request):
    stuid = request.session.get('stuid')
    print(stuid+'q')  # 参数2是测试用，实装用None
    count = settings.COUNT 
    print(count)
    if StudentModels.objects.filter(stuid=stuid).filter(condition=True):
        print(stuid+'w')

        try:
            seatid=request.session.get('seatid',default = '0001')
            #session问题

            seatobj = seat.objects.get(seatid=seatid)
            seatobj.seatstatus='1'
            seatobj.save()
            stuobj = StudentModels.objects.get(stuid=stuid)
            stuobj.condition = False
            stuobj.save()
            orderre=orderrecord.objects.get(student=stuobj,orderstatus='1'or'2') #student是外键，在orderrecord这个表里面查询必须先找到一个student1表的对象
            orderre.orderstatus='3'
            orderre.save()

            del request.session['seatid']
            return JsonResponse({'result':'现在可以离开'},safe=False)
        except:
            traceback.print_exc()  # 打印报错
            return JsonResponse({'result':'success'},safe=False)
    else:
        return JsonResponse({'result':'需要先定座位'},safe=False)



# Create your views here.
