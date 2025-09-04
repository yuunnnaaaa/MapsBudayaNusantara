from django.shortcuts import render
from .models import PopupInfo

# Create your views here.
def index(req):
    popup = PopupInfo.objects.all()
    
    context = {
        'pop_up': popup,
    }
    return render(req,'index_maps.html', context)