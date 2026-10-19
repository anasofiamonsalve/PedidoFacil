from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Pedido


class PedidoTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('tester', password='clave12345')
        self.datos = {
            'numero_pedido': 'P-001',
            'cliente': 'Ana',
            'descripcion': 'Dos cajas',
            'valor_total': '15000',
            'estado': 'pendiente',
        }

    def test_requiere_login(self):
        respuesta = self.client.get(reverse('lista_pedidos'))
        self.assertEqual(respuesta.status_code, 302)
        self.assertIn('/login/', respuesta.url)

    def test_crear_pedido_asigna_usuario(self):
        self.client.login(username='tester', password='clave12345')
        self.client.post(reverse('crear_pedido'), self.datos)
        pedido = Pedido.objects.get(numero_pedido='P-001')
        self.assertEqual(pedido.usuario, self.user)

    def test_numero_duplicado_rechazado(self):
        self.client.login(username='tester', password='clave12345')
        self.client.post(reverse('crear_pedido'), self.datos)
        respuesta = self.client.post(reverse('crear_pedido'), self.datos)
        self.assertEqual(Pedido.objects.filter(numero_pedido='P-001').count(), 1)
        self.assertContains(respuesta, 'Ya existe un pedido con ese número.')