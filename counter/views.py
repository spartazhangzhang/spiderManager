import datetime

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from counter.models import Counter

# 获取当天的数据.
def get_data(request):
    date = datetime.date.today()
    data = Counter.objects.filter(timestamp=date)
    json_data = serializers.serialize("json", data)
    return HttpResponse(json_data, content_type="application/json")

# 保存数据到数据库
def data_handler(request):
    data_number = request.GET.get('number')
    date = datetime.date.today()
    Counter.objects.create(timestamp=date,number=data_number)
    return JsonResponse({'status':'success'})