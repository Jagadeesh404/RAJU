from django.shortcuts import render
from testapp.models import Hydjobs
from testapp.models import Apjobs
from testapp.models import Kajobs

# Create your views here.
def Homepage_view(request):
    return render(request,'testapp/index.html')

def Hydjobs_view(request):
    jobs_list = Hydjobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',my_dict)

def Apjobs_view(request):
    jobs_list = Apjobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/apjobs.html',my_dict)

def Kajobs_view(request):
    jobs_list = Kajobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/ka.html',my_dict)