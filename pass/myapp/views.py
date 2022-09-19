from django.contrib.auth.models import user
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def index (request):

    return render(request,'index.html')

def register (request):
    if request.method=='POST':
       if 'sign-up-form' in request.POST:
          username=request.post.get('username')
          email=request.post.get('email')
          password=request.post.get('password')
          password2=request.post.get('password2')
       if password!=password2:
         msg='Yooh, your passwords are not the same'
         messages.error(request,msg)
         return HttpResponseRedirect (request.index)
    if user.object.filter(username=username).exists():
         msg=f"{username}already exists"
         messages.error(request,msg)
         return HttpResponseRedirect (request.index)

    
    return render(request,'register.html')    