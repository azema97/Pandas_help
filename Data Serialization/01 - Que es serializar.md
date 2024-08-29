# ¿Que es serializar?

Serializar en Ciencia de Datos se refiere al proceso de convertir estructuras de datos o objetos de estado en un formato que puede ser almacenado (por ejemplo, en un archivo o memoria de almacenamiento) o transmitido (por ejemplo, a través de una conexión de red) y reconstruido posteriormente en el mismo u otro entorno informático.

> El término "serialización" proviene del concepto de convertir un objeto en una "serie" o secuencia lineal de bytes.

Este proceso permite a los científicos de datos almacenar los resultados de su trabajo, como modelos de aprendizaje automático, para uso futuro sin tener que volver a entrenar el modelo cada vez. También facilita la compartición de estos modelos entre diferentes plataformas o lenguajes de programación.

En resumen, **serializar implica tomar "objetos" en su código (como listas, diccionarios, clases, etc.) y convertirlos en una cadena de bytes o en un archivo de texto** que puede ser guardado o enviado a cualquier lugar y luego reconstruido (deserializado) más tarde manteniendo todas las características originales del objeto.

Un ejemplo común de serialización en ciencia de datos es el uso de la biblioteca pickle en Python, que permite la serialización y deserialización de objetos de Python directamente en un archivo binario o en una cadena de bytes. Sin embargo, hay que tener cuidado con la seguridad y la compatibilidad al usar pickle, ya que cargar datos pickled puede ejecutar código arbitrario, y los datos pickled pueden no ser compatibles entre diferentes versiones de Python.

[Tutorial from codebasics using Pickle and JobLib (8 minutes)](https://youtu.be/KfnhNlD8WZI?feature=shared)