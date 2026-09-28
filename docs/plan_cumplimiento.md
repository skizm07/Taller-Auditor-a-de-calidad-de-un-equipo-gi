# Bloque 6: plan de cumplimiento (sustentación de 3 minutos)

Guion sugerido para exponer ante el curso. Un integrante por sección, o uno relata y
otro muestra las evidencias en pantalla.

## 0:00–0:30 — El caso y el diagnóstico
La startup entrega cada 2 semanas una app de citas médicas con **defectos escapados,
pruebas manuales y despliegues los viernes sin control**. Mapeamos esos tres problemas a
ISO/IEC 25010:2023: **fiabilidad**, **mantenibilidad** y **safety (restricción operacional)**.

## 0:30–1:15 — Qué pusimos en marcha (Scrum, Kanban, XP)
- **Definition of Done de 6 criterios**, todos verificables sí/no y ligados a un atributo.
- **Tablero Kanban** con límites WIP (3 en desarrollo, 2 en revisión) y políticas de
  entrada/salida por columna; la regla del viernes vive en el tablero.
- **XP/TDD**: escribimos las pruebas antes de la función `calcular_copago` y fijamos
  5 reglas de codificación.

## 1:15–2:00 — La puerta de calidad (DevOps)
Cada push dispara **GitHub Actions**: instala dependencias, corre `pytest` y **falla si la
cobertura baja del 80 %**. *(Mostrar la pestaña Actions en verde y el reporte de cobertura.)*
Así ningún cambio llega a producción sin pruebas que pasen.

## 2:00–2:40 — Los números (métricas DORA)
- Frecuencia: ~5 despliegues/semana. Lead time: 20 h (mediana).
- Tasa de fallo de cambios: **20 %** — es nuestro punto débil.
- MTTR: 4,5 h.
Somos rápidos pero poco estables, y eso es exactamente lo que la puerta de calidad ataca.

## 2:40–3:00 — Compromiso medible
En los próximos 3 sprints bajamos la **tasa de fallo del 20 % al 10 %** manteniendo la
frecuencia, sostenidos por la DoD, el CI y las métricas que ya dejamos montadas.

---
### Checklist de evidencias a mostrar
- [ ] Tabla problema -> atributo (`docs/atributos_iso25010.md`)
- [ ] DoD (`docs/DoD.md`) y tablero Kanban (captura/enlace)
- [ ] Pruebas y función implementada (`tests/`, `src/citas.py`)
- [ ] Workflow en verde (pestaña **Actions**)
- [ ] Hoja/tabla de métricas DORA (`docs/metricas.md`)
