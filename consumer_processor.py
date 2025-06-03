import json
import time
from kafka import KafkaConsumer
import pandas as pd
from collections import deque
import threading # Para que el cerebro y el mensajero trabajen al mismo tiempo
from fastapi import FastAPI # El mensajero
import uvicorn # Para que el mensajero funcione
import dash # La pantalla de dibujos
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go # Para hacer los dibujos

# --- Parte del Cerebro Contable (Kafka Consumer + Pandas) ---
consumer = KafkaConsumer(
    'juguetes_financieros',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='mi_grupo_cerebro',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Una lista donde guardaremos los últimos 100 juguetes para el análisis
ultimos_juguetes = deque(maxlen=100)
# Una variable para guardar los resultados del análisis y que el mensajero los pueda ver
resultados_analisis = {"promedio_valor": 0, "max_valor": 0}

def procesar_mensajes_kafka():
    """Función que escucha Kafka y procesa los datos."""
    print("Escuchando mensajes en el topic 'juguetes_financieros'...")
    for message in consumer:
        juguete = message.value
        print(f"Recibido: {juguete}")

        ultimos_juguetes.append(juguete)

        # Convertir a DataFrame de Pandas
        df = pd.DataFrame(list(ultimos_juguetes))

        # Calcular los resultados con Pandas
        if not df.empty:
            promedio = df['valor'].mean()
            maximo = df['valor'].max()
            global resultados_analisis
            resultados_analisis = {"promedio_valor": promedio, "max_valor": maximo, "datos_grafico": df.to_dict('records')}
        print(f"    Resultados del análisis actualizados: {resultados_analisis['promedio_valor']:.2f}, {resultados_analisis['max_valor']:.2f}")
        print("-" * 30)

# Iniciar el proceso de escuchar Kafka en un "hilo" separado para que no bloquee al mensajero
kafka_thread = threading.Thread(target=procesar_mensajes_kafka)
kafka_thread.daemon = True # Esto hace que el hilo se cierre cuando el programa principal se cierra
kafka_thread.start()

# --- Parte del Mensajero Rápido (FastAPI) ---
app_fastapi = FastAPI()

@app_fastapi.get("/analisis_juguetes") # Cuando alguien pregunte por esta dirección
async def get_analisis_juguetes(): # El mensajero responderá con los resultados
    return resultados_analisis

# --- Parte de la Pantalla de Dibujos (Dash) ---
app_dash = dash.Dash(__name__)

app_dash.layout = html.Div([
    html.H1("Análisis de Juguetes en Tiempo Real"), # Un título grande
    html.Div(id='live-update-text'), # Un espacio para mostrar números
    dcc.Graph(id='live-update-graph'), # Un espacio para el gráfico
    dcc.Interval( # Esto hace que la pantalla se actualice cada segundo
        id='interval-component',
        interval=1*1000, # en milisegundos (1 segundo)
        n_intervals=0
    )
])

@app_dash.callback(Output('live-update-text', 'children'),
                  Output('live-update-graph', 'figure'),
                  Input('interval-component', 'n_intervals'))
def update_graph_live(n):
    # El cerebro le pide los datos al mensajero
    # En una aplicación real, el Dash le pediría los datos a FastAPI.
    # Aquí, como están en el mismo archivo, acceden directamente a resultados_analisis
    data = resultados_analisis

    # Actualizar el texto
    promedio = data.get("promedio_valor", 0)
    maximo = data.get("max_valor", 0)
    text_output = html.Span(f'Valor Promedio: {promedio:.2f} | Valor Máximo: {maximo:.2f}')

    # Actualizar el gráfico
    df_plot = pd.DataFrame(data.get("datos_grafico", []))
    fig = go.Figure()
    if not df_plot.empty:
        fig.add_trace(go.Scatter(x=df_plot['timestamp'], y=df_plot['valor'], mode='lines+markers', name='Valor del Juguete'))
        fig.update_layout(title='Valores de los últimos Juguetes',
                          xaxis_title='Tiempo',
                          yaxis_title='Valor',
                          uirevision='True') # Para que el gráfico no se reinicie al actualizar

    return text_output, fig

# --- Encender el Mensajero Rápido y la Pantalla de Dibujos ---
if __name__ == "__main__":
    # Puedes elegir si quieres iniciar Dash o FastAPI aquí.
    # Para simplificar, vamos a iniciar Dash directamente, que internamente usará los datos de "resultados_analisis"
    # Si quisieras ejecutar FastAPI por separado, harías:
    # uvicorn.run(app_fastapi, host="0.0.0.0", port=8000)
    app_dash.run(debug=True, port=8050)
    # debug=True: recarga la pantalla si cambias el código (solo para desarrollar)