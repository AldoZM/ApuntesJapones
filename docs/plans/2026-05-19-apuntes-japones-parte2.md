# ApuntesJapones Parte 2 — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a 35-unit N4→N3 Japanese notes LaTeX book (Parte 2) with green/navy palette and 4 new section types per unit, organized under `Parte2/` in the same repo.

**Architecture:** Mirror Parte 1 structure (ltjsbook + LuaLaTeX + custom tcolorbox commands). New preamble with jpgreen/jpnavy/jpgold palette. 4 new tcolorbox styles: comparacionbox, coloquialbox, culturabox, lecturabox. Repo reorganized: existing `Inline/` and `OpcionSubagent/` move into `Parte1/`.

**Tech Stack:** LuaLaTeX, ltjsbook, luatexja, luatexja-ruby, tcolorbox, HaranoAji fonts

---

## Task 1: Reorganize repo — move existing content to Parte1/

**Files:**
- Move: `Inline/` → `Parte1/Inline/`
- Move: `OpcionSubagent/` → `Parte1/OpcionSubagent/`
- Move (if exists): root `apendices/` → `Parte1/apendices/`
- Move (if exists): root `unidades/` → `Parte1/unidades/`
- Move (if exists): root `preamble.tex` → `Parte1/preamble.tex`

- [ ] **Step 1: Create Parte1/ and move folders**

```powershell
cd "D:\Codigo Abierto\ApuntesJapones"
New-Item -ItemType Directory -Force Parte1
git mv Inline Parte1/Inline
git mv OpcionSubagent Parte1/OpcionSubagent
if (Test-Path apendices) { git mv apendices Parte1/apendices }
if (Test-Path unidades)  { git mv unidades  Parte1/unidades  }
if (Test-Path preamble.tex) { git mv preamble.tex Parte1/preamble.tex }
```

- [ ] **Step 2: Verify**

```powershell
ls Parte1
```
Expected: `Inline`, `OpcionSubagent` (plus optionally `apendices`, `unidades`, `preamble.tex`)

- [ ] **Step 3: Commit**

```powershell
git commit -m "chore: reorganize repo — move Parte1 content into Parte1/ folder"
git push origin main
```

---

## Task 2: Create Parte2/ scaffold

**Files:**
- Create dirs: `Parte2/unidades/`, `Parte2/apendices/`, `Parte2/assets/`
- Create: `Parte2/ApuntesJaponesPart_2.tex`

- [ ] **Step 1: Create directories**

```powershell
New-Item -ItemType Directory -Force "D:\Codigo Abierto\ApuntesJapones\Parte2\unidades"
New-Item -ItemType Directory -Force "D:\Codigo Abierto\ApuntesJapones\Parte2\apendices"
New-Item -ItemType Directory -Force "D:\Codigo Abierto\ApuntesJapones\Parte2\assets"
```

- [ ] **Step 2: Create Parte2/ApuntesJaponesPart_2.tex**

```latex
\documentclass[12pt, a4paper, openany]{ltjsbook}
\input{preamble}
\begin{document}
\input{assets/portada}
\frontmatter
\tableofcontents
\clearpage
\mainmatter
\input{unidades/01-repaso-n4}
\input{unidades/02-teshimau}
\input{unidades/03-teoku}
\input{unidades/04-tearu}
\input{unidades/05-youto-suru}
\input{unidades/06-pasiva-basica}
\input{unidades/07-pasiva-perjuicio}
\input{unidades/08-causativa}
\input{unidades/09-causativa-pasiva}
\input{unidades/10-tame-ni-you-ni}
\input{unidades/11-you-ni-you-na}
\input{unidades/12-koto-no}
\input{unidades/13-evidencialidad}
\input{unidades/14-hazuda}
\input{unidades/15-wakeda}
\input{unidades/16-dake-shika-bakari}
\input{unidades/17-sugiru}
\input{unidades/18-nikui-yasui}
\input{unidades/19-cambio-estado}
\input{unidades/20-clausulas-relativas}
\input{unidades/21-condicional-tara}
\input{unidades/22-condicional-ba}
\input{unidades/23-condicional-nara}
\input{unidades/24-condicional-to}
\input{unidades/25-expresar-opinion}
\input{unidades/26-citar-reportar}
\input{unidades/27-conjunciones-contraste}
\input{unidades/28-conjunciones-causales}
\input{unidades/29-keigo-sonkeigo}
\input{unidades/30-keigo-kenjogo}
\input{unidades/31-escrito-vs-hablado}
\input{unidades/32-expresiones-coloquiales}
\input{unidades/33-contadores-avanzados}
\input{unidades/34-lectura-n3}
\input{unidades/35-repaso-general}
\backmatter
\appendix
\input{apendices/conjugacion-n4-n3}
\input{apendices/patrones-confusos}
\input{apendices/indice-kanjis-n4-n3}
\input{apendices/referencia-keigo}
\end{document}
```

- [ ] **Step 3: Commit**

```powershell
git add Parte2/
git commit -m "chore: scaffold Parte2/ directory and main file"
```

---

## Task 3: Create Parte2/preamble.tex

**Files:**
- Create: `Parte2/preamble.tex`

- [ ] **Step 1: Create the file**

Create `D:\Codigo Abierto\ApuntesJapones\Parte2\preamble.tex`:

```latex
\usepackage{luatexja}
\usepackage{luatexja-ruby}
\usepackage{luatexja-fontspec}
\setmainjfont{HaranoAjiMincho-Regular}[BoldFont=HaranoAjiMincho-Bold]
\setsansjfont{HaranoAjiGothic-Regular}
\usepackage{emoji}
\usepackage{xcolor}

% --- Palette Parte 2 ---
\definecolor{jpgreen}{HTML}{1A5C2E}
\definecolor{jpnavy}{HTML}{1A3A6B}
\definecolor{jpgold}{HTML}{C8A951}
\definecolor{cream}{HTML}{FAFAF0}
\definecolor{lightgray}{HTML}{F7F7F7}
\definecolor{darkgray}{HTML}{555555}
\definecolor{softgreen}{HTML}{D4EDDA}
% New box colors
\definecolor{readblue}{HTML}{2A4A8B}
\definecolor{cultureamber}{HTML}{D4891A}
\definecolor{comppurple}{HTML}{6B3A7B}
\definecolor{coloquialteal}{HTML}{1A7B6B}

\usepackage[a4paper, margin=2.5cm]{geometry}
\usepackage{booktabs, tabularx, longtable}
\usepackage[most]{tcolorbox}
\tcbuselibrary{skins, breakable}
\tcbset{
  vocabbox/.style={enhanced, breakable, colback=lightgray, colframe=jpnavy,
    coltitle=white, fonttitle=\bfseries\large,
    attach boxed title to top left={yshift=-2mm, xshift=5mm},
    boxed title style={colback=jpnavy, rounded corners}, rounded corners},
  grammarbox/.style={enhanced, breakable, colback=white, colframe=jpgreen,
    coltitle=white, fonttitle=\bfseries\large,
    attach boxed title to top left={yshift=-2mm, xshift=5mm},
    boxed title style={colback=jpgreen, rounded corners}, rounded corners},
  phrasebox/.style={enhanced, colback=cream, colframe=jpgold!80!black,
    rounded corners, fonttitle=\bfseries},
  kanjibox/.style={enhanced, breakable, colback=jpgold!8, colframe=jpgold!70!black,
    coltitle=white, fonttitle=\bfseries\large,
    attach boxed title to top left={yshift=-2mm, xshift=5mm},
    boxed title style={colback=jpgold!70!black, rounded corners}, rounded corners},
  ejerciciobox/.style={enhanced, colback=softgreen!50, colframe=softgreen!80!black,
    rounded corners, fonttitle=\bfseries, coltitle=darkgray},
  % --- NEW Parte 2 styles ---
  comparacionbox/.style={enhanced, breakable, colback=cream, colframe=comppurple,
    coltitle=white, fonttitle=\bfseries\large,
    attach boxed title to top left={yshift=-2mm, xshift=5mm},
    boxed title style={colback=comppurple, rounded corners}, rounded corners},
  coloquialbox/.style={enhanced, colback=cream, colframe=coloquialteal,
    coltitle=white, fonttitle=\bfseries,
    attach boxed title to top left={yshift=-2mm, xshift=5mm},
    boxed title style={colback=coloquialteal, rounded corners}, rounded corners},
  culturaboxstyle/.style={enhanced, colback=cream, colframe=cultureamber,
    coltitle=white, fonttitle=\bfseries,
    attach boxed title to top left={yshift=-2mm, xshift=5mm},
    boxed title style={colback=cultureamber, rounded corners}, rounded corners},
  lecturabox/.style={enhanced, breakable, bicolor, colback=cream,
    colbacklower=lightgray, colframe=readblue,
    coltitle=white, fonttitle=\bfseries\large,
    attach boxed title to top left={yshift=-2mm, xshift=5mm},
    boxed title style={colback=readblue, rounded corners}, rounded corners}
}

\usepackage{hyperref}
\hypersetup{colorlinks=true, linkcolor=jpnavy, urlcolor=jpgreen}
\usepackage{titlesec}
\titleformat{\chapter}[display]{\normalfont\huge\bfseries\color{jpgreen}}
  {}{0pt}{\huge}[\vspace{0.3em}\color{jpgreen}\hrule height 1.5pt\vspace{0.3em}]
\titleformat{\section}{\large\bfseries\color{jpnavy}}
  {}{0em}{}[\vspace{0.1em}\color{jpnavy!40}\hrule height 0.4pt]

% --- Inherited commands (same as Parte 1) ---
\newcommand{\ue}[1]{{\emoji{#1}}}
\newcommand{\unidadheader}[4]{%
  \begin{tcolorbox}[enhanced, colback=jpgreen!5, colframe=jpgreen,
    coltitle=white, fonttitle=\bfseries\Large,
    title={\emoji{seedling} Unidad #1 \enspace \ruby{#2}{} \enspace #3},
    attach boxed title to top center={yshift=-3mm},
    boxed title style={colback=jpgreen, rounded corners}]
  \textit{\textcolor{jpnavy}{\emoji{speaking-head} Tema: #4}}
  \end{tcolorbox}\vspace{0.5em}}
\newcommand{\vocabitem}[4]{\ruby{#1}{#2} & #3 & \textcolor{darkgray}{\small\textit{#4}} \\[4pt]}
\newcommand{\patron}[3]{%
  \begin{tcolorbox}[grammarbox, title={\emoji{gear} #1}]
  \begin{center}{\Large\textbf{#2}}\end{center}\vspace{0.3em}#3
  \end{tcolorbox}}
\newcommand{\ej}[2]{\par\vspace{0.2em}\hspace{1em}▶ \textbf{#1} \hfill {\small\textit{#2}}\vspace{0.1em}}
\newcommand{\frase}[2]{%
  \begin{tcolorbox}[phrasebox]\textbf{#1}\\[2pt]{\small\textit{#2}}\end{tcolorbox}\vspace{0.2em}}
\newcommand{\kanjirow}[5]{{\LARGE #1} & #2 & #3 & #4 & #5 \\[4pt]}

% --- New commands Parte 2 ---
% \comparacion{titulo}{patronA}{patronB}{diferencia}
\newcommand{\comparacion}[4]{%
  \begin{tcolorbox}[comparacionbox, title={\emoji{scales} #1}]
  \begin{tabularx}{\linewidth}{XX}
    \textcolor{jpnavy}{\textbf{#2}} & \textcolor{jpgreen}{\textbf{#3}} \\[4pt]
  \end{tabularx}
  \vspace{0.2em}\small #4
  \end{tcolorbox}\vspace{0.2em}}

% \coloquial{formal}{coloquial}{nota}
\newcommand{\coloquial}[3]{%
  \begin{tcolorbox}[coloquialbox, title={\emoji{speech-balloon} Forma Coloquial}]
  \begin{tabularx}{\linewidth}{lX}
    \textbf{Formal:}    & #1 \\[3pt]
    \textbf{Coloquial:} & \textbf{#2} \\[3pt]
    \textbf{Nota:}      & \small\textit{#3} \\
  \end{tabularx}
  \end{tcolorbox}\vspace{0.2em}}

% \culturabox{titulo}{contenido}
\newcommand{\culturabox}[2]{%
  \begin{tcolorbox}[culturaboxstyle, title={\emoji{torii-gate} #1}]
  #2
  \end{tcolorbox}\vspace{0.2em}}

% \lectura{texto japones}{traduccion}
\newcommand{\lectura}[2]{%
  \begin{tcolorbox}[lecturabox, title={\emoji{open-book} 文章 — Lectura}]
  #1
  \tcblower
  \textit{#2}
  \end{tcolorbox}\vspace{0.2em}}
```

