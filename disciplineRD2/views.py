
from django.shortcuts import render

def index(request):
    return render(request, 'disciplineRD2/index.html')