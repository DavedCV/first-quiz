Usando las recomendaciones de la Open Web Application Security Project (OWASP) para mitigar y seguir estándares que maximicen la seguridad de la aplicación, y tomando el papel del lider de ingeniería de la startup, para garantizar la seguridad nos aseguramos de cumplir las siguientes claves agrupadas segun los puntos recomendados:

- **Broken Access Control**

  En este punto nos queremos asegurar que los usuarios no puedan actuar y realizar acciones que sobrepasen sus respectivos permisos, con el fin de evitar filtraciones y escapes de información importante, así como su incorrecta manipulación. En este punto nos vamos a asegurar de cumplir con los siguientes detalles:
    
  - *Implementar un control de acceso basado en roles:* definimos roles claros y precisos que incluye tanto usuarios como empleados, para que según su posición cada uno tenga un nivel de acceso con responsabilidades y alcances claramente predefinidos.
  - *Implementar control de acceso a las bases de datos:* usar los mecanismos puestos a disposición por MySQL, tales como roles y permisos para restringir acceso a la base de datos a partir de los roles y permisos de los diferentes empleados.
  - *Implementar un sistema fuerte de autenticación:* nos aseguramos que los mecanismos de autenticación sean robustos, usando métodos como OAuth, JWT o SAML. Así mismo podemos asegurarnos de requerir politicas de seguridad de contraseñas, e implementar autenticación multifactor para añadir seguridad y controlar mucho más el acceso.
  - *Asegurar el acceso a la API:* Implementamos mecanismos de control y autorización seguros en la parte del backend. Podemos usar API keys o Tokens y validar los permisos antes de permitir el acceso a información o funcionalidad del sistema.
  - *Implementar adecuadamente el principio de menor priviliegio:* Siguiendo este principio aseguramos a los usuarios, empleados y servicios el mínimo nivel de acceso para desarrollar adecuadamente sus tareas específicas dentro del sistema.  
  - *Implementar un control estricto de manejo de sesiones:* Usando un control preciso sobre las sesiones del sistema, tratamos de prevenir accesos no autorizados y nos encargamos de controlar la validez de las secciones activas por criterios de tiempo, inactividad, entre otros, con el fin de evitar fugas y puntos de acceso.

- **Cryptographic Failures**

  En este punto nos centramos en controlar y evitar a toda costa el manejo de datos sensibles incorrectamente encriptados, que pongan en peligro la privacidad de los usuarios y la seguridad del sistema:

  - *Minimizar la recoleccion de datos:* Mantenemos y recopilamos datos exclusivamente necesarios; evitamos guardar información sensible que no nos sea de completa utilidad.
  - *Encripción de los datos sensibles en el modelo de datos:* Los datos en reposo de los usuarios son encriptados adecuadamente en la base de datos MySQL, por medio de algoritmos y protocolos seguros y actualizados.
  - *Encripción de los datos en transitos por medio de protocolos seguros como TLS.*
  - *Evitamos a toda costa hacer caching sobre datos sensibles.*
  - *Asegurar que los backups estén correctamente asegurados, restringidos y encriptados.*

- **Injection**

  En esta sección nos encargamos de evitar puntos de acceso a nuestro sistema por medio de inyeccion de código, comandos o queries que puedan acceder al sistema y generar acciones que perjudiquen la seguridad. 
  Para minimizar los riesgos en estos casos seguimos los siguientes cuidados:

  - *Uso de queries parametrizados:* nos servimos de queries paraemtrizados o preparados para las interacciones con la base de datos con el fin de evitar inyección SQL. Esto nos sirve para separar los inputs de lo usuarios de queries directos.
  - *Validación de input:* nos aseguramos de controlar el input que los usuarios puedan proveer, tanto en el frontend y en la aplicación, así como en el backend que recibe la información. Con esto buscamos prevenir inputs maliciosos que puedan entrar al servidor.
  - *Uso de un ORM:* nos podemos servir de algún framework que nos ayude a sanitizar y filtrar los queries SQL, minimizando los riesgos de inyección SQL. Trabajando con FastAPI, podemos servirnos de librerias como SQLModel.

- **Security Misconfiguration**

  - *Constante revisión de la seguridad de Kubernetes:* teniendo muy presente esto, nos encargamos de revisar continuamente la configuración con el fin de evitar malas configuraciones que puedan exponer el sistema. Usamos herramientas como Kubernetes Security Context.
  - *AWS asegurado:* nos aseguramos que los servicios y recursos de AWS estén correctamente configurados y controlados limitadamente sobre su acceso y modificación.

- **Identification and Authentication Failures**

  - *Implementar autentificación multifactor:* con esto buscamos reducir los riesgos de ataques como relleno de credenciales, fuerza bruta, uso de credenciales robadas.
  - *Implementar comprobaciones de contraseñas:* buscamos evitar el uso de contraseñas debiles y poco seguras.

- **Security Logging and Monitoring Failures**

  Esta categoría tiene como objetivo ayudar a detectar, escalar y responder a problemas activos.

  - *Asegurar monitoreo suficiente:* Implementar un logging compresivo y robusto a través de la infraestrutura y aplicaciones, con el fin de detectar y responder de la mejor manera posible incidentes y compromisos a la seguridad. 
