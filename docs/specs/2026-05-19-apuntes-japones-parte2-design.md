# Design: ApuntesJapones Parte 2 — N4→N3

**Date:** 2026-05-19  
**Author:** Aldo ZM  
**Scope:** Nuevo libro LaTeX de apuntes japonés nivel intermedio-avanzado N4→N3

---

## 1. Objetivo

Crear la Parte 2 de la serie ApuntesJapones cubriendo el nivel N4→N3. Mismo formato base que Parte 1 con paleta de colores diferente y 4 nuevas secciones por unidad. 35 unidades + 4 apéndices.

---

## 2. Reorganización del Repo

Mover contenido actual a `Parte1/` y crear `Parte2/`:

```
ApuntesJapones/
├── Parte1/
│   ├── Inline/
│   └── OpcionSubagent/
├── Parte2/
│   ├── unidades/        (01-35)
│   ├── apendices/       (4 apéndices)
│   ├── assets/
│   │   └── portada.tex
│   ├── preamble.tex
│   └── ApuntesJaponesPart_2.tex
├── .gitignore
└── LICENSE
```

Las carpetas sueltas `apendices/` y `unidades/` en raíz se mueven dentro de `Parte1/`.

---

## 3. Paleta de Colores

Diferente a Parte 1 (rojo/azul/oro) para distinguir visualmente las partes:

| Variable | Hex | Uso |
|---|---|---|
| `jpgreen` | `#1A5C2E` | Capítulos, headers principales |
| `jpnavy` | `#1A3A6B` | Secciones, subsecciones |
| `jpgold` | `#C8A951` | Acentos, bordes decorativos |
| `cream` | `#FAFAF0` | Fondo de cajas |

Colores para 4 nuevas cajas:

| Caja | Color marco | Hex |
|---|---|---|
| Lectura | Azul medio | `#2A4A8B` |
| Cultura | Ámbar | `#D4891A` |
| Comparación | Morado | `#6B3A7B` |
| Coloquial | Teal | `#1A7B6B` |

---

## 4. Estructura LaTeX por Unidad

Cada unidad sigue este orden (secciones heredadas de Parte 1 + 4 nuevas):

1. `\chapter{emoji kanji — Español}`
2. `\unidadheader{n}{kanji}{español}{tema comunicativo}`
3. **Vocabulario** — `vocabbox` (heredada)
4. **Frases clave** — `phrasebox` (heredada)
5. **Gramática** — `grammarbox` con `\patron` (heredada)
6. **Comparación gramatical** ← **NUEVA** — `comparacionbox`
7. **Expresiones coloquiales** ← **NUEVA** — `coloquialbox`
8. **Nota cultural** ← **NUEVA** — `culturabox`
9. **Lectura** ← **NUEVA** — `lecturabox`
10. **Ejercicios** — `ejerciciobox` (heredada)
11. **Kanjis** — `kanjibox` (heredada)

---

## 5. Nuevos Comandos LaTeX

```latex
% Comparación gramatical
\newcommand{\comparacion}[3]{%
  % #1 = patrón A, #2 = patrón B, #3 = diferencia clave
}

% Expresiones coloquiales
\newcommand{\coloquial}[3]{%
  % #1 = versión formal, #2 = versión coloquial, #3 = nota de uso
}

% Nota cultural
\newcommand{\culturabox}[2]{%
  % #1 = título, #2 = contenido
}

% Lectura con traducción
\newcommand{\lectura}[2]{%
  % #1 = texto japonés, #2 = traducción española
}
```

---

## 6. Plan de 35 Unidades

