# Estilo de Código

# Guía de Estilo
"""
Cuando alguien quiere hacer un cambio en el lenguaje Python, escribe una
propuesta de mejora de Python (PEP). Uno de los PEP más antiguos es PEP8,
que instruye a los programadores de Python sobre cómo diseñar su código.
PEP 8 es bastante largo, pero gran parte se relaciona con estructuras de
codificación más complejas que las que ha visto hasta ahora. La guía de
estilo de Python se escribió con el entendimiento de que el código se
lee con más frecuencia de lo que se escribe. Escribirá su código una vez
y luego comenzará a leerlo cuando comience la depuración. Cuando agrega
características a un programa, pasará más tiempo leyendo su código.
Cuando comparte su código con otros programadores, también lo leerán.
Dada la elección entre escribir código que sea más fácil de escribir o
código que sea más fácil de leer, los programadores de Python casi
siempre lo alentarán a escribir código que sea más fácil de leer.
Las siguientes pautas lo ayudarán a escribir un código
claro desde el principio
"""

# Sangría
"""
PEP 8 recomienda usar cuatro espacios por nivel de sangría. El uso de
cuatro espacios mejora la legibilidad y deja espacio para varios niveles
de sangría en cada línea. En un documento de procesamiento de texto,
las personas a menudo usan tabulaciones en lugar de espacios para
sangria. Esto funciona bien para documentos de procesamiento de texto,
pero el intérprete de Python se confunde cuando las pestañas se mezclan 
con espacios. Cada editor de texto proporciona una configuración que le
permite usar la tecla de tabulación pero luego convierte cada tabulación
a un número determinado de espacios. Definitivamente debe usar su tecla
de tabulación, pero también asegúrese de que su editor esté configurado
para insertar espacios en lugar de tabulaciones en su documento. Mezclar
tabulaciones y espacios en su archivo puede causar problemas que son muy
difíciles de diagnosticar.Si cree que tiene una combinación de
tabulaciones y espacios, puede convertir todas las tabulaciones de un
archivo en espacios en la mayoría de los editores.
"""

# Longitud de Línea
"""
Muchos programadores de Python recomiendan que cada línea tenga menos de
80 caracteres. Históricamente, esta guía se desarrolló porque la mayoría
de las computadoras solo podían incluir 79 caracteres en una sola línea
en una ventana de terminal. Actualmente, las personas pueden colocar
líneas mucho más largas en sus pantallas, pero existen otras razones
para adherirse a la longitud de línea estándar de 79 caracteres. Los
programadores profesionales a menudo tienen varios archivos abiertos en
la misma pantalla, y usar la longitud de línea estándar les permite ver
líneas completas en dos o tres archivos que están abiertos uno al lado
del otro en la pantalla. PEP 8 también recomienda que limite todos sus
comentarios a 72 caracteres por línea, porque algunas de las
herramientas que generan documentación automática para proyectos más
grandes agregan caracteres de formato al comienzo de cada línea
comentada. Las pautas de PEP 8 para la longitud de la línea no son 
inamovibles y algunos equipos prefieren un límite de 99 caracteres.
No se preocupe demasiado por la longitud de línea en su código mientras
aprende, pero tenga en cuenta que las personas que trabajan en
colaboración casi siempre siguen las pautas de PEP 8. La mayoría de los
editores le permiten configurar una señal visual, generalmente una línea 
vertical en su pantalla, que le muestra dónde están estos límites.

Nota: el Apéndice B le muestra cómo configurar su editor de texto para
que siempre inserte cuatro espacios cada vez que presione la tecla de
tabulación y muestre una guía vertical para ayudarlo a seguir el límite
de 79 caracteres.
"""

# Espacio en Blanco
"""
Para agrupar partes de su programa visualmente, use líneas en blanco. 
Debe usar líneas en blanco para organizar sus archivos, pero no lo haga
en exceso. Siguiendo los ejemplos proporcionados en este libro, debe
lograr el equilibrio correcto. Por ejemplo, si tiene cinco líneas de
código que construyen una lista y luego otras tres líneas que hacen algo
con esa lista, es apropiado colocar una línea en blanco entre las dos
secciones. Sin embargo, no debe colocar tres o cuatro líneas en blanco
entre las dos secciones. Las líneas en blanco no afectarán la forma en
que se ejecuta su código, pero afectarán la legibilidad de su código. 
El intérprete de Python usa sangría horizontal para interpretar el
significado de su código, pero ignora el espacio vertical.
"""

# Otras Pautas de Estilo
"""
PEP 8 tiene muchas recomendaciones de estilo adicionales, pero la mayoría
de las pautas se refieren a programas más complejos que los que está 
escribiendo en este momento. A medida que aprenda estructuras de Python
más complejas, compartiré las partes relevantes de las pautas de PEP 8.
"""