import nidaqmx
import time

# Por algun motivo este puerto funciona con logica negativa

# Crear tarea para salida digital
do_task2 = nidaqmx.Task()
do_task2.do_channels.add_do_chan("PXI1Slot4/port0/line7")
# Iniciar la tarea 
do_task2.start()

#Activar el enable
do_task2.write(False)

# Delay 1 segundo
time.sleep(10)

# Finalizar tarea
do_task2.write(True)
do_task2.close()
