import serial
import time

# Configuración del puerto serie
port = "COM12"  # Cambia "COM1" por el nombre del puerto que estés usando
baudrate =9600  # Baudrate del puerto serie
timeout = 1  # Tiempo de espera para leer datos en segundos
bytesize = 7    # Number of data bits = 8
parity   = 'O'  # No parity
stopbits = 1    # Number of Stop bits = 1

# Abrir el puerto serie
ser = serial.Serial(port, baudrate, timeout=timeout, bytesize=bytesize, parity=parity,
                    stopbits=stopbits)

def leer(comando):
    ser.write(comando)
    # Mandar comando
    time.sleep(50/1000) #50 ms es la minima aceptada por el rs232, no mas rapido

    # Leer datos del puerto serie
    data = ser.readline() # Leer una línea de datos

    # Mostrar los datos leídos
    print(data.decode('ascii'))
    # Cerrar la conexion

leer(b'RT,ON\r') # activar el control remoto
#leer(b'RT,OFF\r')
#leer(b'DT,HELLO\r')
leer(b'AC1,20.00,ON\r') # Setear en 20 el MFC y activarlo
time.sleep(2)
leer(b'AC1,0.00,OFF\r') # Setear en 0 el MFC y desactivarlo
leer(b'RT,OFF\r') #quitar el control remoto

ser.close()
