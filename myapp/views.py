from django.shortcuts import render
from django.http import HttpResponse #new


def main(request):
    return render(request,"index.html")

