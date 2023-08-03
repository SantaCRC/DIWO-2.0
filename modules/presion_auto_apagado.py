from rs import leer as presion
from bombas import leer as bombas
import time

fin_secuencia=False
bombas(b'!C904 0\r') # apaga la turbo

while not fin_secuencia:
    velocidad=bombas(b'?V905\r') # Velocidad
    velocidad=velocidad.split()[1].split(';')[0]
    print(velocidad)
    if float(velocidad)<= 5:
        print("Turbo detenida..")
        bombas(b'!C910 0\r') # apagar mecanica
        print("Mecanica detenida..")
        fin_secuencia=True
    else:
        time.sleep(5)


