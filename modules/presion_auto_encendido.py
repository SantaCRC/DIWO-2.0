from rs import leer as presion
from bombas import leer as bombas
import time

fin_secuencia=False
bombas(b'!C910 1\r')

while not fin_secuencia:
    actual = presion(b'#01RDCG2\r')
    actual=actual.replace("*01 ","")
    actual=actual.replace("\r","")
    actual=actual.replace("\x00","")
    print(actual)
    if float(actual) < 5:
        print("Iniciando la turbo")
        bombas(b'!C904 1\r')
        fin_secuencia = True
    else:
        time.sleep(5)


while fin_secuencia:
    velocidad=bombas(b'?V905\r') # Velocidad
    velocidad=velocidad.split()[1].split(';')[0]
    print(velocidad)
    if float(velocidad)> 95:
        print("Velocidad nominal alcanzada, fin de la secuencia...")
        break

    
