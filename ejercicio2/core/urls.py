from django.urls import path
from .views import home, nosotros, servicios, usuarios, editar_usuario, eliminar_usuario, ver_usuario, crear_usuario
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', home, name="home"),
    path('nosotros/', nosotros, name="nosotros"),
    path('servicios/', servicios, name="servicios"),
    path('usuarios/', usuarios, name="usuarios"),
    path('ver-usuario/<id>/', ver_usuario, name="ver_usuario"),
    path('editar-usuario/<id>/', editar_usuario, name="editar_usuario"),
    path('eliminar-usuario/<id>/', eliminar_usuario, name="eliminar_usuario"),
    path('crear-usuario/', crear_usuario, name="crear_usuario"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)