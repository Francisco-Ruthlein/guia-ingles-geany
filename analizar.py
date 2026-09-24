#!/usr/bin/env python3
"""
Análisis gramatical de oraciones del manual de Geany
según el criterio de la cátedra de Inglés I (función gramatical).

Uso:
  python analizar.py "Print a list of Geany's internal filetype names"
  python analizar.py --quiz geany.md
  python analizar.py --obsidian geany.md vault_ingles
  python analizar.py --afijo understand mis dis un
  python analizar.py --afijos geany.md
"""
import re
import sys
import random
from collections import defaultdict, Counter
from pathlib import Path

import spacy
from wordfreq import zipf_frequency

nlp = spacy.load("en_core_web_md")

ESTRUCTURALES = {"artículo definido", "artículo indefinido", "preposición",
                 "conjunción", "pronombre", "auxiliar", "modal",
                 "demostrativo", "determinante", "to + infinitivo",
                 "posesivo"}
CONCEPTUALES = {"sustantivo", "verbo", "adjetivo", "adverbio"}

DEMOSTRATIVOS = {"this", "that", "these", "those"}
POSESIVOS = {"my", "your", "his", "her", "its", "our", "their"}

_cache_verbo = {}


def puede_ser_verbo(palabra):
    """True si la palabra funciona como verbo en 'to <palabra>'."""
    w = palabra.lower()
    if w not in _cache_verbo:
        _cache_verbo[w] = nlp(f"to {w}")[1].tag_ == "VB"
    return _cache_verbo[w]


def imperativo_mal_etiquetado(tok):
    """Corrige imperativos que el modelo confunde con sustantivo/adjetivo:
    'Set initial line...' al inicio, o 'type X and press Y'."""
    if tok.pos_ == "PROPN" or not tok.has_vector:
        return False
    sin_sujeto = not any(t.dep_ in ("nsubj", "nsubjpass", "csubj")
                         for t in tok.sent)
    al_inicio = tok.i == tok.sent.start and sin_sujeto
    if al_inicio:
        # 'Line number margin...', 'Amount of space', 'Middle-click', 'Note:'
        # son títulos o etiquetas nominales, no imperativos
        nxt = tok.nbor(1) if tok.i + 1 < tok.sent.end else None
        if (tok.dep_ == "compound"
                or (nxt is not None and nxt.text in ("-", ":"))
                or any(c.dep_ == "prep" and c.lower_ == "of"
                       for c in tok.children)):
            al_inicio = False
    prev = tok.nbor(-1) if tok.i > tok.sent.start else None
    # 'type X and press Y': la conjunción debe coordinar con un imperativo;
    # si no, 'small and fast IDE' o 'bold and italic' pasan a verbo
    tras_conj = (prev is not None and prev.pos_ == "CCONJ"
                 and prev.head.pos_ == "VERB"
                 and any(t.tag_ == "VB" for t in tok.sent if t.i < tok.i))
    return (al_inicio or tras_conj) and puede_ser_verbo(tok.text)


_cache_participio = {}
# participios que el modelo etiqueta como adjetivo en cualquier contexto
# ('overridden') o que no terminan en -ed/-en ('quit')
PARTICIPIOS_IRREGULARES = {"overridden", "quit"}


def es_participio(palabra):
    """True si la palabra es un participio pasado ('disabled', 'closed') y no
    un adjetivo ('open', 'useful', 'unaffected', 'interested')."""
    w = palabra.lower()
    if w not in _cache_participio:
        t = nlp(f"It was {w} by the user.")[2]
        _cache_participio[w] = (w in PARTICIPIOS_IRREGULARES
                                or (w.endswith(("ed", "en")) and t.tag_ == "VBN"
                                    and t.dep_ != "acomp"))
    return _cache_participio[w]


def participio_tras_be(tok):
    """Pasiva que el modelo no detecta: 'can be overridden', 'is closed'."""
    return (tok.pos_ == "ADJ" and tok.dep_ == "acomp"
            and tok.head.lemma_ == "be" and es_participio(tok.text))


