from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from .forms import AddForm


def compute(request):
    return render(request, 'index.html')


def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = ''
    if a == '' or b == '':
        c = 'Error'
    else:
        c = str(int(a)+int(b))

    return HttpResponse(c)


"""
def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))
    else:
        form = AddForm()
        return render(request, 'compute.html', {'form': form})
"""


def index(request):
    return render(request, 'index1.html')