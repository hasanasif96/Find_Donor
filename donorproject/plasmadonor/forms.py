from django import forms
from .models import Customer, Donor, requests,User


Blood_choices = (
    ("Don't know", "Don't know"),
    ("O+", "O+"),
    ("O-", "O-"),
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
)
class Donorform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Blood_Group = forms.CharField(widget=forms.Select(choices=Blood_choices,attrs={'class':'form-control', 'placeholder':'Choose field'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    when_Recovered = forms.DateField(widget=forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'YYYY-MM-DD'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Donor
        fields = ["name", "age", "Blood_Group", "city", "when_Recovered", "description"]
        
situation_choices = (
    ("Very Serious", "Very Serious"),
    ("In Ventilator", "In Ventilator"),
    ("Oxygen Below 50", "Oxygen Below 50"),
    ("Not so serious", "Not so serious"),

)        
        
class CheckoutForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    currrent_situation = forms.CharField(widget=forms.Select(choices=situation_choices,attrs={'class':'form-control', 'placeholder':'Choose field'}))

    class Meta:
        model = requests
        fields = ["name", "city","mobile", "email", "currrent_situation"]
        
        
class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Customer
        fields = ["username", "password", "email", "full_name", "address"]
        
        
        
    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "Customer with this username already exists.")
        return uname
    
    
class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
