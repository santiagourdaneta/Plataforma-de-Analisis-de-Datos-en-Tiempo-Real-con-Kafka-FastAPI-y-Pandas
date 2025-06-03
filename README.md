# Plataforma-de-An-lisis-de-Datos-en-Tiempo-Real-con-Kafka-FastAPI-y-Pandas
Esta es una Plataforma de Análisis de Datos en Tiempo Real robusta y escalable, construida para ingerir, procesar y visualizar flujos de datos continuos. Utiliza Apache Kafka como sistema de mensajería de alta throughput, FastAPI para una API de datos de baja latencia, y Pandas para el procesamiento y análisis de datos.

🚀 Plataforma de Análisis de Datos en Tiempo Real
Una solución completa para la ingesta, procesamiento y visualización de datos en tiempo real, diseñada para manejar flujos de datos de alto volumen con eficiencia y escalabilidad.

✨ Características Principales

Ingesta de Datos en Tiempo Real: Utiliza Apache Kafka para una transmisión de datos robusta y de alta throughput, asegurando que ningún dato se pierda y que la latencia sea mínima.
Procesamiento Eficiente: Integra Pandas para un procesamiento y análisis de datos en memoria, permitiendo cálculos rápidos y transformaciones complejas sobre los flujos de datos.
API de Datos de Baja Latencia: Desarrollada con FastAPI, proporciona un punto de acceso RESTful asíncrono para consumir los resultados del análisis en tiempo real, ideal para integrar con otras aplicaciones o servicios.
Visualización Interactiva: La interfaz de usuario construida con Plotly/Dash ofrece dashboards dinámicos y personalizables que se actualizan en tiempo real, permitiendo una toma de decisiones informada y rápida.
Contenedorización con Docker: Todos los componentes se despliegan fácilmente utilizando Docker y Docker Compose, garantizando entornos consistentes y facilitando la escalabilidad.

💡 Casos de Uso Potenciales

Análisis Financiero: Monitoreo de cotizaciones bursátiles, detección de anomalías y análisis de mercado en tiempo real.
Internet de las Cosas (IoT): Procesamiento de datos de sensores para monitoreo ambiental, gestión de activos o telemática.
Monitoreo de Salud: Seguimiento de signos vitales, alertas tempranas de condiciones críticas o análisis de tendencias de pacientes.

🛠️ Tecnologías Utilizadas

Python 3.x: Lenguaje de programación principal.
Apache Kafka: Plataforma de streaming distribuida para la mensajería en tiempo real.
FastAPI: Framework web asíncrono para construir APIs rápidas.
Pandas: Librería para manipulación y análisis de datos.
Plotly/Dash: Framework para construir dashboards analíticos interactivos.
Docker & Docker Compose: Para la contenedorización y orquestación de servicios.

🚀 Configuración y Ejecución (Paso a Paso)

Sigue estos pasos para poner en marcha el proyecto en tu máquina local.

Requisitos Previos
Asegúrate de tener instalado lo siguiente:

Python 3.8+
Docker Desktop (con WSL 2 habilitado y configurado en Windows)
Git (opcional, para clonar el repositorio)
1. Clonar el Repositorio (Opcional, si estás usando Git)

git clone https://github.com/santiagourdaneta/Plataforma-de-Analisis-de-Datos-en-Tiempo-Real-con-Kafka-FastAPI-y-Pandas/
cd Plataforma-de-Analisis-de-Datos-en-Tiempo-Real-con-Kafka-FastAPI-y-Pandas

2. Iniciar Apache Kafka con Docker Compose
Desde la raíz de tu proyecto (donde se encuentra docker-compose.yml), abre una terminal (Símbolo del sistema en Windows) y ejecuta:

docker compose up -d
Esto descargará las imágenes de Kafka y Zookeeper e iniciará los servicios en segundo plano. Verifica que estén corriendo con docker ps o en la aplicación Docker Desktop.

3. Instalar Dependencias de Python
Abre una nueva terminal en la raíz de tu proyecto e instala las librerías necesarias:

pip install kafka-python pandas fastapi uvicorn dash plotly

4. Ejecutar el Productor de Datos
En una nueva terminal (diferente a la anterior y a la de Docker), ejecuta el script del productor que simula el envío de datos:

python producer.py
Verás mensajes indicando que los "juguetes" (datos) se están enviando a Kafka.

5. Ejecutar el Procesador y Visualizador de Datos
En una tercera nueva terminal, ejecuta el script principal que consume datos de Kafka, los procesa con Pandas, y sirve la aplicación Dash:

python consumer_processor.py
Después de unos segundos, verás un mensaje indicando que Dash está corriendo en una dirección local, por ejemplo: Dash is running on http://127.0.0.1:8050/.

6. Acceder a la Plataforma de Visualización
Abre tu navegador web (Chrome, Firefox, Edge) y navega a la dirección proporcionada por Dash (normalmente http://127.0.0.1:8050/).

Deberías ver una página web con un título y, después de unos instantes, los valores de promedio y máximo actualizándose, junto con un gráfico que muestra el valor de los datos en tiempo real.

🛑 Detener los Servicios
Para detener todos los servicios de Docker y limpiar los contenedores, abre la terminal donde iniciaste docker compose up -d y ejecuta:

docker compose down
Cierra las otras terminales donde ejecutaste los scripts de Python.
