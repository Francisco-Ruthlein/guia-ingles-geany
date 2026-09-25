# Guía de estudio de Inglés I: manual de Geany

Guía de estudio **gratuita** para preparar **Inglés I** de la carrera **Analista de Sistemas** (FCEQyN, UNaM). El material de lectura de la materia es el manual del editor [Geany](https://www.geany.org/), y todos los ejemplos de la guía salen de ese manual, con su traducción al español.

## ¿Para quién es?

Para estudiantes que preparan el examen de Inglés I. En el examen se toma una oración del manual de Geany y se hacen preguntas de opción múltiple o de verdadero/falso sobre ella:

- ¿Cuántos sustantivos o adjetivos hay en la oración?
- ¿Qué función gramatical cumple una palabra?
- ¿Cuál de estas palabras es una preposición o un artículo definido?
- ¿Qué prefijo o sufijo se le puede agregar a una palabra?

La guía sigue los criterios de la cátedra. El principal: **las palabras se clasifican por la función que cumplen en la oración, no por su categoría en el diccionario**. Por ejemplo, en *command line*, *command* funciona como **adjetivo**.

## Contenido

| Archivo | Qué es |
| --- | --- |
| [`GUIA.md`](GUIA.md) | La guía de estudio (ver las secciones abajo). |
| [`geany.md`](geany.md) | El manual completo de Geany, convertido a Markdown desde el HTML oficial. |
| [`analizar.py`](analizar.py) | Script que analiza oraciones del manual con los criterios de la cátedra, arma un quiz de práctica y resuelve preguntas de afijos. |
| [`probar_casos.py`](probar_casos.py) | Casos de prueba con respuestas oficiales de la cátedra, para verificar el script. |

### Secciones de la guía

1. [Criterios de la cátedra](GUIA.md#1-criterios-de-la-cátedra): función gramatical, frase nominal y núcleo, casos trampa.
2. [Palabras estructurales](GUIA.md#2-palabras-estructurales): modales, artículos, preposiciones, pronombres y conectores del manual.
3. [Top 40 de sustantivos, adjetivos y verbos](GUIA.md#3-top-40-de-sustantivos-adjetivos-y-verbos).
4. [Frases nominales resueltas](GUIA.md#4-frases-nominales-resueltas), con núcleo y traducción.
5. [Voz pasiva](GUIA.md#5-voz-pasiva).
6. [Afijos: prefijos y sufijos](GUIA.md#6-afijos-prefijos-y-sufijos).
7. [Preguntas de práctica](GUIA.md#7-preguntas-de-práctica): 20 preguntas con respuesta y explicación.

Las clasificaciones dudosas están marcadas con ⚠️. Son casos en los que el análisis automático puede equivocarse o en los que la gramática admite más de una lectura. Ante la duda, consultá con la cátedra.

## Instalación de `analizar.py`

Para leer la guía no hace falta instalar nada. El script es opcional y sirve para practicar con cualquier oración del manual.

Requisitos: Python 3 (el script se probó con Python 3.11).

```bash
git clone https://github.com/Francisco-Ruthlein/guia-ingles-geany
cd <carpeta-del-repositorio>

python3 -m venv venv
source venv/bin/activate          # en Windows: venv\Scripts\activate

pip install -r requirements.txt
python -m spacy download en_core_web_md
```

El script usa [spaCy](https://spacy.io/) para el análisis gramatical y [wordfreq](https://github.com/rspeer/wordfreq) para saber si una palabra existe en inglés.

## Uso

Activá el entorno virtual (`source venv/bin/activate`) antes de correr cualquier comando.

### Analizar una oración

```bash
python analizar.py "Show the status bar at the bottom of the main window."
```

Muestra la función de cada palabra según los criterios de la cátedra, si es una palabra estructural o conceptual, el conteo por categoría, las frases nominales con su núcleo y si la oración tiene voz pasiva.

### Quiz de práctica: `--quiz`

```bash
python analizar.py --quiz geany.md
```

Elige al azar una oración del manual y pregunta cuántos sustantivos, adjetivos, verbos, preposiciones o adverbios tiene. Después de responder, podés ver el análisis completo de la oración. Con `q` salís y ves el resultado.

El quiz no usa oraciones con nombres de opciones o menús del programa (*the Use escape sequences option*, *the Find dialog*), porque esos nombres funcionan en bloque y sus palabras no se cuentan por separado.

### Prefijos y sufijos: `--afijo`

```bash
python analizar.py --afijo use ful ly less
```

```console
Base: use
  ful     -> useful             (adjetivo positivo: lleno de, con (useful))
  ly      -> no existe          (adverbio: de manera... (automatically))
  less    -> useless            (adjetivo negativo: sin (useless))
```

Indica qué opciones forman una palabra real con la base y qué categoría forma cada sufijo. Sirve para las preguntas del tipo "¿qué prefijo o sufijo se le puede agregar a…?". La consigna hay que leerla igual: si pide un **adjetivo positivo**, la respuesta es *-ful*, aunque *useless* también exista.

### Otros modos

- `python analizar.py --afijos geany.md` lista las palabras del manual que **podrían** tener un prefijo o sufijo. Es una lista de candidatos para revisar a mano: muchas palabras solo lo parecen (*display* no es *dis-* + *play*).
- `python analizar.py --obsidian geany.md <carpeta>` genera notas en Markdown (por ejemplo, para Obsidian) con todas las palabras del manual agrupadas por función.

### Verificar el script

```bash
python probar_casos.py
```

Corre los casos de prueba con las respuestas oficiales de la cátedra. Si cambiás algo en `analizar.py`, estos casos tienen que seguir dando OK.

## Limitaciones

El análisis automático se equivoca a veces, sobre todo con palabras que el manual usa de forma poco habitual y con nombres técnicos. El script corrige muchos de esos errores con reglas propias, pero no todos. La guía indica los casos conocidos y marca con ⚠️ los dudosos. **Ante una diferencia entre el script y la guía, la referencia es la guía**, que fue revisada a mano.

## Correcciones y aportes

Es un proyecto abierto: si encontrás un error, una traducción que se puede mejorar o una clasificación que la cátedra corrige distinto, avisá.

- **Abrí un _issue_** con la oración, la sección de la guía y lo que habría que cambiar. Si tenés la respuesta de la cátedra, mejor todavía.
- **O mandá un _pull request_** con el cambio. Tené en cuenta:
  - Todo ejemplo nuevo tiene que salir de `geany.md` y llevar su traducción al español.
  - Las clasificaciones dudosas se marcan con ⚠️.
  - No copies preguntas del aula virtual de la cátedra: escribí preguntas propias con el mismo estilo.
  - Si modificás `analizar.py`, corré `python probar_casos.py` antes de enviar el cambio.

Los casos que siguen pendientes de confirmar con la cátedra están marcados con ⚠️ en la guía. Cualquier respuesta oficial sobre esos casos es un buen aporte.
