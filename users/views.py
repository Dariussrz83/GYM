from django.shortcuts import render
from users.forms import DniForm
from users.models import Usuario, Cuota


def registro(request):
    usuario = None
    cuotas_pendientes = None
    ultima_fecha = None
    mensaje_error = None

    if request.method == 'POST':
        form = DniForm(request.POST)
        if form.is_valid():
            dni = form.cleaned_data['dni']
            usuarios = Usuario.objects.filter(dni=dni)

            if usuarios.exists():
                usuario = usuarios.first()
            else:
                mensaje_error = "El usuario no se encuentra registrado."

            # Obtener cuotas pendientes del usuario
            cuotas_pendientes = Cuota.objects.filter(socio=usuario, al_dia=False)

            # Obtener la última fecha de pago (si hay cuotas pagadas)
            ultima_cuota_pagada = Cuota.objects.filter(socio=usuario, al_dia=True).order_by('-fecha').first()
            ultima_fecha = ultima_cuota_pagada.fecha if ultima_cuota_pagada else None

    else:
        form = DniForm()
        # Lógica adicional para obtener la última cuota pagada al buscar al usuario por nombre
        nombre_usuario = request.GET.get('nombre_usuario', None)
        if nombre_usuario:
            usuarios = Usuario.objects.filter(nombre=nombre_usuario)

            if usuarios.exists():
                usuario = usuarios.first()

                # Obtener la última cuota pagada (si hay cuotas pagadas)
                ultima_cuota_pagada = Cuota.objects.filter(socio=usuario, al_dia=True).order_by('-fecha').first()
                ultima_fecha = ultima_cuota_pagada.fecha if ultima_cuota_pagada else None
            else:
                mensaje_error = "El usuario no se encuentra registrado."

    return render(request, 'registro.html', {'form': form, 'usuario': usuario, 'cuotas_pendientes': cuotas_pendientes, 'ultima_fecha': ultima_fecha, 'mensaje_error': mensaje_error})



