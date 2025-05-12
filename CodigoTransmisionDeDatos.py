

import socket
import time

def do_connect(nombre='MiESP32', contra='angel123angel'):
    import network
    global wlan
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Conectando a', nombre, '...')
        wlan.connect(nombre, contra)
        while not wlan.isconnected():
            pass
    print('Configuración de red:', wlan.ifconfig())

def conectar_socket(ip_servidor, puerto=8000):
    global s
    s = socket.socket()  # Crear objeto socket
    s.connect((ip_servidor, puerto))
    print("Conectado al servidor ESP32")

def enviar_mensaje(mensaje):
    s.send(mensaje.encode())
    print(f"Mensaje enviado: {mensaje}")

# Configuración (ajusta estos valores según tu red ESP32)
NOMBRE_RED_ESP32 = "MiESP32"
CONTRASENA_ESP32 = "angel123angel"
IP_SERVIDOR_ESP32 = "192.168.4.1"  # Esta es normalmente la IP del AP de la ESP32
PUERTO = 8000

# Conectar a la red ESP32 (esto sería necesario si estás en un dispositivo como Raspberry Pi)
# do_connect(NOMBRE_RED_ESP32, CONTRASENA_ESP32)

# Conectar al socket del servidor ESP32
conectar_socket(IP_SERVIDOR_ESP32, PUERTO)

# Ejemplo de envío de mensajes
try:
    while True:
        mensaje = input("Ingrese mensaje para enviar a ESP32 (o 'salir' para terminar): ")
        if mensaje.lower() == 'salir':
            break
        enviar_mensaje(mensaje)
        time.sleep(0.5)  # Pequeña pausa entre mensajes
finally:
    s.close()
    print("Conexión cerrada")