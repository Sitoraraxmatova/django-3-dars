from django.shortcuts import render
from django.http import HttpResponse #new


def main(request,name):
    return HttpResponse(f"Salom {name}")

