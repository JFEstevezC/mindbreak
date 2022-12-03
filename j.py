import time

tiempo = int(input('¿Cuánto tiempo deseas que dure el temporizador (en segundos)? '))

for x in range(tiempo):
    print(tiempo - x)
    time.sleep(1)

print('¡El tiempo ha terminado!')
