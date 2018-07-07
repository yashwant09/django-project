from django.shortcuts import render
from myfirst_app.forms import RegistrationForm,Login_form
from myfirst_app.models import RegistrationModel
from django.http import  HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
    return render(request,'myfirst_app/index.html')

def userhome(request):
    return render(request,'myfirst_app/userhome.html')

def login_view(request):
    login_form = Login_form
    if request.method == 'POST':
        l_form = Login_form(request.POST)
        if l_form.is_valid():
            uname = request.POST.get('email')
            paswd = request.POST.get('password')
            has_registered = False
            for obj in RegistrationModel.objects.all():
                if obj.email == uname and obj.password == paswd:
                    return HttpResponseRedirect(reverse('userhome'))
            if not has_registered:
                return HttpResponse("Invalid login details")

    return render(request,'myfirst_app/login.html',context={'login_form': login_form})

def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

    return render(request,'myfirst_app/registration.html',context={'singupform':RegistrationForm})