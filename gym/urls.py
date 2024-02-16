from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static

from gym.views import index
from users.views import registro

from gym.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [   
    path('',index, name='index'),
    path('admin/', admin.site.urls),
    path('registro/',registro,name='registro'),
    # path('mostrar-cuotas/', mostrar_cuotas, name='mostrar_cuotas')
    # path('prueba-registro/', prueba_registro, name='prueba-registro')
    
] + static(MEDIA_URL, document_root = MEDIA_ROOT)