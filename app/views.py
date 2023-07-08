from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.views.generic import ListView,DetailView,CreateView
from app.models import *
from app.forms import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# Create your views here.


def home(request):
    if request.session.get('username'):
        username = request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')


def Register(request):
    UFO = UserForm()
    d={'UFO':UFO}
    if request.method == 'POST':
        UFO = UserForm(request.POST)
        if UFO.is_valid():
            NUFO=UFO.save(commit=False)
            password=UFO.cleaned_data['password']
            NUFO.set_password(password)
            NUFO.save()
            return HttpResponse("registration done successfully")

    return render(request,'rigistration.html',d)



def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('insert_data'))
        else:
            return HttpResponse('invalid username or password')
    

    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def insert_data(request):
    d={'CFO':CelebratyForm()}
    if request.method =='POST' and request.FILES:
        CO = CelebratyForm(request.POST,request.FILES)
        if CO.is_valid():
            CO.save()
            return HttpResponse("The data is inserted")
        else:
            return HttpResponse("the data is not valid")
    return render(request,'insert_data.html',d)


class CelebratyData(viewsets.ViewSet):
    def list(self,request):
        ADO=Celebraties.objects.all()
        SJD=CelebratyMS(ADO,many=True)
        d={'data':SJD.data}
        return render(request,'list.html',d)
     
    def retrieve(self,request,pk):
        TO=Celebraties.objects.get(pk=pk)
        SDO=CelebratyMS(TO)
        return Response(SDO.data)
    
    def update(self,request,pk):
        SPO=Celebraties.objects.get(pk=pk)
        SPD=CelebratyMS(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Celebrity is updated'})
        else:
            return Response({'Failed':'Celebrity is Not Updated'})
    
    def partial_update(self,request,pk):
        SPO=Celebraties.objects.get(pk=pk)
        SPD=CelebratyMS(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Celebrity is updated'})
        else:
            return Response({'Failed':'Celebrity is Not Updated'})
    def destroy(self,request,pk):
        Celebraties.objects.get(pk=pk).delete()
        return Response({'Deleted':'Celebrity is deleted'})


    