- [ ] **Step 2: Commit**

```powershell
git add Parte2/preamble.tex
git commit -m "feat: add Parte2 preamble — green/navy palette, 4 new tcolorbox styles"
```

---

## Task 4: Create Parte2/assets/portada.tex

**Files:**
- Create: `Parte2/assets/portada.tex`

- [ ] **Step 1: Create file**

```latex
\begin{titlepage}
\centering
\vspace*{2cm}

{\Huge \emoji{map-of-japan}}\\[1em]

{\huge\bfseries\color{jpgreen} 日本語ノート}\\[0.3em]
{\Large\color{jpnavy} \ruby{第二部}{だいにぶ} — Parte 2}\\[0.5em]
{\large\color{darkgray} Apuntes de Japonés}\\[0.2em]
{\normalsize\color{darkgray} Nivel N4 → N3}\\[2em]

\begin{tcolorbox}[enhanced, colback=jpgold!15, colframe=jpgold,
  width=0.72\textwidth, arc=6pt, boxrule=1.5pt]
\centering
\begin{tabular}{cc}
  \textbf{\emoji{seedling} 35 Unidades} & \textbf{\emoji{books} Kanjis N4-N3} \\[0.6em]
  \textbf{\emoji{gear} Gramática Intermedia} & \textbf{\emoji{bowing-man} Keigo}\\
\end{tabular}
\end{tcolorbox}

\vfill

{\large\textbf{Aldo ZM}}\\[0.3em]
{\small\textcolor{jpnavy}{\url{https://github.com/AldoZM/ApuntesJapones}}}\\[0.5em]
{\small\textit{Basado en Minna no Nihongo \& Marugoto}}

\end{titlepage}
```

- [ ] **Step 2: Commit**

```powershell
git add Parte2/assets/portada.tex
git commit -m "feat: add Parte2 portada with green palette"
```

---

## Task 5: Compile smoke test (empty body)

- [ ] **Step 1: Create minimal stub units so it compiles**

Create `Parte2/unidades/01-repaso-n4.tex` with just `% stub` and repeat for all 35 units + 4 appendices (empty files). Then compile:

```powershell
cd "D:\Codigo Abierto\ApuntesJapones\Parte2"
# Create stub files
1..35 | ForEach-Object {
  $names = @('01-repaso-n4','02-teshimau','03-teoku','04-tearu','05-youto-suru',
    '06-pasiva-basica','07-pasiva-perjuicio','08-causativa','09-causativa-pasiva',
    '10-tame-ni-you-ni','11-you-ni-you-na','12-koto-no','13-evidencialidad',
    '14-hazuda','15-wakeda','16-dake-shika-bakari','17-sugiru','18-nikui-yasui',
    '19-cambio-estado','20-clausulas-relativas','21-condicional-tara',
    '22-condicional-ba','23-condicional-nara','24-condicional-to',
    '25-expresar-opinion','26-citar-reportar','27-conjunciones-contraste',
    '28-conjunciones-causales','29-keigo-sonkeigo','30-keigo-kenjogo',
    '31-escrito-vs-hablado','32-expresiones-coloquiales','33-contadores-avanzados',
    '34-lectura-n3','35-repaso-general')
  Set-Content "unidades/$($names[$_-1]).tex" "% stub $_"
}
Set-Content "apendices/conjugacion-n4-n3.tex" "% stub"
Set-Content "apendices/patrones-confusos.tex" "% stub"
Set-Content "apendices/indice-kanjis-n4-n3.tex" "% stub"
Set-Content "apendices/referencia-keigo.tex" "% stub"
lualatex ApuntesJaponesPart_2.tex
```

Expected: compiles to PDF with TOC and portada. Fix any errors before proceeding.

- [ ] **Step 2: Commit stubs**

```powershell
git add Parte2/
git commit -m "chore: add stub unit and appendix files for compile verification"
```

---

## Task 6: Unit 01 — Repaso N4 express (reference implementation)

**File:** `Parte2/unidades/01-repaso-n4.tex`

This is the reference unit. All subsequent units follow this exact structure.

- [ ] **Step 1: Write the file**

```latex
% unidades/01-repaso-n4.tex
\chapter{\emoji{seedling} \ruby{復習}{ふくしゅう} — Repaso N4}
\unidadheader{01}{復習}{Repaso N4}{Consolidar las bases antes del nivel intermedio}

\begin{tcolorbox}[vocabbox, title={\emoji{pushpin} Vocabulario Clave}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{復習する}{ふくしゅうする}{repasar / revisar}{v. suru}
\vocabitem{確認する}{かくにんする}{confirmar / verificar}{v. suru}
\vocabitem{練習する}{れんしゅうする}{practicar}{v. suru}
\vocabitem{間違える}{まちがえる}{equivocarse}{v. G2}
\vocabitem{覚える}{おぼえる}{memorizar}{v. G2}
\vocabitem{忘れる}{わすれる}{olvidar}{v. G2}
\vocabitem{理解する}{りかいする}{comprender}{v. suru}
\vocabitem{上達する}{じょうたつする}{mejorar (habilidad)}{v. suru}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{\emoji{speech-balloon} Frases Clave}

\frase{もう一度言ってください。}{Por favor dígalo otra vez.}
\frase{\ruby{間違}{まちが}えてもいいです。}{Está bien equivocarse.}
\frase{〜たことがあります。}{He hecho ~. (experiencia pasada)}
\frase{〜なければなりません。}{Tengo que hacer ~. (obligación)}
\frase{〜ようにしています。}{Intento / procuro hacer ~. (hábito intentado)}

\subsection*{\emoji{gear} Gramática — Repaso Rápido N4}

\patron{Estado continuo vs acción en progreso}
  {\ruby{動詞}{どうし}て\ruby{形}{けい} + いる}
  {\ej{\ruby{彼}{かれ}は\ruby{日本語}{にほんご}を\ruby{勉強}{べんきょう}している。}{Él está estudiando japonés. (en progreso)}
   \ej{\ruby{窓}{まど}が\ruby{開}{あ}いている。}{La ventana está abierta. (estado resultante)}}

\patron{Experiencia pasada}
  {〜た + ことがある}
  {\ej{すしを\ruby{食}{た}べたことがあります。}{He comido sushi alguna vez.}
   \ej{\ruby{富士山}{ふじさん}に\ruby{登}{のぼ}ったことがありません。}{Nunca he subido al Monte Fuji.}}

\patron{Obligación}
  {〜なければなりません / 〜なくてはいけません}
  {\ej{\ruby{毎日}{まいにち}\ruby{練習}{れんしゅう}しなければなりません。}{Tengo que practicar todos los días.}
   \ej{\ruby{薬}{くすり}を\ruby{飲}{の}まなくてはいけません。}{Tengo que tomar la medicina.}}

\comparacion{〜ている: dos usos}
  {acción en progreso\\\small\ruby{今}{いま}\ruby{食}{た}べている。\\\textit{Estoy comiendo ahora.}}
  {estado resultante\\\small\ruby{結婚}{けっこん}している。\\\textit{Está casado/a.}}
  {El contexto y tipo de verbo determinan el significado. Verbos de acción → progreso. Verbos de cambio de estado → estado resultante.}

\coloquial{〜なければなりません}{〜なきゃ / 〜なくちゃ}
  {Contracción muy común en habla informal. 行かなければなりません → 行かなきゃ。}

\culturabox{N4から先の日本語}{
  Al pasar del N5-N4 al N3, el japonés empieza a sentirse más \textit{natural}. Los patrones se vuelven más complejos, pero también más expresivos. La clave es leer y escuchar japonés real: noticias de NHK Easy, mangas, dramas. \ruby{継続}{けいぞく}は\ruby{力}{ちから}なり — La constancia es poder.
}

\lectura{\ruby{先生}{せんせい}からのメッセージ\\[0.4em]
  N4まで\ruby{勉強}{べんきょう}したみなさん、\ruby{本当}{ほんとう}によく\ruby{頑張}{がんば}りました。ここからはN3です。\ruby{文法}{ぶんぽう}がもっと\ruby{複雑}{ふくざつ}になりますが、\ruby{表現}{ひょうげん}も\ruby{豊}{ゆた}かになります。\ruby{毎日}{まいにち}少しずつ\ruby{練習}{れんしゅう}すれば、きっと\ruby{上達}{じょうたつ}できます。}
{Mensaje de la profesora\\[0.4em]
  A todos los que han estudiado hasta N4: realmente lo han hecho muy bien. A partir de aquí es N3. La gramática se vuelve más compleja, pero las expresiones también se enriquecen. Si practican un poco cada día, seguramente mejorarán.}

\begin{tcolorbox}[ejerciciobox, title={\emoji{pencil} Ejercicios de Repaso}]
\begin{enumerate}
  \item Conjuga en て-form: \ruby{書}{か}く、\ruby{食}{た}べる、する、くる
  \item Transforma: \ruby{毎日}{まいにち}\ruby{運動}{うんどう}する (→ obligación formal)
  \item ¿Cuál es la diferencia? \ruby{ドアが開いている}{ドアがあいている} vs \ruby{ドアを開けている}{ドアをあけている}
  \item Crea una oración con たことがある sobre una experiencia real tuya.
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) \ruby{書}{か}いて・\ruby{食}{た}べて・して・きて \quad
2) \ruby{毎日}{まいにち}\ruby{運動}{うんどう}しなければなりません \quad
3) 開いている = la puerta está abierta (estado); 開けている = está abriendo la puerta (acción) \quad
4) (respuesta libre)
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={\emoji{mahjong} Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{復}{ふく}{—}{\ruby{repetir}{}/recuperar}{\ruby{復習}{ふくしゅう} / \ruby{復活}{ふっかつ}}
\kanjirow{習}{しゅう}{\ruby{なら}{う}}{\ruby{aprender}{}/practicar}{\ruby{復習}{ふくしゅう} / \ruby{習慣}{しゅうかん}}
\kanjirow{練}{れん}{\ruby{ね}{る}}{\ruby{entrenar}{}/refinar}{\ruby{練習}{れんしゅう} / \ruby{熟練}{じゅくれん}}
\kanjirow{確}{かく}{\ruby{たし}{か}}{\ruby{seguro}{}/confirmar}{\ruby{確認}{かくにん} / \ruby{確実}{かくじつ}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Compile and verify**

```powershell
cd "D:\Codigo Abierto\ApuntesJapones\Parte2"
lualatex ApuntesJaponesPart_2.tex
```

Expected: compiles without errors. Unit 01 appears in PDF with all sections.

- [ ] **Step 3: Commit**

```powershell
git add Parte2/unidades/01-repaso-n4.tex
git commit -m "feat(u01): Repaso N4 — reference unit implementation"
```

---

## Task 7: Units 02–05 (て-form advanced)

Each file follows the exact same structure as Unit 01. Write each file, then compile and commit as a batch.

### Unit 02 — `Parte2/unidades/02-teshimau.tex`

```latex
\chapter{\emoji{dizzy} \ruby{てしまう}{} — Completar con lamento}
\unidadheader{02}{完了}{てしまう / でしまう}{Expresar acciones completadas o lamentadas}

