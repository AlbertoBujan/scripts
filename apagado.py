import time
import subprocess

def programar_apagado(dia, hora, minutos):
    ahora = time.localtime()

    tiempo_programado = time.struct_time((ahora.tm_year, ahora.tm_mon, dia, hora, minutos, 0, ahora.tm_wday, ahora.tm_yday, ahora.tm_isdst))

    diferencia_tiempo = time.mktime(tiempo_programado) - time.mktime(ahora)
    if diferencia_tiempo <= 0:
        print("La hora programada ya ha pasado.")
        return

    print(f"El ordenador se apagará a las {hora:02d}:{minutos:02d} del día {dia:02d}...")
    print(diferencia_tiempo)
    time.sleep(diferencia_tiempo)
    subprocess.run(["shutdown", "/s", "/f", "/t", "0"])

dia_programado = int(input("Ingresa el dia (0-31): "))
hora_programada = int(input("Ingresa la hora (0-23): "))
minutos_programados = int(input("Ingresa los minutos (0-59): "))

programar_apagado(dia_programado, hora_programada, minutos_programados)