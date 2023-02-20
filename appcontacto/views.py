from django.shortcuts import render ,redirect
from  appcontacto.forms import ContactoForm
from django.core.mail import EmailMessage


def contacto(request):
    formulario_contacto = ContactoForm()
    if request.method == "POST":
        formulario_contacto = ContactoForm(data=request.POST)
        if formulario_contacto.is_valid():
            
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')
            

            
            email=EmailMessage("mensaje enviado desde app diango" 
            "el usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n{}".format(nombre,email,contenido)," ",
            
            ["cigu1966@gmail.com"],reply_to=[email])          
            
            try:
                email.send()
                return redirect('/contacto/?valido')
            except: 
                return redirect('/contacto/?novalido')
        
    
    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})