
# Simple CRUD

**Simple CRUD** es una aplicación web de Gestion de Tareas para crear, editar y organizar tareas. Se incluyen el registro e inicio de sesión, tareas prioritarias, marcado de tareas completadas y vistas filtradas (pendientes / completadas). Desarrollada con el framework **Django** y tecnologías web estándar como *HTML, CSS (interfaz responsiva con Bootstrap), JavaScript* y *SQLite* para el almacenamiento de los datos.


## Características

- Registro e inicio de sesión por usuario.
- Crear, editar y eliminar tareas.
- Marcar tareas como importantes.
- Marcar tareas como completadas y ver historial.
- Vistas filtradas y protección de rutas (login requerido).


## Tech Stack
Esta aplicación sigue la arquitectura Django (MTV: Models, Templates, Views) con separación clara de capas:

**Frontend:** HTML, CSS, JavaScript, Bootstrap 5.

**Backend:** Django 5, Django ORM para persistencia en SQLite, autenticación basada en sesiones.

**Patrones aplicados:** separación de responsabilidades (SoC), uso de nombres de rutas y reversión para desacoplar enlaces, manejo de formularios (Form objects) y protección CSRF.

**Views/Controllers:** funciones que gestionan solicitudes HTTP, validación con Django Forms y uso de decoradores como *login_required* para protección de rutas.


## Instalación

**Pre-requisitos**: 
- Python
- pip
- virutalenv

**1 - Crear el directorio**: abrir el terminal y crear el directorio en donde se guardara el proyecto.

```bash
  mkdir CRUD #Para crear el directorio 
```
    
**2 - Clonar el repositorio**: posicionarse en el directorio donde se desea clonar el repositorio y ejecutar git clone

```bash
  cd CRUD
  git clone https://github.com/enridami/simple_crud.git
```

**3 - Crear el entorno virtual:** ingresar cualquiera de las dos opciones para crear el entorno virtual en la carpeta del proyecto

```bash
  virtualenv env
```


```bash
  python -m venv env
```

**4 - Iniciar el entorno virtual:**

```bash
  env\Scripts\activate
```

**5 - Instalar las dependencias requeridas:**

```bash
  pip install -r requirements.txt
```

**6 - Aplicar las migraciones para configurar la base de datos:**

```bash
  python manage.py makemigrations
  python manage.py migrate
```



## Despligue

**Inicializar la aplicación:**

```bash
  python manage.py runserver
```

Una vez realizado todos los pasos abre tu navegador e ingresa al http://localhost:8000/ para acceder al despliegue del proyecto.


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## License

[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)

