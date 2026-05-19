# Design: Apuntes de Japonés N5→N4

**Date:** 2026-05-18  
**Author:** Aldo (AldoZM)  
**Repo:** https://github.com/AldoZM/ApuntesJapones  
**Location:** `D:\Codigo Abierto\ApuntesJapones`

---

## Objetivo

Apuntes de japonés básico-intermedio (N5→N4) en LaTeX/PDF para repasar vocabulario, kanjis y patrones de comunicación. Uso personal. Con emojis para inmersión. Sin sección de hiragana/katakana (ya se conocen).

---

## Fuentes de contenido

- **Minna no Nihongo** — estructura gramatical progresiva, vocabulario base
- **Marugoto** — frases naturales, contextos comunicativos reales, cultura

---

## Decisiones de diseño

| Decisión | Elección |
|---|---|
| Idioma de explicaciones | Español |
| Representación japonesa | Kanji + furigana, sin romaji |
| Estructura de archivos | Multi-archivo con `\input` (opción B) |
| Compilador | LuaLaTeX |
| Alcance | 30 unidades, N5→N4 |
| Organización | Híbrido temático-gramatical |

---

## Estructura de archivos

```
ApuntesJapones/
├── main.tex
├── preamble.tex
├── unidades/
│   ├── 01-presentaciones.tex
│   ├── 02-numeros-tiempo.tex
│   ├── 03-kosoado.tex
│   ├── 04-lugares-direcciones.tex
│   ├── 05-rutina-diaria.tex
│   ├── 06-gustos-preferencias.tex
│   ├── 07-comida-restaurante.tex
│   ├── 08-compras.tex
│   ├── 09-adjetivos.tex
│   ├── 10-familia.tex
│   ├── 11-pasado.tex
│   ├── 12-clima-estaciones.tex
│   ├── 13-te-form-1.tex
│   ├── 14-te-form-2.tex
│   ├── 15-te-iru.tex
│   ├── 16-experiencias.tex
│   ├── 17-planes-citas.tex
│   ├── 18-comparaciones.tex
│   ├── 19-transporte.tex
│   ├── 20-cuerpo-salud.tex
│   ├── 21-forma-potencial.tex
│   ├── 22-deseos.tex
│   ├── 23-dar-recibir.tex
│   ├── 24-forma-casual.tex
│   ├── 25-opinar-citar.tex
│   ├── 26-condicional-1.tex
│   ├── 27-condicional-2.tex
│   ├── 28-voz-pasiva.tex
│   ├── 29-keigo-intro.tex
│   └── 30-repaso-general.tex
├── apendices/
│   ├── mapa-particulas.tex
│   ├── tablas-conjugacion.tex
│   └── indice-kanjis.tex
└── assets/
    ├── portada.tex
    └── img/
```

---

## Paquetes LaTeX

| Paquete | Propósito |
|---|---|
| `luatexja` | Soporte nativo japonés en LuaLaTeX |
| `luatexja-ruby` | Furigana encima de kanji |
| `luatexja-fontspec` | Fuente Noto Sans JP |
| `xcolor` | Colores por sección |
| `tcolorbox` | Cajas estilizadas (vocab, gramática, frases) |
| `emoji` | Emojis en el PDF |
| `hyperref` | Índice clicable, links internos |
| `booktabs` | Tablas limpias |
| `geometry` | Márgenes del documento |
| `titlesec` | Estilo de títulos de unidad |

---

## Estructura interna de cada unidad

```
🎌 UNIDAD XX — Título
Tema comunicativo

📌 VOCABULARIO NUEVO
  Tabla: kanji【furigana】— español — categoría

🗣️ FRASES CLAVE
  Diálogos cortos del contexto real (estilo Marugoto)

⚙️ GRAMÁTICA
  Patrón + explicación en español
  + ejemplos kanji+furigana
  + diagrama ASCII si aplica
  + imagen si aplica

🖼️ REFERENCIA VISUAL (si aplica)
  Imagen o diagrama

📝 EJERCICIOS RÁPIDOS
  3-5 ejercicios: fill-in, traducción, construcción de frases

🀄 KANJIS DE LA UNIDAD
  Tabla: Kanji | Lectura on/kun | Significado | Vocab de ejemplo
```

