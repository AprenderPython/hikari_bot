 
Proyecto Hikari: TestCode
--------------------------


Este proyecto consiste en la creacion de una funcion para el bot Hikari, el cual consistira en proponer restos para programar
y determinar si cumple con lo especificado, todo automatizado en un ambiente lo mas seguro posible.

---------------------------------------------------------------------------------------------------------------------------------------------------
Funcionamiento:
___________________________________________________________________________________________________________________________________________________

Mapa de red:
	*Server Madre:
		Server en donde estan todas las maquinas virtuales alojadas
	*Server HouseBot:
		Server principal donde esta alojado el bot Hikari.
	*Server Sandbox:
		Server secundario en donde se ejecutara el codigo en un ambiente controlado y aislado
	*Firewall:
		Sistema de seguridad que protegera la conexion entre el Server HouseBOt y Server Sandbox

Scripts:

	CodeTest.py:
		Este script gestionara 
	Resolvedor.py:
		Este script probara el codigo del usuario para determinar si cumple con lo especificado.

1.)El usuario interactuara con el bot Hikari, seleccionara un reto y luego enviara el codigo de ese reto en particular
2.)El bot recibira el codigo y realizara algunas comprobaciones tales como: La extencion del archivo, el peso y el nombre.
	Si todo funciona bien: Sigue al siguiente proceso                  Sino:    Se le devuelve un error al usuario.
3.)El bot mandara un codigo al server madre y este creara la maquina virtual preconfigurada del reto en cuestion
4.)Se enviara el programa del usuario por ftp server activado por defecto en la vm.
5.)Se ejecutara el script de CodeTest.py el cual supervizara la ejecucion para gestionar los recursos y autodestruira el server ftp.
6.)Se ejecutara el resolvedor.py el cual probara el programa del usuario y guardara el resoltado (True or False) en un archivo.txt
7.)Una vez termine el programa CodeTest.py se asegurara de eliminar todo rastro de ejecucion del programa del usuario
8.)Se montara un server web con el archivo.txt
9.)El bot hikari estara esperando que este archivo este disponible y tomara la respuesta y la guardara
10)Una vez tenga la respuesta enviara un mensaje al server madre para que elimine la maquina virtual sandbox.

	#Si durante todo este proceso no se obtiene una respuesta en un tiempo determinado, se notificara al usuario que su programa tuvo un error
	#Este proceso solo se ejecutara uno a la vez

----------------------------------------------------------------------------------------------------------------------------------------------------
Medidas de seguridad
____________________________________________________________________________________________________________________________________________________

Seguridad a nivel de Sistema
	*Proteccion de permisos
	*Proteccion de ejecucion mediante CodeTest.py para evitar sobrecargos de sistemas y la duracion de ejecucion del mismo
	*El sistema tendra solo los paquetes minimos para su ejecucion mejorando la seguridad y el consumo de recursos.
	*Cada mes se hara una actualizacion de software el sistema utilizado para la sandbox

Seguridad a nivel de redes
	*El sandbox estara en una red aislada y desconectada de otros hosts
	*Se utilizara un firewall para bloquear paquetes sospechozos
	*Se utilizaran tecnicas de IPS para detectar anomalias en la red y deterner la ejecucion del codigo

Seguridad en el software
	*La vm preconfigurada tendra las librerias necesarias para le ejecucion para evitar el uso de internet para instalar dependencias
	*Se utilizaran tecnicas para evitar que se ejecute algunos codigos maliciosos, ya sea mediante blacklists de palabras u otras formas
	*Resolvedor.py se ejecutara en una instancia virtual y aislada de python.

---------------------------------------------------------------------------------------------------------------------------------------------------
Lineas de defensa
___________________________________________________________________________________________________________________________________________________

#Primera linea de defensa:
	Filtro de hikari para detectar la extencion, el peso y el nombre del archivo.
#Segunda linea de defensa:
	Resolvedor.py para determinar si el codigo esta bien escrito o no.
#Tercera linea de defensa:
	Entorno virtual de python
#Cuarta linea de defensa:
	Permisos limitados del usuario actual
#Quinta linea de defensa:
	Firewall que bloquea todas las conexiones
#Sexta linea de defensa:
	Red aislada de internet y otros dispositivos, solo conectada temporalmente con HouseBot.
#Septima linea de defensa:
	El tiempo limite para la autodestruccion de la maquina virtual.
