from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):

    records = Record.objects.all()


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request=request, username= username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "SUcess!!")
            return redirect('home')
        else:
            messages.success(request, "Failed...")
            return redirect('home')


    else:
        return render(request, "home.html", {'records': records})

# def login_user(request):

#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username = username, password= password)
            login(request, user)
            messages.success(request, "You have registered")
            return redirect('home')
    else:
        form =  SignUpForm()
        return render(request, "register.html", {'form': form})
    
    return render(request, "register.html", {'form': form})

    

def customer_record(request, pk):
    if request.user.is_authenticated:
        req_record = Record.objects.get(id=pk)
    
        return render(request, "record.html", {'customer_record': req_record})
    
    else:
        messages.success(request, "You Must Be Logged In To Do This Operation")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To Do This Operation")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid:
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
            
        return render(request, "add_record.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In To Do This Operation")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        # print(request)

        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            # print(form)
            messages.success(request, "Record Updated...")
            return redirect('home')
        
        return render(request, "update_record.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In To Do This Operation")
        return redirect('home')

        








        