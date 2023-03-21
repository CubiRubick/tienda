from django.shortcuts import render
from .forms import registerform
from django.views.generic import TemplateView

# Create your views here.
class homeDash(TemplateView):
    template_name = 'aut/login.html'

def register_request(request):
    response = ""
    if request.method == 'POST':
        form = registerform(data=request.POST)
        if form.is_valid():
            form.save()
            response = "Registrado Correctamente"
        else:
            response = " Usuario o Correo ya han sido utilizados"
    return render(request, 'aut/register.html',  {'response': response})