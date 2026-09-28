# Tablero Kanban: políticas por columna

Enlace o captura del tablero: _(pegue aquí el enlace a Trello o GitHub Projects, o adjunte captura)_

| Columna | Límite WIP | Política de entrada | Política de salida |
|---|---|---|---|
| Por hacer | 8 | Tarjeta con descripción y criterios de aceptación claros; priorizada por el Product Owner | El equipo la toma solo si hay capacidad libre en "En desarrollo" |
| En desarrollo | 3 | Alguien la asigna a su nombre y crea una rama; hay hueco dentro del WIP | Código con pruebas escritas y commit subido a la rama |
| En revisión / pruebas | 2 | Existe un Pull Request abierto con el CI ejecutándose | CI en verde (pruebas + cobertura >= 80 %) y PR aprobado por otra persona |
| Listo para desplegar | 3 | Cumple los 6 criterios de la Definition of Done | Desplegado en la ventana permitida (no viernes salvo aprobación) |
| Hecho | - | Cambio en producción y verificado | (columna final) |

## Justificación de los límites WIP
- **WIP total bajo** para forzar terminar antes de empezar y reducir defectos escapados.
- El cuello de botella típico es **revisión/pruebas**: se limita a 2 para que las revisiones
  no se acumulen y el lead time se mantenga corto.
- La columna **Listo para desplegar** incluye la política del viernes (Bloque 1: safety),
  de modo que el tablero mismo hace cumplir la restricción operacional.
- Las políticas de entrada/salida son **explícitas**, que es justo lo que Kanban exige
  para que el flujo sea auditable.
