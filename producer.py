import json
import time
from kafka import KafkaProducer

# Configuración del productor de Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'], # Dirección de nuestra tubería Kafka
    value_serializer=lambda v: json.dumps(v).encode('utf-8') # Cómo convertir nuestros mensajes a texto
)

# Nombre del "canal" o "tema" donde enviaremos los juguetes
TOPIC_NAME = 'juguetes_financieros' # ¡Un canal para juguetes financieros!

print(f"Enviando mensajes al topic: {TOPIC_NAME}")

# Vamos a enviar 100 "juguetes" (mensajes)
for i in range(100):
    data = {
        'id_juguete': i + 1,
        'nombre': f'Juguete_{i+1}',
        'valor': round(100 * (1 + (i / 10)), 2), # Un valor que sube un poco
        'timestamp': time.time() # Cuando se generó el juguete
    }
    producer.send(TOPIC_NAME, value=data) # Enviar el juguete a la tubería
    print(f"Enviado: {data}")
    time.sleep(1) # Esperar un segundo antes de enviar el siguiente

producer.flush() # Asegurarse de que todos los mensajes se enviaron
print("Envío de mensajes terminado.")