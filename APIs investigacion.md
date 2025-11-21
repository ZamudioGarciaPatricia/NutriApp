# CETIS#61
Investigación sobre las APIs para el diseño de nuestra NutriApi
# Investigación de APIs Nutricionales

Materia: Desarrollo de frameworks en el desarrollo de software 

Docente: Treviño Tapía Juan Rubén 

Fecha: 25 de Septiembre 2025
 
Alumno: Edwin Jamel Martínez Arias y Patricia Zamudio García 
## Introducción 
API es un acrónimo de «Application Programming Interface», que se traduce como «Interfaz de Programación de Aplicaciones». Se trata de una interfaz informática destinada a conectar un software o una aplicación a otros sistemas distintos para que puedan intercambiar sus funcionalidades, sus servicios, sus tecnologías y sus datos es como la comunicación entre un mesero qué le pide un platillo al mesero (el cliente sería nuestro programa) y se lo pasa al chef qué sería como una base de datos como la qué nosotros usamos en esta investigación sin qué entren o salgan personalmente a verse y hablar entre ellos . La API se materializa 
como una puerta de acceso a una funcionalidad propiedad de una entidad independiente.

Gracias a un lenguaje de programación universal, favorece la interacción entre usuarios y proveedores mediante el envío de solicitudes de acceso a los servicios del proveedor. Facilita la creación e integración de funciones para que los desarrolladores no necesiten tener un control completo sobre el programa que desean utilizar, así se facilita la creación de apps y webs como en nuestro caso qué será necesaria para conseguir información sobre 
como una puerta de acceso a una funcionalidad propiedad de una entidad independiente.

Gracias a un lenguaje de programación universal, favorece la interacción entre usuarios y proveedores mediante el envío de solicitudes de acceso a los servicios del proveedor. Facilita la creación e integración de funciones para que los desarrolladores no necesiten tener un control completo sobre el programa que desean utilizar, así se facilita la creación de apps y webs como en nuestro caso qué será necesaria para conseguir información sobre 
RPC:Estas API se denominan llamadas a procedimientos remotos. El cliente completa una función (o procedimiento) en el servidor, y el servidor devuelve el resultado al cliente.
WebSocket: Es otro desarrollo moderno de la API web que utiliza objetos JSON para transmitir datos. La API de WebSocket admite la comunicación bidireccional entre las aplicaciones cliente y el servidor. El servidor puede enviar mensajes de devolución de llamada a los clientes conectados, por lo que es más eficiente que la API de REST.
Rest:Estas son las API más populares y flexibles que se encuentran en la web actualmente. El cliente envía las solicitudes al servidor como datos. El servidor utiliza esta entrada del cliente para iniciar funciones internas y devuelve los datos de salida al cliente. Veamos las API de REST con más detalle a continuación.
<img width="1036" height="1380" alt="image" src="https://github.com/user-attachments/assets/09b9e651-27a8-450a-beb3-8e4f83bd0a09" />
## API Seleccionada y Justificación
La API de USDA FoodData Central es una excelente opción para proyectos académicos y de investigación en nutrición debido a sus numerosas ventajas. A continuación, se presentan algunas de las razones clave por las que esta API es ideal para tu proyecto de sitio web de nutrición en la escuela:

