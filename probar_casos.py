#!/usr/bin/env python3
"""
Casos de prueba con las respuestas oficiales de la cátedra (ver CLAUDE.md).
Cualquier cambio en analizar.py tiene que seguir pasándolos.

Uso:
  python probar_casos.py
"""
import sys

import analizar as A


def funciones(oracion):
    return [(w, f) for w, f, _ in A.palabras(A.nlp(oracion))]


def funcion_de(oracion, palabra):
    for w, f in funciones(oracion):
        if w.lower() == palabra.lower():
            return f
    raise ValueError(f"'{palabra}' no está en: {oracion}")


def contar(oracion, funcion):
    return [w for w, f in funciones(oracion) if f == funcion]


def caso_cantidad(oracion, funcion, esperadas):
    obtenidas = contar(oracion, funcion)
    ok = sorted(w.lower() for w in obtenidas) == sorted(w.lower() for w in esperadas)
    return ok, f"{len(obtenidas)} ({', '.join(obtenidas)})"


def caso_funcion(oracion, palabra, esperada):
    f = funcion_de(oracion, palabra)
    return f == esperada, f


def caso_opcion(opciones, funcion_buscada, esperada):
    """Cuál de varias palabras cumple una función: cada opción se analiza en
    una oración del manual donde aparece."""
    cumplen = [w for w, oracion in opciones
               if funcion_de(oracion, w) == funcion_buscada]
    return cumplen == [esperada], ", ".join(cumplen) or "(ninguna)"


CASOS = [
    ("Cantidad de sustantivos", "3 (list, Geany's, names)",
     lambda: caso_cantidad("Print a list of Geany's internal filetype names",
                           "sustantivo", ["list", "Geany's", "names"])),
    ("¿COMMAND es sustantivo?", "Falso (función adjetiva)",
     lambda: caso_funcion("To start Geany from a command line, type the "
                          "following and press Return:", "command", "adjetivo")),
    ("Cantidad de adjetivos", "4 (initial, line, first, opened)",
     lambda: caso_cantidad("Set initial line number for the first opened file.",
                           "adjetivo", ["initial", "line", "first", "opened"])),
    ("¿Cuál es preposición? And / At / An", "At",
     lambda: caso_opcion([
         ("and", "To start Geany from a command line, type the following and press Return:"),
         ("at", "Show the status bar at the bottom of the main window."),
         ("an", "An optional sidebar that can show the following tabs:"),
     ], "preposición", "at")),
    ("Prefijo para UNDERSTAND: Mis / Dis / Un", "Mis", None),
    ("¿SOMETIMES es sustantivo?", "Falso (adverbio)",
     lambda: caso_funcion("Sometimes you might need to ask for specific help "
                          "from your distribution.", "sometimes", "adverbio")),
    ("Función de TO", "Preposición",
     lambda: caso_funcion("Additional tabs may be added to the sidebar and "
                          "message window by plugins.", "to", "preposición")),
    ("¿Cuál es artículo definido? A / The / An", "The",
     lambda: caso_opcion([
         ("a", "In a regular expression, the following characters are interpreted:"),
         ("the", "Show the status bar at the bottom of the main window."),
         ("an", "An optional sidebar that can show the following tabs:"),
     ], "artículo definido", "the")),
    ("Sufijo para USE (adjetivo positivo): Ful / Ly / Less", "Ful", None),
    ("Función de OPENED", "Adjetivo",
     lambda: caso_funcion("By default, this contains the last 10 recently "
                          "opened files.", "opened", "adjetivo")),
]


def main():
    fallas = pendientes = 0
    for pregunta, oficial, prueba in CASOS:
        if prueba is None:
            pendientes += 1
            print(f"PENDIENTE  {pregunta} -> oficial: {oficial} "
                  "(analizar.py todavía no tiene la función de afijos)")
            continue
        ok, obtenido = prueba()
        fallas += not ok
        print(f"{'OK   ' if ok else 'FALLA'}      {pregunta} -> oficial: {oficial}; "
              f"script: {obtenido}")
    total = len(CASOS) - pendientes
    print(f"\n{total - fallas}/{total} casos OK, {pendientes} pendientes")
    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    main()
