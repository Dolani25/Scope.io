from django.shortcuts import render , redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

#scope.core/views.py

from core.models import Airdrop, Blockchain, Task, Notification, FollowerProfile ,ScopeUser

from django.http import HttpResponse

#from .form import SignupForm, FileUploadForm


def index(req):
    
    airdrops = Airdrop.objects.all()
    
    return render(req , 'core/index.html',
    {
     'airdrops' : airdrops,
     
    })
    
    
def edit(req):
    return render(req , 'core/edit.html')
    
'''    
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})
    
'''    

        
        
def userprofile(req,username):
    user = ScopeUser.objects.get(username=username)
    return render(req, 'core/profile.html', {'user': user})
    
    
    
"""
 
@login_required       
def login(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        
        user = auth.authenticate(username=username , password=password)
        
        if user is not None:
            auth.login(req,user)
            if req.user.is_authenticated and req.user.username:
                return redirect('profile', username=req.user.username)
            else:
                return render(req , 'core/login.html')
    return render(req, 'core/login.html')
    
"""