| # | Tema | Gramática clave |
|---|---|---|
| 01 | Repaso N4 express | て-form, condicionales básicos, pasado |
| 02 | てしまう / でしまう | Lamento, conclusión involuntaria |
| 03 | ておく | Preparación anticipada |
| 04 | てある | Estado resultante de acción intencional |
| 05 | ようとする / ようとしない | Intentar / negarse a hacer |
| 06 | Voz pasiva 受け身 基礎 | 〜られる grupos 1/2/3 |
| 07 | Pasiva de perjuicio | La lluvia me mojó — pasiva de afectación |
| 08 | Forma causativa 使役 | 〜させる grupos 1/2/3 |
| 09 | Causativa-pasiva 使役受け身 | 〜させられる |
| 10 | ために vs ように | Propósito: meta concreta vs estado deseado |
| 11 | ように / ような | Comparación y similitud |
| 12 | Nominalización こと vs の | Cuándo usar cada uno |
| 13 | Evidencialidad: そうだ / らしい / ようだ | Apariencia, rumor, deducción |
| 14 | はずだ / はずがない | Expectativa lógica y su negación |
| 15 | わけだ / わけがない | Conclusión lógica / imposibilidad |
| 16 | だけ vs しか vs ばかり | Límite y exclusividad |
| 17 | すぎる | Exceso en adjetivos y verbos |
| 18 | にくい / やすい | Dificultad y facilidad inherentes |
| 19 | Cambio de estado | になる / くなる / にする / くする |
| 20 | Cláusulas relativas avanzadas | Modificar sustantivos complejos |
| 21 | Condicional たら | Hipótesis, secuencia, descubrimiento |
| 22 | Condicional ば | Condición general, proverbios |
| 23 | Condicional なら | Condición basada en info del interlocutor |
| 24 | Condicional と | Resultado natural / automático |
| 25 | Expresar opinión | と思う / と考える / と感じる — matices |
| 26 | Citar y reportar | という / といわれている / とのこと |
| 27 | Conjunciones de contraste | けれども / ところが / しかし / でも |
| 28 | Conjunciones causales formales | そのため / したがって / だから / ので |
| 29 | Keigo 尊敬語 | Verbos de respeto hacia el interlocutor |
| 30 | Keigo 謙譲語 | Verbos de humildad sobre uno mismo |
| 31 | Japonés escrito vs hablado | Diferencias de registro y partículas |
| 32 | Expresiones coloquiales N3 | Lenguaje natural cotidiano real |
| 33 | Contadores avanzados | 〜本/枚/台/匹/冊/杯 y más |
| 34 | Estrategias de lectura N3 | Técnicas + texto de práctica real |
| 35 | Repaso general N4→N3 | Integración de todos los patrones |

---

## 7. Apéndices (4)

| # | Título | Contenido |
|---|---|---|
| A | Tablas de conjugación N4-N3 | Pasiva, causativa, causativa-pasiva, potencial — todos los grupos |
| B | Comparación de patrones confusos | Pares problemáticos: たら/ば/なら/と, こと/の, そうだ/らしい/ようだ, etc. |
| C | Índice de kanjis N4-N3 | Kanjis nuevos del nivel con lecturas y vocabulario de ejemplo |
| D | Referencia keigo | Tabla completa 尊敬語/謙譲語/丁寧語 con verbos comunes |

---

## 8. Portada

Misma estructura que Parte 1 con:
- Emoji: 🗾 (mapa de Japón) en lugar de 🎌
- Título: 日本語ノート 第二部
- Subtítulo: "Apuntes de Japonés - Nivel N4 → N3"
- Caja highlight: 35 Unidades, Kanjis N4-N3, Gramática Intermedia-Avanzada, Keigo
- Misma atribución: Minna no Nihongo & Marugoto

---

## 9. Compilación

Igual que Parte 1:
```bash
cd Parte2/
lualatex ApuntesJaponesPart_2.tex
lualatex ApuntesJaponesPart_2.tex  # segunda pasada para TOC
```

Requiere LuaLaTeX + MiKTeX (Windows) con fuentes Yu Gothic instaladas.

---

## 10. Fuera de Alcance

- Audio/pronunciación
- Versión digital interactiva
- Ejercicios con respuestas automáticas
- Parte 3 (N3→N2) — trabajo futuro
