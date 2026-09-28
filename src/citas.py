"""Módulo de citas médicas (código base del taller)."""

# Tarifas de copago por tipo de afiliado (fracción del valor de la consulta).
TARIFAS_COPAGO = {
    "contributivo": 0.10,  # paga el 10 %
    "subsidiado": 0.00,    # paga 0
    "particular": 1.00,    # paga el 100 %
}


def calcular_copago(valor_consulta: float, tipo_afiliado: str) -> float:
    """Calcula el copago que paga el paciente.

    Especificación:
    - "contributivo": paga el 10 % del valor de la consulta.
    - "subsidiado": paga 0.
    - "particular": paga el 100 %.
    - Si valor_consulta es negativo, lanza ValueError.
    - Si tipo_afiliado no es uno de los tres anteriores, lanza ValueError.
    - El resultado se redondea a 2 decimales.
    """
    if valor_consulta < 0:
        raise ValueError("valor_consulta no puede ser negativo")
    if tipo_afiliado not in TARIFAS_COPAGO:
        raise ValueError(f"tipo_afiliado inválido: {tipo_afiliado!r}")
    return round(valor_consulta * TARIFAS_COPAGO[tipo_afiliado], 2)
