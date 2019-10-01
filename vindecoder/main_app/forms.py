from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(label='Ad',required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)

# class VincodeForm(forms.Form):
#     vin=forms.CharField( max_length=21)