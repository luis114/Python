from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from .forms import ContactForm
from django.core.mail import EmailMessage


# Create your views here.


class HomePageView(TemplateView):
    template_name = "index.html"

  

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{'tituloIni': 'Luis Miguel'})  

class  NosotrosPageView(TemplateView):

    template_name = "nosotros.html" 

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{'titulous':'Los saluda Luis.', 'descripcion':'Python'})  


def contacto(request):
    formContact = ContactForm()
    #validar que el formulario tenga una petición post:
    if request.method =="POST":
        formContact =ContactForm(data=request.POST)
        if formContact.is_valid():
            tipomsj = request.POST.get('tipomsj','')
            usuario = request.POST.get('usuario','')
            correo = request.POST.get('correo','')
            mensaje = request.POST.get('mensaje','')


            #creamos el objeto  con las variables del formulario:
            email = EmailMessage(
                "RepoDevelopers: Patrón tienes un nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\nTipo de Mensaje:{}\n{}".format(usuario, correo, tipomsj, mensaje),
                "no-contestar@inbox.mailtrap.io",
                ["vivaspalaciosluismiguel@gmail.com"],
                reply_to=[correo]
            )

            #enviamos el correo
            try:
                email.send()
                # Se envia el correo:
                return redirect(reverse('contacto')+"?ok")
            except:
                # No se ha enviado el correo:
                return redirect(reverse('contacto')+"?fail")
    
    
    return render(request, 'contacto.html', {'formulario':formContact})

            
            