import pandas as pd
import json
import os

def main():
    try:
        print("Iniciando script...")

        # Verificar si el archivo JSON existe
        if not os.path.exists("data.json"):
            print("Error: El archivo data.json no existe en la carpeta actual.")
            return
        
        # Leer JSON
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        print("✅ JSON cargado correctamente:", data)

        # Convertir a lista si es diccionario
        if isinstance(data, dict):
            data = [data]

        # Crear DataFrame
        df = pd.DataFrame(data)

        # Verificar si hay datos
        if df.empty:
            print("El DataFrame está vacío. No se generará el archivo.")
            return
        
        # Guardar Excel
        ruta_salida = os.path.join(os.getcwd(), "output.xlsx")
        print("Intentando guardar archivo en: {ruta_salida}")

        df.to_excel(ruta_salida, index=False, engine='openpyxl')

        # Verificar si el archivo se creó
        if os.path.exists(ruta_salida):
            print("Archivo generado correctamente en: {ruta_salida}")
        else:
            print("Error: No se generó el archivo.")

    except Exception as e:
        print("Error inesperado: {e}")

if __name__ == '__main__':
    main()
