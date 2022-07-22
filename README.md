# Proyecto Final - Curso Python - CoderHouse

# DataHouse

El proyecto consiste en una plataforma online de aprendizaje donde se ofrecen diferentes cursos relacionados a la ciencia de datos.

- - - - - - - - - - - - - - - - - - - - - -

link video:

- - - - - - - - - - - - - - - - - - - - - -

Link de repositorio:

- - - - - - - - - - - - - - - - - - - - - -

Author:
-Dowhyj Lucas

Responsable de todo lo que se realizó en el proyecto

- - - - - - - - - - - - - - - - - - - - - -

# Applied Technologies:
 Python
 Django (v.4.0.5)
 Html
 Css
 Bootstrap (v.5.1.3)
 Pillow (v.9.2.0)

- - - - - - - - - - - - - - - - - - - - - -

# Getting star:

1. Clonar repositorio

2. Instalar requirements.txt

3. Iniciar servidor: Ubicarse en la carpeta "proyecto_final" y ejecutar: python manage.py runserver 

# Comandos extra:
    Instalar django -> python -m pip install django
    Aplicar cambios en base de datos -> 1. python manage.py makemigrations  2. python manage.py migrate
    Cortar servidor -> CTRL + C
    Crear super usuario -> python manage.py createsuperuser


URLS

http://127.0.0.1:8000 -> Pagina inicio

URLS formularios (en estas se van a encontrar formularios para crear alumnos, proferos y cursos)

http://127.0.0.1:8000/AppCoder/crearAlumno/ -> Crear alumno
http://127.0.0.1:8000/AppCoder/crearProfesor/ -> Crear profesor
http://127.0.0.1:8000/AppCoder/crearCurso/ -> Crear curso

URLS vistas (en estas se van a poder visualizar todos los alumnos, profesores y cursos que se hayan creado)

http://127.0.0.1:8000/AppCoder/alumnos -> Muestra a todos los alumnos
http://127.0.0.1:8000/AppCoder/profesores/list -> Muestra a todos los profesores
http://127.0.0.1:8000/AppCoder/curso/list -> Muestra a todos los cursos