TECNICO = re.compile(r"[/\\~#=()\[\]{}<>]|^[-+.]|-$|\w\.\w|\w-\d|\d[a-z]|[a-z]\d",
                     re.I)
ABREVIATURAS = {"e.g.", "i.e.", "etc.", "vs.", "esp."}


def es_tecnico(tok):
    """Nombres de archivo, opciones, rutas: 'snippets.conf', '-o', '~/.config'."""
    return tok.lower_ not in ABREVIATURAS and bool(TECNICO.search(tok.text))


def modifica_sustantivo(tok):
    return (tok.dep_ in ("compound", "amod", "nummod")
            and tok.i < tok.head.i and tok.head.pos_ in ("NOUN", "PROPN"))


def nominalizado(tok):
    """Adjetivo o numeral que funciona como núcleo de la frase:
    'only the first will load', 'does the same', 'most of the templates'."""
    nxt = tok.nbor(1) if tok.i + 1 < len(tok.doc) else None
    if (tok.lower_ == "following" and tok.i > 0
            and tok.nbor(-1).lower_ == "the"
            and (nxt is None or nxt.pos_ not in ("NOUN", "PROPN", "ADJ"))):
        return True                       # 'type the following and press'
    if tok.dep_ not in ("nsubj", "nsubjpass", "dobj", "pobj"):
        return False
    if nxt is not None and (nxt.pos_ in ("NOUN", "PROPN", "ADJ")
                            or nxt.text == ","):
        return False
    return any(c.dep_ == "det" or (c.dep_ == "prep" and c.lower_ == "of")
               for c in tok.children)


