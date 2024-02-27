from django import forms
from carapp.models import OrderVehicle


class OrderVehicleForm(forms.ModelForm):
    class Meta:
        model = OrderVehicle
        fields = ['vehicle', 'buyer', 'num_ordered']
        # Display as a dropdown
        widgets = {'buyer': forms.Select(attrs={'size': 1})}
        # Custom label for num_ordered
        labels = {'num_ordered': 'Number of Vehicles Ordered'}


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(max_length=200, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')
