# Cinco reglas de codificación del equipo

Reglas verificables, pensadas para mantenibilidad y para poder revisarlas en cada Pull Request.

1. **Nombres en español, descriptivos y consistentes.** Funciones y variables en `snake_case`
   (p. ej. `calcular_copago`, `tipo_afiliado`); constantes en `MAYUSCULAS`. Prohibidos los
   nombres de una letra salvo índices de bucle.
2. **Toda función pública lleva docstring** con su especificación: qué hace, parámetros,
   valor de retorno y errores que lanza (como en `calcular_copago`).
3. **Validar las entradas y fallar rápido.** Los datos inválidos lanzan `ValueError` (o la
   excepción adecuada) al inicio de la función; nunca se devuelven valores "mágicos" como -1.
4. **Nada de números ni cadenas "mágicas" repartidas por el código.** Se declaran como
   constantes con nombre (p. ej. `TARIFAS_COPAGO`) para que un cambio se haga en un solo lugar.
5. **Ninguna función supera ~20 líneas ni mezcla responsabilidades.** Si crece, se divide;
   cada función hace una sola cosa y es fácil de probar de forma aislada.

> Estas reglas se marcan como checklist en la plantilla de Pull Request y se ligan al
> criterio 4 de la Definition of Done.
