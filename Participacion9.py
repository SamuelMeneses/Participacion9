from typing import Tuple

class DatosMeteorologicos:

    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:

        total_temperatura = 0
        total_humedad = 0
        total_presion = 0
        total_velocidad_viento = 0
        conteo_registros = 0
        conteo_direcciones = {}

        with open("datos_meteorologicos.txt", "r") as archivo:
            for linea in archivo:

                if linea.startswith("Temperatura:"):
                    total_temperatura += float(linea.split(":")[1])

                elif linea.startswith("Humedad:"):
                    total_humedad += float(linea.split(":")[1])

                elif linea.startswith("Presión:"):
                    total_presion += float(linea.split(":")[1])

                elif linea.startswith("Viento:"):
                    viento = linea.split(":")[1].strip().split(",")
                    total_velocidad_viento += float(viento[0])

                conteo_registros += 1

                temperatura_promedio = total_temperatura / conteo_registros
                humedad_promedio = total_humedad / conteo_registros
                presion_promedio = total_presion / conteo_registros
                velocidad_viento_promedio = total_velocidad_viento / conteo_registros

                max_count = 0
                direccion_viento_prominente = ""

                for direccion, conteo in conteo_direcciones.items():
                    if conteo > max_count:
                        max_count = conteo
                        direccion_viento_prominente = direccion

                return (temperatura_promedio, humedad_promedio, presion_promedio, velocidad_viento_promedio,
                        direccion_viento_prominente)
