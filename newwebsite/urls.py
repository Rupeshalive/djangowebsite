"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name="home"),
    path('success.html', views.success, name='success'),
    path('about.html', views.about, name="about"),
    path('careers.html', views.careers, name="careers"),
    path('faqs.html', views.faqs, name="faqs"),
    path('web_solutions.html', views.web_solutions, name="web_solutions"),
    path('digital_marketing.html', views.digital_marketing, name="digital_marketing"),
    path('public_relation.html', views.public_relation, name="public_relation"),
    path('influencer.html', views.influencer, name="influencer"),
    path('testimonials.html', views.testimonials, name="testimonials"),
    path('blog.html', views.blog, name="blog"),
    path('contact_us.html', views.contact_us, name="contact_us"),
    path('our_team.html', views.our_team, name="our_team"),
    path('why_choose_us.html', views.why_choose_us, name="why_choose_us"),
    path('history.html', views.history, name="history"),

]
