
from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20, label='Your Name', required=True)
    email = forms.EmailField(label='Your Email Address', required=True)
    subject = forms.CharField(max_length=100, label='Subject', required=True)
    message = forms.CharField(widget=forms.Textarea)


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,'contact.html',{'form': form,'submitted':submitted})
