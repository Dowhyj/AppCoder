# AppCoder

Instalar django

python -m pip install django

Aplicar cambios en base de datos

python manage.py makemigrations
python manage.py migrate

Iniciar servidor

python manage.py runserver

Cortar servidor

CTRL + C

Crear usuario administrador

python manage.py createsuperuser

URLS

http://127.0.0.1:8000/AppCoder -> Pagina inicio

URLS formularios (en estas se van a encontrar formularios para crear alumnos, proferos y cursos)

http://127.0.0.1:8000/AppCoder/crearAlumno/ -> Crear alumno
http://127.0.0.1:8000/AppCoder/crearProfesor/ -> Crear profesor
http://127.0.0.1:8000/AppCoder/crearCurso/ -> Crear curso

URLS vistas (en estas se van a poder visualizar todos los alumnos, profesores y cursos que se hayan creado)

http://127.0.0.1:8000/AppCoder/alumnos -> Muestra a todos los alumnos
http://127.0.0.1:8000/AppCoder/profesores -> Muestra a todos los profesores
http://127.0.0.1:8000/AppCoder/cursos -> Muestra a todos los cursos