\begin{tcolorbox}[vocabbox, title={\emoji{pushpin} Vocabulario}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\ \midrule
\vocabitem{落とす}{おとす}{dejar caer / soltar}{v. G1}
\vocabitem{壊す}{こわす}{romper / destruir}{v. G1}
\vocabitem{忘れる}{わすれる}{olvidar}{v. G2}
\vocabitem{遅刻する}{ちこくする}{llegar tarde}{v. suru}
\vocabitem{なくす}{なくす}{perder (objeto)}{v. G1}
\vocabitem{食べ過ぎる}{たべすぎる}{comer en exceso}{v. G2}
\vocabitem{後悔する}{こうかいする}{arrepentirse}{v. suru}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{\emoji{speech-balloon} Frases Clave}
\frase{あ、\ruby{忘}{わす}れてしまった！}{¡Ay, lo olvidé! (con lamento)}
\frase{\ruby{宿題}{しゅくだい}を\ruby{全部}{ぜんぶ}やってしまいます。}{Terminaré toda la tarea (de una vez).}
\frase{\ruby{財布}{さいふ}をなくしてしまいました。}{(Lamentablemente) perdí mi billetera.}
\frase{もう\ruby{食}{た}べてしまいました。}{Ya lo comí todo (para bien o mal).}

\subsection*{\emoji{gear} Gramática}
\patron{てしまう — completar o lamentar}
  {[V-て\ruby{形}{けい}] + しまう}
  {\ej{\ruby{財布}{さいふ}を\ruby{落}{お}としてしまいました。}{(Lamentablemente) dejé caer mi billetera.}
   \ej{\ruby{映画}{えいが}を\ruby{全部}{ぜんぶ}\ruby{見}{み}てしまった。}{Vi la película entera (de principio a fin).}
   \ej{\ruby{電車}{でんしゃ}に\ruby{乗}{の}り\ruby{遅}{おく}れてしまいました。}{(Desafortunadamente) perdí el tren.}}

\patron{てしまう — forma pasado polite}
  {[V-て\ruby{形}{けい}] + しまいました}
  {\ej{\ruby{大切}{たいせつ}なものをなくしてしまいました。}{Perdí algo importante.}
   \ej{つい\ruby{食}{た}べ\ruby{過}{す}ぎてしまいました。}{Sin querer, comí demasiado.}}

\comparacion{てしまう vs てある}
  {てしまう\\\small completar involuntariamente\\\small \ruby{食}{た}べてしまった。\\\textit{(Se) lo comí todo.}}
  {てある\\\small estado resultante intencional\\\small \ruby{弁当}{べんとう}が\ruby{作}{つく}ってある。\\\textit{El bentō ya está preparado.}}
  {てしまう implica que la acción se completó (con lamento o simplemente hasta el final). てある implica que alguien lo hizo intencionalmente y el estado persiste.}

\coloquial{〜てしまう / 〜てしまった}{〜ちゃう / 〜ちゃった (y 〜じゃう / 〜じゃった)}{
  て → ちゃ; で → じゃ. Muy frecuente en habla informal. \\
  \ruby{全部}{ぜんぶ}\ruby{食}{た}べてしまった → \ruby{全部}{ぜんぶ}\ruby{食}{た}べちゃった！}

\culturabox{\ruby{後悔}{こうかい}の\ruby{表現}{ひょうげん} — Expresar arrepentimiento}{
  En japonés, el lamento se expresa sutilmente. てしまう lleva una connotación de «no debería haber pasado» sin necesidad de decirlo explícitamente. En la cultura japonesa, esta expresión indirecta del arrepentimiento es preferida sobre admisiones directas de culpa.
}

\lectura{\ruby{今日}{きょう}は\ruby{最悪}{さいあく}の\ruby{日}{ひ}だった。まず、バスに\ruby{乗}{の}り\ruby{遅}{おく}れてしまった。それから、\ruby{傘}{かさ}を\ruby{忘}{わす}れてしまって、\ruby{雨}{あめ}にぬれた。\ruby{財布}{さいふ}もなくしてしまって、\ruby{本当}{ほんとう}に\ruby{大変}{たいへん}な\ruby{一日}{いちにち}だった。}
{Hoy fue el peor día. Primero, perdí el autobús. Luego, olvidé el paraguas y me mojé con la lluvia. Además, perdí la billetera. Realmente fue un día terrible.}

\begin{tcolorbox}[ejerciciobox, title={\emoji{pencil} Ejercicios}]
\begin{enumerate}
  \item Transforma usando てしまう: \ruby{宿題}{しゅくだい}を\ruby{忘}{わす}れる
  \item ¿Formal o coloquial? Convierte: \ruby{食}{た}べてしまった → forma coloquial
  \item Crea una oración usando てしまいました describiendo algo que lamentas.
  \item ¿てしまう o てある? \ruby{窓}{まど}が\ruby{閉}{し}めて\_\_\_。(alguien lo cerró intencionalmente)
\end{enumerate}
\textbf{Respuestas:}
1) \ruby{宿題}{しゅくだい}を\ruby{忘}{わす}れてしまった \quad
2) \ruby{食}{た}べちゃった \quad
3) (libre) \quad
4) てある
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={\emoji{mahjong} Kanjis}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\ \midrule
\kanjirow{忘}{ぼう}{\ruby{わす}{れる}}{olvidar}{\ruby{忘}{わす}れる / \ruby{忘}{ぼう}\ruby{年}{ねん}\ruby{会}{かい}}
\kanjirow{落}{らく}{\ruby{お}{とす・ちる}}{caer/soltar}{\ruby{落}{お}とす / \ruby{落}{お}ちる}
\kanjirow{壊}{かい}{\ruby{こわ}{す・れる}}{romper}{\ruby{壊}{こわ}す / \ruby{故障}{こしょう}}
\kanjirow{後}{こう}{\ruby{あと・うし}{ろ}}{después/atrás}{\ruby{後悔}{こうかい} / \ruby{午後}{ごご}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

### Unit 03 — `Parte2/unidades/03-teoku.tex`

```latex
\chapter{\emoji{calendar} \ruby{ておく}{} — Preparar con anticipación}
\unidadheader{03}{準備}{ておく}{Acciones realizadas de antemano o en preparación}

\begin{tcolorbox}[vocabbox, title={\emoji{pushpin} Vocabulario}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\ \midrule
\vocabitem{予約する}{よやくする}{reservar}{v. suru}
\vocabitem{準備する}{じゅんびする}{preparar}{v. suru}
\vocabitem{確認する}{かくにんする}{confirmar}{v. suru}
\vocabitem{調べる}{しらべる}{investigar / buscar info}{v. G2}
\vocabitem{片付ける}{かたづける}{ordenar / recoger}{v. G2}
\vocabitem{連絡する}{れんらくする}{contactar / avisar}{v. suru}
\vocabitem{読んでおく}{よんでおく}{leer de antemano}{v. compuesto}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{\emoji{speech-balloon} Frases Clave}
\frase{\ruby{旅行}{りょこう}の\ruby{前}{まえ}に\ruby{宿}{やど}を\ruby{予約}{よやく}しておきます。}{Reservaré el alojamiento antes del viaje.}
\frase{\ruby{会議}{かいぎ}の\ruby{前}{まえ}に\ruby{資料}{しりょう}を\ruby{読}{よ}んでおいてください。}{Por favor lea los materiales antes de la reunión.}
\frase{\ruby{冷蔵庫}{れいぞうこ}に\ruby{入}{い}れておきました。}{Lo guardé en el refrigerador (de antemano).}

\subsection*{\emoji{gear} Gramática}
\patron{ておく — hacer algo de antemano}
  {[V-て\ruby{形}{けい}] + おく}
  {\ej{\ruby{明日}{あした}のために\ruby{弁当}{べんとう}を\ruby{作}{つく}っておきます。}{Prepararé el bentō de antemano para mañana.}
   \ej{\ruby{旅行前}{りょこうまえ}にパスポートを\ruby{確認}{かくにん}しておきました。}{Verifiqué el pasaporte con anticipación antes del viaje.}
   \ej{\ruby{暖房}{だんぼう}をつけておいてください。}{Por favor pon la calefacción de antemano.}}

\comparacion{ておく vs てしまう}
  {ておく\\\small preparación intencional\\\small \ruby{読}{よ}んでおく\\\textit{leer de antemano (plan)}}
  {てしまう\\\small completar (con lamento)\\\small \ruby{読}{よ}んでしまう\\\textit{terminar de leer (de una vez / ay)}}
  {ておく implica previsión y preparación consciente. てしまう implica que la acción se completa, a veces involuntariamente.}

\coloquial{〜ておく}{〜とく / 〜どく}{
  Contracción oral muy común: ておく → とく、ておいて → といて。\\
  \ruby{準備}{じゅんび}しておく → \ruby{準備}{じゅんび}しとく。\ruby{読}{よ}んでおいて → \ruby{読}{よ}んどいて。}

\culturabox{\ruby{先}{さき}を\ruby{読}{よ}む\ruby{文化}{ぶんか} — La cultura de anticiparse}{
  En Japón, la previsión y preparación son valores muy apreciados. No causar molestia a los demás (\ruby{迷惑}{めいわく}をかけない) pasa por hacer las cosas de antemano. ておく refleja esta mentalidad: actuar ahora para que las cosas salgan bien después.
}

\lectura{\ruby{旅行}{りょこう}の\ruby{前日}{ぜんじつ}、アルドはいろいろ\ruby{準備}{じゅんびjun}しておいた。まず、パスポートと\ruby{航空券}{こうくうけん}を\ruby{確認}{かくにん}しておいた。それから、\ruby{ホテル}{ほてる}に\ruby{連絡}{れんらく}しておいた。\ruby{荷物}{にもつ}もまとめておいたので、\ruby{当日}{とうじつ}はとても\ruby{楽}{らく}だった。}
{La víspera del viaje, Aldo preparó varias cosas de antemano. Primero, verificó el pasaporte y el boleto de avión. Luego, contactó al hotel. Como también había empacado todo de antemano, el día del viaje fue muy tranquilo.}

\begin{tcolorbox}[ejerciciobox, title={\emoji{pencil} Ejercicios}]
\begin{enumerate}
  \item Transforma con ておく: \ruby{旅行前}{りょこうまえ}に地図を\ruby{調}{しら}べる
  \item Convierte a forma coloquial とく: \ruby{先}{さき}に\ruby{連絡}{れんらく}しておく
  \item ¿Por qué se usa ておく aquí? \ruby{試験}{しけん}の\ruby{前}{まえ}に\ruby{よく寝}{ねむ}ておきましょう。
\end{enumerate}
\textbf{Respuestas:}
1) \ruby{旅行前}{りょこうまえ}に地図を\ruby{調}{しら}べておく \quad
2) \ruby{先}{さき}に\ruby{連絡}{れんらく}しとく \quad
3) Es conveniente dormir bien antes del examen — acción preparatoria con beneficio futuro.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={\emoji{mahjong} Kanjis}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\ \midrule
\kanjirow{準}{じゅん}{—}{estándar/preparar}{\ruby{準備}{じゅんび} / \ruby{基準}{きじゅん}}
\kanjirow{備}{び}{\ruby{そな}{える}}{equipar/preparar}{\ruby{準備}{じゅんび} / \ruby{設備}{せつび}}
\kanjirow{予}{よ}{—}{anticipado/previo}{\ruby{予約}{よやく} / \ruby{予定}{よてい}}
\kanjirow{約}{やく}{—}{acuerdo/aproximado}{\ruby{予約}{よやく} / \ruby{約束}{やくそく}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

### Unit 04 — `Parte2/unidades/04-tearu.tex`

```latex
\chapter{\emoji{broom} \ruby{てある}{} — Estado resultante intencional}
\unidadheader{04}{結果}{てある}{Describir estados que resultan de acciones intencionales}

\begin{tcolorbox}[vocabbox, title={\emoji{pushpin} Vocabulario}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\ \midrule
\vocabitem{貼る}{はる}{pegar / colocar (en pared)}{v. G1}
\vocabitem{置く}{おく}{colocar / poner}{v. G1}
\vocabitem{閉める}{しめる}{cerrar (transitivo)}{v. G2}
\vocabitem{開ける}{あける}{abrir (transitivo)}{v. G2}
\vocabitem{冷やす}{ひやす}{enfriar}{v. G1}
\vocabitem{用意する}{ようするい}{preparar / disponer}{v. suru}
\vocabitem{飾る}{かざる}{decorar}{v. G1}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{\emoji{speech-balloon} Frases Clave}
\frase{\ruby{黒板}{こくばん}に\ruby{名前}{なまえ}が\ruby{書}{か}いてあります。}{Hay un nombre escrito en la pizarra (alguien lo escribió).}
\frase{\ruby{冷蔵庫}{れいぞうこ}に\ruby{飲}{の}み\ruby{物}{もの}が\ruby{冷}{ひ}やしてあります。}{En el refrigerador hay bebidas enfriadas (puestas allí).}
\frase{\ruby{壁}{かべ}にポスターが\ruby{貼}{は}ってあります。}{Hay un póster pegado en la pared.}

\subsection*{\emoji{gear} Gramática}
\patron{てある — estado resultante de acción intencional}
  {[V\ruby{他動詞}{たどうし}-て\ruby{形}{けい}] + ある}
  {\ej{\ruby{窓}{まど}が\ruby{閉}{し}めてあります。}{La ventana está cerrada (alguien la cerró intencionalmente).}
   \ej{\ruby{机}{つくえ}の\ruby{上}{うえ}に\ruby{本}{ほん}が\ruby{置}{お}いてあります。}{Hay un libro colocado sobre el escritorio.}
   \ej{\ruby{部屋}{へや}にお\ruby{花}{はな}が\ruby{飾}{かざ}ってありました。}{Había flores decorando la habitación.}}

\comparacion{てある vs ている (〜閉まっている)}
  {てある\\\small agente intencional implícito\\\small \ruby{窓}{まど}が\ruby{閉}{し}めてある\\\textit{La ventana está cerrada (alguien la cerró)}}
  {ている (v. intransitivo)\\\small estado sin agente implícito\\\small \ruby{窓}{まど}が\ruby{閉}{し}まっている\\\textit{La ventana está cerrada (simplemente lo está)}}
  {てある usa verbos transitivos + ある. ている con intransitivos solo describe estado. La diferencia clave: てある implica que alguien lo hizo a propósito.}

\coloquial{てある}{てる (en contexto obvio)}{
  En habla muy casual, el contexto hace obvia la intencionalidad y てある puede usarse igual que ている. La distinción formal siempre se mantiene en escritura.}

\culturabox{\ruby{気遣}{きづか}い — Hacer cosas por otros sin decirlo}{
  En Japón, preparar algo silenciosamente para que otros lo encuentren listo es una forma de cuidado (気遣い). El uso de てある en una conversación puede implicar: «ya lo hice por ti». Es una forma de hospitalidad discreta.
}

\lectura{ホテルの\ruby{部屋}{へや}に\ruby{入}{はい}ると、\ruby{花}{はな}が\ruby{飾}{かざ}ってあって、\ruby{冷蔵庫}{れいぞうこ}には\ruby{飲}{の}み\ruby{物}{もの}が\ruby{冷}{ひ}やしてあった。\ruby{机}{つくえ}の\ruby{上}{うえ}には\ruby{案内}{あんない}\ruby{地図}{ちず}が\ruby{置}{お}いてあった。スタッフがすべて\ruby{準備}{じゅんび}してくれていたのだ。}
{Al entrar a la habitación del hotel, había flores decoradas, y en el refrigerador había bebidas enfriadas. Sobre el escritorio había un mapa guía colocado. El personal había preparado todo.}

\begin{tcolorbox}[ejerciciobox, title={\emoji{pencil} Ejercicios}]
\begin{enumerate}
  \item ¿てある o ている? \ruby{電気}{でんき}が\_\_\_。(solo describe que está encendida)
  \item Transforma con てある: \ruby{誰}{だれ}かが\ruby{手紙}{てがみ}を\ruby{書}{か}いた → \ruby{手紙}{てがみ}が\_\_\_
  \item Crea una oración describiendo tu habitación usando てある.
\end{enumerate}
\textbf{Respuestas:}
1) \ruby{電気}{でんき}がついている (intransitivo, no hay agente implícito) \quad
2) \ruby{手紙}{てがみ}が\ruby{書}{か}いてある \quad
3) (libre)
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={\emoji{mahjong} Kanjis}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\ \midrule
\kanjirow{置}{ち}{\ruby{お}{く}}{colocar}{\ruby{置}{お}く / \ruby{位置}{いち}}
\kanjirow{貼}{ちょう}{\ruby{は}{る}}{pegar}{\ruby{貼}{は}る / \ruby{貼}{は}り\ruby{紙}{がみ}}
\kanjirow{飾}{しょく}{\ruby{かざ}{る}}{decorar}{\ruby{飾}{かざ}る / \ruby{装飾}{そうしょく}}
\kanjirow{壁}{へき}{\ruby{かべ}{}}{pared}{\ruby{壁}{かべ} / \ruby{障壁}{しょうへき}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

### Unit 05 — `Parte2/unidades/05-youto-suru.tex`

```latex
\chapter{\emoji{running} \ruby{ようとする}{} — Intentar / Negarse}
\unidadheader{05}{意志}{ようとする / ようとしない}{Expresar intento de acción o resistencia}

\begin{tcolorbox}[vocabbox, title={\emoji{pushpin} Vocabulario}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\ \midrule
\vocabitem{逃げる}{にげる}{huir / escapar}{v. G2}
\vocabitem{起きる}{おきる}{levantarse / despertarse}{v. G2}
\vocabitem{諦める}{あきらめる}{rendirse / abandonar}{v. G2}
\vocabitem{挑戦する}{ちょうせんする}{desafiar / intentar}{v. suru}
\vocabitem{謝る}{あやまる}{disculparse}{v. G1}
\vocabitem{認める}{みとめる}{reconocer / admitir}{v. G2}
\vocabitem{拒否する}{きょひする}{rechazar / negarse}{v. suru}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{\emoji{speech-balloon} Frases Clave}
\frase{\ruby{起}{お}きようとしたが、できなかった。}{Intenté levantarme pero no pude.}
\frase{\ruby{逃}{に}げようとしても\ruby{無駄}{むだ}です。}{Es inútil intentar huir.}
\frase{\ruby{彼}{かれ}は\ruby{謝}{あやま}ろうとしない。}{Él se niega a disculparse.}
\frase{\ruby{諦}{あきら}めようとしたとき、\ruby{奇跡}{きせき}が\ruby{起}{お}きた。}{Justo cuando estaba a punto de rendirme, ocurrió un milagro.}

\subsection*{\emoji{gear} Gramática}
\patron{ようとする — estar a punto de / intentar}
  {[V-\ruby{意向形}{いこうけい}] + とする}
  {\ej{\ruby{寝}{ね}ようとしたとき、\ruby{電話}{でんわ}が\ruby{鳴}{な}った。}{Justo cuando estaba a punto de dormir, sonó el teléfono.}
   \ej{ドアを\ruby{開}{あ}けようとしたが、\ruby{鍵}{かぎ}がかかっていた。}{Intenté abrir la puerta, pero estaba con llave.}
   \ej{\ruby{立}{た}ち\ruby{上}{あ}がろうとしている。}{Está intentando ponerse de pie.}}

\patron{ようとしない — negarse a / no querer}
  {[V-\ruby{意向形}{いこうけい}] + としない}
  {\ej{\ruby{彼}{かれ}は\ruby{謝}{あやま}ろうとしない。}{Él se niega a disculparse.}
   \ej{\ruby{子供}{こども}が\ruby{野菜}{やさい}を\ruby{食}{た}べようとしない。}{El niño se niega a comer verduras.}}

\comparacion{ようとする vs ようとしない}
  {ようとする\\\small intento / a punto de\\\small \ruby{起}{お}きようとした\\\textit{Intentó levantarse}}
  {ようとしない\\\small resistencia / negativa\\\small \ruby{起}{お}きようとしない\\\textit{Se niega a levantarse}}
  {La misma base (forma volitiva + と) con する o しない cambia completamente el significado: esfuerzo vs resistencia.}

\coloquial{ようとしている}{ようとしてる / ようとしてんの？}{
  En habla casual: としている → としてる。 Para preguntar con incredulidad: \ruby{逃}{に}げようとしてんの？ ¿Estás intentando escapar?}

\culturabox{\ruby{意志}{いし}の\ruby{表現}{ひょうげん} — Expresar la voluntad en japonés}{
  La forma volitiva (\ruby{意向形}{いこうけい}) expresa la voluntad del hablante. Al combinarse con とする, el foco pasa del resultado a la intención. En la cultura japonesa, expresar que se «intenta» algo (esfuerzo) es valorado incluso cuando no se logra: \ruby{頑張}{がんば}ろうとした (intenté esforzarme).
}

\lectura{\ruby{彼女}{かのじょ}は\ruby{何度}{なんど}も\ruby{立}{た}ち\ruby{上}{あ}がろうとした。\ruby{足}{あし}が\ruby{痛}{いた}くて、なかなかできなかった。それでも\ruby{諦}{あきら}めようとしなかった。\ruby{周}{まわ}りの\ruby{人}{ひと}が\ruby{応援}{おうえん}してくれて、ついに\ruby{成功}{せいこう}した。}
{Ella intentó ponerse de pie muchas veces. Le dolían los pies y no lo lograba fácilmente. Aun así, no quiso rendirse. Las personas a su alrededor la animaron y al final lo logró.}

\begin{tcolorbox}[ejerciciobox, title={\emoji{pencil} Ejercicios}]
\begin{enumerate}
  \item Conjuga en forma volitiva: \ruby{食}{た}べる、する、\ruby{来}{く}る、\ruby{書}{か}く
  \item Transforma: \ruby{彼}{かれ}は\ruby{認}{みと}めない (→ usa ようとしない)
  \item Crea una oración con ようとしたが usando una experiencia propia.
\end{enumerate}
\textbf{Respuestas:}
1) \ruby{食}{た}べよう・しよう・こよう・\ruby{書}{か}こう \quad
2) \ruby{彼}{かれ}は\ruby{認}{みと}めようとしない \quad
3) (libre)
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={\emoji{mahjong} Kanjis}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\ \midrule
\kanjirow{逃}{とう}{\ruby{に}{げる}}{huir}{\ruby{逃}{に}げる / \ruby{逃亡}{とうぼう}}
\kanjirow{挑}{ちょう}{\ruby{いど}{む}}{desafiar}{\ruby{挑戦}{ちょうせん} / \ruby{挑}{いど}む}
\kanjirow{諦}{てい}{\ruby{あきら}{める}}{resignarse}{\ruby{諦}{あきら}める}
\kanjirow{認}{にん}{\ruby{みと}{める}}{reconocer}{\ruby{認}{みと}める / \ruby{認識}{にんしき}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Compile and commit units 02–05**

```powershell
cd "D:\Codigo Abierto\ApuntesJapones\Parte2"
lualatex ApuntesJaponesPart_2.tex
git add Parte2/unidades/02-teshimau.tex Parte2/unidades/03-teoku.tex Parte2/unidades/04-tearu.tex Parte2/unidades/05-youto-suru.tex
git commit -m "feat(u02-05): てしまう, ておく, てある, ようとする"
```

---

## Task 8: Units 06–09 (voz pasiva y causativa)

### Unit 06 — `Parte2/unidades/06-pasiva-basica.tex`

Vocab: \vocabitem{褒める}{ほめる}{elogiar}{v.G2}, \vocabitem{叱る}{しかる}{regañar}{v.G1}, \vocabitem{噛む}{かむ}{morder}{v.G1}, \vocabitem{踏む}{ふむ}{pisar}{v.G1}, \vocabitem{盗む}{ぬすむ}{robar}{v.G1}, \vocabitem{誘う}{さそう}{invitar}{v.G1}, \vocabitem{選ぶ}{えらぶ}{elegir}{v.G1}

Chapter: `\chapter{\emoji{shield} \ruby{受け身}{うけみ} — Voz Pasiva Básica}`

Gramática — dos patrones:
- Formación pasiva: G1 final u→aれる (書く→書かれる), G2 ru→られる (食べる→食べられる), G3 する→される, くる→こられる
- Estructura: [sujeto]は/が [agente]に [V-pasiva]
  - ej: \ruby{先生}{せんせい}に\ruby{褒}{ほ}められました。Fui elogiado por el profesor.
  - ej: \ruby{友達}{ともだち}に\ruby{誘}{さそ}われました。Fui invitado por mi amigo/a.

Comparación: activa vs pasiva — \ruby{先生}{せんせい}が\ruby{私}{わたし}を\ruby{褒}{ほ}めた → \ruby{私}{わたし}は\ruby{先生}{せんせい}に\ruby{褒}{ほ}められた

Coloquial: formas pasivas igual en habla informal; solo cambia です/ます → だ

Cultura: 受け身文化 — Japanese often describes events as happening *to* oneself. Encodes perspective of person affected.

Lectura: \ruby{大変}{たいへん}な\ruby{一日}{いちにち} — a day described from passive perspective (被害者視点)

Kanjis: 受(じゅ/うける), 褒(ほう/ほめる), 叱(しつ/しかる)

### Unit 07 — `Parte2/unidades/07-pasiva-perjuicio.tex`

Chapter: `\chapter{\emoji{cloud-with-rain} \ruby{迷惑}{めいわく}の\ruby{受け身}{うけみ} — Pasiva de Perjuicio}`

Vocab: 降る(ふる)fall-rain, 泣く(なく)cry, 騒ぐ(さわぐ)make noise, 逃げる(にげる)escape, 邪魔する(じゃまする)interrupt, 死ぬ(しぬ)die

Gramática:
- Pasiva de perjuicio con V intransitivo: \ruby{雨}{あめ}に\ruby{降}{ふ}られた (La lluvia me cayó encima — fui perjudicado por la lluvia)
- Pasiva de pérdida de posesión: [persona]に[objeto]を[V]-られる — \ruby{泥棒}{どろぼう}に\ruby{自転車}{じてんしゃ}を\ruby{盗}{ぬす}まれました。(Me robaron la bicicleta)

Comparación: pasiva directa (褒められる — neutral/positivo) vs pasiva de perjuicio (泣かれる — evento negativo para el sujeto)

Coloquial: 〜られて困った muy común para expresar incomodidad

Cultura: 被害者意識 — victim perspective. Japanese grammar allows encoding being negatively affected.

Lectura: 電車の中で — things happening to you on a train (迷惑な人たち)

Kanjis: 迷(めい/まよう), 惑(わく/まどう), 盗(とう/ぬすむ)

### Unit 08 — `Parte2/unidades/08-causativa.tex`

Chapter: `\chapter{\emoji{arrows-counterclockwise} \ruby{使役}{しえき} — Forma Causativa}`

Vocab: 食べさせる(たべさせる), 待たせる(またせる), 働かせる(はたらかせる), 笑わせる(わらわせる), 発表させる(はっぴょうさせる), 自由にさせる(じゆうにさせる)

Gramática:
- Formación: G1 final u→aせる (書く→書かせる), G2 ru→させる (食べる→食べさせる), G3 する→させる, くる→こさせる
- Estructura: [causante]が [causado]を/に [V-causativa]
  - \ruby{子供}{こども}に\ruby{野菜}{やさい}を\ruby{食}{た}べさせた。I made the child eat vegetables.
  - \ruby{先生}{せんせい}が\ruby{学生}{がくせい}を\ruby{発表}{はっぴょう}させた。The teacher made the students present.
- Nuance de permiso: させてください/させてあげる

Comparación: を (forced) vs に (allowed): 子供を食べさせる (force) vs 子供に食べさせる (allow/let eat)

Coloquial: 〜させる → 〜さす en Kansai / habla muy casual masculina

Cultura: 上下関係 — hierarchy in Japan. Causative reflects power dynamics: superiors make subordinates do things.

Lectura: 会社での一日 — using causative in workplace context

Kanjis: 役(やく/-), 働(どう/はたらく), 笑(しょう/わらう)

### Unit 09 — `Parte2/unidades/09-causativa-pasiva.tex`

Chapter: `\chapter{\emoji{weary-face} \ruby{使役受け身}{しえきうけみ} — Causativa-Pasiva}`

Vocab: 残業する(ざんぎょうする), 謝る(あやまる), 走る(はしる), 我慢する(がまんする), 飲む(のむ), 待つ(まつ)

Gramática:
- Formación: V-causativa + られる: 食べさせる→食べさせられる; 書かせる→書かされる (forma corta G1)
- Significado: ser obligado a hacer algo (involuntario, frecuentemente negativo)
  - \ruby{上司}{じょうし}に\ruby{残業}{ざんぎょう}させられました。Fui obligado a trabajar horas extra por mi jefe.
  - \ruby{子供}{こども}のとき、\ruby{嫌}{きら}いな\ruby{野菜}{やさい}を\ruby{食}{た}べさせられた。De niño, me obligaban a comer verduras que no me gustaban.
- Forma corta (G1 4+ moras): 飲まされる (en vez de 飲まさせられる)

Comparación: させる (hacer hacer) vs させられる (ser hecho hacer — involuntario)

Coloquial: 〜させられた ¡muy común para quejarse! Tono de resignación/queja.

Cultura: 日本の職場文化 — Japanese work culture, obligatory overtime (残業), implicit pressure to follow superiors.

Lectura: 新入社員の愚痴 — new employee venting about being forced to do things

Kanjis: 残(ざん/のこる), 業(ぎょう/-), 我(が/われ), 慢(まん/-)

- [ ] **Compile and commit units 06–09**

```powershell
cd "D:\Codigo Abierto\ApuntesJapones\Parte2"
lualatex ApuntesJaponesPart_2.tex
git add Parte2/unidades/06-pasiva-basica.tex Parte2/unidades/07-pasiva-perjuicio.tex Parte2/unidades/08-causativa.tex Parte2/unidades/09-causativa-pasiva.tex
git commit -m "feat(u06-09): pasiva básica, pasiva perjuicio, causativa, causativa-pasiva"
```

> **NOTE for units 06-09:** Write each file using the full LaTeX structure shown in Units 01-05. Use the vocab, grammar patterns, comparación, coloquial, culturabox, lectura, ejercicios, and kanjibox sections listed above. Follow the exact same tcolorbox command structure as the reference unit (Unit 01).

---

## Task 9: Units 10–15 (propósito, nominalización, evidencialidad)

For each unit below, create the full `.tex` file following the Unit 01 structure. Specific content:

### Unit 10 — `10-tame-ni-you-ni.tex`
Chapter: `\chapter{\emoji{dart} \ruby{ために}{} vs \ruby{ように}{} — Propósito}`
Vocab: 合格する(ごうかくする), 痩せる(やせる), 貯金する(ちょきんする), 健康になる(けんこうになる), 覚える(おぼえる), 努力する(どりょくする)
- Pattern ために: [V-dict / N+の] + ために — concrete goal
  ej: \ruby{医者}{いしゃ}になるために\ruby{毎日}{まいにち}\ruby{勉強}{べんきょう}しています。
- Pattern ように: [V-potential / negative] + ように — desired ability/state
  ej: \ruby{泳}{およ}げるように\ruby{毎日}{まいにち}\ruby{練習}{れんしゅう}しています。
  ej: \ruby{忘}{わす}れないようにメモを\ruby{取}{と}ります。
Comparación: ために (meta concreta directa) vs ように (capacidad/estado deseado — con potencial o negativo)
Coloquial: ambos naturales en habla cotidiana
Cultura: 努力の文化 — work ethic and purpose-driven effort in Japan
Kanjis: 合(ごう/あう), 格(かく/-), 努(ど/つとめる), 力(りょく/ちから)

### Unit 11 — `11-you-ni-you-na.tex`
Chapter: `\chapter{\emoji{sparkles} \ruby{ように}{}/\ruby{ような}{} — Como / Semejante a}`
Vocab: 夢(ゆめ), 氷(こおり), 嘘(うそ), 鬼(おに), 羽(はね), 砂糖(さとう)
- Pattern ようだ: [V/adj/N+の] + ようだ — deducción/apariencia del hablante
  ej: \ruby{外}{そと}は\ruby{雨}{あめ}のようです。Parece que afuera llueve.
- Pattern ような: [V/adj/N+の] + ような + sustantivo — modificar con similitud
  ej: \ruby{夢}{ゆめ}のような\ruby{話}{はなし}。Una historia como un sueño.
  ej: \ruby{鬼}{おに}のような\ruby{上司}{じょうし}。Un jefe como un demonio.
Comparación: ようだ (deducción propia) vs らしい (info externa/típico del sujeto) vs そうだ (apariencia inmediata visual)
Coloquial: ようだ → みたいだ en habla casual: \ruby{雨}{あめ}みたいだ。
Cultura: 比喩表現 — Japanese figurative language and common similes
Kanjis: 夢(む/ゆめ), 氷(ひょう/こおり), 鬼(き/おに)

### Unit 12 — `12-koto-no.tex`
Chapter: `\chapter{\emoji{scroll} \ruby{こと}{} vs \ruby{の}{} — Nominalización}`
Vocab: 趣味(しゅみ), 驚く(おどろく), 得意(とくい), 苦手(にがて), 気づく(きづく), 感じる(かんじる)
- Pattern こと: [V-plain] + こと — abstracto/general
  ej: \ruby{泳}{およ}ぐことが\ruby{得意}{とくい}です。Soy bueno nadando (habilidad general).
  ej: \ruby{約束}{やくそく}を\ruby{守}{まも}ることは\ruby{大切}{たいせつ}です。
- Pattern の: [V-plain] + の + が/を — concreto/perceptual
  ej: \ruby{子供}{こども}が\ruby{笑}{わら}うのを\ruby{見}{み}た。Vi reír al niño (evento percibido).
  ej: \ruby{鳥}{とり}が\ruby{飛}{と}ぶのが\ruby{見}{み}えた。Pude ver pájaros volando.
Comparación: こと (abstracto — reglas, hábitos, sentimientos) vs の (concreto — ver, oír, esperar algo que ocurre)
Coloquial: の más frecuente en habla casual: 行くの好き。
Cultura: 日本語の抽象化 — cómo el japonés nominaliza y abstrae acciones
Kanjis: 趣(しゅ/おもむき), 味(み/あじ), 驚(きょう/おどろく)

### Unit 13 — `13-evidencialidad.tex`
Chapter: `\chapter{\emoji{magnifying-glass-tilted-left} \ruby{そうだ}{}/\ruby{らしい}{}/\ruby{ようだ}{} — Evidencialidad}`
Vocab: 台風(たいふう), 噂(うわさ), 天気予報(てんきよほう), 情報(じょうほう), 証拠(しょうこ), 観察(かんさつ)
- そうだ (hearsay): [oración plain] + そうです — «me dijeron que»
  ej: \ruby{明日}{あした}は\ruby{雪}{ゆき}が\ruby{降}{ふ}るそうです。Dicen que mañana nevará.
- らしい (evidencia indirecta/típico): [V/adj/N] + らしい
  ej: \ruby{彼}{かれ}は\ruby{日本人}{にほんじん}らしい\ruby{話}{はな}し\ruby{方}{かた}をする。Habla de una manera típicamente japonesa.
  ej: あの\ruby{店}{みせ}は\ruby{人気}{にんき}があるらしい。Según parece, esa tienda es popular.
- ようだ (deducción observacional): [V/adj/N] + ようだ
  ej: \ruby{彼女}{かのじょ}は\ruby{怒}{おこ}っているようだ。Parece que está enojada (lo noto).
Comparación tres vías: そうだ (info de otros) vs らしい (evidencia indirecta/comportamiento típico) vs ようだ (deducción propia observacional)
Coloquial: らしい y ようだ → みたい en casual
Cultura: 曖昧な言い方 — Japanese preference for non-committal, indirect language
Kanjis: 台(だい/-), 風(ふう/かぜ), 噂(うわさ/うわさ)

### Unit 14 — `14-hazuda.tex`
Chapter: `\chapter{\emoji{thinking-face} \ruby{はずだ}{}/\ruby{はずがない}{} — Expectativa Lógica}`
Vocab: 確かな(たしかな), 間違い(まちがい), 予定(よてい), 証明する(しょうめいする), 信じる(しんじる), 当然(とうぜん)
- はずだ: [V/adj plain / N+の] + はずだ — expectativa lógica basada en conocimiento
  ej: \ruby{彼}{かれ}はもう\ruby{着}{つ}いているはずだ。Lógicamente ya debería haber llegado.
  ej: \ruby{明日}{あした}は\ruby{晴}{は}れるはずです。Debería estar despejado mañana.
- はずがない / はずはない: [V/adj plain / N+の] + はずがない — imposibilidad lógica
  ej: \ruby{彼女}{かのじょ}がそんなことをするはずがない。No hay manera de que ella haga algo así.
Comparación: はずだ (esperado por lógica/conocimiento) vs だろう (conjetura general)
Coloquial: はずだよ (casual afirmativo); はずないよ (casual negativo)
Cultura: 期待と現実 — gap between expectation and reality in Japanese social contexts
Kanjis: 確(かく/たしか), 証(しょう/あかし), 信(しん/しんじる)

### Unit 15 — `15-wakeda.tex`
Chapter: `\chapter{\emoji{bulb} \ruby{わけだ}{}/\ruby{わけがない}{} — Conclusión Lógica}`
Vocab: 当然(とうぜん), 結局(けっきょく), 納得(なっとく), 道理(どうり), 結論(けつろん), 説明(せつめい)
- わけだ: conclusión lógica inevitable — «así que naturalmente»
  ej: \ruby{彼}{かれ}は\ruby{毎日}{まいにち}10\ruby{時間}{じかん}\ruby{勉強}{べんきょう}している。そりゃ\ruby{合格}{ごうかく}するわけだ。
  ej: \ruby{彼女}{かのじょ}はネイティブだから、\ruby{日本語}{にほんご}が\ruby{上手}{じょうず}なわけだ。
- わけがない: absoluta imposibilidad
  ej: \ruby{彼}{かれ}がそんなことをするわけがない。
- わけではない: «no es que»
  ej: \ruby{嫌}{きら}いなわけではありません。No es que no me guste.
Comparación: わけだ (conclusión lógica — aha moment) vs はずだ (expectativa previa)
Coloquial: そういうわけで = «y es por eso que»; わけ？ = «¿o sea que...?» (pregunta casual)
Cultura: 説明の文化 — explaining oneself. わけ used to justify and explain.
Kanjis: 道(どう/みち), 理(り/-), 納(のう/おさめる)

- [ ] **Compile and commit units 10–15**

```powershell
lualatex ApuntesJaponesPart_2.tex
git add Parte2/unidades/10-tame-ni-you-ni.tex Parte2/unidades/11-you-ni-you-na.tex Parte2/unidades/12-koto-no.tex Parte2/unidades/13-evidencialidad.tex Parte2/unidades/14-hazuda.tex Parte2/unidades/15-wakeda.tex
git commit -m "feat(u10-15): ために/ように, ように/ような, こと/の, evidencialidad, はずだ, わけだ"
```

---

## Task 10: Units 16–20 (límites, exceso, cambio de estado)

### Unit 16 — `16-dake-shika-bakari.tex`
Chapter: `\chapter{\emoji{balance-scale} \ruby{だけ}{}/\ruby{しか}{}/\ruby{ばかり}{} — Solo / Nada más que / No hace más que}`
Vocab: 残り(のこり), 限る(かぎる), 他(ほか), 全部(ぜんぶ), 僅か(わずか), 専ら(もっぱら)
- だけ: [N/V] + だけ — solo/únicamente (neutro)
  ej: 一つだけ食べます。
- しか〜ない: [N] + しか + negativo — solo (con insuficiencia implícita)
  ej: 百円しかありません。Solo tengo 100 yenes (no es suficiente).
- ばかり: [N/V-te] + ばかり — no hace más que, exceso
  ej: ゲームばかりしている。No hace más que jugar videojuegos.
Comparación: だけ (neutro) vs しか (insuficiencia) vs ばかり (exceso/obsesión)
Coloquial: ばかり → ばっかり / ばっか en casual
Cultura: 節制と過剰 — moderation vs excess. ばかり lleva connotación crítica.
Kanjis: 限(げん/かぎる), 残(ざん/のこる), 他(た/ほか)

### Unit 17 — `17-sugiru.tex`
Chapter: `\chapter{\emoji{warning} \ruby{すぎる}{} — Demasiado}`
Vocab: 食べ過ぎ(たべすぎ), 働き過ぎ(はたらきすぎ), 飲み過ぎ(のみすぎ), 真面目すぎる(まじめすぎる), 複雑すぎる(ふくざつすぎる)
- V-stem + すぎる: 食べすぎた。
- adj-stem + すぎる: この映画は長すぎる。; 彼は真面目すぎる。
- すぎて: この料理は辛すぎて食べられない。
Comparación: すぎる (exceso negativo) vs とても/非常に (muy — solo intensificador sin juicio)
Coloquial: すぎ como sustantivo: 食べすぎ = comer en exceso; 言いすぎ = exagerar
Cultura: 過労死 — karoshi. Japanese work culture and working too much.
Kanjis: 過(か/すぎる・すごす), 労(ろう/-), 複(ふく/-)

### Unit 18 — `18-nikui-yasui.tex`
Chapter: `\chapter{\emoji{wrench} V-stem + \ruby{にくい}{}/\ruby{やすい}{} — Difícil/Fácil de hacer}`
Vocab: 滑る(すべる), 壊れる(こわれる), 使う(つかう), 理解する(りかいする), 折れる(おれる)
- V-stem + やすい: このペンは書きやすい。; この話は分かりやすい。
  また: 壊れやすい = se rompe fácilmente (tendencia negativa)
- V-stem + にくい: この字は読みにくい。; 彼とは話しにくい。
Comparación: にくい (difícil técnicamente) vs づらい (difícil emocionalmente/incómodo)
  ej: 言いにくい vs 言いづらい
Coloquial: mismas formas, uso diario natural
Cultura: ユニバーサルデザイン — universal design. やすい/にくい common in product feedback.
Kanjis: 折(せつ/おる・おれる), 滑(かつ/すべる), 壊(かい/こわす・こわれる)

### Unit 19 — `19-cambio-estado.tex`
Chapter: `\chapter{\emoji{seedling} \ruby{変化}{へんか} — Cambio de Estado: になる/くなる/にする/くする}`
Vocab: 静か(しずか), 暖かい(あたたかい), 悲しい(かなしい), 幸せ(しあわせ), 元気(げんき), 便利(べんり)
- [N/な-adj] + になる: 春になった。; 先生になりたい。
- [い-adj stem] + くなる: 暖かくなった。; 上手くなりました。
- [N/な-adj] + にする: コーヒーにします。(decidir); 部屋を静かにして。
- [い-adj stem] + くする: 部屋を暖かくした。
Comparación: になる/くなる (cambio natural) vs にする/くする (acción intencional para causar cambio)
Coloquial: 〜になってきた = ha ido convirtiéndose en... (progresivo)
Cultura: 変化の表現 — expressing change (seasons, life stages, relationships)
Kanjis: 暖(だん/あたたかい), 静(せい/しずか), 幸(こう/しあわせ)

### Unit 20 — `20-clausulas-relativas.tex`
Chapter: `\chapter{\emoji{chain} \ruby{関係節}{かんけいせつ} — Cláusulas Relativas Avanzadas}`
Vocab: 事件(じけん), 原因(げんいん), 場所(ばしょ), 理由(りゆう), 方法(ほうほう), 人物(じんぶつ)
- Modificar sustantivo con cláusula verbal:
  ej: 私が読んだ本はとても面白かった。
  ej: 彼女が作ったケーキを食べた。
- Cláusulas relativas complejas (lugar, tiempo, razón):
  ej: 田中さんに会った場所に行きたい。
  ej: 子供が生まれた日を忘れられない。
- Cláusulas nominalizadas con の/こと:
  ej: 彼が来なかったのは残念だ。
Comparación: cláusula relativa simple (昨日読んだ本) vs cláusula nominalizada con の/こと
Coloquial: misma estructura; formas casuales en predicado final
Cultura: SOV構造 — SOV word order and its effect on relative clause placement (pre-nominal)
Kanjis: 原(げん/もと), 因(いん/よる), 理(り/-), 由(ゆう/よし)

- [ ] **Compile and commit units 16–20**

```powershell
lualatex ApuntesJaponesPart_2.tex
git add Parte2/unidades/16-dake-shika-bakari.tex Parte2/unidades/17-sugiru.tex Parte2/unidades/18-nikui-yasui.tex Parte2/unidades/19-cambio-estado.tex Parte2/unidades/20-clausulas-relativas.tex
git commit -m "feat(u16-20): だけ/しか/ばかり, すぎる, にくい/やすい, cambio estado, cláusulas relativas"
```

---

## Task 11: Units 21–24 (condicionales)

### Unit 21 — `21-condicional-tara.tex`
Chapter: `\chapter{\emoji{if} \ruby{たら条件}{たらじょうけん} — Condicional たら}`
Vocab: 当たる(あたる), 宝くじ(たからくじ), 卒業する(そつぎょうする), 戻る(もどる), 気づく(きづく)
- Formación: [V-past] + ら
- Usos: (1) secuencia (家に着いたら電話します), (2) hipótesis con もし (もし当たったら), (3) descubrimiento (開けたら手紙があった)
- ej: 家に着いたら電話します。; もし宝くじが当たったら旅行します。
Comparación: たら (secuencia/hipótesis — evento completado desencadena resultado) vs と (automático/inevitable)
Coloquial: たら es el condicional más frecuente en habla casual
Cultura: もし〜たら — hypothetical daydreaming in small talk
Kanjis: 当(とう/あたる), 卒(そつ/-), 業(ぎょう/-)

### Unit 22 — `22-condicional-ba.tex`
Chapter: `\chapter{\emoji{scales} \ruby{ば条件}{ばじょうけん} — Condicional ば}`
Vocab: 早起き(はやおき), 規則(きそく), 節約する(せつやくする), 解決する(かいけつする), 成功する(せいこうする)
- Formación: G1 final u→eba; G2 ru→reba; G3 sureba, kureba
  Adj-i: stem + ければ; adj-na: ならば; N: ならば
- ej: 勉強すれば合格できる。; 早く起きれば電車に乗れる。
- 〜ばよかった (arrepentimiento): もっと早く来ればよかった。
Comparación: ば (general/hipotético — proverbios y verdades generales) vs たら (eventos específicos secuenciales)
Coloquial: ばよかった muy frecuente para arrepentimiento
Cultura: 諺とばの形 — Japanese proverbs use ば: 急がば回れ。
Kanjis: 規(き/-), 則(そく/のり), 成(せい/なる・なす), 功(こう/-)

### Unit 23 — `23-condicional-nara.tex`
Chapter: `\chapter{\emoji{ear} \ruby{なら条件}{ならじょうけん} — Condicional なら}`
Vocab: アドバイス, 場合(ばあい), 相談(そうだん), 選ぶ(えらぶ), 提案(ていあん), 判断(はんだん)
- [N/plain form] + なら — dado que (basado en info recibida/asumida)
- ej: 日本に行くなら、富士山を見てください。
- ej: A: 明日試験があります。B: 試験があるなら、今日勉強したほうがいい。
- なら responde a información del interlocutor → consejos/sugerencias
Comparación: なら (situación ya dada → consejo/respuesta) vs たら (después de que ocurra) vs と (resultado automático)
Coloquial: 〜なら muy natural para dar consejos en respuesta a problemas
Cultura: 相談文化 — consultation culture. なら used when responding to someone's stated situation.
Kanjis: 相(そう/あい), 談(だん/-), 提(てい/さげる), 案(あん/-)

### Unit 24 — `24-condicional-to.tex`
Chapter: `\chapter{\emoji{arrows-clockwise} \ruby{と条件}{とじょうけん} — Condicional と (Automático)}`
Vocab: 押す(おす), 回す(まわす), 引く(ひく), 曲がる(まがる), 溶ける(とける), 自動的(じどうてき)
- [V-dict / adj] + と — resultado natural/automático invariable
- ej: このボタンを押すと電気がつく。; 春になると花が咲く。
- Usos: (1) hechos científicos/naturales, (2) instrucciones de dirección, (3) resultados habituales automáticos
- NO se usa con verbos volitivos en la cláusula resultado: ✗ 行くとしましょう
Comparación: と (automático — sin voluntad) vs たら (secuencial/hipotético — puede tener resultado volitivo)
Coloquial: natural para direcciones y explicar cómo funcionan cosas
Cultura: 道案内の文化 — giving directions in Japan. と is the standard conditional for this.
Kanjis: 押(おう/おす), 引(いん/ひく), 曲(きょく/まがる・まげる)

- [ ] **Compile and commit units 21–24**

```powershell
lualatex ApuntesJaponesPart_2.tex
git add Parte2/unidades/21-condicional-tara.tex Parte2/unidades/22-condicional-ba.tex Parte2/unidades/23-condicional-nara.tex Parte2/unidades/24-condicional-to.tex
git commit -m "feat(u21-24): condicionales たら, ば, なら, と"
```

---

## Task 12: Units 25–30 (opinión, citar, conjunciones, keigo)

### Unit 25 — `25-expresar-opinion.tex`
Chapter: `\chapter{\emoji{thought-balloon} \ruby{意見}{いけん} — Expresar Opinión}`
Vocab: 意見(いけん), 考え(かんがえ), 感想(かんそう), 判断(はんだん), 批判(ひはん), 主張(しゅちょう)
- 〜と思う (opinión/conjetura): [plain] + と思う ej: 明日は晴れると思います。
- 〜と考える (juicio intelectual deliberado — más formal): ej: この問題は難しいと考えます。
- 〜と感じる (sentimiento personal): ej: 日本語は美しいと感じています。
Comparación: と思う (opinión/suposición general) vs と考える (juicio deliberado) vs と感じる (sentimiento emocional)
Coloquial: 〜って思う / 〜と思う (ya casual); 〜じゃない？ para opinión
Cultura: 意見の言い方 — indirect opinion expression. と思います softens assertions.
Kanjis: 意(い/-), 見(けん/みる), 感(かん/かんじる), 想(そう/-)

### Unit 26 — `26-citar-reportar.tex`
Chapter: `\chapter{\emoji{newspaper} \ruby{引用}{いんよう}/\ruby{報告}{ほうこく} — Citar y Reportar}`
Vocab: 発表(はっぴょう), 報道(ほうどう), 伝える(つたえる), 引用(いんよう), 専門家(せんもんか), 確認(かくにん)
- という: nominalizar o introducir contenido: 「〜」という言葉; 〜ということを知っていましたか。
- といわれている: se dice que (formal/generalizado): 日本は安全だといわれています。
- とのことだ: información transmitida (formal): 部長は来週不在とのことです。
Comparación: そうだ (hearsay casual) vs といわれている (widely said — formal) vs とのことだ (transmitted formal)
Coloquial: 〜って言ってた en casual: 田中さんが来るって言ってた。
Cultura: 情報の伝達 — conveying information in Japanese. Reporting vs direct quotation in business.
Kanjis: 報(ほう/むくいる), 道(どう/みち), 伝(でん/つたえる)

### Unit 27 — `27-conjunciones-contraste.tex`
Chapter: `\chapter{\emoji{arrows-left-right} \ruby{逆接}{ぎゃくせつ} — Conjunciones de Contraste}`
Vocab: 予想(よそう), 意外(いがい), 逆(ぎゃく), 反対(はんたい), 矛盾(むじゅん), 期待(きたい)
- けれども/けれど/けど: espectro formal→casual; ej: 雨が降っています。けれど、出かけます。
- ところが: resultado inesperado/contrario; ej: 準備した。ところが、試験は中止になった。
- それに: además/por si fuera poco; ej: 高いです。それに、不便です。
Comparación: けれども (contraste general) vs ところが (resultado sorprendente — elemento de sorpresa) vs しかし (contraste formal)
Coloquial: けど (muy frecuente); でも (también muy frecuente)
Cultura: 婉曲な断り方 — indirect refusal in Japanese using けど: 行きたいんですが...
Kanjis: 予(よ/-), 想(そう/おもう), 逆(ぎゃく/さか)

### Unit 28 — `28-conjunciones-causales.tex`
Chapter: `\chapter{\emoji{chain-link} \ruby{因果}{いんが} — Conjunciones Causales Formales}`
Vocab: 対策(たいさく), 実施する(じっしする), 影響(えいきょう), 改善(かいぜん), 原因(げんいん), 結果(けっか)
- そのため: [causa] + そのため + [resultado] — formal escrito; ej: 台風が来た。そのため、イベントは中止になった。
- したがって: consecuentemente — formal/escrito; ej: 証拠がある。したがって、彼は有罪です。
- その結果: como resultado; ej: 毎日練習した。その結果、上達した。
Comparación: そのため (formal — por lo tanto) vs だから (casual — así que) vs ので (cláusula causa — dentro de oración)
Coloquial: だから y ので en habla diaria; そのため/したがって en escritura/reportes
Cultura: ビジネス日本語 — business Japanese. Reports and presentations use these formal connectors.
Kanjis: 実(じつ/みのる), 施(し/ほどこす), 影(えい/かげ), 響(きょう/ひびく)

### Unit 29 — `29-keigo-sonkeigo.tex`
Chapter: `\chapter{\emoji{bowing-man} \ruby{尊敬語}{そんけいご} — Lenguaje de Respeto}`
Vocab: いらっしゃる, おっしゃる, なさる, めしあがる, ご覧になる(ごらんになる), ご存知(ごぞんじ)
- お/ご + V-stem + になる: ej: 先生がお帰りになりました。
- Verbos especiales: いる/行く/来る→いらっしゃる; 言う→おっしゃる; する→なさる; 食べる/飲む→めしあがる; 知っている→ご存知だ
  ej: 先生はいらっしゃいますか？; 何をなさっていますか？
Comparación: 尊敬語 (respeto — sobre acciones del superior) vs 謙譲語 (humildad — sobre acciones propias)
Coloquial: Keigo no se simplifica en casual — se usa o no se usa (code switching)
Cultura: 敬語の必要性 — when keigo is required: business, customers, teachers, seniors.
Kanjis: 尊(そん/とうとい), 敬(けい/うやまう), 謙(けん/-), 語(ご/かたる)

### Unit 30 — `30-keigo-kenjogo.tex`
Chapter: `\chapter{\emoji{folded-hands} \ruby{謙譲語}{けんじょうご} — Lenguaje de Humildad}`
Vocab: 申す(もうす), いたす, 参る(まいる), いただく, 拝見する(はいけんする), 存じる(ぞんじる)
- お/ご + V-stem + する: ej: 明日お電話します。; ご案内します。
- Verbos especiales: いる→おる; 行く/来る→参る; 言う→申す; する→いたす; もらう/食べる/飲む→いただく; 見る→拝見する; 知っている→存じる
  ej: 私も存じておりません。; 資料を拝見しました。; 私が田中と申します。
Comparación: 謙譲語 (humillar propio yo) vs 丁寧語 (neutral — です/ます)
Coloquial: Usado en contextos profesionales; con profesores y mayores
Cultura: お客様は神様 — «el cliente es dios». How 謙譲語 is central to service industry.
Kanjis: 申(しん/もうす), 参(さん/まいる), 拝(はい/おがむ)

- [ ] **Compile and commit units 25–30**

```powershell
lualatex ApuntesJaponesPart_2.tex
git add Parte2/unidades/25-expresar-opinion.tex Parte2/unidades/26-citar-reportar.tex Parte2/unidades/27-conjunciones-contraste.tex Parte2/unidades/28-conjunciones-causales.tex Parte2/unidades/29-keigo-sonkeigo.tex Parte2/unidades/30-keigo-kenjogo.tex
git commit -m "feat(u25-30): opinión, citar, conjunciones, keigo 尊敬語/謙譲語"
```

---

## Task 13: Units 31–35 (registro, coloquial, contadores, lectura, repaso)

### Unit 31 — `31-escrito-vs-hablado.tex`
Chapter: `\chapter{\emoji{memo} \ruby{書き言葉}{かきことば} vs \ruby{話し言葉}{はなしことば}}`
Vocab: 文語(ぶんご), 口語(こうご), 省略(しょうりゃく), 縮約形(しゅくやくけい), 文体(ぶんたい), 助詞(じょし)
- Contracciones orales: ている→てる, てしまう→ちゃう, ておく→とく, のだ→んだ
- Partículas: は/が/を frecuentemente omitidas en habla; な en vez de ない en prohibición casual
- Registros: である体 (formal escrito) vs です・ます体 (polite) vs だ体 (casual)
Comparación: formal written (〜ではない) vs casual spoken (〜じゃない); 〜ている vs 〜てる
Coloquial: Esta unidad DOCUMENTA las formas coloquiales — es la comparación misma
Cultura: SNS日本語 — cómo la escritura japonesa cambia en redes sociales mezclando patrones orales
Kanjis: 語(ご/かたる), 体(たい/からだ), 省(しょう/はぶく)

### Unit 32 — `32-expresiones-coloquiales.tex`
Chapter: `\chapter{\emoji{speech-balloon} \ruby{若者言葉}{わかものことば} — Expresiones Coloquiales N3}`
Vocab: むかつく(irritar), うざい(molesto/pesado), やばい(increíble/terrible), まじで(en serio), ガチ(de verdad), なんか(como que/algo)
- なんか: filler — なんか、よくわからないんだよね。
- てか: o más bien / de todos modos — てか、それどういう意味？
- 〜じゃん: ¿verdad? / ¡claro que sí! — これ面白いじゃん！
- 〜でしょ: ¿verdad? casual — わかるでしょ？
- っていうか: o sea / quiero decir — っていうか、全然違う。
- やばい: dual meaning (terrible OR amazing según contexto): やばい、遅刻する！vs この料理やばい！
Comparación: habla estándar vs expresiones de jóvenes vs slang de internet
Coloquial: Esta unidad es habla coloquial
Cultura: 若者言葉の進化 — evolution of youth language in Japan
Kanjis: 言(げん/いう), 葉(よう/は) — enfocado en vocabulario expresivo, no en kanji

### Unit 33 — `33-contadores-avanzados.tex`
Chapter: `\chapter{\emoji{abacus} \ruby{助数詞}{じょすうし} — Contadores Avanzados}`
Vocab: 本(ほん)—objetos largos, 枚(まい)—objetos planos, 台(だい)—máquinas, 匹(ひき)—animales pequeños, 冊(さつ)—libros encuadernados, 杯(はい)—vasos/tazas, 着(ちゃく)—ropa, 足(そく)—calzado
- Lecturas irregulares: 1本=いっぽん, 3本=さんぼん, 6本=ろっぽん; 1匹=いっぴき, 3匹=さんびき; 1杯=いっぱい, 3杯=さんばい
- Tabla completa en el apéndice de conjugación
  ej: えんぴつを3本ください。; 犬を2匹飼っています。; ビールを一杯お願いします。
Comparación: 〜個(こ) contador general vs contadores específicos
Coloquial: いくつ (¿cuántos? — informal); 何本？何枚？ (formal counting questions)
Cultura: 助数詞の文化 — abundance of Japanese counters reflects how Japanese categorizes objects
Kanjis: 枚(まい/-), 匹(ひき/-), 冊(さつ/-), 杯(はい/-)

### Unit 34 — `34-lectura-n3.tex`
Chapter: `\chapter{\emoji{open-book} \ruby{読解}{どっかい} — Estrategias de Lectura N3}`
Vocab: 段落(だんらく), 文脈(ぶんみゃく), 推測する(すいそくする), 接続詞(せつぞくし), 要約する(ようやくする), 主題(しゅだい)
- Estrategia 1: Usar conectores para entender flujo (だから/しかし/そのため/ところが)
- Estrategia 2: Identificar oración temática (usualmente primera o última del párrafo)
- Estrategia 3: Usar contexto para adivinar vocabulario desconocido
- Estrategia 4: は vs が para encontrar el foco de la oración
- Texto de práctica N3 (100-150 caracteres): texto sobre tema social (ej: 環境問題、SNSの影響)
Comparación: 精読 (lectura intensiva) vs 速読 (skimming/lectura extensiva)
Coloquial: N/A — unidad de estrategias
Cultura: 日本の新聞 — Japanese newspaper style. NHK Easy News como recurso de aprendizaje.
Kanjis: 段(だん/-), 落(らく/おちる), 脈(みゃく/-), 推(すい/おす)

### Unit 35 — `35-repaso-general.tex`
Chapter: `\chapter{\emoji{checkered-flag} \ruby{総復習}{そうふくしゅう} — Repaso General N4→N3}`

Esta unidad es un repaso integrador. Contiene:
1. Tabla resumen: pasiva/causativa/causativa-pasiva (todos los grupos)
2. Tabla comparativa de condicionales: たら/ば/なら/と
3. Referencia rápida de evidencialidad: そうだ/らしい/ようだ/はずだ/わけだ
4. Tabla de verbos keigo (尊敬語/謙譲語) más comunes
5. Texto de lectura integrador (150-200 caracteres) usando múltiples patrones
6. Ejercicios integradores que mezclan todos los patrones
No añadir vocabbox nueva — referenciar lo aprendido. No añadir kanjibox — usar tabla resumen en su lugar.

- [ ] **Compile and commit units 31–35**

```powershell
lualatex ApuntesJaponesPart_2.tex
git add Parte2/unidades/31-escrito-vs-hablado.tex Parte2/unidades/32-expresiones-coloquiales.tex Parte2/unidades/33-contadores-avanzados.tex Parte2/unidades/34-lectura-n3.tex Parte2/unidades/35-repaso-general.tex
git commit -m "feat(u31-35): escrito/hablado, coloquial, contadores, lectura, repaso general"
```

---

## Task 14: Appendices (4 files)

### Appendix A — `apendices/conjugacion-n4-n3.tex`

```latex
\chapter{Tablas de Conjugación N4-N3}
```

Incluir tablas completas en tabularx para:
1. Voz pasiva — G1/G2/G3
2. Forma causativa — G1/G2/G3
3. Causativa-pasiva — G1/G2/G3 (forma larga y corta)
4. Forma potencial — G1/G2/G3
Formato: 5 columnas: Diccionario | て-form | Pasiva | Causativa | Caus-Pas.

### Appendix B — `apendices/patrones-confusos.tex`

```latex
\chapter{Comparación de Patrones Confusos}
```

Incluir sección por cada par problemático:
- たら vs ば vs なら vs と (tabla comparativa)
- こと vs の (cuándo usar cada uno)
- そうだ vs らしい vs ようだ vs はずだ vs わけだ
- ために vs ように
- にくい vs づらい
- だけ vs しか vs ばかり
Cada sección: breve explicación + 2 ejemplos contrastivos

### Appendix C — `apendices/indice-kanjis-n4-n3.tex`

```latex
\chapter{Índice de Kanjis N4-N3}
```

Lista todos los kanjis presentados en las 35 unidades en orden de aparición. Formato kanjibox:
kanji | on | kun | significado | vocabulario de ejemplo
Organizado por unidad.

### Appendix D — `apendices/referencia-keigo.tex`

```latex
\chapter{Referencia Keigo}
```

Tabla completa en tabularx (4 columnas): Significado | Común (丁寧語) | 尊敬語 | 謙譲語

| Significado | 丁寧語 | 尊敬語 | 謙譲語 |
|---|---|---|---|
| ser/estar | います | いらっしゃいます | おります |
| ir/venir | 行きます/来ます | いらっしゃいます | 参ります |
| decir | 言います | おっしゃいます | 申します |
| hacer | します | なさいます | いたします |
| comer/beber | 食べます/飲みます | めしあがります | いただきます |
| ver | 見ます | ご覧になります | 拝見します |
| saber | 知っています | ご存知です | 存じております |
| recibir | もらいます | — | いただきます |
| dar | あげます | — | 差し上げます |
| dar (a mí) | くれます | くださいます | — |

- [ ] **Compile and commit appendices**

```powershell
lualatex ApuntesJaponesPart_2.tex
lualatex ApuntesJaponesPart_2.tex
git add Parte2/apendices/
git commit -m "feat: add 4 appendices — conjugation tables, pattern comparison, kanji index, keigo reference"
```

---

## Task 15: Final compilation and cleanup

- [ ] **Step 1: Full double-compile**

```powershell
cd "D:\Codigo Abierto\ApuntesJapones\Parte2"
lualatex ApuntesJaponesPart_2.tex
lualatex ApuntesJaponesPart_2.tex
```

Expected: clean compile, PDF with complete TOC, all 35 units + 4 appendices.

- [ ] **Step 2: Add .gitignore for LaTeX artifacts**

Add to `Parte2/.gitignore`:
```
*.aux
*.log
*.out
*.toc
*.fls
*.fdb_latexmk
*.synctex.gz
```

- [ ] **Step 3: Add README to Parte2/**

Create `Parte2/README.md`:
```markdown
# ApuntesJapones — Parte 2 (N4→N3)

35-unit intermediate Japanese notes. Compile with LuaLaTeX (run twice for TOC).

**Requirements:** MiKTeX + HaranoAji fonts + emoji package

**Compile:**
lualatex ApuntesJaponesPart_2.tex
lualatex ApuntesJaponesPart_2.tex
```

- [ ] **Step 4: Final commit and push**

```powershell
git add Parte2/.gitignore Parte2/README.md
git commit -m "chore: add Parte2 gitignore and README"
git push origin main
```

---

## Execution Options

Plan complete and saved to `docs/plans/2026-05-19-apuntes-japones-parte2.md`.

**1. Subagent-Driven (recommended)** — fresh subagent per task, review between tasks

**2. Inline Execution** — execute tasks in this session using executing-plans skill

Which approach?
