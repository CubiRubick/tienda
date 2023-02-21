from django.shortcuts import render
from .forms import registerform
from django.views.generic import TemplateView

# Create your views here.
class homeDash(TemplateView):
    template_name = 'aut/login.html'

def register_request(request):
    if request.method == 'POST':
        form = registerform(data=request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'aut/register.html', {'formulario': form})