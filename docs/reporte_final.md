# Reporte de Rendimiento de Canales de Marketing Digital

**Cliente:** TiendaOnline Corp
**Periodo analizado:** Enero - Marzo 2026
**Fecha del reporte:** Agosto 2026

## Resumen ejecutivo

Analizamos 5,000 sesiones web distribuidas entre 5 canales de marketing
digital (Google Ads, Instagram, Facebook Ads, Email y Organico). El hallazgo
principal es que el canal con mayor inversion en volumen (Google Ads) no es
el mas eficiente: Email, con el menor volumen de sesiones, genera casi el
doble de tasa de conversion que cualquier otro canal.

## Hallazgos principales

### 1. Google Ads domina en volumen, pero no en eficiencia

Google Ads genero 1,760 sesiones (35% del total), la cifra mas alta de
todos los canales. Sin embargo, su tasa de conversion (2.90%) queda muy
por debajo de la de Email.

### 2. Email es el canal mas eficiente

Con solo 538 sesiones (11% del total), Email genero 31 conversiones y
$4,476 en ingresos - una tasa de conversion de 5.76%, casi el doble que
el segundo mejor canal (Google Ads, 2.90%).

### 3. La campana "carrito abandonado" es la mas rentable de todo el dataset

Dentro de Email, la campana de recuperacion de carritos abandonados
alcanzo una tasa de conversion de 6.96%, la mas alta entre todas las
campanas analizadas (con un minimo de 50 sesiones para ser considerada
estadisticamente relevante).

### 4. Desktop convierte mejor que Mobile, a pesar de menor volumen

Mobile concentra el 60% de las sesiones, pero Desktop tiene una tasa de
conversion ligeramente superior (2.93% vs 2.44%). La duracion promedio de
sesion es similar entre dispositivos.

## Recomendaciones

1. **Aumentar la inversion en Email marketing**, particularmente en
   campanas de recuperacion de carrito abandonado, dado su ROI
   comprobado frente a los demas canales.

2. **Revisar la eficiencia de la inversion en Google Ads.** Si bien
   genera el mayor volumen, su costo por conversion probablemente sea
   mas alto que el de Email - se recomienda un analisis de costo por
   canal para confirmarlo (no incluido en el alcance de este analisis).

3. **Optimizar la experiencia de compra en Mobile**, ya que concentra
   la mayoria del trafico pero convierte por debajo de Desktop -
   podria haber friccion en el proceso de pago desde dispositivos
   moviles que valga la pena investigar.

4. **Escalar la campana de carrito abandonado** a otros canales
   (por ejemplo, retargeting en Facebook Ads o Instagram), replicando
   la logica que la hizo exitosa en Email.

## Metodologia

- Datos: 5,000 sesiones web simuladas con logica de negocio realista
  (dataset de aprendizaje, no datos reales del cliente)
- Herramientas: PySpark y SQL sobre Databricks
- Periodo: Enero - Marzo 2026
- Dashboard interactivo disponible en Databricks:
  notebooks/03_dashboard_cliente
