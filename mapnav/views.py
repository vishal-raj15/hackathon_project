from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm

from mapnav.forms import signupform  #we ARE USING OUR OWN FORM

from django.contrib import messages

from django.contrib.auth.decorators import login_required



from .models import Order





# Create your views here.

def form_pg(request):
    return render(request,'mapnav/form_pg.html')

@login_required
def index(request):
    return render(request,'mapnav/index.html')




def first(request):
    return render(request,'mapnav/first.html')

def activity(request):
    return render(request,'mapnav/activity.html')

def order(request):

    if request.method =="POST":
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        phone = request.POST.get('phone', '')
        
        order=Order(name=name,amount=amount, phone=phone)
        order.save()
        

    return render(request , 'mapnav/order.html')

def login(request):
    if request.method == 'POST':
        if not request.POST.get('remember',None):
            request.session.set_expiry(0)
    return redirect("/mapnav/login/")


def logout(request):
    #messages.success(request, f'{username} have been logged out! ')
    return redirect("/mapnav/first/")

def signup(request):
    form = signupform()
    if request.method =='POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'account created for {username}! ')
            
            return redirect("/mapnav/first/")  #/mapnav/first/
         
    else:
        messages.warning(request, 'Please use alphabets with nos.')
        form = signupform()
            
    return render(request, 'mapnav/signup.html',{'form':form})

    #return HttpResponseRedirect("/mapnav/first/")



    


