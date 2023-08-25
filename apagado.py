import time
import subprocess

def programar_apagado(hora, minutos):
    ahora = time.localtime()
    tiempo_programado = time.struct_time((ahora.tm_year, ahora.tm_mon, ahora.tm_mday, hora, minutos, 0, ahora.tm_wday, ahora.tm_yday, ahora.tm_isdst))

    diferencia_tiempo = time.mktime(tiempo_programado) - time.mktime(ahora)
    if diferencia_tiempo <= 0:
        print("La hora programada ya ha pasado.")
        return

    print(f"Apagando la computadora a las {hora}:{minutos}...")
    time.sleep(diferencia_tiempo)
    subprocess.run(["shutdown", "/s", "/f", "/t", "0"])

hora_programada = int(input("Ingresa la hora (0-23): "))
minutos_programados = int(input("Ingresa los minutos (0-59): "))

programar_apagado(hora_programada, minutos_programados)
