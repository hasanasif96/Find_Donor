from django.urls import path
from .views import *

app_name= "plasmadonor"

urlpatterns=[
        path("", HomeView.as_view(), name="home"),
        path("contact/", contact.as_view(), name="contact"),
        path("explore/", explore.as_view(), name="explore"),
        path("donor-register/", Donorcreateview.as_view(), name="registerdonor"),
        path("request/<int:d_id>/", Requestview.as_view(), name="request"),
        path("register/", CustomerRegistrationView.as_view(), name="customerregistration"),
        path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
        path("login/", CustomerLoginView.as_view(), name="customerlogin"),
        path("allrequest/", allrequestview.as_view(), name="allrequest"),
        path("acceptedrequest/", acceptedrequests.as_view(), name="acceptedrequests"),
        path("manage-request/<int:r_id>/", managerequestview.as_view(), name="managerequest"),
        path("requestmade/", requestmadeview.as_view(), name="requestmade"),
        path("managedonor/", mydonorview.as_view(), name="managedonor"),
        path("manage-donors/<int:d_id>/", managedonorview.as_view(), name="deldonor"),
        
        
        
        
]