def funcion(tok):
    """Devuelve la función gramatical de un token según la cátedra."""
    t, pos, dep, tag = tok.lower_, tok.pos_, tok.dep_, tok.tag_

    if pos in ("PUNCT", "SPACE", "SYM", "X") or tok.is_punct:
        return None
    if tag == "POS":                      # la 's de Geany's
        return None

    # el modelo etiqueta mal los nombres técnicos (NUM, ADJ, INTJ, VERB...):
    # se clasifican sólo por su función
    if es_tecnico(tok) and pos not in ("CCONJ", "SCONJ"):
        return "adjetivo" if modifica_sustantivo(tok) else "sustantivo"

    if (pos in ("ADJ", "NUM") or tag == "VBG") and nominalizado(tok):
        return "pronombre" if t == "one" else "sustantivo"
    # 'one' sin sustantivo después reemplaza a uno: 'select one of these
    # items', 'the current one'. Delante de sustantivo es numeral (adjetivo).
    if t == "one" and not modifica_sustantivo(tok):
        return "pronombre"

    # errores de etiquetado: 'A' (PRON) en 'Documents - A document list',
    # 'hex'/'meta' (PRON) delante de sustantivo, 'Go to symbol definition'
    if pos == "PRON" and t in ("a", "an", "the"):
        return "artículo definido" if t == "the" else "artículo indefinido"
    if (pos == "PRON" or tag in ("VB", "VBP")) and dep == "compound" \
            and modifica_sustantivo(tok) and not imperativo_mal_etiquetado(tok):
        return "adjetivo"
    if tag in ("VB", "VBP") and dep in ("pobj", "nsubj"):
        return "sustantivo"

    # decisiones de la cátedra sobre palabras que el modelo etiqueta mal
    if t == "than":                       # 'more than one': conj. comparativa
        return "conjunción"
    if pos == "SCONJ" and dep == "prep":  # 'upon opening', 'except for',
        return "preposición"              # 'since Geany 0.13'
    if pos == "ADP" and t.endswith("est"):
        return "adjetivo"                 # 'the word nearest the cursor'
    if pos == "ADP" and (
            (dep == "compound" and modifica_sustantivo(tok))    # 'home directory'
            or (dep == "conj" and modifica_sustantivo(tok.head))):  # 'up and down arrows'
        return "adjetivo"
    nxt = tok.nbor(1) if tok.i + 1 < len(tok.doc) else None
    prev = tok.nbor(-1) if tok.i > 0 else None
    if (t == "drop" and nxt is not None and nxt.lower_ == "down") or \
            (t == "down" and prev is not None and prev.lower_ == "drop"
             and nxt is not None and nxt.pos_ in ("NOUN", "PROPN")):
        return "adjetivo"                 # 'drop down box'
    if participio_tras_be(tok):
        return "verbo"                    # pasiva: 'can be overridden'

    # gerundio (-ing) como sujeto o después de preposición -> sustantivo:
    # 'Setting it to 0 will...', 'after selecting', 'during typing'
    if tag == "VBG" and dep in ("csubj", "csubjpass", "pcomp", "pobj"):
        return "sustantivo"
    # 'Editing system files is...': el modelo lo toma como modificador de
    # 'files', pero el verbo en singular muestra que el sujeto es 'Editing'
    if (tag == "VBG" and tok.i == tok.sent.start and dep in ("amod", "compound")
            and tok.head.tag_ == "NNS" and tok.head.dep_ in ("nsubj", "nsubjpass")
            and tok.head.head.tag_ == "VBZ"):
        return "sustantivo"

    # verbo base entre dos sustantivos sin sujeto propio al lado:
    # 'the popup menu click position' -> premodificador del núcleo
    if (tag in ("VB", "VBP") and prev is not None and nxt is not None
            and prev.pos_ == "NOUN" and prev.head != tok
            and nxt.pos_ == "NOUN" and nxt.head == tok and nxt.dep_ == "dobj"
            and not any(c.dep_ == "det" for c in nxt.children)):
        return "adjetivo"

    if pos in ("NOUN", "ADJ") or (tag in ("VBN", "VBD") and dep == "amod"):
        if imperativo_mal_etiquetado(tok):
            return "verbo"

    # Regla clave: sustantivo que modifica a otro sustantivo -> adjetivo
    if pos in ("NOUN", "PROPN"):
        if dep == "compound" and tok.head.pos_ in ("NOUN", "PROPN"):
            return "adjetivo"
        # el modelo corta la frase: 'the users home directory' -> 'users'
        # queda como núcleo, pero está delante de otro modificador de 'directory'
        # (no se aplica a la primera palabra, que puede ser un verbo mal
        # etiquetado, ni delante de nombres técnicos o propios: 'the option
        # Directory levels', 'A shorthand S-E')
        if (pos == "NOUN" and nxt is not None and nxt.dep_ in ("compound", "amod")
                and nxt.head.i > nxt.i and nxt.head.pos_ == "NOUN"
                and tok.head != nxt.head and tok.i != tok.sent.start
                and nxt.is_alpha
                and not (nxt.text[:1].isupper() and tok.text[:1].islower())
                # 'project related', 'syntax highlighted' sí; '0 disables
                # automatic updates' no (ahí 'disables' es el verbo)
                and (nxt.dep_ == "compound" or nxt.tag_ in ("VBN", "VBG"))):
            return "adjetivo"
        return "sustantivo"

    # Participios (-ed) y formas -ing que modifican a un sustantivo -> adjetivo
    if tag in ("VBN", "VBG") and dep in ("amod", "compound"):
        return "adjetivo"

    if tag == "MD":
        return "modal"
    if pos == "AUX":
        return "auxiliar"
    if pos == "VERB":
        return "verbo"
    if pos == "ADJ":
        return "adjetivo"
    if pos == "ADV":
        return "adverbio"
    if pos == "NUM":                      # 'two files' vs. 'set it to 0'
        return "adjetivo" if dep == "nummod" else "sustantivo"
    if t in POSESIVOS:
        return "posesivo"
    if pos == "PRON":
        if tag in ("WDT", "WP"):          # relativo: 'the theme that is set'
            return "pronombre"
        return "demostrativo" if t in DEMOSTRATIVOS else "pronombre"
    if tag == "RP":                       # partícula: 'hold down', 'look up'
        return "adverbio"
    if pos == "DET":
        if t == "the":
            return "artículo definido"
        if t in ("a", "an"):
            return "artículo indefinido"
        if t in DEMOSTRATIVOS:
            return "demostrativo"
        return "determinante"
    if pos == "ADP":
        return "preposición"
    if pos == "PART" and t == "to":
        return "to + infinitivo"
    if pos in ("CCONJ", "SCONJ"):
        return "conjunción"
    if pos == "PART":
        return "adverbio"                 # not, n't
    if pos == "INTJ":
        return {"please": "adverbio", "like": "preposición",
                "ok": "sustantivo"}.get(t, "interjección")
    return pos.lower()