-Acceso gratuito: La API es completamente gratuita, lo que elimina barreras económicas para estudiantes y desarrolladores. 
Esto te permite enfocarte en desarrollar tu proyecto sin preocuparte por los costos.
- Fuente oficial: La API es proporcionada por el Departamento de Agricultura de los Estados Unidos, lo que garantiza datos confiables y estandarizados. Esto es fundamental para un proyecto de nutrición, donde la precisión de la información es crucial.
- Amplia variedad de alimentos: La API contiene una amplia variedad de alimentos genéricos, procesados y de marca, incluyendo valores de macro y micronutrientes. Esto te permite
- acceder a una gran cantidad de información nutricional para diferentes tipos de alimentos.
- Límites de uso adecuados: Los límites de uso de 1000 solicitudes por hora son suficientes para pruebas académicas y prototipos. Esto te da la flexibilidad de probar y desarrollar tu proyecto sin preocuparte por exceder los límites de uso.
- Documentación clara: La documentación oficial es clara y proporciona ejemplos que facilitan la implementación. Esto te ayuda a entender cómo funciona la API y a implementarla de manera efectiva en tu proyecto.
Otras opciones como Spoonacular o Edamam no serían las mejores opciones para este proyecto debido a que están más orientadas a proyectos comerciales y requieren una suscripción o pago para acceder a sus funcionalidades completas, lo que puede ser un obstáculo para un proyecto académico o de investigación con recursos limitados.
## Ejemplos de Solicitudes y Respuestas
"totalHits": 4834,
    "currentPage": 1,
    "totalPages": 97,
    "pageList": [   ],
    "foodSearchCriteria": {
        "query": "pear",
        "generalSearchInput": "pear",
        "pageNumber": 1,
        "numberOfResultsPerPage": 50,
        "pageSize": 50,
        "requireAllWords": false
    },
    "foods": [
        {
            "fdcId": 2709254,
            "description": "Pear, raw",
            "commonNames": "",
            "additionalDescriptions": "pear, NFS",
            "dataType": "Survey (FNDDS)",
            "foodCode": 63137010,
            "publishedDate": "2024-10-31",
            "foodCategory": "Pears",
            "foodCategoryId": 3306056,
            "allHighlightFields": "<b>Includes</b>: <em>pear</em>, NFS",
              "score": 440.74396,
            "microbes": [],
            "foodNutrients": [
                {
                    "nutrientId": 1003,
                    "nutrientName": "Protein",
                    "nutrientNumber": "203",
                    "unitName": "G",
                    "value": 0.37,
                    "rank": 600,
                    "indentLevel": 1,
                    "foodNutrientId": 34387709
<img width="900" height="594" alt="image" src="https://github.com/user-attachments/assets/52e19f8e-e83e-4edf-8a64-deb2a5b2957c" />

totalHits": 4491,
    "currentPage": 1,
    "totalPages": 90,
    "pageList": 
    ],
    "foodSearchCriteria": {
        "query": "broccoli",
"generalSearchInput": "broccoli",
        "pageNumber": 1,
        "numberOfResultsPerPage": 50,
        "pageSize": 50,
        "requireAllWords": false
    },
    "foods": [
        {
"fdcId": 2549992,
            "description": "BROCCOLI",
            "dataType": "Branded",
            "gtinUpc": "078742237329",
            "publishedDate": "2023-05-25",
            "brandOwner": "Wal-Mart Stores, Inc.",
            "brandName": "GREAT VALUE",
            "ingredients": "BROCCOLI FLORETS.",
            "marketCountry": "United States",
            "foodCategory": "Frozen Vegetables",
            "modifiedDate": "2023-04-03",
            "dataSource": "LI",
            "packageWeight": "12 oz/340 g",
            "servingSizeUnit": "GRM",
            "servingSize": 85.0,
            "householdServingFullText": "1 cup",
            "shortDescription": "",
            "tradeChannels": [
                "NO_TRADE_CHANNEL"
            ],
            "allHighlightFields": "<b>Ingredients</b>: <em>BROCCOLI</em> FLORETS.",
            "score": 1129.3969,
            "microbes": [],
            "foodNutrients": [
                {
                },
<img width="900" height="479" alt="image" src="https://github.com/user-attachments/assets/91e25b5d-682c-4b32-b369-b9a17aea0d43" />
## Dificultades Encontradas y Soluciones
Durante la investigación y pruebas con las APIs nutricionales se encontraron varias dificultades comunes:
- Algunos alimentos carecen de información completa en ciertos nutrientes. La solución es combinar datos de diferentes bases o mostrar advertencias al usuario.
- Las APIs imponen límites de solicitudes, lo que puede afectar pruebas masivas. Para resolverlo, se recomienda implementar almacenamiento en caché y optimización de consultas.
- La interpretación de unidades de medida varía entre APIs (gramos, porciones, tazas). Se sugiere estandarizar todas las 
medidas a gramos o mililitros.
- La gestión de claves de API requiere seguridad, ya que no deben compartirse en repositorios públicos. Se recomienda almacenarlas en variables de entorno.
- En algunas APIs, la documentación no es totalmente clara o está incompleta. Se recomienda apoyarse en foros y ejemplos comunitarios.
##Conclusiones
Las APIs pueden ser muy útiles para el desarrollo web, especialmente para programadores ya qué te permite acceder a una gran cantidad de información facilidad y es una gran herramienta qué puede ser útil en varias funciones más allá de las nutricionales qué es para lo qué nosotros lo vamos a utilizar. Las APIs tienen una forma útil de funcionar y los desarrolladores pueden construir aplicaciones más confiables y son muy convenientes para proyectos escolares como el nuestro dónde se necesita de versatilidad, costo nulo para investigación pero a su vez qué sea lo suficientemente profesional eh seguro para nuestra
comunidad por si los estudiantes del cetis#61 llegarán a utilizarla y así mejorar su calidad de vida de ser posible con el desarrollo de nuestro sitio web (NutriApp).
