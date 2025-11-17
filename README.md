# ⚡ Plataforma de Análisis de Datos en Tiempo Real: Kafka, FastAPI y Pandas

Esta es una solución de arquitectura de datos en tiempo real (Real-Time Data Platform) diseñada para la ingesta, procesamiento, análisis y visualización de flujos de datos continuos. El proyecto demuestra un *pipeline* escalable y de alta disponibilidad, ideal para monitoreo de sistemas, IoT o análisis financiero.

## ⚙️ Arquitectura de la Solución

El sistema se basa en una arquitectura de microservicios y streaming, donde cada componente cumple una función específica:

| Componente | Tecnología | Rol en el Pipeline |
| :--- | :--- | :--- |
| **Ingesta/Mensajería** | **Apache Kafka** | Broker de mensajería de alta throughput para desacoplar el productor del consumidor y asegurar la persistencia del flujo de datos. |
| **Procesamiento** | **Python (Consumer) + Pandas** | Consume datos de Kafka y realiza transformaciones, agregaciones y análisis estadísticos rápidos en memoria. |
| **API de Datos** | **FastAPI (Integrado)** | Sirve los resultados del análisis en tiempo real a través de endpoints RESTful asíncronos de baja latencia (Uvicorn). |
| **Visualización** | **Plotly / Dash** | Dashboard interactivo que se actualiza en tiempo real para reflejar las métricas de negocio. |
| **Orquestación** | **Docker & Docker Compose** | Contenedorización de Zookeeper y Kafka para un despliegue rápido y consistente en cualquier entorno. |

## ✨ Características Clave

* **Baja Latencia y Alta Disponibilidad:** Utilización de Kafka para gestionar picos de tráfico y garantizar la entrega de datos.
* **Análisis Eficiente:** Pandas se utiliza para realizar cálculos complejos y analítica descriptiva (promedios, máximos, agregaciones) sobre el *stream* de datos.
* **Despliegue Simplificado:** Configuración completa de servicios con `docker-compose.yml`.
* **Visualización Dinámica:** Dashboards construidos con Plotly/Dash que permiten la toma de decisiones inmediata.

## 🚀 Configuración y Ejecución

### Requisitos Previos

* **Python 3.8+**
* **Docker Desktop** (para levantar Kafka y Zookeeper)
* **Git**

### 1. Clonar el Repositorio

```bash
git clone [https://github.com/santiagourdaneta/Plataforma-de-Analisis-de-Datos-en-Tiempo-Real-con-Kafka-FastAPI-y-Pandas.git](https://github.com/santiagourdaneta/Plataforma-de-Analisis-de-Datos-en-Tiempo-Real-con-Kafka-FastAPI-y-Pandas.git)
cd Plataforma-de-Analisis-de-Datos-en-Tiempo-Real-con-Kafka-FastAPI-y-Pandas

2. Iniciar Servicios de Mensajería (Kafka)
Desde la raíz del proyecto, levanta los servicios de Kafka y Zookeeper usando Docker Compose:

docker compose up -d

3. Instalar Dependencias de Python
Instala las librerías requeridas (FastAPI, Pandas, kafka-python, Dash, Plotly, etc.):

pip install -r requirements.txt

4. Ejecutar el Pipeline
Abre tres terminales separadas:

1 (Productor) producer.py python producer.py Simula y envía datos continuos a un topic de Kafka.
2 (Consumidor/API) consumer_processor.py python consumer_processor.py Consume datos, los procesa con Pandas y sirve la API/Dash.

5. Acceder a la Plataforma
Navega a la URL proporcionada por el script consumer_processor.py (generalmente http://127.0.0.1:8050/) para ver el dashboard de datos en tiempo real.

🛑 Detener Servicios
Para detener todos los contenedores de Docker:

docker compose down




