# Acceso a datos - Proyecto NBA

_Proyecto de desarrollo de una aplicación web con Symfony_

## Comenzando 🚀

_Debemos crear una copia de la carpeta **sf-app-provisioning** de nuestro proyecto symfony anterior y 
renombrarla a **apinba**. Podemos mover la carpeta a otro directorio para trabajar más cómodamente_

```
// Por consola
cp -R sf-app-provisioning apinba
mv apinba ../apinba
cd ../apinba
```

_Podemos incluir un dominio personalizado en nuestro archivo **hosts** para acceder a la aplicación de **Symfony** 
de manera más intuitiva._  
![archivo hosts: 127.0.0.1 apinba.local](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)


### Pre-requisitos 📋
_- Disponer de un contenedor Docker con MySQL accesible._ <br/>
_- Relizar las siguientes modificaciones en los archivos a continuación:_

* _**.env.webapp**:_
```
APACHE_SERVER_NAME=apinba.local
APACHE_SERVER_ALIAS=apinba.local
APACHE_DOCUMENT_ROOT=/code/public
```

* _**docker-compose.yml**:_
```
container_name: apinba
```


### Instalación 🔧

_Una vez estos archivos han sido modificados, construimos el contenedor y 
accedemos a él para crear nuestro proyecto._

```
docker-compose up --build
docker exec -it apinba bash
```

_A continuación creamos el proyecto symfony indicando la versión y evitando la
inicialización del repositorio git._ 
_Esto creará un nuevo directorio con el mismo nombre **apinba**. Movemos el contenido de este
 a nuestro directorio de trabajo_

```
symfony new apinba --version=4.4 --full --no-git
mv apinba/* .
mv apinba/.env .
```

_Abrimos el navegador y accedemos a la url de nuestro proyecto. Si no es accesible debemos cambiar los 
permisos del directorio **/var/log**_

```
chmod 777 -R /var/log
```


### Conexión e importación de base de datos

_Importar archivo **.sql**_
```
mysql -u root -pdbrootpass -h mysql-container < archivo.sql
```


### Insertar datos en las tablas

_Ejecutamos los **scripts** de python para insertar datos en el siguiente orden:_
```
python3 scripts/equipos.py  
python3 scripts/jugadores.py  
python3 scripts/partidos.py  
python3 scripts/estadisticas.py
```


### Doctrine. Entities y repositorios

_El siguiente comando permite incluir unas dependencias extra en el proyecto para 
facilitar el uso de las bases de datos con doctrine.  
Un ejemplo incluyendo GroupConcat y DateFormat:_ 
```
composer require beberlei/doctrineextensions  

// Incluir en el archivo doctrine.yaml (bajo 'auto-mapping', a la misma altura)
dql:
    string_functions:
        group_concat: DoctrineExtensions\Query\Mysql\GroupConcat
        date_format: DoctrineExtensions\Query\Mysql\DateFormat
```

Añadimos las siguientes variables de entorno al archivo _**.env**:_
```
DB_HOST=mysql-container
DB_PASSWORD=dbrootpass
DB_USER=root
DB_NAME=nba
DB_DATABASE_URL="mysql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:3306/${DB_NAME}?serverVersion=5.7"
```

_Creamos las distintas entities desde la base de datos_
```
php bin/console doctrine:mapping:convert annotation src/Entity/ --from-database
```
_Este comando creará una entity por tabla existente en la base de datos. El siguiente paso es agregarle
a cada una el **namespace** ( App\Entity ), los **getters** y los **setters** (eliminando la barra que se 
incluye junto al tipado cuando hace referencia a otros objetos)._

_El siguiente paso es crear, en sus respectivas carpetas, los **repositorios** y **controladores** de cada entidad,
desde los cuales operaremos con la base de datos._

## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **Fulanito Detal** - *Documentación* - [fulanitodetal](#fulanito-de-tal)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.



---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊
