import pandas as pd
import json
import os

def main():
    print("🚀 Iniciando script...")

    # Verificar si el archivo JSON existe
    if not os.path.exists("data.json"):
        print("❌ Error: El archivo data.json no existe en la carpeta actual.")
        return
    
    # Leer el archivo JSON
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("✅ JSON cargado correctamente:", data)

    # Si el JSON es un diccionario único, convertirlo en una lista
    if isinstance(data, dict):
        data = [data]

    # Crear DataFrame
    df = pd.DataFrame(data)

    # Verificar si el DataFrame está vacío
    if df.empty:
        print("⚠️ El DataFrame está vacío. No se generará el archivo.")
        return

    # Guardar en un archivo Excel
    ruta_salida = "output.xlsx"
    print(f"📝 Intentando guardar archivo en: {ruta_salida}")

    df.to_excel(ruta_salida, index=False, engine='openpyxl')

    # Verificar si el archivo se creó
    if os.path.exists(ruta_salida):
        print(f"✅ Archivo generado correctamente en: {ruta_salida}")
    else:
        print("❌ Error: No se generó el archivo.")

if __name__ == '__main__':
    main()
