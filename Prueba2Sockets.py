from machine import Timer
import network
from time import *
import socket

def gen_ap(nombre='ESP32-AP', contra="12345678"):
    global ap
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=nombre)
    ap.config(authmode=3, password=contra)
    ap.config(channel=10, max_clients=10, hidden=0)
    print("Se inició un AP en este dispositivo con la siguiente configuración:")
    print(f"Nombre del AP: {nombre}")
    print(f"Contraseña: {contra}")
    print("Configuración de red:", ap.ifconfig())
    return ap





def abrir_socket(puerto=8000, max_conexiones=10):
    global conn, addr, s
    direccion_ip = ap.ifconfig()[0]  # obtener dirección IP del AP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # crear socket TCP/IP
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # permitir reuso de dirección
    s.bind((direccion_ip, puerto))  # vincular socket con dirección y puerto
    s.listen(max_conexiones)  # establecer máximo de conexiones en cola
    print(f"Servidor escuchando en {direccion_ip}:{puerto}...")
    print("Esperando conexión cliente...")
    (conn, addr) = s.accept()  # aceptar conexión entrante
    print(f"Conexión establecida con cliente: {addr}")
    return conn, addr

def recibir_mensaje(n_bytes):
    print("Recibiendo mensajes...")
    mensaje = conn.recv(n_bytes)  # Recibir bytes del cliente
    print("Mensaje recibido:", mensaje)
    return mensaje

def cerrar_socket():
    if 'conn' in globals():
        conn.close()
    if 's' in globals():
        s.close()
    print("Socket y conexión cerrados correctamente")

def desborde(timer):
    global n_bytes
    recibir_mensaje(n_bytes)
    

#Función1
# ap = gen_ap()  # Con valores por defecto
ap = gen_ap("MiESP32", "angel123angel")  # Con valores personalizados
# Función2
conn, addr = abrir_socket()  # Con valores por defecto
# conn, addr = abrir_socket(puerto=8080, max_conexiones=5)  # Con valores personalizados
n_bytes=8

temp=Timer(0)
temp.init(period=1000, mode=Timer.PERIODIC, callback=desborde)

