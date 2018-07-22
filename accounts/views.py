from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from accounts.models import Acounts,Website
import json
def index(request):
    return render(request,'accounts/index.html')

    # 展示账号数据
def account_list(request):
    query_list = Acounts.objects.all()
    context = {'objs':query_list}
    return render(request,'accounts/accounts_list.html',context)

    # 增加账号
def create(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        website = request.POST.get('website')
        account = Acounts.objects.create(phone=phone,password=password,website=website)
        return redirect("accounts:list")
    websites = Website.objects.all()
    context = {'webs': websites}
    return render(request,'accounts/accounts_create.html',context=context)

    # 更新账号
def update(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        website = request.POST.get('website')
        obj = Acounts.objects.get(phone=phone)
        obj.password = password
        obj.website = website
        obj.save()
        return redirect("accounts:list")
    phone = request.GET.get('phone')
    obj = Acounts.objects.filter(phone=phone)
    context = {'obj':obj}
    return render(request,'accounts/accounts_update.html',context)

def delete(request):
    phone = request.GET.get('phone','')
    if phone:
        obj = Acounts.objects.filter(phone=phone)
        obj.delete()
        return redirect("accounts:list")

# 爬虫账号维护----------------------------------------------------------------

def get_all_acounts(request):
    '''
    返回列表包含账号 status == 1 的
    :param request:
    :return:
    '''
    query_set = Acounts.objects.all()
    json_data = serializers.serialize("json", query_set)
    return HttpResponse(json_data,content_type="application/json")

def get_acounts(request):
    '''
    返回列表包含账号 status == 1 的
    :param request:
    :return:
    '''
    query_set = Acounts.objects.filter(status=1)
    json_data = serializers.serialize("json", query_set)
    return HttpResponse(json_data,content_type="application/json")


def get_bad_acounts(request):
    '''
    获取被ban的账号
    :param request:
    :return:
    '''
    query_set = Acounts.objects.filter(status=2)
    json_data = serializers.serialize("json", query_set)
    return HttpResponse(json_data, content_type="application/json")

def update_cookie(request):
    phone = request.POST.get('phone')
    cookie = request.POST.get('cookie','')
    obj = Acounts.objects.filter(phone=phone)
    obj.cookie=cookie
    obj.save()