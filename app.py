from typing import Dict, Any

class Analizador_de_eventos:
    def __init__(self, nombre_archivo:str):
        self.nombre_archivo=nombre_archivo

    def procesar_eventos(self) -> Dict[str, Any]:
        eventos_totales=0
        eventos_por_tipo={}
        eventos_por_servidor={}

        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                if linea.startswith("tipo de evento"):
                    tipo_evento=linea.split(":")[1].strip()
                    eventos_por_tipo[tipo_evento]=eventos_por_tipo.get(tipo_evento,0)+1
                elif linea.startswith("servidor:"):
                    nombre_servidor=linea.split(":")[1].strip()
                    eventos_por_servidor[nombre_servidor]=eventos_por_servidor.get(nombre_servidor,0)+1
                

                eventos_totales+=1
        estadisticas={
            "numero total de eventos registrados": eventos_totales,
            "numero de eventos por tipo": eventos_por_tipo,
            "numero de eventos por servidor": eventos_por_servidor
        }
        

        return estadisticas