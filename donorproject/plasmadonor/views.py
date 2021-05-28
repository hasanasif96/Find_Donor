from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView,FormView, DetailView, ListView
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .forms import *
from django.db.models import Q
from django.contrib import messages
from .filters import DonorFilter









class HomeView(TemplateView):
    template_name= "home.html"
    
    
class contact(TemplateView):
    template_name= "contact.html"
    
    
class explore(TemplateView):
    template_name= "alldonor.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        donor=Donor.objects.all()
        
        donorfilter=DonorFilter(self.request.GET, queryset=donor)
        donor=donorfilter.qs
        context['donorfilter']=donorfilter
        context['alldonors'] = donor
        return context
    
    
class Donorcreateview(CreateView):
    template_name = "registerdonor.html"
    form_class = Donorform
    success_url = reverse_lazy("plasmadonor:home")


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.customer:
            pass
        else:
            return redirect("/login/?next=/donor-register/")
        return super().dispatch(request, *args, **kwargs)
    
    
    def form_valid(self, form):
        requests=form.save(commit=False)
        requests.d_user=self.request.user.customer
        requests.save()
        return super().form_valid(form)


class Requestview(CreateView):
    template_name = "checkout.html"
    form_class = CheckoutForm
    success_url = reverse_lazy("plasmadonor:home")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['d_id']
        donor = Donor.objects.get(id=url_slug)
        context['donor'] = donor
        return context
    
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.customer:
            pass
        else:
            return redirect("/login/?next=/request/<slug:slug>/")
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        url_slug = self.kwargs['d_id']
        donor=Donor.objects.get(id=url_slug)
        if donor.d_user==self.request.user.customer:
            messages.success(self.request, 'OOPS!!! You cannot send request to yourself')
            return redirect("/explore")
        else:
            requests=form.save(commit=False)
            requests.create_by=self.request.user.customer
            requests.donor=donor
            requests.save()
            messages.success(self.request, 'Congratulations!!! You have succesfuly made request to the donor.')
            return super().form_valid(form)
    
class CustomerRegistrationView(CreateView):
    template_name = "customerregistration.html"
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy("plasmadonor:home")
    
    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        login(self.request, user)
        return super().form_valid(form)


class CustomerLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("plasmadonor:home")


class CustomerLoginView(FormView):
    template_name = "customerlogin.html"
    form_class = CustomerLoginForm
    success_url = reverse_lazy("plasmadonor:home")

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and usr.customer:
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})

        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url 
        
        

class allrequestview(TemplateView):
    template_name = "allrequest.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name=self.request.user.customer
        exclude_list = ["Request Accepted", "Request Cancelled"]
        orders = requests.objects.filter(donor__d_user=name).exclude(Q(order_status="Request Accepted") | Q(order_status="Request Cancelled")).order_by("-id")
        context["orders"] = orders
        return context


class acceptedrequests(TemplateView):
    template_name = "acceptedrequests.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name=self.request.user.customer
        accepted = requests.objects.filter(donor__d_user=name).exclude(order_status="Request Pending").order_by("-id")
        context["accepted"] = accepted
        return context


class managerequestview(View):
    def get(self, request, *args, **kwargs):
        r_id = self.kwargs["r_id"]
        action = request.GET.get("action")
        request_obj = requests.objects.get(id=r_id)

        if action == "acc":
            request_obj.order_status = "Request Accepted"
            request_obj.save()
        elif action == "rmv":
            request_obj.order_status = "Request Cancelled"
            request_obj.save()
        else:
            pass
        return redirect("plasmadonor:allrequest")
    
    
    
    
class requestmadeview(TemplateView):
    template_name = "notification.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name=self.request.user.customer
        orders = requests.objects.filter(create_by=name).order_by("-id")
        context["orders"] = orders
        return context
    
    
    
    
    
class mydonorview(TemplateView):
    template_name = "managedonor.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name=self.request.user.customer
        my_donor = Donor.objects.filter(d_user=name).order_by("-id")
        context["my_donor"] = my_donor
        return context
    
    
    
class managedonorview(View):
    
    def get(self, request, *args, **kwargs):
        d_id = self.kwargs["d_id"]
        action = request.GET.get("action")
        donor_obj = Donor.objects.get(id=d_id)

        if action == "del":
            donor_obj.delete()
        else:
            pass
        return redirect("plasmadonor:managedonor")
