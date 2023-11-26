from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
# Create your views here.
def home(request):
    print('SPOTIFY')
    return render(request,'home.html')