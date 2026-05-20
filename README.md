# ApuntesJapones

Apuntes de japonés en LaTeX. Compilado con LuaLaTeX.

## Parte 1 — N5→N4 (103 páginas)

Cubre gramática básica N5→N4: partículas, conjugaciones, て-form, たい・ながら・たり,
formas de cortesía, ている・てある, y más.

**PDF:** `Parte1/ApuntesJaponeses.pdf`

## Parte 2 — N4→N3 (157 páginas)

35 unidades + 4 apéndices cubriendo gramática N4→N3:

| Unidades | Tema |
|----------|------|
| 01–05 | Repaso N4 / て-form avanzado (てしまう, ておく, てある, ようとする) |
| 06–09 | Voz pasiva y causativa |
| 10–15 | Propósito, nominalización, evidencialidad (はずだ, わけだ) |
| 16–20 | Límites, exceso, cambio de estado, cláusulas relativas |
| 21–24 | Los 4 condicionales: たら, ば, なら, と |
| 25–30 | Opinión, citar/reportar, conjunciones, keigo (尊敬語・謙譲語) |
| 31–35 | Registro escrito/hablado, coloquial, contadores, lectura N3, repaso |

**Apéndices:** Tablas de conjugación · Patrones confusos · Índice de kanjis · Referencia keigo

**PDF:** `Parte2/ApuntesJaponesPart_2.pdf`

## Compilar

```bash
cd Parte2
lualatex ApuntesJaponesPart_2.tex
lualatex ApuntesJaponesPart_2.tex  # segunda pasada para TOC
```

Requiere MiKTeX o TeX Live con `luatexja`, `haranoaji-fonts`, `tcolorbox`, `emoji`.
