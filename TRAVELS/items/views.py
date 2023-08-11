from django.shortcuts import render,redirect

# Create your views here.
from .models import destination,agencies,booking
from .forms import booking_form
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

@login_required
def home_view(request):
    content=True
    content1=True
    content2=False
    context={
        'content':content,
        'content1':content1,
        'content2':content2,
    }

    return render(request,'items/home.html',context)

@login_required
def booking_view(request):
    form=booking_form(request.POST or None)
    content=True
    content1=False
    content2=True
    context={
        'form':form,   
        'content':content,
        'content1':content1,
        'content2':content2, 
    }
    
    if form.is_valid():
        
        obj=form.save()
        
        context['success']='True'
        context['obj']=obj
    return render(request,'items/booking.html',context)

@login_required    
def agency_view(request):
    content=True
    content1=False
    content2=True
    agenci=agencies.objects.all()
    des=destination.objects.all()
    context={
        'agenci':agenci,
        'des':des,
        'content':content,
        'content1':content1,
        'content2':content2,
    }   
    
    return render(request,'items/agencies.html',context)

@login_required
def route_view(request,id=None):
    content=True
    content1=False
    content2=False
    context={
        'content':content,
        'content1':content1,
        'content2':content2,
    }
    if id:
        
        des=destination.objects.get(id=id)   
        context['des']=des
        
        return render(request,'items/route.html',context=context)

@login_required
def booking_list_view(request):
    book=booking.objects.all()
    content=True
    content1=False
    content2=False
    form={
        'book':book,
        'content':content,
        'content1':content1,
        'content2':content2,
    }    
    return render(request,'items/booking_list.html',form)

def registration_view(request):
    user=UserCreationForm(request.POST or None)
    content=False
    content1=False
    content2=True
    context={
        'user':user,
        'content':content,
        'content1':content1,
        'content2':content2,
    }
    if user.is_valid():
        user.save()
        return redirect('/login/')
        
    return render(request,'items/registration.html',context)

def login_view(request):
    user=AuthenticationForm(data=request.POST or None)
    if user.is_valid():
        form=user.get_user()
        login(request,form)
        return redirect('/')
    content=True
    content1=False
    content2=False
    context={
        "user":user,
        'content':content,
        'content1':content1,
        'content2':content2,
    }
    return render(request,'items/login.html',context)

@login_required
def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('/login/')
    return render(request,'items/logout.html',{})

        