---

## Apéndices

| Apéndice | Contenido |
|---|---|
| 🗺️ Mapa de partículas | は vs が vs を vs に vs で vs へ — usos y diferencias |
| 🔢 Tablas de conjugación | Verbos grupo 1/2/3 en todos los tiempos cubiertos |
| 📇 Índice de kanjis | Todos los kanjis vistos, número de unidad donde aparece |

---

## Las 30 unidades

| # | Archivo | Tema | Gramática clave |
|---|---|---|---|
| 01 | 01-presentaciones | 自己紹介 — Presentarse | です/ですか、〜は〜です |
| 02 | 02-numeros-tiempo | 数字と時間 — Números y tiempo | 〜時、〜分、〜円 |
| 03 | 03-kosoado | これ・それ・あれ — Señalar cosas | こそあど、〜の |
| 04 | 04-lugares-direcciones | 場所と道案内 — Lugares y direcciones | に/で/へ、あります/います |
| 05 | 05-rutina-diaria | 毎日の生活 — Rutina diaria | 動詞ます形、時間の表現 |
| 06 | 06-gustos-preferencias | 好き・嫌い — Gustos | 〜が好き/嫌い |
| 07 | 07-comida-restaurante | 食べ物と注文 — Comida | 〜をください、〜はありますか |
| 08 | 08-compras | 買い物 — De compras | 〜はいくらですか、助数詞 |
| 09 | 09-adjetivos | 形容詞 — Describir | い形容詞、な形容詞 |
| 10 | 10-familia | 家族 — La familia | 内/外の呼び方 |
| 11 | 11-pasado | 過去形 — Pasado | ました/ませんでした |
| 12 | 12-clima-estaciones | 天気と季節 — Clima | 〜でしょう、〜ですね |
| 13 | 13-te-form-1 | て形① — Secuencia | 動詞て形、〜てから |
| 14 | 14-te-form-2 | て形② — Favores | 〜てください、〜てもいいですか |
| 15 | 15-te-iru | 〜ている — Progreso/estado | 〜ています |
| 16 | 16-experiencias | 経験と回数 — Experiencias | 〜たことがある、〜回 |
| 17 | 17-planes-citas | 計画と予定 — Planes | 〜つもり、〜予定 |
| 18 | 18-comparaciones | 比較 — Comparaciones | 〜より、〜の方が、一番 |
| 19 | 19-transporte | 移動と交通 — Transporte | 〜で行く、〜に乗る |
| 20 | 20-cuerpo-salud | 体と健康 — Salud | 〜が痛い、〜てはいけない |
| 21 | 21-forma-potencial | 可能形 — Poder | 動詞可能形、〜ができる |
| 22 | 22-deseos | 欲しい・たい — Deseos | 〜たい、〜がほしい |
| 23 | 23-dar-recibir | 授受表現 — Dar/recibir | あげる/もらう/くれる |
| 24 | 24-forma-casual | 普通形 — Casual | 動詞/形容詞普通形 |
| 25 | 25-opinar-citar | 〜と思う・〜と言う — Opinar | 〜と思います、〜と言っていました |
| 26 | 26-condicional-1 | 条件① — と/ば | 〜と、〜ば |
| 27 | 27-condicional-2 | 条件② — たら/なら | 〜たら、〜なら |
| 28 | 28-voz-pasiva | 受身形 — Pasiva | 動詞受身形 |
| 29 | 29-keigo-intro | 敬語入門 — Formal básico | 〜ていただく、お〜になる |
| 30 | 30-repaso-general | 総復習 — Repaso N5→N4 | Todos los patrones vistos |
