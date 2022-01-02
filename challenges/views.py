from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
     challenge_text = None
     if month == 'january':
          challenge_text = 'Take a shower and get some exercise, ya filthy animal'
     elif month == 'february':
          challenge_text = "It's february in Texas, where nothing breaks easy."
          

