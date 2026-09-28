# Bloque 5: métricas

## Métricas DORA (datos en `datos/despliegues.csv`, periodo de 28 días)

Cálculo sobre los 20 despliegues del archivo (4 fallidos: ids 3, 8, 13, 17).

- **Frecuencia de despliegue:** 20 despliegues / 28 días = **0,71 por día (~5 por semana)**.
- **Lead time de cambios (mediana, en horas):** **20 h** (media 24,7 h). Se calcula por fila
  como `fecha_despliegue - fecha_commit` y se toma la mediana.
- **Tasa de fallo de cambios:** 4 de 20 = **20 %**.
- **Tiempo medio de recuperación (MTTR):** promedio de `horas_recuperacion` en los fallos
  (5, 3, 2, 8) = **4,5 h**.

### Cómo se calculan (para reproducir en Google Sheets)
- Lead time por fila: `=(C2-B2)*24` (horas). Mediana: `=MEDIANA(rango)`.
- Frecuencia: `=CONTARA(A2:A21)/28`.
- Tasa de fallo: `=CONTAR.SI(D2:D21;"no")/CONTARA(D2:D21)`.
- MTTR: `=PROMEDIO.SI(D2:D21;"no";E2:E21)`.

### Lectura del resultado (para el plan de cumplimiento)
- **Velocidad buena:** despliegan seguido (~5/semana) y con lead time menor a un día.
- **Estabilidad floja:** una tasa de fallo del 20 % es alta (lo deseable suele ser <= 15 %).
  Es el problema de "defectos escapados" del caso, medido con números.
- **Recuperación aceptable:** 4,5 h de media para restablecer.
- Conclusión: el plan prioriza **bajar la tasa de fallo** (pruebas automáticas + puerta de
  calidad del CI) sin sacrificar la velocidad.

## Cuatro métricas por enfoque
| Enfoque | Métrica | Qué atributo ISO 25010 respalda |
|---|---|---|
| Scrum | Velocidad del sprint / % de compromiso cumplido | Adecuación funcional (se entrega lo comprometido) |
| Kanban | Lead time y trabajo en curso (WIP) promedio | Mantenibilidad / eficiencia del flujo |
| XP | Cobertura de pruebas (% de líneas) y n.º de pruebas | Mantenibilidad (capacidad de prueba) |
| DevOps | Tasa de fallo de cambios (DORA) | Fiabilidad (ausencia de fallos) |
