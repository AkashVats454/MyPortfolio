from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()

        return context

def user_info(request):
        if request.method == 'POST':
            if request.POST.get('full_name') and request.POST.get('email') and request.POST.get('messages'):
                user=User()
                user.full_name = request.POST.get('full_name')
                user.email = request.POST.get('email')
                user.messages = request.POST.get('messages')
                user.save()


                return render(request, 'home.html')

        else:
                return render(request,'home.html')
