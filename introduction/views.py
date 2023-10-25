#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import SDGs
from .forms import SDGsForm, RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def sdgs(request):
  q = request.GET.get('q', None)
  sdgs = ''
  if q is None or q is "":
    sdgs = SDGs.objects.all()
  elif q is not None:
    sdgs = SDGs.objects.filter(title__contains=q)
  return render(request, 'SDGs/sdgs.html', {'sdgs': sdgs})


def detail(request, slug=None):
  sdgs = get_object_or_404(SDGs, slug=slug)
  return render(request, 'SDGs/detail.html', locals())


def create(request):
  if request.method == 'POST':
    form = SDGsForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('sdgs/')
  else:
    form = SDGsForm()
  return render(request, 'SDGs/edit.html', {'form': form})


def edit(request, pk=None):
  sdgs = get_object_or_404(SDGs, pk=pk)
  if request.method == "POST":
    form = SDGsForm(request.POST, instance=sdgs)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('sdgs/')
  else:
    form = SDGsForm(instance=sdgs)

  return render(request, 'SDGs/edit.html', {'form': form})


def delete(request, pk=None):
  sdgs = get_object_or_404(SDGs, pk=pk)
  sdgs.delete()
  return render(request, 'sdgs/')


#註冊
def sign_up(request):
  form = RegisterForm()
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
      redirect('/login')  #重新導向到登入畫面
  context = {'form': form}
  return render(request, 'CookieSessionApp/register.html', context)