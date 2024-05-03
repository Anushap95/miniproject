from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import FoodItem
from .forms import Itemdetail


def Index(request):
    item=FoodItem.objects.all()
    context ={
    'items':item
    }
    return render(request,'ind.html',context)


def home(request):
    return render(request, 'base.html')

def menu(request):
    menu_items = FoodItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')








def detail(request,id):
    item = FoodItem.objects.get(id=id)
    return render(request,'detail.html',{'items':item})
 
def create_item(request):
    form = Itemdetail(request.POST or None, request.FILES or None)
    if form.is_valid():
        image=form.cleaned_data.get('image')
        name=form.cleaned_data.get('name')
        desc=form.cleaned_data.get('desc')
        price=form.cleaned_data.get('price')
        obj=FoodItem.objects.create(name=name,desc=desc,price=price,image=image)
        obj.save()
        form.save()
        return redirect('Index')
    return render(request,'item-add.html',{'form':form})


def order_item(request,id):
    item = FoodItem.objects.get(id=id)
    form = Itemdetail(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('Index')
    return render(request,'item_update.html',{'form':form,'items':item})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('success')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request,user)
            # Redirect to a success page.
            return redirect('success')
    else:
        return render(request,'register.html')
    


def logout_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('success')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
