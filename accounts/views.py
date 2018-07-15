from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

from accounts.models import Acounts


def index(request):
    return render(request,'accounts/index.html')

# 展示账号数据
def account_list(request):
    # query_list = Acounts.objects.all()
    # # 15个一页 分页
    # paginator = Paginator(query_list, 15)
    # page_request_var = 'page'
    # page = request.GET.get('page')
    # try:
    #     queryset = paginator.page(page)
    # except PageNotAnInteger:
    #     queryset = paginator.page(1)
    # except EmptyPage:
    #     queryset = paginator.page(paginator.num_pages)
    # context = {}
    # return

    return render(request,'accounts/accounts_list.html')

# 增加账号

# 删除账号

# 修改账号

# 查询账号