# Evaluación de TMOB

Utilizando **Python3**, **Django versión 2** escribir código que resuelva los siguientes puntos:

Representar el siguiente modelo de datos en Django utilizando **MySQL** como motor de base de datos.

### Nombre del modelo: **Redirect**
Campos:
- key (string)
- url (string)
- active (boolean)
- updated_at (datetime)
- created_at (datetime)
Propertys:
get_redirect(key)

Consideraciones:
- created_at: representa la fecha y hora en que se creo por primera vez el registro.
- updated_at: representa la fecha y hora de la ultima modificación del registro.-

Ambos valores no deben ser ingresados por el usuario, sino que deben colocarse automáticamente.


Crear una **signal** asociada a las actualizaciones del modelo anterior que tome todos los datos con active=True; y los coloque en una estructura de datos en cache (preferentemente usar **MEMCACHED** y la estructura de datos se deja a criterio del programador)


Crear una view que reciba mediante **GET HTTP** el parámetro key y retorne la URL asociada de acuerdo con el modelo. La respuesta debe ser un Json con la siguiente estructura:
```
{
    “key”: “[el valor de la key]”, 
    “url”: “[la url correspondiente]”
}
```
**Obtener el valor de la URL desde cache y No desde la DB.**

Disponibilizar el **Admin** de Django para poder configurar la aplicación.

---

# Pasos a Seguir
Clonar el repositorio y pararse en el directorio raiz.

### CREACION DE ENTORNO:
Yo utilizo la librería venv y Python version 3.8

Pararse en el directorio clonado, crear el entorno activarlo e instalar las librerias
```
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

### BASE DE DATOS
Para replicar la db de Mysql la forma mas fácil es a traves de docker con el siguiente comando de una sola línea. *Elegir la contraseña deseada*.

```
docker run --name mysql-db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=mypassword -v $PWD/volume:/var/lib/mysql -d mysql
```

Por buenas prácticas yo utilizo la librería **python-dotenv**
Las variables de entorno entonces pueden ser guardadas en:
- el **sistema operativo**
- en archivo llamado **.env** en la raiz del directorio
- si utilizas Visual Code pueden guardarse en el workspace.

Vamos a usar el del archivo .env
### CREAR MODIFICAR ARCHIVO .env
crear un archivo .env en el directorio raiz con valores propios.

```
MYSQL_ROOT_PASSWORD=mypassword
DJANGO_SECRET_KEY="$4k4wtf_7v557brq&0mjae)o1mn6cqwst99(pm!pq+iqx_^_72"
```
* **Tener en cuenta que el password MYSQL_ROOT_PASSWORD debe ser el mismo que se uso para el comando del DOCKER usado mas arriba (mypassword).**

### MIGRAR Y CREAR SUPERUSUARIO
En este paso debemos las migraciones para que se creen las tablas necesarias para Django y crear el superusuario para poder ingresar al administrador
```
python manage.py migrate
python manage.py createsuperuser
```





