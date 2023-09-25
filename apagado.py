import time
import subprocess
import tkinter as tk

def programar_apagado():
    dia_programado = int(dia_entry.get())
    hora_programada = int(hora_entry.get())
    minutos_programados = int(minutos_entry.get())

    ahora = time.localtime()

    tiempo_programado = time.struct_time((ahora.tm_year, ahora.tm_mon, dia_programado, hora_programada, minutos_programados, 0, ahora.tm_wday, ahora.tm_yday, ahora.tm_isdst))

    diferencia_tiempo = time.mktime(tiempo_programado) - time.mktime(ahora)
    if diferencia_tiempo <= 0:
        resultado_label.config(text="La hora programada ya ha pasado.")
        return

    resultado_label.config(text=f"El ordenador se apagará a las {hora_programada:02d}:{minutos_programados:02d} del día {dia_programado:02d}...")
    ventana.update()
    time.sleep(diferencia_tiempo)
    subprocess.run(["shutdown", "/s", "/f", "/t", "0"])

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Programar Apagado")

# Etiquetas
dia_label = tk.Label(ventana, text="Día (0-31):")
dia_label.pack()
dia_entry = tk.Entry(ventana)
dia_entry.pack()

hora_label = tk.Label(ventana, text="Hora (0-23):")
hora_label.pack()
hora_entry = tk.Entry(ventana)
hora_entry.pack()

minutos_label = tk.Label(ventana, text="Minutos (0-59):")
minutos_label.pack()
minutos_entry = tk.Entry(ventana)
minutos_entry.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

programar_button = tk.Button(ventana, text="Programar Apagado", command=programar_apagado)
programar_button.pack()

ventana.mainloop()