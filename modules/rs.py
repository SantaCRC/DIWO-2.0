import serial
import time

# Configuración del puerto serie
port = "COM18"  # Cambia "COM1" por el nombre del puerto que estés usando
baudrate =9600  # Baudrate del puerto serie
timeout = 1  # Tiempo de espera para leer datos en segundos
bytesize = 8    # Number of data bits = 8
parity   = 'N'  # No parity
stopbits = 1    # Number of Stop bits = 1

# Abrir el puerto serie
ser = serial.Serial(port, baudrate, timeout=timeout, bytesize=bytesize, parity=parity,
                    stopbits=stopbits)

def leer(comando):
    ser.write(comando)
    # Mandar comando
    time.sleep(50/1000) #50 ms es la minima aceptada por el rs232, no mas rapido

    # Leer datos del puerto serie
    data = ser.read(13)  # Leer una línea de datos

    # Mostrar los datos leídos
    decoded = data.decode('ascii')
    print(decoded)
    # return
    return decoded
if __name__ == "__main__":
    leer(b'#01RS\r')
    leer(b'#01RDS\r')
    leer(b'#01IG1\r')
    leer(b'#01RD\r')
    leer(b'#01RDCG2\r')
    ser.close()



