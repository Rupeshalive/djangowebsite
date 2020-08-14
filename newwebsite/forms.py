from django import forms

class ContactForm(forms.Form):
    #name = forms.CharField(max_length=100)
    #email = forms.EmailField()
    #company = forms.CompanyField(max_length=100)
    #inquiry = forms.InquiryField()
    #message = forms.CharField(widget=forms.Textarea)
    #subject = forms.CharField(max_length=100)
    #message = forms.CharField(widget=forms.Textarea)
    #sender = forms.EmailField()
    #cc_myself = forms.BooleanField(required=False)
    
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')