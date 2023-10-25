from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .forms import ChartDataForm
from .models import ChartData  # 导入您的模型
from django.utils import timezone

# vote01的视图
def vote01(request):
    
    if request.method == 'POST':
        #form = ChartDataForm(request.POST)
        #if form.is_valid():
            # 提取需要的数据
        user = request.user
        vote_type = request.POST.get('vote')
        data = timezone.now()
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        number3 = int(request.POST.get('number3'))
        number4 = int(request.POST.get('number4'))
        number5 = int(request.POST.get('number5'))
        number6 = int(request.POST.get('number6'))
        number7 = int(request.POST.get('number7'))
        number8 = int(request.POST.get('number8'))
        number9 = int(request.POST.get('number9'))
        number10 = int(request.POST.get('number10'))
        number11 = int(request.POST.get('number11'))
        number12 = int(request.POST.get('number12'))
        number13 = int(request.POST.get('number13'))
        number14 = int(request.POST.get('number14'))
        number15 = int(request.POST.get('number15'))
        number16 = int(request.POST.get('number16'))
        
        chart_data = ChartData.objects.create(user=user, vote_type=vote_type, data=data, value1=number1, value2=number2,value3=number3,value4=number4,value5=number5,value6=number6,value7=number7,value8=number8,value9=number9,value10=number10,value11=number11,value12=number12,value13=number13,value14=number14,value15=number15,value16=number16)
        
        chart_data.save()
        return redirect('result01')  # 重定向到结果页面

    else:
        form = ChartDataForm()
        #判斷vote01還是vote02
        votetype='vote01'
        

    return render(request, 'issue/vote01.html', locals())

# vote02的视图（逻辑类似）
def vote02(request):
    if request.method == 'POST':
        form = ChartDataForm(request.POST)
        if form.is_valid():
            user = request.user
            vote_type = 'vote02'
            data = timezone.now()
            value1 = form.cleaned_data['value1']
            value2 = form.cleaned_data['value2']
            value3 = form.cleaned_data['value3']
            value4 = form.cleaned_data['value4']
            value5 = form.cleaned_data['value5']
            value6 = form.cleaned_data['value6']
            value7 = form.cleaned_data['value7']
            value8 = form.cleaned_data['value8']
            value9 = form.cleaned_data['value9']
            value10 = form.cleaned_data['value10']
            value11 = form.cleaned_data['value11']
            value12 = form.cleaned_data['value12']
            value13 = form.cleaned_data['value13']
            value14 = form.cleaned_data['value14']
            value15 = form.cleaned_data['value15']
            value16 = form.cleaned_data['value16']
            
            chart_data = ChartData(user=user, vote_type=vote_type, data=data, value1=value1, value2=value2,vaue3=value3,value4=value4,value5=value5,value6=value6,value7=value7,value8=value8,value9=value9,value10=value10,value11=value11,value12=value12,value13=value13,value14=value14,value15=value15,value16=value16)
            
            chart_data.save()
            return redirect('result02')  # 重定向到结果页面

    else:
        form = ChartDataForm()

    context = {'form': form}
    return render(request, 'issue/vote02.html', context)


# result01的视图
def result01(request):
    context = {
        'variable1': 'value1',
        'variable2': 'value2',
      # 添加其他变量
    }
    return render(request, 'issue/result01.html')

# result02的视图
def result02(request):
    context = {
      'variable1': 'value1',
      'variable2': 'value2',
    # 添加其他变量
  }
    return render(request, 'issue/result02.html')
  
# 处理表单的视图
def chart_data(request):
    if request.method == 'POST':
        form = ChartDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chart_data_success')  # 重定向到成功页面
        # 如果表单无效，仍然显示表单并提示错误
    else:
        form = ChartDataForm()

    context = {'form': form}
    return render(request, 'issue/chart_data_form.html', context)

# 成功页面视图
def chart_data_success(request):
    return render(request, 'issue/chart_data_success.html')
  
# bigissue的视图
def bigissue(request):
    return render(request, 'issue/bigissue.html', locals())


