from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "post":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            mail = request.POST.get('mail', '')
            content = request.POST.get('content', '')

            # Creación del correo
            # mail = EmailMessage(
            #     'La sabrosa: Nuevo mensaje de contacto', # asunto
            #     'De', name, mail, "\n\nEscribió:\n\n", content, # mensaje
            #     'lasabrosa.com', # email de origen
            #     ['lasabrosa.django@gmail.com'], #email de destino
            #     reply_to=[mail]
            # )

            
    return render(request, 'contact.html', {'form':contact_form})
