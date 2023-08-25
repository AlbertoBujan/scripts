import json
import tkinter as tk
from tkinter import filedialog

def analizar_json(archivo):
    with open(archivo, 'r') as f:
        try:
            data = json.load(f)
            print("El JSON es válido y no contiene errores.")
        except json.JSONDecodeError as e:
            print("Error en el JSON:")
            print(e.msg)
            print("En la línea:", e.lineno)
            print("En la columna:", e.colno)
            print("Posición:", e.pos)
            print("Contexto:", e.doc)
            print("Ubicación:", e.pos)

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
    if archivo:
        analizar_json(archivo)

ventana = tk.Tk()
ventana.title("Analizador de JSON")

btn_seleccionar = tk.Button(ventana, text="Seleccionar Archivo JSON", command=seleccionar_archivo)
btn_seleccionar.pack(padx=20, pady=10)

ventana.mainloop()