import nidaqmx
import time
import argparse

# Crear la entrada por argumentos
parser = argparse.ArgumentParser(description='Modulo de control del magnetron')
parser.add_argument('--tiempo', metavar='t', type=int, help='Tiempo de descarga')

tiempo = os.sys.argv[0]
potencia = os.sys.argv[1]

# Determinar el voltaje de referencia a partir de la potencia relación 450W*V
voltaje = float(potencia)*0.0022222222222222222


# Crear tarea 1 para salida analógica
ao_task1 = nidaqmx.Task()
ao_task1.ao_channels.add_ao_voltage_chan("PXI1Slot2/ao0")

# Iniciar la tarea 1
ao_task1.start()

# Crear tarea 2 para salida digital
do_task2 = nidaqmx.Task()
do_task2.do_channels.add_do_chan("PXI1Slot2/port0/line1")
# Iniciar la tarea 2
do_task2.start()

# Voltaje de refencia
ao_task1.write(voltaje)

#Activar el enable
do_task2.write(True)

# Delay 1 segundo
time.sleep(tiempo)

# Detener y cerrar las tareas
ao_task1.write(0)
ao_task1.close()

do_task2.write(False)
do_task2.close()
