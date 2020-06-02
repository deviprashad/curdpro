from django.shortcuts import render
from .models import ProductData
from .forms import ProductDeleteForm,ProductUpdateForm,ProductInsertForm
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')
def create(request):
    if request.method == 'POST':
        cform=ProductInsertForm(request.POST)
        if cform.is_valid():
            pid1=request.POST.get('pid','')
            pname1=request.POST.get('pname','')
            pcost1=request.POST.get('pcost','')
            pcolor1=request.POST.get('pcolor','')
            pclass1=request.POST.get('pclass','')
            cname1=request.POST.get('cname','')
            cmob1=request.POST.get('cmob','')
            cemail1=request.POST.get('cemail','')
            data=ProductData(
                pid=pid1,
                pname=pname1,
                pcost=pcost1,
                pcolor=pcolor1,
                pclass=pclass1,
                cname=cname1,
                cmob=cmob1,
                cemail=cemail1
            )
            data.save()
            cform=ProductInsertForm()
            return render(request,'create.html',{'create':cform})
        else:
            return HttpResponse('Plz fill all the fields properly before submitting')
    else:
        cform = ProductInsertForm()
        return render(request, 'create.html', {'create': cform})
def retrive(request):
    rform=ProductData.objects.all()
    return render(request,'retrive.html',{'retrive':rform})
def update(request):
    if request.method=='POST':
        uform=ProductUpdateForm(request.POST)
        if uform.is_valid():
            pid1=request.POST.get('pid','')
            pcost1=request.POST.get('pcost','')
            data=ProductData.objects.filter(pid=pid1)
            if not data:
                return HttpResponse('ID not Found')
            else:
                data.update(pcost=pcost1)
                uform=ProductUpdateForm()
                return render(request,'update.html',{'update':uform})
        else:
            return HttpResponse('Plz fill all the fields properly before submitting')
    else:
        uform = ProductUpdateForm()
        return render(request, 'update.html', {'update': uform})
def delete(request):
    if request.method=='POST':
        dform=ProductDeleteForm(request.POST)
        if dform.is_valid():
            pid1=request.POST.get('pid','')
            data=ProductData.objects.filter(pid=pid1)
            if not data:
                return HttpResponse('Id not found')
            else:
                data.delete()
                dform=ProductDeleteForm()
                return render(request,'delete.html',{'delete':dform})
        else:
            return HttpResponse('Plz fill all the fields properly before submitting')
    else:
        dform = ProductDeleteForm()
        return render(request, 'delete.html', {'delete': dform})

# Create your views here.
