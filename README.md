# TiendaOnline Corp — Analitica de Marketing Digital

Proyecto de consultoria de datos para TiendaOnline Corp (cliente ficticio,
proyecto de aprendizaje).

## Objetivo del cliente

TiendaOnline Corp quiere entender que canales de marketing digital
(Google Ads, Instagram, Email, Organico) traen mas visitas a su sitio web,
y cuales de esos canales realmente convierten esas visitas en ventas.

## Alcance

- Analisis de sesiones web por canal y campana
- Calculo de metricas de marketing: tasa de conversion, CTR, rendimiento por canal
- Entregable final: reporte con recomendaciones

## Stack

- Databricks (PySpark + SQL) para el analisis
- Databricks Workflows para automatizar el pipeline
- Git / GitHub con flujo main - develop - feature branches

## Estructura del proyecto

tiendaonline-marketing-analytics/
  notebooks/    (notebooks de Databricks, sincronizados via Databricks Repos)
  data/         (datos de ejemplo)
  docs/         (brief del cliente, notas, reporte final)
