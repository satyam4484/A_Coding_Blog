from django.contrib.auth import authenticate
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login,logout
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import   Paginator,PageNotAnInteger,EmptyPage
from .forms import formsignup,formlogin,contactform,postform,formchange
from .models import postmodel
# Create your views here.

# home page view which also show the paginator 
def home(request):
    form = postmodel.objects.all()   # fetch all post form postmodel 

    paginator = Paginator(form,5)    #paginator function 
    page = request.GET.get('page')
    try:
        form = paginator.page(page)
    except PageNotAnInteger:
        form = paginator.page(1)
    except EmptyPage:
        form = paginator.page(paginator.num_pages)
    return render(request,'home.html',{'form':form})


# user dashboard page 
def dashboard(request):
    if request.user.is_authenticated:    # only authenticated user can see dashboard 
        # fetch the particular user post form blog models 
        form = postmodel.objects.filter(user = request.user)

        # paginator code for user 
        paginator = Paginator(form,5)
        page = request.GET.get('page')
        try:
            form = paginator.page(page)
        except PageNotAnInteger:
            form = paginator.page(1)
        except EmptyPage:
            form = paginator.page(paginator.num_pages)

        # data=formchange()
        # Return all user post to dashboard page 
        return render(request,'dashboard.html',{'form':form})

        # if user is not authenticted the he need to first login 
    else:   
        return HttpResponseRedirect('/login/')


# this function is used to fetch the particular post and pass it to view page 
def viewdata(request,id):
    form = postmodel.objects.get(pk=id)
    return render(request,'view.html',{'form':form})


# this function delets the particular post only requested by user 
def deletedata(request,id):
    if request.method == 'POST':
        md = postmodel.objects.get(pk = id)
        md.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/')
    

# def retrive(request):
#     try:
#         profile = request.user.profile
#     except postmodel.DoesNotExist:
#         profile = postmodel(user = request.user)
#         profile.save()
#     return profile

# this is used to edit user profile 
def editprofile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            # userprofile = retrive(request)
            form = formchange(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
        
        else:
            # userprofile = retrive(request)
            form = formchange(instance=request.user)
        return render(request,'profile.html',{'form':form})

# this function add a post when user is login 
def addpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # fetch the form data and save it 
            form=postform(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return HttpResponseRedirect('/dashboard/')
        else :
            form = postform()
        return render(request,'edit.html',{'form':form})
        
    else:
        return HttpResponseRedirect('/')     # if user is not login then redirect to home page 

# this function edit the particular post requested by user 
def Edit(request,id):
    if request.method == 'POST':
        md = postmodel.objects.get(pk=id)
        form = postform(request.POST,instance=md)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        md = postmodel.objects.get(pk=id)
        form = postform(instance=md)

    return render(request,'edit.html',{'form':form,'data':md})


# this is contact page which contact the user ( modification required )
def contact(request):
    if request.method =='POST':
        form = contactform(request.POST)
        if form.is_valid():
            subject = f"HI i am {form.cleaned_data['name']} need help ."
            message = form.cleaned_data['message']
            emailfrom = form.cleaned_data['email']
            print(form.cleaned_data['email'])
            to = [settings.EMAIL_HOST_USER,]
            send_mail(subject,message,emailfrom,to)
        form=contactform()
        
    else:
        form = contactform()
    return render(request,'contact.html',{'form':form})

# it is the search function which search the data with title whenever somone searched  in blog 
def search(request):
    name =request.GET['query']
    form = postmodel.objects.filter(title__icontains = name)
    # paginator = Paginator(form,2)
    # page = request.GET.get('page')
    # try:
    #     form = paginator.page(page)
    # except PageNotAnInteger:
    #     form = paginator.page(1)
    # except EmptyPage:
    #     form = paginator.page(paginator.num_pages)
    
    return render(request,'search.html',{'name':name,'form':form})

# this is the user sign up page which also sends the mail to user when he sign up 
def usersignup(request):
    if not request.user.is_authenticated:     # when user is already login then he cant again sign up 
        if request.method == 'POST':
            form = formsignup(request.POST)
            if form.is_valid():
                form.save()
                subject = f"welcome to out site {form.cleaned_data['username']} "
                message= f"This is a secret mail to you so that you cant forget your login details  username - {form.cleaned_data['username']} and password - {form.cleaned_data['password1']}"
                emailto = [form.cleaned_data['email'],]
                send_mail(subject,message,settings.EMAIL_HOST_USER,emailto)
                # messages.success(request,"Sign up succefully")
                return HttpResponseRedirect('/login/')
        else :
            form = formsignup()
        return render(request,'signup.html',{'form':form})
    else :
        return HttpResponseRedirect('/')
                
    
# user login form from forms.py 
def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = formlogin(request= request,data = request.POST)

            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = uname,password = upass)

                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')
        else:
            form = formlogin()
        return render(request,'login.html',{'form':form})
    else :
        return HttpResponseRedirect('/')


# user logout function 
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# def 