def tipo_palabra(f):
    if f in ESTRUCTURALES:
        return "estructural"
    if f in CONCEPTUALES:
        return "conceptual"
    return "-"


def palabras(sent):
    """Lista de (palabra, función) de una oración, fusionando Geany + 's."""
    res = []
    for tok in sent:
        f = funcion(tok)
        if f:
            texto = tok.text
            nxt = tok.nbor(1) if tok.i + 1 < len(tok.doc) else None
            if nxt is not None and nxt.tag_ == "POS":
                texto += nxt.text
            res.append((texto, f, tok))
    return res


def frases_nominales(sent):
    salida = []
    for chunk in sent.noun_chunks:
        mods = [t.text for t in chunk if t.i < chunk.root.i
                and funcion(t) == "adjetivo"]
        if mods:
            salida.append((chunk.text, chunk.root.text, mods))
    return salida


def es_pasiva(sent):
    return any(t.dep_ in ("auxpass", "nsubjpass") or participio_tras_be(t)
               for t in sent)


def analizar_oracion(texto):
    doc = nlp(texto)
    for sent in doc.sents:
        items = palabras(sent)
        print(f"\nOración: {sent.text.strip()}\n")
        print(f"{'Palabra':<18}{'Función':<22}Tipo")
        print("-" * 52)
        for w, f, _ in items:
            print(f"{w:<18}{f:<22}{tipo_palabra(f)}")

        conteo = Counter(f for _, f, _ in items)
        print("\nConteo:")
        for f, n in conteo.most_common():
            print(f"  {f}: {n}")

        modales = [w for w, f, _ in items if f == "modal"]
        if modales:
            print(f"\nModal: {', '.join(modales)}")
        if es_pasiva(sent):
            print("Voz pasiva: sí")
        for texto_fn, nucleo, mods in frases_nominales(sent):
            print(f"Frase nominal: '{texto_fn}' -> núcleo: {nucleo}; "
                  f"modificadores: {', '.join(mods)}")


# ---------- Afijos ----------

# frecuencia Zipf (wordfreq): 0 = no aparece en inglés; 'useful' = 4.7.
# Por debajo del umbral la palabra se considera inexistente ('usely' = 0).
UMBRAL_ZIPF = 1.0

PREFIJOS = {
    "un": "no, lo contrario (unable, undo)",
    "dis": "no, lo opuesto (disable, disagree)",
    "mis": "mal, de forma incorrecta (misunderstand, misuse)",
    "re": "de nuevo (reload, redo)",
    "pre": "antes (preview, pre-defined)",
    "non": "no (non-option, nonexistent)",
    "in": "no (incompatible, invisible)",
    "im": "no, ante b/m/p (impossible)",
    "il": "no, ante l (illegal)",
    "ir": "no, ante r (irregular)",
    "multi": "muchos (multi-line)",
    "auto": "automático, por sí mismo (auto-indentation)",
    "sub": "debajo, parte de (subdirectory)",
    "over": "por encima, reemplazar (override, overwrite)",
    "under": "por debajo (underline)",
    "de": "quitar, revertir (deselect)",
    "inter": "entre (interactive)",
}

# sufijo -> (categoría que forma, significado)
SUFIJOS = {
    "ful": ("adjetivo positivo", "lleno de, con (useful)"),
    "less": ("adjetivo negativo", "sin (useless)"),
    "ly": ("adverbio", "de manera... (automatically)"),
    "able": ("adjetivo", "que se puede (configurable)"),
    "ible": ("adjetivo", "que se puede (visible)"),
    "ness": ("sustantivo", "cualidad (darkness)"),
    "ment": ("sustantivo", "acción o resultado (replacement)"),
    "ation": ("sustantivo", "acción o resultado (configuration)"),
    "ion": ("sustantivo", "acción o resultado (selection)"),
    "er": ("sustantivo", "quien hace algo / herramienta (editor, parser)"),
    "or": ("sustantivo", "quien hace algo / herramienta (editor)"),
    "ity": ("sustantivo", "cualidad (functionality)"),
    "al": ("adjetivo", "relativo a (optional)"),
    "ive": ("adjetivo", "que tiene la cualidad de (interactive)"),
    "ous": ("adjetivo", "que tiene (various)"),
    "ize": ("verbo", "convertir en (customize)"),
    "ise": ("verbo", "convertir en (customise)"),
}


