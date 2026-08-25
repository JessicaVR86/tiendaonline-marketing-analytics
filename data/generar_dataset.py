import random
from datetime import datetime
from faker import Faker
import pandas as pd

fake = Faker()
Faker.seed(42)
random.seed(42)

# --- Configuración del dataset ---
NUM_SESIONES = 5000
FECHA_INICIO = datetime(2026, 1, 1)
FECHA_FIN = datetime(2026, 3, 31)

# Cada canal tiene: peso (qué tan frecuente es) y tasa de conversión (probabilidad de compra)
CANALES = {
    "Google Ads":    {"peso": 35, "tasa_conversion": 0.03, "campanas": ["busqueda_marca", "busqueda_generica", "shopping"]},
    "Instagram":     {"peso": 25, "tasa_conversion": 0.02, "campanas": ["stories_verano", "reels_producto", "influencers"]},
    "Facebook Ads":  {"peso": 15, "tasa_conversion": 0.025,"campanas": ["retargeting", "lookalike_clientes"]},
    "Email":         {"peso": 10, "tasa_conversion": 0.08, "campanas": ["newsletter_semanal", "carrito_abandonado"]},
    "Organico":      {"peso": 15, "tasa_conversion": 0.015,"campanas": ["seo_blog", "busqueda_directa"]},
}

DISPOSITIVOS = {"Mobile": 60, "Desktop": 32, "Tablet": 8}

def elegir_ponderado(opciones_con_peso):
    """Elige una clave de un diccionario {opcion: peso} respetando las probabilidades."""
    opciones = list(opciones_con_peso.keys())
    pesos = list(opciones_con_peso.values())
    return random.choices(opciones, weights=pesos, k=1)[0]

def generar_sesion(session_id):
    canal = elegir_ponderado({c: datos["peso"] for c, datos in CANALES.items()})
    info_canal = CANALES[canal]

    campana = random.choice(info_canal["campanas"])
    dispositivo = elegir_ponderado(DISPOSITIVOS)
    fecha = fake.date_time_between(start_date=FECHA_INICIO, end_date=FECHA_FIN)

    paginas_vistas = max(1, int(random.gauss(3, 2)))
    duracion_segundos = max(5, int(random.gauss(120, 80)))

    convirtio = random.random() < info_canal["tasa_conversion"]
    valor_compra = round(random.uniform(20, 250), 2) if convirtio else 0.0

    return {
        "session_id": session_id,
        "fecha": fecha,
        "canal": canal,
        "campana": campana,
        "dispositivo": dispositivo,
        "paginas_vistas": paginas_vistas,
        "duracion_segundos": duracion_segundos,
        "conversion": convirtio,
        "valor_compra": valor_compra,
    }

if __name__ == "__main__":
    sesiones = [generar_sesion(i) for i in range(1, NUM_SESIONES + 1)]
    df = pd.DataFrame(sesiones)

    print(df.head())
    print(f"\nTotal de sesiones generadas: {len(df)}")
    print(f"Total de conversiones: {df['conversion'].sum()}")
    print(f"Tasa de conversión global: {df['conversion'].mean():.2%}")

    output_path = "data/sesiones_web.csv"
    df.to_csv(output_path, index=False)
    print(f"\nArchivo guardado en: {output_path}")