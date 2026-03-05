# Implementando un administrador de contraseñas con Python y Programación Orientada a Objetos
Un administrador de contraseñas es una herramienta de software que permite almacenar, generar, y autocompletar 
información de login en diferentes plataformas, de manera segura.

La manera general en la que funciona es que, solo con una contraseña maestra (**master password**), puede desencriptar 
la información sensible almacenada para cada usuario (contraseñas).

Existen varias soluciones de administradores de contraseñas, siendo las más conocidas **Google Password Manager**, 
**BitWarden**, y **1Password**.

En este proyecto final del aprendizaje de Python para Data Science crearemos un administrador de contraseñas simple, 
escrito completamente en Python, y almacenamiento en memoria (sin bases de datos).

Deberás tomar en cuenta que este es un problema complejo, por lo tanto será de muchísima utilidad aplicar los conceptos 
de **Programación Orientada a Objetos**.


## Requerimientos Técnicos

Consideremos nuestro administrador de contraseñas como un objeto de una clase llamada `PasswordManager`.
`PasswordManager` debe contar con las siguientes funcionalidades:

- **Inicialización**. En el primer uso del administrador, debe brindarse la contraseña maestra (un `str`), a la cual se 
le aplica una KDF (Key Derivation Function) para usarla como llave (`key`) al encriptar y desencriptar las contraseñas. 
La inicialización del `PasswordManager` crea también un `Vault`, clase que almacenará la información de login del usuario (
    clase de tipo `VaultEntry` la cual almacenará la página, usuario y contraseña encriptada, y un alias (por defecto el dominio de la página).
  )

- **Añadir entradas**. `PasswordManager` debe poseer un método para poder agregar nuevos logins.
`add_login_entry(entry: VaultEntry)` debe encriptar la contraseña con el key obtenido en el primer paso, y 
agregar la información de login al objeto `Vault`. Por completitud, también deberá tener métodos para eliminar y modificar 
los logins, `remove_login_entry(entry_alias: str)` y `modify_login_entry(entry_alias: str)`,

- **Mostrar entradas**. `PasswordManager` debe tener la funcionalidad de mostrar la contraseña encriptada de un login al usuario. `show_login_entry(entry_alias: str)`
 la cual desencripta la contraseña guardada en el `Vault` y la muestra al usuario.

- **Bloqueo**. `PasswordManager` debe tener un método de bloqueo, `lock()`, el cual elimina el key, forzando a re-autenticarse 
con la contraseña maestra para volver a tener acceso. Por consiguiente también será necesario un método de `login`.

- **Exportar Contraseñas**. En caso el usuario solicite, las contraseñas deberán poder ser exportadas, en formato CSV o JSON.
- **Importar Contraseñas**. Las contraseñas podrán ser importadas nuevamente, desde otro `PasswordManager`.

## Consideraciones de diseño

1. Responsabilidad de las clases. Cada clase debe tener una funcionalidad clara y definida. Antes de escribir el código, 
elabora un diagrama que te permita describir claramente las relaciones entre las clases, sus atributos y métodos.

2. Construcción de objetos. Piensa qué datos son necesarios para construir los objetos de una clase, y además, quién sería el 
responsable de construirlos (el usuario mediante el programa, la clase `PasswordManager`, la clase `Vault`, etc.)

3. Manejo de errores. Piensa qué partes del programa pueden generar errores (por ejemplo, tratar de acceder a una contraseña sin haber 
hecho login primero). Con `try` y `except` puedes manejar estos errores de manera adecuada.

## Sugerencias / Ayuda
- Puede que sea necesaria una librería para encriptación y desencriptación. Recomiendo `bcrypt` para hashing y verificación, 
`cryptography` para algoritmos de encriptación.
Preguntar a Sergio en el canal de WhatsApp.
- Puedes usar cualquier versión de Python. Te recomiendo una versión superior a 3.8, y utilizar un entorno virtual para el proyecto (
recomendable `venv` o `uv`
  )
- El proyecto debe ser avanzado en este repositorio. Solo necesitamos saber lo básico de GitHub, usa VsCode o Pycharm para 
poder subir tus cambios más fácilmente.