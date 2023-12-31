# PythonCoderHouse

## Entrega Final del Proyecto  

- Curso de Python 
- Comisión: 43880
- Alumnos: Diaz Daniel - Andres Vallejos

## Descripción de la distribucion de tareas

Se decidió utilizar dos aplicaciones para el proyecto. Una para controlar la lógica de las vistas, otra para manejar la autenticación de usuarios,
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

##link del vídeo explicativo:

https://drive.google.com/file/d/10RJSfL0Lo7CD8dOMAFxf3RclnRIU2jSh/view?usp=drivesdk

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

##Vistas de cada tipo de usuario:

1. Vista de la pagina sin usuario logueado:
    https://drive.google.com/file/d/1vAKIIt2ykpm2_xAndk4UMChGua92DKZ1/view?usp=drive_link

2. Vista de la pagina con usuario regular:
	https://drive.google.com/file/d/18ksLfUynFu--gO2Eoc_87FZwUqfMjeNT/view?usp=drive_link
	
3. Vista de usuario staff:
	https://drive.google.com/file/d/1o3C3l1c44zODjWtPr51ibu0POrKwByTC/view?usp=drive_link

4. Vista superuser:
	https://drive.google.com/file/d/11RIcKPUSTGXSgxoHXvwYTqavH-0_kT-8/view?usp=drive_link
