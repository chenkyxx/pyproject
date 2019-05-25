import base64

from django.shortcuts import render
from django.http import HttpResponse
import json
import uuid
# Create your views here.
from Api.models import IMG, Test
from UtilsMethod.UtilsMethod import UtilsMethod


def get_aa(request):

    if request.method == "POST":
        dict1 = {}
        if request.POST:  # 判断是否传参
            a = request.POST.get("a", 0)
            b = request.POST.get("b", 0)

            if a and b:   # 判断参数中是否有a和b
                dict1["number"] = a+b
                json_data = json.dumps(dict1)
                print("===========================>>>request success!"+"\n"+str(uuid.uuid1()))
                return HttpResponse(json_data)
            else:
                return HttpResponse("input error")
        else:
            return HttpResponse("parameters can be not empty or null!")
    else:
        return HttpResponse("request method error!")


def get_process_info(request):
    print("进入方法")
    if request.method == "GET":
        if request.GET:
            pid = int(request.GET.get("pid"))
            a = UtilsMethod().get_process_info(pid)
            kk = json.dumps(a)
            return HttpResponse(kk)
        else:
            return HttpResponse("请求参数不能为空")
    else:
        return HttpResponse("request method error!")


def post_sql(request):
    try:
        print("***********************************")
        if request.method == "POST":
            json_str = json.loads(request.body.decode())
            img = json_str.get("img")
            data = open(img, "rb").read()
            name = json_str.get("name")
            instance = IMG(img=data, name=name)
            instance.save()
            return HttpResponse("success!")
        else:
            return HttpResponse("request method error")
    except Exception as e:
        return HttpResponse(str(e))


def post_other_sql(request):
    try:
        if request.method == "POST":
            json_str = json.loads(request.body.decode())
            photo = json_str.get("photo")
            data = open(photo, "rb").read()
            instance = Test(photo=data)
            instance.save()
            return HttpResponse("success!")
        else:
            return HttpResponse("request method error!")
    except Exception as e:
        return HttpResponse(str(e))
