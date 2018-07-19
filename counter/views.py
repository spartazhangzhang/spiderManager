import datetime

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from counter.models import Counter

# 获取当天的数据.
def get_data(request):
    date = datetime.date.today()
    data = Counter.objects.filter(timestamp=date)
    json_data = serializers.serialize("json", data)

    return render(request,'counter/today.html')

# 保存数据到数据库
def data_handler(request):
    data_number = request.GET.get('number')
    date = datetime.date.today()
    print(date)
    print(data_number)
    Counter.objects.create(timestamp=date,number=data_number).save()
    return JsonResponse({'status':'success'})
