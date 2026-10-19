from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pedidos, name='lista_pedidos'),
    path('nuevo/', views.crear_pedido, name='crear_pedido'),
    path('<int:pk>/', views.detalle_pedido, name='detalle_pedido'),
    path('<int:pk>/editar/', views.editar_pedido, name='editar_pedido'),
    path('<int:pk>/eliminar/', views.eliminar_pedido, name='eliminar_pedido'),
    path('<int:pk>/estado/', views.cambiar_estado, name='cambiar_estado'),
]