def existe(palabra):
    """True si la palabra se usa en inglés (según su frecuencia en wordfreq)."""
    return zipf_frequency(palabra.lower(), "en") >= UMBRAL_ZIPF


def formas_con_sufijo(base, sufijo):
    """Variantes ortográficas de base + sufijo: use+able -> usable,
    easy+ly -> easily, use+ful -> useful."""
    b = base.lower()
    formas = [b + sufijo]
    if b.endswith("e") and sufijo[0] in "aeiou":
        formas.append(b[:-1] + sufijo)                 # use -> usable
    if b.endswith("y") and len(b) > 2 and b[-2] not in "aeiou":
        formas.append(b[:-1] + "i" + sufijo)           # easy -> easily
    if b.endswith("le") and sufijo == "ly":
        formas.append(b[:-1] + "y")                    # possible -> possibly
    return formas


def agregar_afijo(base, afijo):
    """Palabra existente que resulta de agregar el afijo (prefijo o sufijo)
    a la base, o None. 'understand' + 'mis' -> 'misunderstand'."""
    a = afijo.lower().strip("-")
    if a in SUFIJOS:
        candidatas = formas_con_sufijo(base, a)
    else:
        candidatas = [a + base.lower()]
    return next((c for c in candidatas if existe(c)), None)


def afijos_posibles(base, opciones, categoria=None):
    """Cuáles de las opciones (prefijos o sufijos) forman una palabra real
    con la base. Con 'categoria' se filtran los sufijos por lo que forman:
    afijos_posibles('use', ['ful', 'ly', 'less'], 'adjetivo positivo')."""
    res = []
    for op in opciones:
        a = op.lower().strip("-")
        if categoria and SUFIJOS.get(a, ("",))[0] != categoria:
            continue
        if agregar_afijo(base, a):
            res.append(op)
    return res


def descomponer(palabra):
    """Prefijos y sufijos reconocibles de una palabra, si la base existe
    por sí sola: 'unaffected' -> [('un', 'affected')].
    Es heurístico: los resultados se revisan a mano."""
    w = palabra.lower().replace("-", "")
    res = []
    for p in sorted(PREFIJOS, key=len, reverse=True):
        base = w[len(p):]
        if w.startswith(p) and len(base) >= 3 and existe(base) \
                and zipf_frequency(base, "en") >= 3:
            res.append(("prefijo", p, base))
            break
    for s in sorted(SUFIJOS, key=len, reverse=True):
        if not w.endswith(s) or len(w) - len(s) < 3:
            continue
        raiz = w[:-len(s)]
        for base in (raiz, raiz + "e", raiz[:-1] + "y" if raiz.endswith("i") else None):
            if base and existe(base) and zipf_frequency(base, "en") >= 3 \
                    and w in formas_con_sufijo(base, s):
                res.append(("sufijo", s, base))
                break
        else:
            continue
        break
    return res


def afijos_del_manual(ruta):
    """Palabras del manual con prefijo o sufijo, con una oración de ejemplo."""
    vistas = {}
    for s in oraciones_del_manual(ruta, 4, 25):
        o = " ".join(s.text.split())
        for tok in s:
            w = tok.lower_
            if not re.fullmatch(r"[a-z]+(-[a-z]+)?", w) or w in vistas:
                continue
            partes = descomponer(w)
            if partes:
                vistas[w] = (partes, funcion(tok), o)
    return vistas


