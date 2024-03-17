from django import forms
from django.contrib.auth.forms import UserCreationForm
from carapp.models import OrderVehicle, Vehicle, User


class OrderVehicleForm(forms.ModelForm):
    class Meta:
        model = OrderVehicle
        fields = ['vehicle', 'buyer', 'num_ordered']
        # Display as a dropdown
        widgets = {'buyer': forms.Select(attrs={'size': 1})}
        # Custom label for num_ordered
        labels = {'num_ordered': 'Number of Vehicles To Order'}


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(max_length=200, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')


class SearchVehicleForm(forms.Form):
    car_name = forms.ModelChoiceField(queryset=Vehicle.objects.all(), empty_label="Select Vehicle")


class SearchCartypeForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['car_type']
        # Display as a dropdown
        widgets = {'car_type': forms.Select(attrs={'size': 1})}


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]
