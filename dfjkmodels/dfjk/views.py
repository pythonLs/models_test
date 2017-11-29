from django.shortcuts import render,HttpResponse
from dfjk.models import Device

# Create your views here.


def load(request):
    return render(request, 'index.html')

def add(request):
    device = Device.objects.create(device_id = request.POST['a'])
    print ('ok')
    return HttpResponse('ok')