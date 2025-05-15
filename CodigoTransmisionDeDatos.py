import socket
import time
import sys

class ESP32Client:
    def __init__(self, server_ip, port=8000, timeout=5, retry_delay=2, max_retries=3):
        self.server_ip = server_ip
        self.port = port
        self.timeout = timeout
        self.retry_delay = retry_delay
        self.max_retries = max_retries
        self.socket = None

    def connect(self):
        """Establece conexión con el servidor ESP32"""
        attempts = 0
        while attempts < self.max_retries:
            try:
                if self.socket:
                    self.socket.close()
                
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.settimeout(self.timeout)
                self.socket.connect((self.server_ip, self.port))
                print(f"Conectado al servidor ESP32 en {self.server_ip}:{self.port}")
                return True
            except socket.error as e:
                attempts += 1
                print(f"Error de conexión (intento {attempts}/{self.max_retries}): {e}")
                if attempts < self.max_retries:
                    time.sleep(self.retry_delay)
        return False

    def send_message(self, message):
        """Envía un mensaje al servidor ESP32"""
        try:
            if not self.socket:
                raise socket.error("Socket no inicializado")
                
            self.socket.sendall(message.encode())
            print(f"Mensaje enviado: {message}")
            return True
        except socket.error as e:
            print(f"Error al enviar mensaje: {e}")
            return False

    def close(self):
        """Cierra la conexión correctamente"""
        if self.socket:
            self.socket.close()
            self.socket = None
            print("Conexión cerrada correctamente")

    def __enter__(self):
        """Para usar con 'with' statement"""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Para usar con 'with' statement"""
        self.close()

def main():
    # Configuración (ajusta estos valores según tu red ESP32)
    SERVER_IP = "192.168.4.1"  # IP del AP de la ESP32
    PORT = 8000
    
    # Crear instancia del cliente
    client = ESP32Client(SERVER_IP, PORT)
    
    if not client.connect():
        print("No se pudo establecer la conexión inicial. Saliendo...")
        return

    try:
        while True:
            message = input("Ingrese mensaje para enviar a ESP32 (o 'salir' para terminar): ")
            if message.lower() == 'salir':
                break
                
            # Intentar enviar el mensaje
            if not client.send_message(message):
                print("Intentando reconectar...")
                if not client.connect():
                    print("No se pudo reconectar. Saliendo...")
                    break
                    
            time.sleep(0.5)  # Pequeña pausa entre mensajes
            
    except KeyboardInterrupt:
        print("\nInterrupción por teclado recibida.")
    finally:
        client.close()

if __name__ == "__main__":
    main()