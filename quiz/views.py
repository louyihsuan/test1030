from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    current_time = datetime.now().time()
    return render(request, 'index.html', {'current_time':current_time})