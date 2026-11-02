import socket
import sys
import os
import json
import paho.mqtt.client as mqtt
from datetime import datetime

print("Iniciando Servidor Fermax Meet Me MQTT...")

# Leer opciones de Home Assistant Add-on (se guardan en /data/options.json)
options_path = '/data/options.json'
if os.path.exists(options_path):
    with open(options_path) as f:
        config = json.load(f)
    MQTT_SERVER = config.get("MQTTserver", "127.0.0.1")
    MQTT_USER = config.get("MQTTuser", "")
    MQTT_PASS = config.get("MQTTpass", "")
else:
    MQTT_SERVER = "127.0.0.1"
    MQTT_USER = ""
    MQTT_PASS = ""

print(f"Configurando MQTT hacia: {MQTT_SERVER}")

# Codigo original del script de dave-code-ruiz (socket server en puerto 9800)
# Aqui va la logica de escucha del videoportero...
sys.stdout.flush()
