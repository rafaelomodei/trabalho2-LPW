
from django.shortcuts import render

def index(request):
    return render(request, 'disciplineFSI/index.html')