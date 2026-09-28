# Taller: Auditoría de calidad de un equipo ágil — RESUELTO

Curso: Estándares y Métricas de Calidad de Software · Tema: cumplimiento de estándares en Scrum, Kanban, XP y DevOps.

---

## Cómo ejecutar y verificar este proyecto
El proyecto es una app en Python con pruebas automáticas. Hay tres formas de comprobarlo;
la **Opción A** es la más rápida y no requiere instalar nada.

### Opción A · Ver la evidencia automática en GitHub (30 segundos, recomendado)
Cada vez que se sube un cambio, GitHub ejecuta las pruebas solo.
1. Abrir el repositorio en GitHub.
2. Entrar a la pestaña **Actions** (arriba, junto a *Code*, *Issues*, *Pull requests*).
3. Abrir la ejecución más reciente llamada **"CI de calidad"**.
4. Debe aparecer con un **check verde ✓**. Al abrir el paso
   *"Ejecutar pruebas con cobertura"* se ve `6 passed` y `Total coverage: 100%`.

> El check verde es la prueba de que las pruebas pasan **y** de que la cobertura es ≥ 80 %.
> Si estuviera en rojo, el cambio no cumpliría la puerta de calidad.

### Opción B · Ejecutarlo en el navegador con Codespaces (sin instalar nada)
1. En el repositorio, botón verde **Code → Codespaces → Create codespace on main**.
   Se abre un editor VS Code en el navegador.
2. En la terminal (abajo), instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar las pruebas con la misma puerta de calidad que usa el CI:
   ```bash
   pytest --cov=src --cov-report=term-missing --cov-fail-under=80
   ```
4. Resultado esperado: **`6 passed`** y **`Required test coverage of 80% reached. Total coverage: 100.00%`**.


### Dónde está cada entregable
| Bloque | Entregable | Ubicación |
|---|---|---|
| 1. Diagnóstico | Tabla problema → atributo ISO/IEC 25010 | `docs/atributos_iso25010.md` |
| 2. Scrum y Kanban | Definition of Done + políticas del tablero + captura | `docs/DoD.md`, `docs/politicas_kanban.md` |
| 3. XP | Pruebas (TDD), función y reglas de codificación | `tests/test_citas.py`, `src/citas.py`, `docs/reglas_codificacion.md` |
| 4. DevOps | Workflow de CI (puerta de calidad 80 %) | `.github/workflows/ci.yml` + pestaña **Actions** |
| 5. Métricas | Métricas DORA y métricas por enfoque | `docs/metricas.md` |
| 6. Socialización | Guion del plan de cumplimiento (3 min) | `docs/plan_cumplimiento.md` |

---

## Caso
Una startup desarrolla una app de citas médicas. Entrega cada 2 semanas, tiene defectos que llegan a producción, pruebas manuales y despliega los viernes. Su equipo debe demostrar calidad con evidencia verificable.

## Requisitos (todo en línea, sin instalar nada)
- Cuenta gratuita de GitHub (y Trello o GitHub Projects para el tablero).
- Este repositorio: use **Use this template** o **Fork** y abra **Codespaces** (o edite en el navegador con la tecla `.`).

## Bloques
| Bloque | Min | Qué hacer | Archivo / entregable |
|---|---|---|---|
| 1. Diagnóstico | 15 | Asociar problemas del caso con atributos de ISO/IEC 25010:2023 | `docs/atributos_iso25010.md` |
| 2. Scrum y Kanban | 15 | Redactar la Definition of Done (6 criterios) y montar un tablero con límites WIP y políticas por columna | `docs/DoD.md`, `docs/politicas_kanban.md`, captura del tablero |
| 3. XP | 15 | Escribir 3 pruebas unitarias antes de implementar (TDD) y proponer 5 reglas de codificación | `tests/test_citas.py`, `src/citas.py`, `docs/reglas_codificacion.md` |
| 4. DevOps | 20 | Completar el workflow para que ejecute pruebas y falle si la cobertura es menor al 80 % | `.github/workflows/ci.yml` |
| 5. Métricas | 10 | Calcular las 4 métricas DORA con los datos simulados y elegir 4 métricas por enfoque | `docs/metricas.md` |
| 6. Socialización | 15 | Sustentación de 3 minutos del plan de cumplimiento | Exposición (`docs/plan_cumplimiento.md`) |

## Entrega
Un enlace al repositorio con el último commit y la ejecución del workflow en verde (pestaña **Actions**).

## Pistas para el bloque 3 (TDD)
1. Lea la especificación en `src/citas.py`.
2. Escriba primero las pruebas (deben fallar).
3. Implemente hasta que pasen.
4. Ejecute en la terminal de Codespaces: `pip install -r requirements.txt && pytest --cov=src`.
