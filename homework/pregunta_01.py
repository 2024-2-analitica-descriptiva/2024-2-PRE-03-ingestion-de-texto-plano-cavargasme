"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd

def pregunta_01():
    with open('files/input/clusters_report.txt','r', encoding = 'utf-8') as file:
        lines = file.readlines()

    info = lines[4:]
    
    data = [["cluster","cantidad_de_palabras_clave","porcentaje_de_palabras_clave","principales_palabras_clave"]]
    
    listAux = []

    primera = True

    for linea in info:
        linea.strip()
        linea = linea.split()
        print(linea)
        if len(linea) > 0 and primera:
            listAux.append(int(linea[0]))
            listAux.append(int(linea[1]))
            listAux.append(float(linea[2].replace(',','.')))
            listAux.append(" ".join(linea[4:]))
            primera = False
        
        elif len(linea) > 0:
            listAux.append(" ".join(linea))
            
        else:
            primera =True
            listAux[3] = ' '.join(listAux[3:]).replace('.', '')
            data.append(listAux[:4])
            listAux = []    
    return pd.DataFrame(data[1:], columns = data[0])     