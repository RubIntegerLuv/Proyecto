# Proyecto de Gestión de Datos

Este es un sistema de gestión de datos que permite realizar consultas dinámicas entre diferentes tablas (empresa, trabajador y documento). Utiliza un backend desarrollado en **Django** y un frontend en **Angular**, además de una base de datos SQL Server.

## Tecnologías Utilizadas

- **Backend**: Django 4.x
- **Frontend**: Angular 16.x
- **Base de Datos**: SQL Server
- **Frameworks**:
  - Bootstrap 5
  - Django REST Framework
- **Otros**:
  - Material Design (para el frontend)

---

## Para ejecutar se necesita:

- Python 3.10+
- Node.js 16+
- Angular CLI
- SQL Server

---

## Pasos de Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/RubIntegerLuv/Proyecto.git
cd Proyecto


2. Crear la Base de Datos y Configurar la Conexión

Abre tu SQL Server Management Studio (SSMS) o cualquier herramienta que utilices para manejar bases de datos SQL Server.
Ejecuta el script de "base_desafio.sql"  para genererar la base de datos

Configura la conexión en el archivo Backend/practica/settings.py en la sección DATABASES asi:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sql_server',
        'NAME': 'desafio_kis',  # Nombre de tu base de datos
        'USER': 'root',  # Usuario de tu base de datos
        'PASSWORD': 'tu_contraseña',  # Contraseña del usuario
        'HOST': 'localhost',  # Servidor SQL Server
        'PORT': '3306',  # Puerto por defecto de SQL Server
    }
}

3. Configuración del Backend (Django) :

cd Backend
pip install -r requirements.txt

Migrar la base de datos:
    python manage.py makemigrations
    python manage.py migrate

Ejecutar el servidor:
    python manage.py runserver


4. Configuración del Frontend (Angular)

cd ../Frontend
npm install
ng serve

Accede al frontend en http://localhost:4200.
```
