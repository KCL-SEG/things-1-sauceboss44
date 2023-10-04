from django.shortcuts import render

def home(response):
    response = render(response, 'home.html')
    return response