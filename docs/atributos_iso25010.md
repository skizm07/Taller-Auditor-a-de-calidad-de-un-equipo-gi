# Bloque 1: problemas del caso y atributos ISO/IEC 25010:2023

Modelo de calidad del producto 2023 (9 características): adecuación funcional,
eficiencia de desempeño, compatibilidad, **capacidad de interacción** (antes usabilidad),
fiabilidad, seguridad, mantenibilidad, **flexibilidad** (antes portabilidad) y
**seguridad operacional / safety** (nueva).

| Problema del caso | Atributo afectado | Subcaracterística | Métrica propuesta |
|---|---|---|---|
| Defectos que llegan a producción | Fiabilidad | Ausencia de fallos (faultlessness) | Tasa de fallo de cambios (% de despliegues que requieren corrección) |
| Pruebas solo manuales | Mantenibilidad | Capacidad de prueba (testability) | Cobertura de pruebas automatizadas (% de líneas de `src` cubiertas) |
| Despliegues los viernes sin control | Seguridad operacional (safety) | Restricción operacional (operational constraint) | N.º de despliegues fuera de la ventana permitida / total |
| Despliegue manual y lento, sin repetibilidad | Flexibilidad | Instalabilidad (installability) | Lead time de cambios (horas de commit a producción) |
| Manejo de datos clínicos sensibles del paciente | Seguridad | Confidencialidad (confidentiality) | N.º de hallazgos de seguridad abiertos (por severidad) |

## Cómo lo defendemos (razonamiento)
- **Defectos escapados** son fallos observados en producción -> **fiabilidad / ausencia de fallos**.
- **Pruebas manuales** hacen que el software sea difícil de verificar de forma repetible ->
  **mantenibilidad / capacidad de prueba**. La automatización de los Bloques 3 y 4 lo ataca directo.
- **Despliegues los viernes sin control** es una restricción operativa no gestionada ->
  **safety / restricción operacional**: el riesgo es desplegar antes del fin de semana sin
  capacidad de respuesta.
- El **despliegue manual** hace que instalar una versión nueva sea lento y no repetible ->
  **flexibilidad / instalabilidad**; se mide con el lead time de cambios.
- Una app de **citas médicas** maneja datos personales de salud -> **seguridad / confidencialidad**.
