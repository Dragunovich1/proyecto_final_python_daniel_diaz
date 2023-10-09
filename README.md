# PythonCoderHouse

## Entrega Final del Proyecto  

- Curso de Python 
- Comisión: 43880
- Alumnos: Diaz Daniel - Andres Vallejos

## Descripción de la distribucion de tareas

Se decidió utilizar dos aplicaciones para el proyecto. Una para controlar la lógica de las vistas, otra para manejar la autenticación de usuarios
hemos distribuido equitativamente las tareas, reuniendonos casi periodicamente por Microsoft Teams para el desarrollo.


## Objetivos generales

Desarrollar una WEB Django estilo Blogo con patrón MVT subida a Github.

## Se debe entregar
Requisitos base: 

- Video con la web funcionando (lo disponibilizamos en link directo en la web y tambien en github)
- 3 Casos de prueba debidamente documentados en una planilla xls.
- Contar con un admin en route admin/ donde se puedan manejar los datos en la app.
- Contar con un route about/ donde se contará acerca de los dueños de la página
- Contar con algún acceso visible a la vista de blogs que debe alojarse en el route pages/
- Contar con páginas para:
- Crear {ítems}
- Actualizar {ítems}
- Borrar {ítems}
- Buscar un {ítem} en base a un campo
- Debe existir conexiones o links entre la página principal (todos los ítems) y las páginas secundarias (crear, actualizar, borrar y buscar un ítem).
- No deberá contener links rotos o que no lleven a ninguna parte.
- Toda la aplicación deberá funcionar. (Admin)

## Datos de superusuario/staff
- Superusuario: dragunovich1 - password: DNDefault123
- Usuario staff: elmanquito86 - password: DNDefault123

##Instrucciones:

1. Clonar repo en tu máquina local.

2. Ejecutar terminal en la raiz del proyecto

3. Crear y activar el entorno virtual:	python -m venv nombre_del_entorno
										
										En Windows: .\nombre_del_entorno\Scripts\activate.
										En Linux/Mac: source ./nombre_del_entorno/bin/activate.

    
4. Instala las dependencias del proyecto: pip install -r requirements.txt.

5. En la terminal, navega hasta la carpeta del proyecto con cd blogfierros (directorio donde se aloja manage.py)

6. Ejecuta las migraciones de Django con el comando: python manage.py makemigrations

7. Ejecuta las migraciones de Django con el comando: python manage.py migrate

8. Ejecuta el servidor con el comando: python manage.py runserver.

9. Abre un navegador y navega hasta http://127.0.0.1:8000/ o http://localhost:8000/ para ver la página principal.


## Estructura de archivos del proyecto


< RAIZ DEL PROYECTO (Blogfierros) >
|
|
|-- db.sqlite3							#Base de datos.
|
|-- README.md							#Documentacion del proyecto (este archivo jeje).
|
|-- manage.py							#Archivo de administracion del proyecto.
|
|
|
|-- static/appfierros								
|		|		
|		|
|		|--- css/					
|		|
|		|--- images/					#Directorio donde se encuentran las imagenes STATIC (utilizadas por ejemplo en el favicon).
|		|
|		|--- js/					
|
|
|-- appfierros							#Implementa la logica de la app.
|		|
|		|--- templates/					#Directorio donde se encuentran todas las vistas HTML.
|		|
|		|--- migrations/				#Directorio de las migraciones de la DB.
|		|
|		|--- admin.py					#Archivo donde activamos las funcionalidades que se manejaran desde el panel de control.
|		|
|		|--- apps.py
|		|
|		|--- forms.py					#Define los formularios para la app.
|		|
|		|--- models.py					#Define los modelos para la app.
|		|
|		|--- tests.py					
|		|
|		|--- urls.py					#Define las urls para el ruteo.
|		|
|		|--- views.py					#Define las vistas para la app.
|
|
|
|
|-- blogfierros/
|			|						
|			|
|			|--- settings.py        #app django bootstrapper.
|			|
|			|--- urls.py			#archivo para las urls del proyecto base, fue necesario incluir la vista PasswordsChangeView aqui.
|
|
|
|--  media/							#Directorio definido para el almacenamiento de imagenes de perfil y las publicadas en los posts.
|		|
|		|
|		|--- images/
|				|
|				|
|				|--- profile/
|				
|
|
|-- members/						#Directorio definido para el manejo de la autenticacion, logueo y manejo de usuarios y perfiles.
|		|
|		|
|		|--- migrations/			#Directorio de las migraciones de la DB
|		|
|		|
|		|--- templates/				#Directorio donde se almacenan las vistas HTML relacionadas al manejo de usuarios.
|		|
|		|--- admin.py				#Archivo donde activamos las funcionalidades que se manejaran desde el panel de control.
|		|
|		|--- apps.py
|		|
|		|--- forms.py				#Define los formularios para la app de autenticacion.
|		|
|		|--- models.py				#Define los modelos para la app de autenticacion.
|		|
|		|--- tests.py					
|		|
|		|--- urls.py				#Define las urls para el ruteo orientado a la autenticacion
|		|
|		|--- views.py				#Define las vistas para la app orientado a la autenticacion
