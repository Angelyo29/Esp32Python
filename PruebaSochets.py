#Hola bb

import network
from time import *

""" CREACTÓN DE ESTACIÓN """
# https://docs.micropython.org/en/latest/library/network.WLAN.html
wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)    # activate the interface
#wlan.disconnect() # desconectar de red

"""ESCANEAR REDES"""
"""Wifi: (ssid, bssid, channel, RSSI, authmode, hidden).
There may be further fields, specific to a particular device."""
""" There are five values for authmode:
0 - open
1 - WEP
2 - WPA-PSK
3 - WPA2-PSK
4 - WPA/WPA2-PSK """
l = wlan.scan()
print(l)    # scan for access points
[print(i) for i in l] # crear lista de elementos en la lista de scan
"""
def do_connect(nombre='Angel wifi', contra='angel123'):
    import network
    import time
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print('Conectando a la red...')
        wlan.connect(nombre, contra)
        
        # Esperar hasta que esté conectado (con tiempo de espera máximo)
        max_intentos = 10
        for i in range(max_intentos):
            if wlan.isconnected():
                break
            print(f'Intentando conectar... ({i+1}/{max_intentos})')
            time.sleep(1)
        else:
            print('Error: No se pudo conectar después de', max_intentos, 'intentos')
            return False
    
    print('Configuración de red:', wlan.ifconfig())
    return True

# Ejemplo de uso:
# do_connect()  # Usa valores por defecto
# do_connect('MiWifi', 'MiContraseña')  # Especifica SSID y contraseña
"""

# Crear y configurar Access Point
ap = network.WLAN(network.AP_IF)  # Crear interfaz Access Point
ap.active(True)                   # Activar la interfaz
ap.config(essid='ESP32-AP')       # Establecer nombre de la red (SSID)
ap.config(authmode=2, password="12345678")  # Autenticación WPA2 y contraseña
ap.config(channel=10)             # Establecer canal WiFi (1-14)
ap.config(max_clients=10)         # Número máximo de clientes permitidos
ap.config(hidden=0)               # Red visible (0=visible, 1=oculta)