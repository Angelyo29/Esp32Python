import socket
import time

def conectar_socket(ip_servidor, puerto):
    try:
        s = socket.socket()
        s.settimeout(10)  # 5 segundos de timeout
        s.connect((ip_servidor, puerto))
        print("Conexión exitosa con la ESP32")
        return s
    except Exception as e:
        print(f"Error al conectar: {e}")
        return None

IP_SERVIDOR_ESP32 = "192.168.4.1"
PUERTO = 8000

s = conectar_socket(IP_SERVIDOR_ESP32, PUERTO)
if s:
    try:
        while True:
            mensaje = input("Mensaje a enviar (o 'salir'): ")
            if mensaje.lower() == "salir":
                break
            s.send(mensaje.encode())
    finally:
        s.close()