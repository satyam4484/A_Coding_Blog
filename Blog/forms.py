from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import Textarea, Widget
from .models import postmodel
from ckeditor.widgets import CKEditorWidget
   

# this form inherits usercreation form sign up user 
class formsignup(UserCreationForm):
    ''' i have bascilly added some css classes '''

    username=forms.CharField(label_suffix=' ',label='Username',widget = forms.TextInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline','placeholder':'username'}))
    first_name = forms.CharField(label_suffix=' ',label='First Name ',widget = forms.TextInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline','placeholder':'First Name'}))
    last_name = forms.CharField(label_suffix=' ',label='Last Name ',widget = forms.TextInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline','placeholder':'Last Name'}))
    email=forms.CharField(label_suffix=' ',label='Email',widget = forms.TextInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline','placeholder':'Personal Email'}))
    password1=forms.CharField(label_suffix=' ',label='Password',widget = forms.PasswordInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline','placeholder':'Enter password'}))
    password2=forms.CharField(label_suffix=' ',label='password (confirm) ',widget = forms.PasswordInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline','placeholder':'Enter again'}))

    # display the feilds in form 
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']


# this is user login form which inherits authentication form 
class formlogin(AuthenticationForm):
    username=forms.CharField(label_suffix=' ',label='Username',widget = forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password=forms.CharField(label_suffix=' ',label='Password',widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}))
    class Meta:
        model = User
        fields = ['username']
    
# contact form so that user can contact 
class contactform(forms.Form):
    name = forms.CharField(label='FULL Name',label_suffix=' ',widget=forms.TextInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline'}))
    email= forms.EmailField(label ='EMAIL',label_suffix=' ',widget=forms.EmailInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline'}))
    message = forms.CharField(label = 'MESSAGE' ,label_suffix=' ',widget = forms.Textarea(attrs={'class':'w-full h-32 bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline'}))


# post form which basiclly save data to post model so it is model form combined from model.py 
class postform(forms.ModelForm):
    title = forms.CharField(label ='Title ',label_suffix=' ',widget = forms.TextInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline'}))
    language = forms.CharField(label ='Language',label_suffix=' ',widget=forms.TextInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline'}))
    des = forms.CharField(label='Description',label_suffix=' ',widget=forms.Textarea(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline'}))
    code = forms.CharField(label = 'Code ',label_suffix=' ',widget=forms.Textarea(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline',}))
    # postedon = forms.DateField(label='Posted on ',label_suffix=' ',widget=forms.DateInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline'}))

    class Meta:
        model = postmodel
        fields = ['title','language','des','code']


# user profile change form ( modification required )
class formchange(UserChangeForm):
    # username = forms.CharField(label_suffix=' ',label='User Name',widget=forms.TextInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline'}))
    # email = forms.EmailField(label_suffix=' ',widget=forms.TextInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline'}))
    # first_name = forms.CharField(label_suffix=' ',widget=forms.TextInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline'}))
    # last_name = forms.CharField(label_suffix=' ',widget=forms.TextInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline'}))
    # date_joined = forms.DateField(label_suffix=' ',widget=forms.TextInput(attrs={'class':'w-full bg-gray-300 text-gray-900 mt-2 p-3 rounded-lg focus:outline-none focus:shadow-outline'}))
    # # last_login = forms.CharField(label_suffix=' ')
    password=None
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','date_joined','last_login']
        labels = {
            'username':'User Name',
            'email':'Email',
            'first_name':'First Name',
            'last_name':'Last Name',
            'date_joined':'Date Joined',
            'last_login':'Last Login'
        }
     