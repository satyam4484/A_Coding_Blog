from django.urls import path
from . import views

# blofg urls 
urlpatterns = [


    path('',views.home,name='home'),            # link to home page 
    path('dashboard/',views.dashboard,name='dashboard'),  # link to user dashboard 
    path('Contact/',views.contact,name='contact'),      # link to contact form 
    path('signup/',views.usersignup,name='signup'),     # for user sign up 
    path('login/',views.userlogin,name='login'),       # for user login 
    path('logout/',views.userlogout,name='logout'),      # user logout       
    path('view/<int:id>',views.viewdata,name='viewdata'),    # viewing a particular post separetly
    path('Edit/<int:id>',views.Edit,name='edit'),             # edit the partiular post by user 
    path('Delete/<int:id>',views.deletedata,name='delete'),    # delete the partiular post by user 
    path('addpost/',views.addpost,name='addpost'),             # add a particular post 
    path('editprofile',views.editprofile,name='editprofile'),   # edit the user profile 
    path('search',views.search,name='search'),                  # search function to search in blog 
]
