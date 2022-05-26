from django.shortcuts import render
from django.views.generic import DetailView
from . models import Doctor
# Create your views here.


class DoctorDetailView(DetailView):
    model = Doctor
