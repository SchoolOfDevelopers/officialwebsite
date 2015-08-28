from django.views.generic.edit import CreateView
from django.views.generic import View,ListView
from django.http import HttpResponse
from django.shortcuts import render
from Enquiry.models import Enquiry
from Internship.models import Internship
from Career.models import CareerApplyModel
from django import get_version


class Index(CreateView):
    template_name = 'home.html'
    model = Enquiry
    fields = ['name', 'email', 'subject', 'message']
    success_url = '/Success'
class CareerDisplayView(ListView):
    template_name = 'career.html'

class InternshipApplyView(CreateView):
    template_name = 'internship.html'
    model = Internship
    fields = '__all__'

class CareerApplyView(CreateView):
    template_name = 'career_apply.html'
    model = CareerApplyModel
    fields = '__all__'

class ContactUs(CreateView):
    template_name = 'contactus.html'
    model = Enquiry
    fields = ['name', 'email', 'subject', 'message']
    success_url = '/Success'
