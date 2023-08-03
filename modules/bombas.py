import serial
import time 

# Configuración del puerto serie
port = "COM11"  # Cambia "COM1" por el nombre del puerto que estés usando
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
    data = ser.readline()  # Leer una línea de datos
    decoded = data.decode('ascii')
    # Mostrar los datos leídos
    print(decoded)
    # Cerrar la conexion
    return decoded

if __name__ == "__main__":
    leer(b'?S902\r')
    leer(b'?S910\r')
    leer(b'!C910 1\r') # Encender la bomba mecanica con el 0 se apaga, y con 1 se enciende
    leer(b'!V910\r')
    leer(b'!C904 0\r') # Encender la turbo
    while True:
        velocidad=leer(b'?V905\r') # Velocidad
        velocidad=velocidad.split()[1].split(';')
        print(velocidad[0])


