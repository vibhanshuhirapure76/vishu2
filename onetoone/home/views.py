from django.shortcuts import render
from .models import Student,Trainer
def home(request):
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'index.html',{'tr':tr,'st':st})
def addtrainers(request):
    t=Trainer()
    t.tname=request.POST['tname']
    t.language=request.POST['lang']
    t.save()
    tr=Trainer.objects.all()
    st=Student.objects.all()
    return render(request,'index.html',{'tr':tr,'st':st})