def mostrar_afijo(base, opciones):
    print(f"\nBase: {base}")
    for op in opciones:
        a = op.lower().strip("-")
        palabra = agregar_afijo(base, a)
        tipo = SUFIJOS[a][0] if a in SUFIJOS else "prefijo"
        significado = SUFIJOS[a][1] if a in SUFIJOS else PREFIJOS.get(a, "?")
        estado = f"-> {palabra}" if palabra else "-> no existe"
        print(f"  {op:8}{estado:22}({tipo}: {significado})")


# ---------- Limpieza del Markdown ----------

def limpiar_markdown(md):
    md = re.sub(r"```.*?```", " ", md, flags=re.S)       # bloques de código
    md = re.sub(r"<[^>]+>", " ", md)                     # HTML
    lineas = []
    for l in md.splitlines():
        s = l.strip()
        # el código viene en bloques ```; las líneas con sangría son
        # párrafos dentro de viñetas y se conservan
        if not s or s.startswith("|"):
            continue
        if s.startswith("$") or s.startswith("%"):
            continue                                     # prompts de shell
        s = re.sub(r"\\([\\`*_{}\[\]()#+\-.!>|=])", r"\1", s)  # escapes .md
        s = re.sub(r"\s*-+>\s*", " > ", s)               # Tools->Color Chooser
        s = re.sub(r"^>\s*", "", s)                      # citas
        s = re.sub(r"^#+\s*", "", s)                     # títulos
        s = re.sub(r"^[-*+]\s+", "", s)                  # viñetas
        s = re.sub(r"^\d+\.\s+", "", s)
        s = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", s)      # imágenes
        s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)   # links
        s = re.sub(r"https?://\S+", " ", s)
        s = re.sub(r"[`*_]", "", s)
        lineas.append(s)
    return "\n".join(lineas)


def oraciones_del_manual(ruta, min_palabras=6, max_palabras=25):
    texto = limpiar_markdown(Path(ruta).read_text(encoding="utf-8"))
    # cada línea del .md es un párrafo: se procesan por separado para que
    # títulos y viñetas no se peguen a la oración siguiente
    parrafos = [l for l in texto.splitlines() if len(l.split()) >= 3]
    res = []
    for doc in nlp.pipe(parrafos, batch_size=64):
        for s in doc.sents:
            t = " ".join(s.text.split())
            n = len([x for x in s if not x.is_punct])
            if (min_palabras <= n <= max_palabras and t[-1:] in ".:"
                    and t[0].isupper()):
                res.append(s)
    return res


# ---------- Modo quiz ----------

NUCLEOS_DE_OPCION = {"option", "options", "preference", "preferences",
                     "setting", "settings", "checkbox", "box", "button",
                     "field", "item", "dialog", "command", "keybinding",
                     "expander", "tab", "menu", "bar", "entry"}


def tiene_nombre_de_opcion(sent):
    """True si la oración nombra una opción del programa que empieza con un
    verbo: 'the Use escape sequences option', 'the Enable plugin support
    general preference'. Ese nombre funciona en bloque como adjetivo, y sus
    palabras no se cuentan por separado: el quiz descarta estas oraciones."""
    toks = list(sent)
    for i, t in enumerate(toks[1:-1], 1):
        if not (t.text[:1].isupper() and toks[i - 1].lower_ == "the"
                and puede_ser_verbo(t.text)):
            continue
        for u in toks[i + 1:i + 8]:
            if u.lower_ in NUCLEOS_DE_OPCION:
                return True
            if u.is_punct or u.pos_ in ("AUX", "ADP", "SCONJ", "CCONJ"):
                break
    return False


def quiz(ruta):
    sents = [s for s in oraciones_del_manual(ruta)
             if not tiene_nombre_de_opcion(s)]
    print(f"{len(sents)} oraciones cargadas. Enter para seguir, 'q' para salir.")
    plural = {"sustantivo": "sustantivos", "adjetivo": "adjetivos",
              "verbo": "verbos", "preposición": "preposiciones",
              "adverbio": "adverbios"}
    preguntas = list(plural)
    aciertos = total = 0
    while True:
        sent = random.choice(sents)
        items = palabras(sent)
        cat = random.choice(preguntas)
        correcta = sum(1 for _, f, _ in items if f == cat)
        print(f"\n{' '.join(sent.text.split())}")
        try:
            r = input(f"¿Cuántos {plural[cat]} hay? ").strip()
        except EOFError:
            break
        if r.lower() == "q":
            break
        total += 1
        if r == str(correcta):
            aciertos += 1
            print("Correcto.")
        else:
            print(f"Incorrecto. Son {correcta}.")
        detalle = [w for w, f, _ in items if f == cat]
        print(f"  {plural[cat]}: {', '.join(detalle) or '(ninguno)'}")
        if input("¿Ver análisis completo? (s/Enter) ").lower() == "s":
            analizar_oracion(sent.text)
    print(f"\nResultado: {aciertos}/{total}")


