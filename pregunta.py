"""
Laboratorio 05 - Ingestión de datos textuales
-----------------------------------------------------------------------------------------

Generar dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos archivos deben tener la siguiente estructura:

phrase: Texto de la frase. hay una frase por cada archivo de texto.
sentiment: Sentimiento de la frase. Puede ser "positive", "negative" o "neutral". Este corresponde al nombre del directorio donde se encuentra ubicado el archivo.

"""

# python -m venv .venv
# .venv\Scripts\activate
# python.exe -m pip install --upgrade pip
# pip3 install pyarrow pandas

import os
import pandas as pd

def create_dataset_csv(base_path, output_filename):
    rows = []
    
    # Recorremos cada subcarpeta
    for sentiment in ['negative', 'positive', 'neutral']:
        sentiment_path = os.path.join(base_path, sentiment)
        
        # Recorremos cada archivo en la carpeta del sentimiento
        for filename in os.listdir(sentiment_path):
            file_path = os.path.join(sentiment_path, filename)
            
            # Leemos el contenido del archivo
            with open(file_path, 'r') as file:
                phrase = file.read().strip()
            
            # Añadimos la frase y el sentimiento al dataset
            rows.append({'phrase': phrase, 'sentiment': sentiment})
    
    # Convertimos la lista de tuplas a un dataframe y guardamos
    df = pd.DataFrame(rows, columns=['phrase', 'sentiment'])
    df.to_csv(output_filename, index=False)

create_dataset_csv('train', 'train_dataset.csv')
create_dataset_csv('test', 'test_dataset.csv')
