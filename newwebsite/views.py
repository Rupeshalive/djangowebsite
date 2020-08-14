from django.views.decorators.csrf import requires_csrf_token
from django.template.defaulttags import csrf_token
from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.core.mail import send_mail
from django.template.context_processors import csrf
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect




from django.views.decorators.csrf import csrf_protect

from django.template import RequestContext, Template, Context
from django.views.generic import View
#from django.core.context_processors import csrf
from django.http import HttpResponse # Add this

from .forms import ContactForm
from django import forms # Add this


# Create your views here.

#@csrf_protect
#@csrf_token()
def home(request):
	if request.method == "POST" and "email" and "name":
		#con_name = request.POST['con_name']
		#con_email = request.POST['con_email']
		#con_company = request.POST['con_company']
		#inquiry = request.POST['inquiry']
		#con_message = request.POST['con_message']
		#context = RequestContext(request)
		#context_dict={'con_name':con_name}
		#context_dict.update(csrf(request))
		#return render(request, 'home.html',{'con_name':con_name })

	#else:
		#return render(request, 'home.html',{})
		form = ContactForm(request.POST)
		
		if form.is_valid():
			pass  # does nothing, just trigger the validation
			send_mail(
    			'name',
    			'message.',
    			'email',
    			['web.transcendent@gmail.com'],
    			fail_silently=False,
					)
		
	else:	
		form = ContactForm()
	return render(request, 'home.html', {'form': form})



def about(request):
	return render(request, 'about.html',{})

def careers(request):
	return render(request, 'careers.html',{})

def faqs(request):
	return render(request, 'faqs.html',{})

def web_solutions(request):
	return render(request, 'web_solutions.html',{})

def digital_marketing(request):
	return render(request, 'digital_marketing.html',{})

def public_relation(request):
	return render(request, 'public_relation.html',{})

def influencer(request):
	return render(request, 'influencer.html',{})

def testimonials(request):
	return render(request, 'testimonials.html',{})

def blog(request):
	return render(request, 'blog.html',{})
#@cache_page(60 * 15)
#@csrf_protect
#@requires_csrf_token
def contact_us(request):
	#if request.method == 'POST':
		#con_name = request.POST['con_name']
		#con_email = request.POST['con_email']
		#con_company = request.POST['con_company']
		#inquiry = request.POST['inquiry']
		#con_message = request.POST['con_message']
		#context = RequestContext(request)
		#context={'con_name':con_name,'con_email':con_email,'con_email':con_email,'inquiry':inquiry, 'con_message':con_message }
		#context_dict.update(csrf(request))
		#return render(request, 'contact_us.html', context)
		#return render(request, 'contact_us.html',{'con_name':con_name})

	#else:
	return render(request, 'contact_us.html',{})
	

def our_team(request):
	return render(request, 'our_team.html',{})

def why_choose_us(request):
	return render(request, 'why_choose_us.html',{})

def history(request):
	return render(request, 'history.html',{})
