from django.shortcuts import render
from django.http import HttpResponse #new
# Create your views here.

def main(request,name):
    return HttpResponse(f"Salom {name}")

# def name(request);
#     print