# ---------- Modo Obsidian ----------

def obsidian(ruta, carpeta):
    out = Path(carpeta)
    out.mkdir(parents=True, exist_ok=True)
    sents = oraciones_del_manual(ruta, min_palabras=3, max_palabras=60)

    por_funcion = defaultdict(Counter)
    ejemplos = {}
    modales, pasivas, frases = [], [], []

    for s in sents:
        oracion = " ".join(s.text.split())
        for w, f, tok in palabras(s):
            # los participios adjetivos se listan tal cual ('opened', no
            # 'open'); los modales por lema ('won't' -> 'will', no 'wo')
            if f == "modal" or (f in CONCEPTUALES and not (
                    f == "adjetivo" and tok.tag_ in ("VBN", "VBG", "VBD"))):
                clave = tok.lemma_.lower()
            else:
                clave = w.lower()
            por_funcion[f][clave] += 1
            ejemplos.setdefault((f, clave), oracion)
            if f == "modal":
                modales.append((w, oracion))
        if es_pasiva(s):
            pasivas.append(oracion)
        for texto, nucleo, mods in frases_nominales(s):
            if len(mods) >= 2:
                frases.append((texto, nucleo, mods))

    for f, cont in por_funcion.items():
        nombre = f.replace(" ", "-").replace("+", "mas")
        lineas = [f"# {f.capitalize()}", "",
                  f"Tipo: palabra {tipo_palabra(f)}", "",
                  "| Palabra | Veces | Ejemplo del manual |",
                  "|---|---|---|"]
        for w, n in cont.most_common():
            ej = ejemplos[(f, w)].replace("|", "\\|")
            lineas.append(f"| {w} | {n} | {ej} |")
        (out / f"{nombre}.md").write_text("\n".join(lineas), encoding="utf-8")

    def escribir(nombre, titulo, filas):
        (out / nombre).write_text("\n".join([f"# {titulo}", ""] + filas),
                                  encoding="utf-8")

    escribir("Modales.md", "Modales",
             ["| Modal | Oración |", "|---|---|"] +
             [f"| {w} | {o.replace('|', chr(92) + '|')} |" for w, o in modales])
    escribir("Voz-pasiva.md", "Voz pasiva", [f"- {o}" for o in pasivas])
    vistas = set()
    filas = ["| Frase nominal | Núcleo | Modificadores (función adjetiva) |",
             "|---|---|---|"]
    for t, n, m in frases:
        if t.lower() not in vistas:
            vistas.add(t.lower())
            filas.append(f"| {t} | {n} | {', '.join(m)} |")
    escribir("Frases-nominales.md", "Frases nominales", filas)

    print(f"Notas generadas en {out.resolve()}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
    elif args[0] == "--quiz" and len(args) == 2:
        quiz(args[1])
    elif args[0] == "--obsidian" and len(args) == 3:
        obsidian(args[1], args[2])
    elif args[0] == "--afijo" and len(args) >= 3:
        mostrar_afijo(args[1], args[2:])
    elif args[0] == "--afijos" and len(args) == 2:
        print("⚠️ Candidatos automáticos: revisar a mano. Muchas palabras solo "
              "parecen tener afijo ('display' no es dis + play).\n")
        for w, (partes, f, o) in sorted(afijos_del_manual(args[1]).items()):
            desc = ", ".join(f"{t} {a} + {b}" for t, a, b in partes)
            print(f"{w:20}{f:14}{desc:32}| {o}")
    else:
        analizar_oracion(" ".join(args))
