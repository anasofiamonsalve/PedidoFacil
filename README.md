# PedidoFácil

Aplicación web en Django para gestionar productos y pedidos, con inicio de sesión,
validaciones en JavaScript y Django, base de datos PostgreSQL en Neon y despliegue en Render.

**URL publicada:** https://pedidofacil-1.onrender.com/login/

## Tecnologías
Python, Django, HTML5, CSS3, JavaScript, Bootstrap, PostgreSQL (Neon), Render, Git y GitHub.

## Instalación local

1. Clonar el repositorio:
```bash
   git clone https://github.com/anasofiamonsalve/PedidoFacil.git
   cd pedidofacil
```
2. Crear y activar el entorno virtual:
```bash
   python -m venv venv
   venv\Scripts\activate        
```
3. Instalar dependencias:
```bash
   pip install -r requirements.txt
```
4. Crear un archivo `.env` en la raíz con:
```
   SECRET_KEY=tu-clave-secreta
   DEBUG=True
   DATABASE_URL=postgresql://usuario:clave@host/neondb?sslmode=require
```
5. Aplicar migraciones y crear un usuario:
```bash
   python manage.py migrate
   python manage.py createsuperuser
```
6. Ejecutar:
```bash
   python manage.py runserver
```
   Abrir http://127.0.0.1:8000/

## Funcionalidades
- Inicio y cierre de sesión (autenticación de Django)
- CRUD de productos y de pedidos
- Búsqueda por nombre de producto y por cliente
- Validaciones con JavaScript y con Django
- Número de pedido único; el usuario queda asociado al pedido que registra

## Despliegue en Render
- Build command: `bash build.sh`
- Start command: `gunicorn pedidofacil.wsgi:application`
- Variables de entorno: `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, `PYTHON_VERSION`