# Definition of Done (6 criterios)

Cada criterio debe ser verificable (sí/no) y estar ligado a un atributo de calidad.

| # | Criterio | Atributo ISO 25010 | Evidencia |
|---|---|---|---|
| 1 | Toda función nueva o modificada tiene pruebas unitarias automatizadas | Mantenibilidad (capacidad de prueba) | Archivos en `tests/`; pruebas visibles en el commit |
| 2 | La cobertura de pruebas sobre `src` es >= 80 % | Mantenibilidad (capacidad de prueba) | Reporte de cobertura en la ejecución del workflow |
| 3 | El workflow de CI (Actions) está en verde en la rama principal | Fiabilidad (ausencia de fallos) | Pestaña **Actions** con la ejecución exitosa |
| 4 | El código respeta las 5 reglas de codificación del equipo | Mantenibilidad (modificabilidad) | Revisión en el Pull Request (checklist marcada) |
| 5 | Todo cambio se integró por Pull Request revisado por otra persona | Seguridad (integridad) + Mantenibilidad | PR con al menos una aprobación antes del merge |
| 6 | No hay despliegues los viernes salvo aprobación explícita registrada | Seguridad operacional (restricción operacional) | Registro de despliegue con fecha y, si aplica, la aprobación |

## Notas de sustentación
- Los 6 criterios son **binarios**: se pueden responder sí/no sin interpretación.
- Cada criterio ataca un problema del Bloque 1: automatización de pruebas (1, 2),
  defectos escapados (3), mantenibilidad del código (4, 5) y despliegues del viernes (6).
