# Japanese Notes N5→N4 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build 30-unit Japanese study notes in LuaLaTeX covering N5→N4 grammar, vocabulary, kanji, and communication patterns, compiled to a styled PDF with furigana and emoji.

**Architecture:** Multi-file LuaLaTeX project. `preamble.tex` defines all packages and custom commands. `main.tex` assembles 30 unit files + 3 appendices via `\input`. Each unit follows a fixed structure: vocabulary table → key phrases → grammar patterns → exercises → kanji review. Custom tcolorbox environments provide consistent visual styling.

**Tech Stack:** LuaLaTeX, ltjsbook (luatexja), luatexja-ruby (furigana), luatexja-fontspec, tcolorbox, booktabs, tabularx, hyperref, geometry, titlesec, xcolor, emoji

---

## Phase 1: Infrastructure

### Task 1: Initialize project + git

**Files:**
- Create: `D:\Codigo Abierto\ApuntesJapones\` (root)
- Create: `.gitignore`
- Create: `README.md`
- Create: dirs `unidades/`, `apendices/`, `assets/img/`

- [ ] **Step 1: Create directory structure**

```powershell
cd "D:\Codigo Abierto\ApuntesJapones"
New-Item -ItemType Directory -Force unidades, apendices, "assets\img"
```

- [ ] **Step 2: Create .gitignore**

```
*.aux
*.log
*.out
*.toc
*.synctex.gz
*.fls
*.fdb_latexmk
*.bcf
*.blg
*.bbl
*.run.xml
```

- [ ] **Step 3: Create README.md**

```markdown
# 📚 Apuntes de Japonés N5→N4

Apuntes personales de japonés en LaTeX. 30 unidades, nivel N5→N4.

## Compilar

Requiere LuaLaTeX (MiKTeX):

```powershell
lualatex main.tex
lualatex main.tex
```

El PDF se genera como `main.pdf`.

## Fuentes

Basado en **Minna no Nihongo** y **Marugoto**.
```

- [ ] **Step 4: Git init + remote + first commit**

```powershell
git init
git remote add origin https://github.com/AldoZM/ApuntesJapones.git
git add .gitignore README.md
git commit -m "chore: init project"
git branch -M main
git push -u origin main
```

---

### Task 2: Create preamble.tex

**Files:**
- Create: `preamble.tex`

- [ ] **Step 1: Write preamble.tex**

```latex
% preamble.tex
\usepackage{luatexja}
\usepackage{luatexja-ruby}
\usepackage[match,deluxe]{luatexja-fontspec}

% === Fuentes japonesas (Windows 10 fonts) ===
\setmainjfont{Yu Mincho}[BoldFont=Yu Gothic Bold]
\setsansjfont{Yu Gothic}

% === Fuentes latinas ===
\setmainfont{Georgia}
\setsansfont{Calibri}

% === Emoji ===
% Instalar via MiKTeX Package Manager: "emoji"
\usepackage{emoji}
% Si emoji package no disponible, comentar la línea anterior
% y usar: \newcommand{\emoji}[1]{#1}

% === Colores ===
\usepackage{xcolor}
\definecolor{jpred}{HTML}{BC002D}
\definecolor{jpblue}{HTML}{1A3A6B}
\definecolor{jpgold}{HTML}{C8A951}
\definecolor{sakura}{HTML}{FFB7C5}
\definecolor{lightgray}{HTML}{F7F7F7}
\definecolor{darkgray}{HTML}{555555}
\definecolor{softgreen}{HTML}{D4EDDA}

% === Diseño de página ===
\usepackage[a4paper, top=2.5cm, bottom=2.5cm, left=3cm, right=3cm]{geometry}

% === Tablas ===
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{array}
\usepackage{longtable}

% === tcolorbox ===
\usepackage[most]{tcolorbox}
\tcbuselibrary{skins, breakable}

\tcbset{
  vocabbox/.style={
    enhanced, breakable,
    colback=lightgray, colframe=jpblue,
    coltitle=white, fonttitle=\bfseries\large,
    attach boxed title to top left={yshift=-2mm, xshift=5mm},
    boxed title style={colback=jpblue, rounded corners},
    rounded corners
  },
  grammarbox/.style={
    enhanced, breakable,
    colback=white, colframe=jpred,
    coltitle=white, fonttitle=\bfseries\large,
    attach boxed title to top left={yshift=-2mm, xshift=5mm},
    boxed title style={colback=jpred, rounded corners},
    rounded corners
  },
  phrasebox/.style={
    enhanced,
    colback=sakura!15, colframe=sakura!80!black,
    rounded corners, fonttitle=\bfseries
  },
  kanjibox/.style={
    enhanced, breakable,
    colback=jpgold!8, colframe=jpgold!70!black,
    coltitle=white, fonttitle=\bfseries\large,
    attach boxed title to top left={yshift=-2mm, xshift=5mm},
    boxed title style={colback=jpgold!70!black, rounded corners},
    rounded corners
  },
  ejerciciobox/.style={
    enhanced,
    colback=softgreen!50, colframe=softgreen!80!black,
    rounded corners, fonttitle=\bfseries,
    coltitle=darkgray
  }
}

% === Hyperref ===
\usepackage{hyperref}
\hypersetup{
  colorlinks=true,
  linkcolor=jpblue,
  urlcolor=jpred,
  pdftitle={Apuntes de Japonés N5-N4},
  pdfauthor={Aldo ZM}
}

% === Títulos ===
\usepackage{titlesec}

\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries\color{jpred}}{}
  {0pt}{\huge}
  [\vspace{0.3em}\color{jpred}\hrule height 1.5pt\vspace{0.3em}]

\titleformat{\section}
  {\large\bfseries\color{jpblue}}{}
  {0em}{}
  [\vspace{0.1em}\color{jpblue!40}\hrule height 0.4pt]

\titleformat{\subsection}
  {\normalsize\bfseries\color{darkgray}}{}
  {0em}{}

% =============================================
% COMANDOS CUSTOM
% =============================================

% Encabezado visual de unidad
% #1=número, #2=kanji título, #3=título español, #4=tema comunicativo
\newcommand{\unidadheader}[4]{%
  \begin{tcolorbox}[
    enhanced, colback=jpred!5, colframe=jpred,
    coltitle=white, fonttitle=\bfseries\Large,
    title={🎌 Unidad #1 \enspace \ruby{#2}{} \enspace #3},
    attach boxed title to top center={yshift=-3mm},
    boxed title style={colback=jpred, rounded corners}
  ]
  \textit{\textcolor{jpblue}{🗣️ Tema comunicativo: #4}}
  \end{tcolorbox}
  \vspace{0.5em}
}

% Entrada de vocabulario
% #1=kanji+kana, #2=furigana, #3=español, #4=tipo gramatical
\newcommand{\vocabitem}[4]{%
  \ruby{#1}{#2} & #3 & \textcolor{darkgray}{\small\textit{#4}} \\[4pt]
}

% Patrón gramatical
% #1=nombre patrón, #2=fórmula, #3=explicación+ejemplos
\newcommand{\patron}[3]{%
  \begin{tcolorbox}[grammarbox, title={⚙️ #1}]
  \begin{center}{\Large\textbf{#2}}\end{center}
  \vspace{0.3em}
  #3
  \end{tcolorbox}
}

% Ejemplo dentro de patrón
% #1=japonés (con ruby), #2=español
\newcommand{\ej}[2]{%
  \par\vspace{0.2em}
  \hspace{1em}▶ #1 \hfill {\small\textit{#2}}
  \vspace{0.1em}
}

% Frase clave
% #1=japonés, #2=español
\newcommand{\frase}[2]{%
  \begin{tcolorbox}[phrasebox]
  \textbf{#1}\\[2pt]
  {\small\textit{#2}}
  \end{tcolorbox}
  \vspace{0.2em}
}

% Entrada de kanji en tabla
% #1=kanji, #2=lecturas on, #3=lecturas kun, #4=significado, #5=vocab ejemplo (con ruby)
\newcommand{\kanjirow}[5]{%
  {\LARGE #1} & #2 & #3 & #4 & #5 \\[4pt]
}
```

- [ ] **Step 2: Commit**

```bash
git add preamble.tex
git commit -m "chore: add LaTeX preamble with packages and custom commands"
```

---

### Task 3: Create main.tex

**Files:**
- Create: `main.tex`

- [ ] **Step 1: Write main.tex**

```latex
\documentclass[12pt, a4paper, openany]{ltjsbook}
\input{preamble}

\begin{document}

\input{assets/portada}

\frontmatter
\tableofcontents

\mainmatter

% ===== UNIDADES =====
\input{unidades/01-presentaciones}
\input{unidades/02-numeros-tiempo}
\input{unidades/03-kosoado}
\input{unidades/04-lugares-direcciones}
\input{unidades/05-rutina-diaria}
\input{unidades/06-gustos-preferencias}
\input{unidades/07-comida-restaurante}
\input{unidades/08-compras}
\input{unidades/09-adjetivos}
\input{unidades/10-familia}
\input{unidades/11-pasado}
\input{unidades/12-clima-estaciones}
\input{unidades/13-te-form-1}
\input{unidades/14-te-form-2}
\input{unidades/15-te-iru}
\input{unidades/16-experiencias}
\input{unidades/17-planes-citas}
\input{unidades/18-comparaciones}
\input{unidades/19-transporte}
\input{unidades/20-cuerpo-salud}
\input{unidades/21-forma-potencial}
\input{unidades/22-deseos}
\input{unidades/23-dar-recibir}
\input{unidades/24-forma-casual}
\input{unidades/25-opinar-citar}
\input{unidades/26-condicional-1}
\input{unidades/27-condicional-2}
\input{unidades/28-voz-pasiva}
\input{unidades/29-keigo-intro}
\input{unidades/30-repaso-general}

% ===== APÉNDICES =====
\backmatter
\appendix
\input{apendices/mapa-particulas}
\input{apendices/tablas-conjugacion}
\input{apendices/indice-kanjis}

\end{document}
```

- [ ] **Step 2: Commit**

```bash
git add main.tex
git commit -m "chore: add main.tex document root"
```

---

### Task 4: Create assets/portada.tex

**Files:**
- Create: `assets/portada.tex`

- [ ] **Step 1: Write assets/portada.tex**

```latex
% assets/portada.tex
\begin{titlepage}
  \begin{center}
    \vspace*{1.5cm}
    {\color{jpred}\rule{\linewidth}{3pt}}
    \vspace{1cm}

    {\fontsize{60}{70}\selectfont 🇯🇵}

    \vspace{0.5cm}
    {\Huge\bfseries\color{jpred} 日本語ノート}

    \vspace{0.3cm}
    {\Large\color{jpblue} \ruby{日本語}{にほんご}の\ruby{勉強}{べんきょう}ノート}

    \vspace{0.5cm}
    {\large Apuntes de Japonés} \\[0.3em]
    {\large\color{darkgray} Nivel N5 → N4}

    \vspace{1cm}
    \begin{tcolorbox}[
      width=0.65\linewidth,
      colback=jpgold!10, colframe=jpgold!70!black,
      rounded corners, halign=center
    ]
    \large
    📚 30 Unidades \\[4pt]
    🀄 Kanjis N5--N4 \\[4pt]
    🗣️ Comunicación Real \\[4pt]
    ⚙️ Gramática Progresiva
    \end{tcolorbox}

    \vspace{1cm}
    {\large Aldo ZM} \\[0.3em]
    {\small\color{darkgray}\url{https://github.com/AldoZM/ApuntesJapones}}

    \vfill
    {\color{jpred}\rule{\linewidth}{3pt}}
    {\small\color{darkgray} Basado en Minna no Nihongo \& Marugoto}
  \end{center}
\end{titlepage}
```

- [ ] **Step 2: Commit**

```bash
git add assets/portada.tex
git commit -m "content: add cover page"
```

---

## Phase 2: Unidades N5 Básico (01–10)

### Task 5: Unidad 01 — Presentaciones

**Files:**
- Create: `unidades/01-presentaciones.tex`

- [ ] **Step 1: Write unidades/01-presentaciones.tex**

```latex
% unidades/01-presentaciones.tex
\chapter{🎌 自己紹介 — Presentaciones}
\unidadheader{01}{自己紹介}{Presentaciones}{Conocer a alguien por primera vez}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{名前}{なまえ}{nombre}{sust.}
\vocabitem{学生}{がくせい}{estudiante}{sust.}
\vocabitem{先生}{せんせい}{maestro / profesor}{sust.}
\vocabitem{会社員}{かいしゃいん}{empleado de empresa}{sust.}
\vocabitem{〜人}{じん}{persona de [país]}{sufijo}
\vocabitem{〜語}{ご}{idioma de [país]}{sufijo}
\vocabitem{〜歳}{さい}{años de edad}{sufijo}
\vocabitem{友だち}{ともだち}{amigo/a}{sust.}
\vocabitem{国}{くに}{país}{sust.}
\vocabitem{仕事}{しごと}{trabajo / ocupación}{sust.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{はじめまして。}{Mucho gusto. (al conocer a alguien)}
\frase{\ruby{私}{わたし}は〜と\ruby{申}{もう}します。}
  {Me llamo ~. (formal)}
\frase{どうぞよろしくお\ruby{願}{ねが}いします。}
  {Encantado/a de conocerle.}
\frase{お\ruby{名前}{なまえ}は\ruby{何}{なん}ですか？}
  {¿Cuál es su nombre?}
\frase{〜から\ruby{来}{き}ました。}
  {Vengo de ~ / Soy de ~.}

\subsection*{⚙️ Gramática}

\patron{Afirmación: ser / identificar}
  {〜は〜です}
  {\ruby{私}{わたし}はアルドです。
  \ej{\ruby{私}{わたし}は\ruby{学生}{がくせい}です。}{Soy estudiante.}
  \ej{\ruby{田中}{たなか}さんは\ruby{先生}{せんせい}です。}{El Sr. Tanaka es maestro.}}

\patron{Negación: no ser}
  {〜じゃありません \quad / \quad 〜ではありません}
  {じゃありません = informal \quad | \quad ではありません = formal
  \ej{\ruby{私}{わたし}は\ruby{会社員}{かいしゃいん}じゃありません。}{No soy empleado de empresa.}}

\patron{También: igual categoría}
  {〜も〜です}
  {\ej{\ruby{田中}{たなか}さんも\ruby{学生}{がくせい}です。}{El Sr. Tanaka también es estudiante.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item ¿Cómo te presentas en japonés? (Di tu nombre con はじめまして)
  \item Traduce: \ruby{私}{わたし}はメキシコ\ruby{人}{じん}です。
  \item Niega la siguiente oración: \ruby{田中}{たなか}さんは\ruby{学生}{がくせい}です。
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) はじめまして。[nombre]と申します。どうぞよろしく。\quad
2) Soy mexicano/a.\quad
3) \ruby{田中}{たなか}さんは\ruby{学生}{がくせい}じゃありません。
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{名}{めい・みょう}{な}{nombre}{\ruby{名前}{なまえ} / \ruby{名刺}{めいし}}
\kanjirow{前}{ぜん}{まえ}{frente / antes}{\ruby{名前}{なまえ} / \ruby{前}{まえ}}
\kanjirow{学}{がく}{まな}{estudiar / aprender}{\ruby{学生}{がくせい} / \ruby{学校}{がっこう}}
\kanjirow{生}{せい・しょう}{い・う}{vida / nacer}{\ruby{先生}{せんせい} / \ruby{学生}{がくせい}}
\kanjirow{先}{せん}{さき}{antes / punta}{\ruby{先生}{せんせい} / \ruby{先}{さき}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Test partial compile**

```powershell
cd "D:\Codigo Abierto\ApuntesJapones"
lualatex -interaction=batchmode main.tex
```
Expected: Compiles (other units not yet present — comment them out in main.tex temporarily, or create stub files).

- [ ] **Step 3: Commit**

```bash
git add unidades/01-presentaciones.tex
git commit -m "content: add unidad 01 - presentaciones"
```

---

### Task 6: Unidad 02 — Números y Tiempo

**Files:**
- Create: `unidades/02-numeros-tiempo.tex`

- [ ] **Step 1: Write unidades/02-numeros-tiempo.tex**

```latex
\chapter{🔢 数字と時間 — Números y Tiempo}
\unidadheader{02}{数字と時間}{Números y Tiempo}{Hablar de horas, fechas y precios}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{〜時}{じ}{hora ~ (ej: 三時 = 3:00)}{contador}
\vocabitem{〜分}{ふん・ぷん}{minuto ~ (ej: 五分 = 5 min)}{contador}
\vocabitem{午前}{ごぜん}{AM / mañana}{sust.}
\vocabitem{午後}{ごご}{PM / tarde}{sust.}
\vocabitem{半}{はん}{y media (30 min)}{sust.}
\vocabitem{今}{いま}{ahora}{adv.}
\vocabitem{〜年}{ねん}{año ~ (ej: 二〇二六年)}{contador}
\vocabitem{〜月}{がつ}{mes ~ (ej: 五月 = mayo)}{contador}
\vocabitem{〜日}{にち・か}{día ~ (ej: 三日 = día 3)}{contador}
\vocabitem{〜曜日}{ようび}{día de semana (月・火・水・木・金・土・日)}{sust.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\begin{tcolorbox}[phrasebox, title={🔢 Números 1–10000}]
\begin{tabular}{llllll}
一 いち & 二 に & 三 さん & 四 し/よん & 五 ご & 六 ろく \\
七 なな/しち & 八 はち & 九 く/きゅう & 十 じゅう & 百 ひゃく & 千 せん \\
\end{tabular}\\[4pt]
\small 百 (100) · 千 (1000) · 万 (10000) · 十万 (100000)
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{\ruby{今}{いま}\ruby{何時}{なんじ}ですか？}{¿Qué hora es ahora?}
\frase{\ruby{午後}{ごご}\ruby{三時}{さんじ}\ruby{半}{はん}です。}{Son las 3:30 PM.}
\frase{\ruby{今日}{きょう}は\ruby{何月何日}{なんがつなんにち}ですか？}
  {¿A qué fecha estamos hoy?}
\frase{\ruby{誕生日}{たんじょうび}はいつですか？}{¿Cuándo es tu cumpleaños?}

\subsection*{⚙️ Gramática}

\patron{Expresar hora}
  {〜時〜分です}
  {\ej{\ruby{午前}{ごぜん}\ruby{七時}{しちじ}\ruby{十五分}{じゅうごふん}です。}{Son las 7:15 AM.}
  \ej{\ruby{十二時}{じゅうにじ}\ruby{半}{はん}です。}{Son las 12:30.}}

\patron{Expresar fecha}
  {〜年〜月〜日（〜曜日）}
  {\ej{二〇二六\ruby{年}{ねん}\ruby{五月}{ごがつ}\ruby{十八日}{じゅうはちにち}\ruby{月曜日}{げつようび}です。}
  {Es lunes, 18 de mayo de 2026.}}

\patron{Desde... hasta}
  {〜から〜まで}
  {\ej{\ruby{九時}{くじ}から\ruby{五時}{ごじ}まではたらきます。}
  {Trabajo de 9 a 5.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item ¿Cómo se dice "Son las 8:45 PM"?
  \item Escribe tu fecha de cumpleaños en japonés.
  \item ¿Cuánto es 三千八百円?
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) \ruby{午後}{ごご}\ruby{八時}{はちじ}\ruby{四十五分}{よんじゅうごふん}です。\quad
2) (personal)\quad
3) 3800 yen.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{時}{じ}{とき}{tiempo / hora}{\ruby{時間}{じかん} / \ruby{何時}{なんじ}}
\kanjirow{分}{ふん・ぶん}{わ}{minuto / dividir}{\ruby{五分}{ごふん} / \ruby{半分}{はんぶん}}
\kanjirow{年}{ねん}{とし}{año}{\ruby{今年}{ことし} / \ruby{来年}{らいねん}}
\kanjirow{月}{がつ・つき}{つき}{mes / luna}{\ruby{一月}{いちがつ} / \ruby{月曜日}{げつようび}}
\kanjirow{日}{にち・じつ}{ひ・か}{día / sol}{\ruby{今日}{きょう} / \ruby{誕生日}{たんじょうび}}
\kanjirow{今}{こん・きん}{いま}{ahora / este}{\ruby{今日}{きょう} / \ruby{今}{いま}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/02-numeros-tiempo.tex
git commit -m "content: add unidad 02 - numeros y tiempo"
```

---

### Task 7: Unidad 03 — Demostrativos (こそあど)

**Files:**
- Create: `unidades/03-kosoado.tex`

- [ ] **Step 1: Write unidades/03-kosoado.tex**

```latex
\chapter{👆 これ・それ・あれ — Demostrativos}
\unidadheader{03}{これ・それ・あれ}{Demostrativos}{Señalar y preguntar por objetos y lugares}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{これ}{—}{esto (cerca del hablante)}{pron.}
\vocabitem{それ}{—}{eso (cerca del oyente)}{pron.}
\vocabitem{あれ}{—}{aquello (lejos de ambos)}{pron.}
\vocabitem{ここ}{—}{aquí}{pron. lugar}
\vocabitem{そこ}{—}{ahí}{pron. lugar}
\vocabitem{あそこ}{—}{allá}{pron. lugar}
\vocabitem{この〜}{—}{este/esta ~ (+ sust.)}{det.}
\vocabitem{どんな}{—}{qué tipo de ~}{det.}
\vocabitem{何}{なに・なん}{qué}{pron.}
\vocabitem{誰}{だれ}{quién}{pron.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\begin{tcolorbox}[phrasebox, title={🗺️ Sistema こそあど}]
\begin{tabular}{lllll}
\toprule
 & \textbf{こ (cerca)} & \textbf{そ (oyente)} & \textbf{あ (lejos)} & \textbf{ど (pregunta)} \\
\midrule
cosa & これ & それ & あれ & どれ \\
+sust. & この & その & あの & どの \\
lugar & ここ & そこ & あそこ & どこ \\
dirección & こちら & そちら & あちら & どちら \\
tipo & こんな & そんな & あんな & どんな \\
\bottomrule
\end{tabular}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{これは\ruby{何}{なん}ですか？}{¿Qué es esto?}
\frase{それは〜さんのですか？}{¿Es eso de ~san?}
\frase{\ruby{誰}{だれ}のですか？}{¿De quién es?}
\frase{あそこはどこですか？}{¿Qué lugar es aquel de allá?}

\subsection*{⚙️ Gramática}

\patron{Demostrativo + sustantivo}
  {この/その/あの/どの + 名詞}
  {\ej{この\ruby{本}{ほん}はいくらですか？}{¿Cuánto cuesta este libro?}
  \ej{あの\ruby{人}{ひと}は\ruby{誰}{だれ}ですか？}{¿Quién es aquella persona?}}

\patron{Posesión con の}
  {A の B = B de A}
  {\ej{これは\ruby{私}{わたし}の\ruby{本}{ほん}です。}{Este es mi libro.}
  \ej{\ruby{田中}{たなか}さんの\ruby{名前}{なまえ}は…}{El nombre del Sr. Tanaka es…}}

\patron{Pregunta de precio}
  {〜はいくらですか？}
  {\ej{このかばんはいくらですか？}{¿Cuánto cuesta esta bolsa?}
  \ej{\ruby{二千円}{にせんえん}です。}{Son 2000 yen.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Señala algo lejano a ambos y pregunta qué es.
  \item Completa: \_\_\_は\ruby{私}{わたし}のかばんです。(Este es mi bolso)
  \item Traduce: \ruby{誰}{だれ}のノートですか？
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) あれは\ruby{何}{なん}ですか？\quad
2) これ\quad
3) ¿De quién es este cuaderno?
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{何}{か}{なに・なん}{qué / cuánto}{\ruby{何}{なに} / \ruby{何時}{なんじ}}
\kanjirow{誰}{すい}{だれ}{quién}{\ruby{誰}{だれ} / \ruby{誰か}{だれか}}
\kanjirow{物}{ぶつ・もつ}{もの}{cosa / objeto}{\ruby{物}{もの} / \ruby{買い物}{かいもの}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/03-kosoado.tex
git commit -m "content: add unidad 03 - demostrativos kosoado"
```

---

### Task 8: Unidad 04 — Lugares y Direcciones

**Files:**
- Create: `unidades/04-lugares-direcciones.tex`

- [ ] **Step 1: Write unidades/04-lugares-direcciones.tex**

```latex
\chapter{🗺️ 場所と道案内 — Lugares y Direcciones}
\unidadheader{04}{場所と道案内}{Lugares y Direcciones}{Preguntar y dar indicaciones}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{駅}{えき}{estación (tren/metro)}{sust.}
\vocabitem{学校}{がっこう}{escuela}{sust.}
\vocabitem{病院}{びょういん}{hospital}{sust.}
\vocabitem{銀行}{ぎんこう}{banco}{sust.}
\vocabitem{図書館}{としょかん}{biblioteca}{sust.}
\vocabitem{右}{みぎ}{derecha}{sust.}
\vocabitem{左}{ひだり}{izquierda}{sust.}
\vocabitem{前}{まえ}{frente / adelante}{sust.}
\vocabitem{後ろ}{うしろ}{atrás}{sust.}
\vocabitem{近く}{ちかく}{cerca (de)}{sust./adv.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{〜はどこですか？}{¿Dónde está ~?}
\frase{〜の\ruby{近}{ちか}くにあります。}{Está cerca de ~.}
\frase{まっすぐ\ruby{行}{い}ってください。}{Vaya recto, por favor.}
\frase{\ruby{右}{みぎ}に\ruby{曲}{ま}がってください。}{Doble a la derecha, por favor.}
\frase{\ruby{二}{に}つ\ruby{目}{め}の\ruby{角}{かど}です。}{Es la segunda esquina.}

\subsection*{⚙️ Gramática}

\patron{Hay / Existe (cosas y lugares)}
  {〜が あります　／　〜がいます}
  {あります = cosas inanimadas \quad | \quad います = seres animados
  \ej{\ruby{駅}{えき}の\ruby{近}{ちか}くにコンビニがあります。}
    {Hay un convenience store cerca de la estación.}
  \ej{そこに\ruby{先生}{せんせい}がいます。}{Hay un maestro ahí.}}

\patron{Partículas de lugar}
  {〜に (existencia)　／　〜で (acción)　／　〜へ・に (dirección)}
  {\ej{\ruby{図書館}{としょかん}に\ruby{本}{ほん}があります。}
    {Hay libros en la biblioteca. (existencia)}
  \ej{\ruby{図書館}{としょかん}で\ruby{勉強}{べんきょう}します。}
    {Estudio en la biblioteca. (acción)}
  \ej{\ruby{学校}{がっこう}へ\ruby{行}{い}きます。}
    {Voy a la escuela. (dirección)}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item ¿に o で? Completa: コンビニ\_\_\_ジュースを\ruby{買}{か}います。
  \item Pregunta dónde está el hospital en japonés.
  \item Traduce: \ruby{駅}{えき}の\ruby{右}{みぎ}に\ruby{銀行}{ぎんこう}があります。
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) で\quad
2) \ruby{病院}{びょういん}はどこですか？\quad
3) Hay un banco a la derecha de la estación.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{駅}{えき}{—}{estación}{\ruby{駅}{えき} / \ruby{終点}{しゅうてん}}
\kanjirow{右}{ゆう}{みぎ}{derecha}{\ruby{右}{みぎ} / \ruby{右手}{みぎて}}
\kanjirow{左}{さ}{ひだり}{izquierda}{\ruby{左}{ひだり} / \ruby{左手}{ひだりて}}
\kanjirow{前}{ぜん}{まえ}{frente / antes}{\ruby{前}{まえ} / \ruby{前後}{ぜんご}}
\kanjirow{近}{きん}{ちか}{cerca}{\ruby{近く}{ちかく} / \ruby{近所}{きんじょ}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/04-lugares-direcciones.tex
git commit -m "content: add unidad 04 - lugares y direcciones"
```

---

### Task 9: Unidad 05 — Rutina Diaria

**Files:**
- Create: `unidades/05-rutina-diaria.tex`

- [ ] **Step 1: Write unidades/05-rutina-diaria.tex**

```latex
\chapter{⏰ 毎日の生活 — Rutina Diaria}
\unidadheader{05}{毎日の生活}{Rutina Diaria}{Hablar de actividades cotidianas}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{起きる}{おきる}{levantarse}{v. gr.2}
\vocabitem{寝る}{ねる}{dormir / acostarse}{v. gr.2}
\vocabitem{食べる}{たべる}{comer}{v. gr.2}
\vocabitem{飲む}{のむ}{beber}{v. gr.1}
\vocabitem{働く}{はたらく}{trabajar}{v. gr.1}
\vocabitem{勉強する}{べんきょうする}{estudiar}{v. irr.}
\vocabitem{帰る}{かえる}{regresar (a casa)}{v. gr.1}
\vocabitem{毎日}{まいにち}{todos los días}{adv.}
\vocabitem{毎朝}{まいあさ}{todas las mañanas}{adv.}
\vocabitem{毎晩}{まいばん}{todas las noches}{adv.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\begin{tcolorbox}[phrasebox, title={⚙️ Conjugación: Forma ます (repaso grupos)}]
\begin{tabular}{llll}
\toprule
\textbf{Grupo} & \textbf{Regla} & \textbf{Ejemplo} & \textbf{ます形} \\
\midrule
1 (う-verbos) & う→い + ます & \ruby{飲}{の}む & \ruby{飲}{の}みます \\
2 (る-verbos) & る → ます & \ruby{食}{た}べる & \ruby{食}{た}べます \\
3 (irregulares) & memorizar & する / くる & します / きます \\
\bottomrule
\end{tabular}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{\ruby{毎朝}{まいあさ}\ruby{六時}{ろくじ}に\ruby{起}{お}きます。}
  {Me levanto a las 6 todas las mañanas.}
\frase{\ruby{学校}{がっこう}で\ruby{昼}{ひる}ごはんを\ruby{食}{た}べます。}
  {Como el almuerzo en la escuela.}
\frase{\ruby{夜}{よる}\ruby{十一時}{じゅういちじ}に\ruby{寝}{ね}ます。}
  {Me duermo a las 11 de la noche.}
\frase{\ruby{毎日}{まいにち}\ruby{日本語}{にほんご}を\ruby{勉強}{べんきょう}します。}
  {Estudio japonés todos los días.}

\subsection*{⚙️ Gramática}

\patron{Forma ます — afirmativa, negativa y pasada}
  {V-ます / V-ません / V-ました / V-ませんでした}
  {\ej{\ruby{毎日}{まいにち}\ruby{コーヒー}{こーひー}を\ruby{飲}{の}みます。}
    {Bebo café todos los días.}
  \ej{きのう\ruby{学校}{がっこう}に\ruby{行}{い}きませんでした。}
    {Ayer no fui a la escuela.}}

\patron{Hora de la acción}
  {〜時に〜ます}
  {\ej{\ruby{八時}{はちじ}に\ruby{起}{お}きます。}{Me levanto a las 8.}
  \ej{\ruby{七時}{しちじ}に\ruby{家}{いえ}に\ruby{帰}{かえ}ります。}
    {Regreso a casa a las 7.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Conjuga en ます形: \ruby{働}{はたら}く → ?
  \item Conjuga en negativa pasada: \ruby{食}{た}べる → ?
  \item Escribe tu rutina mañanera en 2 oraciones.
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) \ruby{働}{はたら}きます\quad
2) \ruby{食}{た}べませんでした\quad
3) (personal)
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{起}{き}{お}{levantarse}{\ruby{起}{お}きる / \ruby{起床}{きしょう}}
\kanjirow{寝}{しん}{ね}{dormir / acostarse}{\ruby{寝}{ね}る / \ruby{就寝}{しゅうしん}}
\kanjirow{食}{しょく}{た}{comer / alimento}{\ruby{食}{た}べる / \ruby{食事}{しょくじ}}
\kanjirow{飲}{いん}{の}{beber}{\ruby{飲}{の}む / \ruby{飲み物}{のみもの}}
\kanjirow{毎}{まい}{—}{cada / todo}{\ruby{毎日}{まいにち} / \ruby{毎週}{まいしゅう}}
\kanjirow{勉}{べん}{—}{esforzarse}{\ruby{勉強}{べんきょう}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/05-rutina-diaria.tex
git commit -m "content: add unidad 05 - rutina diaria"
```

---

### Task 10: Unidad 06 — Gustos y Preferencias

**Files:**
- Create: `unidades/06-gustos-preferencias.tex`

- [ ] **Step 1: Write unidades/06-gustos-preferencias.tex**

```latex
\chapter{❤️ 好き・嫌い — Gustos y Preferencias}
\unidadheader{06}{好き・嫌い}{Gustos y Preferencias}{Expresar lo que te gusta y no te gusta}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{好き}{すき}{gustar / que se gusta}{adj-な}
\vocabitem{嫌い}{きらい}{disgustar / que no se gusta}{adj-な}
\vocabitem{得意}{とくい}{ser bueno en ~}{adj-な}
\vocabitem{苦手}{にがて}{ser malo en ~ / no ser lo tuyo}{adj-な}
\vocabitem{趣味}{しゅみ}{hobby / pasatiempo}{sust.}
\vocabitem{音楽}{おんがく}{música}{sust.}
\vocabitem{映画}{えいが}{película / cine}{sust.}
\vocabitem{料理}{りょうり}{cocina / cocinar}{sust./v.}
\vocabitem{読書}{どくしょ}{lectura}{sust.}
\vocabitem{スポーツ}{—}{deporte}{sust.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{\ruby{趣味}{しゅみ}は\ruby{何}{なん}ですか？}{¿Cuál es tu hobby?}
\frase{\ruby{音楽}{おんがく}が\ruby{大好}{だいす}きです。}{Me encanta la música.}
\frase{スポーツは\ruby{苦手}{にがて}です。}{El deporte no es lo mío.}
\frase{〜はどうですか？}{¿Qué te parece ~? / ¿Cómo te va con ~?}

\subsection*{⚙️ Gramática}

\patron{Me gusta / No me gusta}
  {〜が 好き / 嫌い です}
  {好き・嫌い son adjetivos-な, no verbos.
  \ej{\ruby{私}{わたし}はラーメンが\ruby{好}{す}きです。}{Me gusta el ramen.}
  \ej{\ruby{私}{わたし}は\ruby{虫}{むし}が\ruby{嫌}{きら}いです。}{Los insectos me disgustan.}
  \ej{\ruby{猫}{ねこ}が\ruby{大好}{だいす}きです！}{¡Adoro los gatos!}}

\patron{Ser bueno / malo en algo}
  {〜が 得意 / 苦手 です}
  {\ej{\ruby{数学}{すうがく}が\ruby{得意}{とくい}です。}{Soy bueno en matemáticas.}
  \ej{\ruby{歌}{うた}が\ruby{苦手}{にがて}です。}{No soy bueno cantando.}}

\patron{¿Qué te parece…?}
  {〜はどうですか？}
  {\ej{この\ruby{映画}{えいが}はどうですか？}{¿Qué te parece esta película?}
  \ej{とても\ruby{面白}{おもしろ}いです！}{¡Es muy interesante!}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Di dos cosas que te gustan mucho usando 大好き.
  \item Pregunta a alguien cuál es su hobby.
  \item Completa: \ruby{私}{わたし}は\ruby{料理}{りょうり}が\_\_\_\_です。(Soy bueno/a cocinando)
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) (personal)\quad
2) \ruby{趣味}{しゅみ}は\ruby{何}{なん}ですか？\quad
3) \ruby{得意}{とくい}
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{好}{こう}{す・この}{gustar}{\ruby{好き}{すき} / \ruby{好物}{こうぶつ}}
\kanjirow{嫌}{けん・けん}{きら・いや}{desagradar}{\ruby{嫌い}{きらい} / \ruby{嫌}{いや}}
\kanjirow{音}{おん・いん}{おと}{sonido / música}{\ruby{音楽}{おんがく} / \ruby{音}{おと}}
\kanjirow{楽}{がく・らく}{たの}{música / fácil / placer}{\ruby{音楽}{おんがく} / \ruby{楽しい}{たのしい}}
\kanjirow{映}{えい}{うつ}{reflejar / proyectar}{\ruby{映画}{えいが} / \ruby{映}{うつ}る}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/06-gustos-preferencias.tex
git commit -m "content: add unidad 06 - gustos y preferencias"
```

---

### Task 11: Unidad 07 — Comida y Restaurante

**Files:**
- Create: `unidades/07-comida-restaurante.tex`

- [ ] **Step 1: Write unidades/07-comida-restaurante.tex**

```latex
\chapter{🍱 食べ物と注文 — Comida y Restaurante}
\unidadheader{07}{食べ物と注文}{Comida y Restaurante}{Pedir comida y hablar de alimentos}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{ご飯}{ごはん}{arroz cocido / comida}{sust.}
\vocabitem{肉}{にく}{carne}{sust.}
\vocabitem{魚}{さかな}{pescado}{sust.}
\vocabitem{野菜}{やさい}{verdura / vegetal}{sust.}
\vocabitem{水}{みず}{agua}{sust.}
\vocabitem{お茶}{おちゃ}{té (japonés)}{sust.}
\vocabitem{注文する}{ちゅうもんする}{pedir / ordenar}{v. irr.}
\vocabitem{おいしい}{—}{delicioso}{adj-い}
\vocabitem{メニュー}{—}{menú}{sust.}
\vocabitem{お会計}{おかいけい}{la cuenta}{sust.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\begin{tcolorbox}[phrasebox, title={🔢 Contadores de comida}]
\begin{tabular}{lll}
\toprule
\textbf{Contador} & \textbf{Uso} & \textbf{Ejemplo} \\
\midrule
〜つ (hitotsu…) & objetos generales (1-9) & \ruby{一つ}{ひとつ}ください \\
〜杯 (はい/ぱい) & líquidos, tazas & \ruby{一杯}{いっぱい} \\
〜枚 (まい) & cosas planas & \ruby{一枚}{いちまい} \\
〜本 (ほん/ぼん) & cosas largas & \ruby{一本}{いっぽん} \\
\bottomrule
\end{tabular}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{〜をください。}{Quiero ~, por favor. / Deme ~.}
\frase{〜はありますか？}{¿Tienen ~?}
\frase{これにします。}{Me decido por esto.}
\frase{お\ruby{会計}{かいけい}をお\ruby{願}{ねが}いします。}{La cuenta, por favor.}
\frase{おいしかったです！}{¡Estaba delicioso!}

\subsection*{⚙️ Gramática}

\patron{Pedir algo: ください}
  {〜を ください}
  {\ej{\ruby{水}{みず}を\ruby{一杯}{いっぱい}ください。}{Un vaso de agua, por favor.}
  \ej{ラーメンを\ruby{一つ}{ひとつ}ください。}{Un ramen, por favor.}}

\patron{Preguntar disponibilidad}
  {〜は ありますか？}
  {\ej{ベジタリアンメニューはありますか？}{¿Tienen menú vegetariano?}
  \ej{\ruby{英語}{えいご}のメニューはありますか？}{¿Tienen menú en inglés?}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Pide una taza de té en japonés.
  \item ¿Cómo preguntas si tienen sushi?
  \item Traduce: この\ruby{魚}{さかな}はとてもおいしいです。
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) お\ruby{茶}{ちゃ}を\ruby{一杯}{いっぱい}ください。\quad
2) すしはありますか？\quad
3) Este pescado está muy delicioso.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{肉}{にく}{—}{carne}{\ruby{肉}{にく} / \ruby{牛肉}{ぎゅうにく}}
\kanjirow{魚}{ぎょ}{さかな・うお}{pescado}{\ruby{魚}{さかな} / \ruby{金魚}{きんぎょ}}
\kanjirow{野}{や}{の}{campo / silvestre}{\ruby{野菜}{やさい} / \ruby{野原}{のはら}}
\kanjirow{菜}{さい}{な}{vegetal / verdura}{\ruby{野菜}{やさい} / \ruby{菜食}{さいしょく}}
\kanjirow{水}{すい}{みず}{agua}{\ruby{水}{みず} / \ruby{水曜日}{すいようび}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/07-comida-restaurante.tex
git commit -m "content: add unidad 07 - comida y restaurante"
```

---

### Task 12: Unidad 08 — De Compras

**Files:**
- Create: `unidades/08-compras.tex`

- [ ] **Step 1: Write unidades/08-compras.tex**

```latex
\chapter{🛍️ 買い物 — De Compras}
\unidadheader{08}{買い物}{De Compras}{Comprar cosas, preguntar precios y tamaños}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{値段}{ねだん}{precio}{sust.}
\vocabitem{安い}{やすい}{barato}{adj-い}
\vocabitem{高い}{たかい}{caro / alto}{adj-い}
\vocabitem{大きい}{おおきい}{grande}{adj-い}
\vocabitem{小さい}{ちいさい}{pequeño}{adj-い}
\vocabitem{色}{いろ}{color}{sust.}
\vocabitem{赤}{あか}{rojo}{sust.}
\vocabitem{青}{あお}{azul}{sust.}
\vocabitem{白}{しろ}{blanco}{sust.}
\vocabitem{黒}{くろ}{negro}{sust.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\begin{tcolorbox}[phrasebox, title={🔢 Contadores para compras}]
\begin{tabular}{lll}
\toprule
\textbf{Contador} & \textbf{Para} & \textbf{Ej.} \\
\midrule
〜枚 まい & cosas planas (ropa, papel) & シャツ\ruby{一枚}{いちまい} \\
〜本 ほん & cosas largas (lápices, botellas) & ペン\ruby{二本}{にほん} \\
〜冊 さつ & libros y cuadernos & \ruby{本}{ほん}\ruby{三冊}{さんさつ} \\
〜個 こ & objetos pequeños & りんご\ruby{四個}{よんこ} \\
\bottomrule
\end{tabular}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{これはいくらですか？}{¿Cuánto cuesta esto?}
\frase{〜\ruby{円}{えん}です。}{Son ~ yen.}
\frase{\ruby{少}{すこ}し\ruby{安}{やす}くなりますか？}{¿Puede ser un poco más barato?}
\frase{〜をください。/〜にします。}{Quiero ~ / Me llevo ~.}
\frase{カードで\ruby{払}{はら}えますか？}{¿Puedo pagar con tarjeta?}

\subsection*{⚙️ Gramática}

\patron{Pregunta de precio + cantidad}
  {〜はいくらですか？　／　〜円です}
  {\ej{このシャツはいくらですか？}{¿Cuánto cuesta esta camisa?}
  \ej{\ruby{二千五百円}{にせんごひゃくえん}です。}{Son 2500 yen.}}

\patron{Adjetivos い — modificar sustantivos}
  {adj-い + 名詞}
  {\ej{\ruby{安}{やす}いセーターがほしいです。}{Quiero un suéter barato.}
  \ej{\ruby{大}{おお}きいサイズはありますか？}{¿Tienen talla grande?}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Pregunta el precio de unos zapatos en japonés.
  \item ¿Cómo dices "Quiero dos libros"?
  \item Traduce: この\ruby{黒}{くろ}いかばんはとても\ruby{高}{たか}いです。
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) この\ruby{靴}{くつ}はいくらですか？\quad
2) \ruby{本}{ほん}を\ruby{二冊}{にさつ}ください。\quad
3) Esta bolsa negra es muy cara.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{安}{あん}{やす}{barato / tranquilo}{\ruby{安い}{やすい} / \ruby{安全}{あんぜん}}
\kanjirow{高}{こう}{たか}{caro / alto}{\ruby{高い}{たかい} / \ruby{高校}{こうこう}}
\kanjirow{大}{だい・たい}{おお}{grande}{\ruby{大きい}{おおきい} / \ruby{大学}{だいがく}}
\kanjirow{小}{しょう}{ちい・こ}{pequeño}{\ruby{小さい}{ちいさい} / \ruby{小学校}{しょうがっこう}}
\kanjirow{色}{しょく}{いろ}{color}{\ruby{色}{いろ} / \ruby{色々}{いろいろ}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/08-compras.tex
git commit -m "content: add unidad 08 - de compras"
```

---

### Task 13: Unidad 09 — Adjetivos

**Files:**
- Create: `unidades/09-adjetivos.tex`

- [ ] **Step 1: Write unidades/09-adjetivos.tex**

```latex
\chapter{✨ 形容詞 — Adjetivos}
\unidadheader{09}{形容詞}{Adjetivos}{Describir personas, lugares y cosas}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{きれい}{—}{bonito/a / limpio/a}{adj-な}
\vocabitem{面白い}{おもしろい}{interesante / gracioso}{adj-い}
\vocabitem{つまらない}{—}{aburrido}{adj-い}
\vocabitem{便利}{べんり}{conveniente / práctico}{adj-な}
\vocabitem{新しい}{あたらしい}{nuevo/a}{adj-い}
\vocabitem{古い}{ふるい}{viejo/a / antiguo}{adj-い}
\vocabitem{難しい}{むずかしい}{difícil}{adj-い}
\vocabitem{やさしい}{—}{fácil / amable}{adj-い}
\vocabitem{楽しい}{たのしい}{divertido / entretenido}{adj-い}
\vocabitem{暇}{ひま}{libre (sin plan) / aburrimiento}{adj-な/sust.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\begin{tcolorbox}[phrasebox, title={⚙️ Conjugación de adjetivos}]
\begin{tabular}{lllll}
\toprule
\textbf{Tipo} & \textbf{Presente +} & \textbf{Presente -} & \textbf{Pasado +} & \textbf{Pasado -} \\
\midrule
adj-い & 〜い です & 〜くない & 〜かった & 〜くなかった \\
adj-な & 〜な です & 〜じゃない & 〜でした & 〜じゃなかった \\
\bottomrule
\end{tabular}\\[4pt]
\small Ej: \ruby{面白}{おもしろ}い → \ruby{面白}{おもしろ}くない / \ruby{面白}{おもしろ}かった / \ruby{面白}{おもしろ}くなかった
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{この\ruby{映画}{えいが}は\ruby{面白}{おもしろ}いですか？}
  {¿Es interesante esta película?}
\frase{あまり\ruby{面白}{おもしろ}くなかったです。}
  {No fue muy interesante.}
\frase{この\ruby{町}{まち}はとても\ruby{便利}{べんり}です。}
  {Esta ciudad es muy conveniente.}
\frase{\ruby{日本語}{にほんご}は\ruby{難}{むずか}しいですか？}
  {¿Es difícil el japonés?}

\subsection*{⚙️ Gramática}

\patron{Adjetivos い — todas las formas}
  {adj-い: 〜い / 〜くない / 〜かった / 〜くなかった}
  {\ej{この\ruby{本}{ほん}は\ruby{面白}{おもしろ}いです。}{Este libro es interesante.}
  \ej{この\ruby{本}{ほん}は\ruby{面白}{おもしろ}くないです。}{Este libro no es interesante.}
  \ej{きのうの\ruby{授業}{じゅぎょう}は\ruby{難}{むずか}しかったです。}
    {La clase de ayer fue difícil.}}

\patron{Adjetivos な — antes de sustantivo}
  {adj-な + な + 名詞}
  {\ej{\ruby{便利}{べんり}なアプリです。}{Es una aplicación práctica.}
  \ej{きれいな\ruby{花}{はな}ですね。}{Es una flor bonita, ¿verdad?}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Conjuga en pasado negativo: \ruby{楽}{たの}しい → ?
  \item ¿Cuál es la diferencia entre やさしい y きれい como tipo de adjetivo?
  \item Describe tu ciudad usando dos adjetivos.
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) \ruby{楽}{たの}しくなかった(です)\quad
2) やさしい = adj-い; きれい = adj-な (no termina en い fonético para conjugar)\quad
3) (personal)
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{新}{しん}{あたら・あら}{nuevo}{\ruby{新しい}{あたらしい} / \ruby{新幹線}{しんかんせん}}
\kanjirow{古}{こ}{ふる}{antiguo / viejo}{\ruby{古い}{ふるい} / \ruby{古典}{こてん}}
\kanjirow{難}{なん・なん}{むずか}{difícil}{\ruby{難しい}{むずかしい} / \ruby{難問}{なんもん}}
\kanjirow{便}{べん}{たよ}{conveniente}{\ruby{便利}{べんり} / \ruby{便}{べん}}
\kanjirow{楽}{がく・らく}{たの}{placer / fácil}{\ruby{楽しい}{たのしい} / \ruby{楽}{らく}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/09-adjetivos.tex
git commit -m "content: add unidad 09 - adjetivos"
```

---

### Task 14: Unidad 10 — La Familia

**Files:**
- Create: `unidades/10-familia.tex`

- [ ] **Step 1: Write unidades/10-familia.tex**

```latex
\chapter{👨‍👩‍👧‍👦 家族 — La Familia}
\unidadheader{10}{家族}{La Familia}{Hablar de tu familia}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo — うち (mi familia) vs そと (familia ajena)}]
\begin{tabularx}{\linewidth}{lll}
\toprule
\textbf{Familiar} & \textbf{Mi familia (うち)} & \textbf{Familia ajena (そと)} \\
\midrule
padre & \ruby{父}{ちち} & お\ruby{父}{とう}さん \\
madre & \ruby{母}{はは} & お\ruby{母}{かあ}さん \\
hermano mayor & \ruby{兄}{あに} & お\ruby{兄}{にい}さん \\
hermana mayor & \ruby{姉}{あね} & お\ruby{姉}{ねえ}さん \\
hermano menor & \ruby{弟}{おとうと} & \ruby{弟}{おとうと}さん \\
hermana menor & \ruby{妹}{いもうと} & \ruby{妹}{いもうと}さん \\
abuelo & \ruby{祖父}{そふ} & お\ruby{祖父}{じい}さん \\
abuela & \ruby{祖母}{そぼ} & お\ruby{祖母}{ばあ}さん \\
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{\ruby{家族}{かぞく}は\ruby{何人}{なんにん}ですか？}{¿Cuántos miembros tiene tu familia?}
\frase{\ruby{四人家族}{よにんかぞく}です。}{Somos familia de 4.}
\frase{\ruby{兄}{あに}が\ruby{一人}{ひとり}います。}{Tengo un hermano mayor.}
\frase{\ruby{兄弟}{きょうだい}はいますか？}{¿Tienes hermanos?}
\frase{一\ruby{人}{り}っ\ruby{子}{こ}です。}{Soy hijo/a único/a.}

\subsection*{⚙️ Gramática}

\patron{Cuántos hay: contador de personas}
  {〜人 (にん) / ひとり・ふたり}
  {1人 ひとり, 2人 ふたり, 3人以上 〜にん
  \ej{\ruby{家族}{かぞく}は\ruby{五人}{ごにん}います。}
    {En mi familia somos 5 personas.}
  \ej{\ruby{弟}{おとうと}が\ruby{二人}{ふたり}います。}
    {Tengo dos hermanos menores.}}

\patron{Presentar a la familia (うち vs そと)}
  {}
  {Hablar de MI familia → forma humilde (うち): 父、母、兄…\\
  Hablar de la familia AJENA → forma honorífica (そと): お父さん、お母さん…
  \ej{これは\ruby{父}{ちち}です。}{Este es mi padre. (hablando de propio padre)}
  \ej{お\ruby{父}{とう}さんはお\ruby{元気}{げんき}ですか？}
    {¿Está bien su padre? (preguntando por el de otro)}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Di cómo se llama tu familia usando うち vocabulary.
  \item Pregunta a alguien cuántos hermanos tiene.
  \item ¿Cómo dices "Tengo una hermana mayor y un hermano menor"?
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) (personal)\quad
2) \ruby{兄弟}{きょうだい}は\ruby{何人}{なんにん}いますか？\quad
3) \ruby{姉}{あね}が\ruby{一人}{ひとり}と\ruby{弟}{おとうと}が\ruby{一人}{ひとり}います。
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{父}{ふ}{ちち}{padre}{\ruby{父}{ちち} / お\ruby{父}{とう}さん}
\kanjirow{母}{ぼ}{はは}{madre}{\ruby{母}{はは} / お\ruby{母}{かあ}さん}
\kanjirow{兄}{けい}{あに}{hermano mayor}{\ruby{兄}{あに} / お\ruby{兄}{にい}さん}
\kanjirow{姉}{し}{あね}{hermana mayor}{\ruby{姉}{あね} / お\ruby{姉}{ねえ}さん}
\kanjirow{弟}{てい}{おとうと}{hermano menor}{\ruby{弟}{おとうと}}
\kanjirow{妹}{まい}{いもうと}{hermana menor}{\ruby{妹}{いもうと}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/10-familia.tex
git commit -m "content: add unidad 10 - la familia"
```

---

## Phase 3: Unidades N5 Avanzado (11–20)

### Task 15: Unidad 11 — Pasado

**Files:**
- Create: `unidades/11-pasado.tex`

- [ ] **Step 1: Write unidades/11-pasado.tex**

```latex
\chapter{⏪ 過去形 — El Pasado}
\unidadheader{11}{過去形}{El Pasado}{Contar lo que hiciste}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{見る}{みる}{ver / mirar}{v. gr.2}
\vocabitem{聞く}{きく}{escuchar / preguntar}{v. gr.1}
\vocabitem{買う}{かう}{comprar}{v. gr.1}
\vocabitem{読む}{よむ}{leer}{v. gr.1}
\vocabitem{書く}{かく}{escribir}{v. gr.1}
\vocabitem{話す}{はなす}{hablar / contar}{v. gr.1}
\vocabitem{泳ぐ}{およぐ}{nadar}{v. gr.1}
\vocabitem{走る}{はしる}{correr}{v. gr.1}
\vocabitem{遊ぶ}{あそぶ}{jugar / divertirse}{v. gr.1}
\vocabitem{昨日}{きのう}{ayer}{adv.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{きのう\ruby{何}{なに}をしましたか？}{¿Qué hiciste ayer?}
\frase{\ruby{映画}{えいが}を\ruby{見}{み}ました。}{Vi una película.}
\frase{あまり\ruby{楽}{たの}しくなかったです。}{No fue muy divertido.}
\frase{\ruby{先週}{せんしゅう}どこへ\ruby{行}{い}きましたか？}{¿A dónde fuiste la semana pasada?}

\subsection*{⚙️ Gramática}

\patron{Pasado afirmativo y negativo}
  {〜ました / 〜ませんでした}
  {\ej{\ruby{図書館}{としょかん}で\ruby{本}{ほん}を\ruby{読}{よ}みました。}
    {Leí un libro en la biblioteca.}
  \ej{きのう\ruby{学校}{がっこう}に\ruby{行}{い}きませんでした。}
    {Ayer no fui a la escuela.}}

\patron{Pregunta en pasado}
  {〜ましたか？}
  {\ej{あの\ruby{映画}{えいが}を\ruby{見}{み}ましたか？}
    {¿Viste esa película?}
  \ej{はい、\ruby{見}{み}ました。/ いいえ、\ruby{見}{み}ませんでした。}
    {Sí, la vi. / No, no la vi.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Conjuga en pasado negativo: \ruby{書}{か}く → ?
  \item ¿Cómo preguntas qué hizo alguien el fin de semana?
  \item Describe qué hiciste ayer en 2 oraciones.
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) \ruby{書}{か}きませんでした\quad
2) \ruby{週末}{しゅうまつ}に\ruby{何}{なに}をしましたか？\quad
3) (personal)
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{見}{けん}{み}{ver / mostrar}{\ruby{見}{み}る / \ruby{見物}{けんぶつ}}
\kanjirow{聞}{ぶん・もん}{き}{escuchar / preguntar}{\ruby{聞}{き}く / \ruby{新聞}{しんぶん}}
\kanjirow{買}{ばい}{か}{comprar}{\ruby{買}{か}う / \ruby{買い物}{かいもの}}
\kanjirow{読}{どく}{よ}{leer}{\ruby{読}{よ}む / \ruby{読書}{どくしょ}}
\kanjirow{書}{しょ}{か}{escribir}{\ruby{書}{か}く / \ruby{教科書}{きょうかしょ}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/11-pasado.tex
git commit -m "content: add unidad 11 - pasado"
```

---

### Task 16: Unidad 12 — Clima y Estaciones

**Files:**
- Create: `unidades/12-clima-estaciones.tex`

- [ ] **Step 1: Write unidades/12-clima-estaciones.tex**

```latex
\chapter{🌤️ 天気と季節 — Clima y Estaciones}
\unidadheader{12}{天気と季節}{Clima y Estaciones}{Hablar del tiempo y las estaciones}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{晴れ}{はれ}{soleado / despejado}{sust.}
\vocabitem{曇り}{くもり}{nublado}{sust.}
\vocabitem{雨}{あめ}{lluvia}{sust.}
\vocabitem{雪}{ゆき}{nieve}{sust.}
\vocabitem{風}{かぜ}{viento}{sust.}
\vocabitem{暑い}{あつい}{caluroso}{adj-い}
\vocabitem{寒い}{さむい}{frío}{adj-い}
\vocabitem{涼しい}{すずしい}{fresco}{adj-い}
\vocabitem{暖かい}{あたたかい}{cálido / tibio}{adj-い}
\vocabitem{天気予報}{てんきよほう}{pronóstico del tiempo}{sust.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{きょうの\ruby{天気}{てんき}はどうですか？}{¿Cómo está el clima hoy?}
\frase{\ruby{晴}{は}れています。}{Está soleado.}
\frase{\ruby{明日}{あした}は\ruby{雨}{あめ}でしょう。}{Mañana probablemente lloverá.}
\frase{\ruby{春}{はる}はとても\ruby{暖}{あたた}かいですね。}
  {La primavera es muy cálida, ¿verdad?}

\subsection*{⚙️ Gramática}

\patron{Probabilidad / Pronóstico: でしょう}
  {〜でしょう (probablemente ~)}
  {\ej{\ruby{明日}{あした}は\ruby{晴}{は}れでしょう。}
    {Mañana probablemente estará soleado.}
  \ej{\ruby{来週}{らいしゅう}は\ruby{寒}{さむ}くなるでしょう。}
    {La semana que viene probablemente hará frío.}}

\patron{Confirmación / Acuerdo: ですね}
  {〜ですね (¿verdad? / ¿no?)}
  {\ej{きょうは\ruby{暑}{あつ}いですね。}
    {Hoy hace calor, ¿verdad?}
  \ej{このラーメン、おいしいですね。}
    {Este ramen está rico, ¿no?}}

\patron{Quizás: かもしれません}
  {〜かもしれません (tal vez / quizás)}
  {\ej{\ruby{雨}{あめ}が\ruby{降}{ふ}るかもしれません。}
    {Tal vez llueva.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item ¿Cómo dices "Mañana quizás nieve"?
  \item Usa ですね para comentar sobre el clima de hoy.
  \item Describe el clima de tu ciudad en verano.
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) \ruby{明日}{あした}は\ruby{雪}{ゆき}が\ruby{降}{ふ}るかもしれません。\quad
2) (personal)\quad
3) (personal)
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{天}{てん}{あめ・そら}{cielo / naturaleza}{\ruby{天気}{てんき} / \ruby{天国}{てんごく}}
\kanjirow{気}{き・け}{—}{energía / ánimo / clima}{\ruby{天気}{てんき} / \ruby{気持ち}{きもち}}
\kanjirow{雨}{う}{あめ・あま}{lluvia}{\ruby{雨}{あめ} / \ruby{雨季}{うき}}
\kanjirow{雪}{せつ}{ゆき}{nieve}{\ruby{雪}{ゆき} / \ruby{雪山}{ゆきやま}}
\kanjirow{暑}{しょ}{あつ}{caluroso}{\ruby{暑い}{あつい} / \ruby{暑気}{しょき}}
\kanjirow{寒}{かん}{さむ}{frío}{\ruby{寒い}{さむい} / \ruby{寒波}{かんぱ}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/12-clima-estaciones.tex
git commit -m "content: add unidad 12 - clima y estaciones"
```

---

### Task 17: Unidad 13 — Forma て (I)

**Files:**
- Create: `unidades/13-te-form-1.tex`

- [ ] **Step 1: Write unidades/13-te-form-1.tex**

```latex
\chapter{🔗 て形① — Forma て (I): Secuencias}
\unidadheader{13}{て形①}{Forma て (I)}{Conectar acciones y describir secuencias}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{入る}{はいる}{entrar}{v. gr.1}
\vocabitem{出る}{でる}{salir}{v. gr.2}
\vocabitem{持つ}{もつ}{sostener / tener (en mano)}{v. gr.1}
\vocabitem{貸す}{かす}{prestar (dar)}{v. gr.1}
\vocabitem{借りる}{かりる}{pedir prestado / tomar}{v. gr.2}
\vocabitem{洗う}{あらう}{lavar}{v. gr.1}
\vocabitem{開ける}{あける}{abrir (algo)}{v. gr.2}
\vocabitem{閉める}{しめる}{cerrar (algo)}{v. gr.2}
\vocabitem{起こす}{おこす}{despertar a alguien}{v. gr.1}
\vocabitem{直す}{なおす}{reparar / corregir}{v. gr.1}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\begin{tcolorbox}[phrasebox, title={⚙️ Reglas de conversión a て形}]
\begin{tabular}{lll}
\toprule
\textbf{Terminación} & \textbf{→ て形} & \textbf{Ejemplo} \\
\midrule
く → & いて & \ruby{書}{か}く → \ruby{書}{か}いて \\
ぐ → & いで & \ruby{泳}{およ}ぐ → \ruby{泳}{およ}いで \\
す → & して & \ruby{話}{はな}す → \ruby{話}{はな}して \\
む/ぶ/ぬ → & んで & \ruby{飲}{の}む → \ruby{飲}{の}んで \\
る/う/つ → & って & \ruby{買}{か}う → \ruby{買}{か}って \\
gr.2 (〜る) → & て & \ruby{食}{た}べる → \ruby{食}{た}べて \\
する → & して & する → して \\
くる → & きて & くる → きて \\
\bottomrule
\end{tabular}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{\ruby{手}{て}を\ruby{洗}{あら}ってから\ruby{食}{た}べてください。}
  {Lávate las manos y luego come.}
\frase{\ruby{宿題}{しゅくだい}をしてから\ruby{遊}{あそ}びます。}
  {Hago la tarea y después juego.}
\frase{\ruby{音楽}{おんがく}を\ruby{聞}{き}きながら\ruby{勉強}{べんきょう}します。}
  {Estudio mientras escucho música.}

\subsection*{⚙️ Gramática}

\patron{Secuencia de acciones: てから}
  {V-て + から + V2 (primero ~ y luego ~)}
  {\ej{\ruby{シャワー}{しゃわー}を\ruby{浴}{あ}びてから\ruby{寝}{ね}ます。}
    {Me ducho y luego me acuesto.}
  \ej{\ruby{日本}{にほん}に\ruby{来}{き}てから\ruby{日本語}{にほんご}を\ruby{勉強}{べんきょう}しました。}
    {Después de venir a Japón, estudié japonés.}}

\patron{Acciones simultáneas: ながら}
  {V(ます-stem) + ながら + V2 (mientras hace A, hace B)}
  {\ej{コーヒーを\ruby{飲}{の}みながら\ruby{新聞}{しんぶん}を\ruby{読}{よ}みます。}
    {Leo el periódico mientras tomo café.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Convierte a て形: \ruby{泳}{およ}ぐ / \ruby{持}{も}つ / \ruby{出}{で}る
  \item Une con てから: \ruby{宿題}{しゅくだい}をする → \ruby{ゲーム}{げーむ}をする
  \item Describe algo que haces simultáneamente.
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) \ruby{泳}{およ}いで / \ruby{持}{も}って / \ruby{出}{で}て\quad
2) \ruby{宿題}{しゅくだい}をしてから\ruby{ゲーム}{げーむ}をします。\quad
3) (personal)
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{入}{にゅう}{はい・い}{entrar}{\ruby{入}{はい}る / \ruby{入口}{いりぐち}}
\kanjirow{出}{しゅつ}{で・だ}{salir / dar}{\ruby{出}{で}る / \ruby{出口}{でぐち}}
\kanjirow{持}{じ}{も}{sostener / tener}{\ruby{持}{も}つ / \ruby{持参}{じさん}}
\kanjirow{借}{しゃく}{か}{pedir prestado}{\ruby{借}{か}りる / \ruby{借金}{しゃっきん}}
\kanjirow{洗}{せん}{あら}{lavar}{\ruby{洗}{あら}う / \ruby{洗濯}{せんたく}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/13-te-form-1.tex
git commit -m "content: add unidad 13 - te-form secuencias"
```

---

### Task 18: Unidad 14 — Forma て (II)

**Files:**
- Create: `unidades/14-te-form-2.tex`

- [ ] **Step 1: Write unidades/14-te-form-2.tex**

```latex
\chapter{🙏 て形② — Forma て (II): Permisos y Peticiones}
\unidadheader{14}{て形②}{Forma て (II)}{Pedir favores, dar permisos y expresar prohibiciones}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{使う}{つかう}{usar}{v. gr.1}
\vocabitem{置く}{おく}{poner / colocar}{v. gr.1}
\vocabitem{捨てる}{すてる}{tirar / desechar}{v. gr.2}
\vocabitem{手伝う}{てつだう}{ayudar}{v. gr.1}
\vocabitem{急ぐ}{いそぐ}{apurarse}{v. gr.1}
\vocabitem{休む}{やすむ}{descansar / faltar}{v. gr.1}
\vocabitem{続ける}{つづける}{continuar}{v. gr.2}
\vocabitem{始める}{はじめる}{comenzar (algo)}{v. gr.2}
\vocabitem{気をつける}{きをつける}{tener cuidado}{v. gr.2}
\vocabitem{片付ける}{かたづける}{ordenar / limpiar}{v. gr.2}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{ここに\ruby{座}{すわ}ってもいいですか？}{¿Puedo sentarme aquí?}
\frase{どうぞ。}{Adelante. / Por favor.}
\frase{ここでたばこを\ruby{吸}{す}ってはいけません。}
  {Aquí no está permitido fumar.}
\frase{\ruby{窓}{まど}を\ruby{開}{あ}けてください。}{Abra la ventana, por favor.}

\subsection*{⚙️ Gramática}

\patron{Petición amable}
  {V-て + ください}
  {\ej{\ruby{名前}{なまえ}を\ruby{書}{か}いてください。}
    {Por favor, escriba su nombre.}
  \ej{もう\ruby{少}{すこ}しゆっくり\ruby{話}{はな}してください。}
    {Por favor, hable un poco más despacio.}}

\patron{Pedir permiso}
  {V-て + もいいですか？}
  {\ej{\ruby{写真}{しゃしん}を\ruby{撮}{と}ってもいいですか？}
    {¿Puedo tomar una foto?}
  \ej{トイレを\ruby{使}{つか}ってもいいですか？}
    {¿Puedo usar el baño?}}

\patron{Prohibición}
  {V-て + はいけません / はだめです}
  {\ex{ここで\ruby{走}{はし}ってはいけません。}{No está permitido correr aquí.}
  \ej{ゴミを\ruby{捨}{す}ててはだめです。}{No debes tirar basura.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Pide a alguien que espere (待つ) en japonés.
  \item Pregunta si puedes usar un diccionario (辞書).
  \item Traduce la prohibición: No está permitido entrar aquí.
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) \ruby{待}{ま}ってください。\quad
2) \ruby{辞書}{じしょ}を\ruby{使}{つか}ってもいいですか？\quad
3) ここに\ruby{入}{はい}ってはいけません。
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{使}{し}{つか}{usar}{\ruby{使}{つか}う / \ruby{使用}{しよう}}
\kanjirow{置}{ち}{お}{poner / dejar}{\ruby{置}{お}く / \ruby{位置}{いち}}
\kanjirow{急}{きゅう}{いそ}{urgente / apurarse}{\ruby{急}{いそ}ぐ / \ruby{急行}{きゅうこう}}
\kanjirow{休}{きゅう}{やす}{descansar}{\ruby{休}{やす}む / \ruby{休日}{きゅうじつ}}
\kanjirow{始}{し}{はじ}{comenzar}{\ruby{始}{はじ}める / \ruby{開始}{かいし}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/14-te-form-2.tex
git commit -m "content: add unidad 14 - te-form permisos"
```

---

### Task 19: Unidad 15 — ～ている

**Files:**
- Create: `unidades/15-te-iru.tex`

- [ ] **Step 1: Write unidades/15-te-iru.tex**

```latex
\chapter{🔄 〜ている — Progreso y Estado}
\unidadheader{15}{〜ている}{Progreso y Estado}{Expresar acciones en curso y estados resultantes}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{着る}{きる}{ponerse (ropa)}{v. gr.2}
\vocabitem{住む}{すむ}{vivir / residir en}{v. gr.1}
\vocabitem{知る}{しる}{saber / conocer}{v. gr.1}
\vocabitem{結婚する}{けっこんする}{casarse}{v. irr.}
\vocabitem{太る}{ふとる}{engordar}{v. gr.1}
\vocabitem{痩せる}{やせる}{adelgazar}{v. gr.2}
\vocabitem{疲れる}{つかれる}{cansarse}{v. gr.2}
\vocabitem{終わる}{おわる}{terminar (algo)}{v. gr.1}
\vocabitem{始まる}{はじまる}{empezar (algo intrans.)}{v. gr.1}
\vocabitem{慣れる}{なれる}{acostumbrarse}{v. gr.2}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{いま\ruby{何}{なに}をしていますか？}{¿Qué estás haciendo ahora?}
\frase{テレビを\ruby{見}{み}ています。}{Estoy viendo la televisión.}
\frase{\ruby{東京}{とうきょう}に\ruby{住}{す}んでいます。}{Vivo en Tokio.}
\frase{\ruby{彼}{かれ}はもう\ruby{結婚}{けっこん}していますか？}{¿Él ya está casado?}

\subsection*{⚙️ Gramática}

\patron{Acción en progreso}
  {V-て + います (está haciendo ~)}
  {\ej{いま\ruby{電話}{でんわ}しています。}{Estoy hablando por teléfono ahora.}
  \ej{\ruby{雨}{あめ}が\ruby{降}{ふ}っています。}{Está lloviendo.}}

\patron{Estado resultante de una acción}
  {V-て + います (ya está en ese estado)}
  {Para verbos de cambio (結婚する、住む、知る、着る), ている = estado actual.
  \ej{\ruby{大阪}{おおさか}に\ruby{住}{す}んでいます。}{Vivo en Osaka. (estado)}
  \ej{\ruby{田中}{たなか}さんを\ruby{知}{し}っていますか？}
    {¿Conoce/sabe quién es el Sr. Tanaka?}
  \ej{はい、\ruby{知}{し}っています。}{Sí, lo conozco.}}

\patron{Negación: no está haciendo / no sabe}
  {V-て + いません}
  {\ej{まだ\ruby{食}{た}べていません。}{Aún no he comido.}
  \ej{\ruby{知}{し}りません。}{No lo sé. ← ojo: 知りません, no 知っていません}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item ¿Qué estás haciendo ahora? Responde con ています.
  \item Traduce: \ruby{彼女}{かのじょ}はもう\ruby{日本}{にほん}に\ruby{住}{す}んでいます。
  \item ¿Cuándo usas 知りません vs 知っていません?
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) (personal)\quad
2) Ella ya vive en Japón.\quad
3) 知りません = respuesta estándar para "no sé"; 知っていません es técnicamente válido pero menos natural.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{着}{ちゃく}{き・つ}{llegar / ponerse ropa}{\ruby{着}{き}る / \ruby{到着}{とうちゃく}}
\kanjirow{住}{じゅう}{す}{vivir / residir}{\ruby{住}{す}む / \ruby{住所}{じゅうしょ}}
\kanjirow{知}{ち}{し}{saber / conocer}{\ruby{知}{し}る / \ruby{知識}{ちしき}}
\kanjirow{疲}{ひ}{つか}{cansarse}{\ruby{疲}{つか}れる / \ruby{疲労}{ひろう}}
\kanjirow{終}{しゅう}{お}{terminar}{\ruby{終}{お}わる / \ruby{終了}{しゅうりょう}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/15-te-iru.tex
git commit -m "content: add unidad 15 - te-iru progreso y estado"
```

---

### Task 20: Unidad 16 — Experiencias

**Files:**
- Create: `unidades/16-experiencias.tex`

- [ ] **Step 1: Write unidades/16-experiencias.tex**

```latex
\chapter{🌟 経験と回数 — Experiencias}
\unidadheader{16}{経験と回数}{Experiencias y Veces}{Contar experiencias y cuántas veces hiciste algo}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{経験}{けいけん}{experiencia}{sust.}
\vocabitem{〜度}{ど}{vez / grado (contador)}{contador}
\vocabitem{〜回}{かい}{vez (contador de acciones)}{contador}
\vocabitem{初めて}{はじめて}{por primera vez}{adv.}
\vocabitem{一度も}{いちども}{ni una sola vez (+ neg.)}{adv.}
\vocabitem{まだ}{—}{todavía / aún (no)}{adv.}
\vocabitem{もう}{—}{ya (+ afirmativo)}{adv.}
\vocabitem{外国}{がいこく}{país extranjero}{sust.}
\vocabitem{海外}{かいがい}{el extranjero / exterior}{sust.}
\vocabitem{留学する}{りゅうがくする}{estudiar en el extranjero}{v. irr.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{\ruby{日本}{にほん}に\ruby{行}{い}ったことがありますか？}{¿Has ido a Japón alguna vez?}
\frase{はい、\ruby{二回}{にかい}\ruby{行}{い}ったことがあります。}
  {Sí, he ido dos veces.}
\frase{いいえ、まだ\ruby{行}{い}ったことがありません。}
  {No, todavía no he ido.}
\frase{\ruby{初}{はじ}めて\ruby{寿司}{すし}を\ruby{食}{た}べました。}
  {Comí sushi por primera vez.}

\subsection*{⚙️ Gramática}

\patron{Haber tenido experiencia}
  {V-た + ことがあります / ことがありません}
  {\ej{\ruby{富士山}{ふじさん}に\ruby{登}{のぼ}ったことがあります。}
    {He escalado el Monte Fuji.}
  \ej{スカイダイビングをしたことがありません。}
    {Nunca he hecho paracaidismo.}}

\patron{Cuántas veces: 〜回 / 〜度}
  {数字 + 回/度 + V}
  {\ej{\ruby{三回}{さんかい}\ruby{見}{み}たことがあります。}
    {Lo he visto tres veces.}
  \ej{一度も\ruby{遅刻}{ちこく}したことがありません。}
    {Nunca he llegado tarde.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Pregunta a alguien si alguna vez comió takoyaki (たこ焼き).
  \item Di algo que nunca has hecho usando ことがありません.
  \item Traduce: もう\ruby{宿題}{しゅくだい}をしましたか？
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) たこ\ruby{焼}{や}きを\ruby{食}{た}べたことがありますか？\quad
2) (personal)\quad
3) ¿Ya hiciste la tarea?
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{経}{けい}{へ}{pasar / experiencia}{\ruby{経験}{けいけん} / \ruby{経済}{けいざい}}
\kanjirow{験}{けん}{—}{experiencia / examen}{\ruby{経験}{けいけん} / \ruby{試験}{しけん}}
\kanjirow{度}{ど・たく}{たび}{vez / grado}{\ruby{一度}{いちど} / \ruby{温度}{おんど}}
\kanjirow{回}{かい}{まわ}{vuelta / vez}{\ruby{三回}{さんかい} / \ruby{回転}{かいてん}}
\kanjirow{初}{しょ}{はじ・うい}{primero / inicio}{\ruby{初}{はじ}めて / \ruby{初日}{しょにち}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/16-experiencias.tex
git commit -m "content: add unidad 16 - experiencias"
```

---

### Task 21: Unidad 17 — Planes y Citas

**Files:**
- Create: `unidades/17-planes-citas.tex`

- [ ] **Step 1: Write unidades/17-planes-citas.tex**

```latex
\chapter{📅 計画と予定 — Planes y Citas}
\unidadheader{17}{計画と予定}{Planes y Citas}{Hablar de intenciones, planes e invitaciones}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{予定}{よてい}{plan / agenda}{sust.}
\vocabitem{計画}{けいかく}{plan / proyecto}{sust.}
\vocabitem{旅行}{りょこう}{viaje}{sust.}
\vocabitem{来週}{らいしゅう}{la semana que viene}{adv.}
\vocabitem{来月}{らいげつ}{el mes que viene}{adv.}
\vocabitem{来年}{らいねん}{el año que viene}{adv.}
\vocabitem{〜週間}{しゅうかん}{durante ~ semanas}{contador}
\vocabitem{〜ヶ月}{かげつ}{durante ~ meses}{contador}
\vocabitem{誘う}{さそう}{invitar / proponer}{v. gr.1}
\vocabitem{決める}{きめる}{decidir}{v. gr.2}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{いっしょに\ruby{映画}{えいが}を\ruby{見}{み}ませんか？}
  {¿No quieres ver una película juntos?}
\frase{いいですね！\ruby{行}{い}きましょう！}{¡Qué buena idea! ¡Vamos!}
\frase{すみません、\ruby{予定}{よてい}があります。}
  {Lo siento, tengo planes.}
\frase{\ruby{来週}{らいしゅう}\ruby{京都}{きょうと}に\ruby{行}{い}くつもりです。}
  {Tengo la intención de ir a Kioto la semana que viene.}

\subsection*{⚙️ Gramática}

\patron{Intención: つもりです}
  {V-dict. + つもりです (tengo la intención de ~)}
  {\ej{\ruby{大学}{だいがく}に\ruby{入}{はい}るつもりです。}
    {Tengo la intención de entrar a la universidad.}
  \ej{たばこをやめるつもりです。}
    {Tengo la intención de dejar de fumar.}}

\patron{Plan / Agenda: 予定です}
  {V-dict. + 予定です (está planeado ~)}
  {\ej{\ruby{来月}{らいげつ}\ruby{日本}{にほん}に\ruby{行}{い}く\ruby{予定}{よてい}です。}
    {Está planeado que vaya a Japón el mes que viene.}}

\patron{Invitación: ませんか / ましょう}
  {V-ません + か (¿no quieres ~?) / V-ましょう (¡hagamos ~!)}
  {\ej{いっしょに\ruby{食}{た}べませんか？}{¿No comemos juntos?}
  \ej{そろそろ\ruby{行}{い}きましょう。}{Ya vámonos.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Invita a alguien a tomar café usando ませんか.
  \item Di tu plan para las vacaciones usando 予定です.
  \item ¿Cuál es la diferencia entre つもりです y 予定です?
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) コーヒーを\ruby{飲}{の}みませんか？\quad
2) (personal)\quad
3) つもり = intención personal, puede cambiar; 予定 = plan concreto ya establecido/agendado.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{予}{よ}{あらかじ}{de antemano / plan}{\ruby{予定}{よてい} / \ruby{予約}{よやく}}
\kanjirow{定}{てい}{さだ}{establecer / fijo}{\ruby{予定}{よてい} / \ruby{定期}{ていき}}
\kanjirow{計}{けい}{はか}{calcular / plan}{\ruby{計画}{けいかく} / \ruby{時計}{とけい}}
\kanjirow{旅}{りょ}{たび}{viaje}{\ruby{旅行}{りょこう} / \ruby{旅}{たび}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/17-planes-citas.tex
git commit -m "content: add unidad 17 - planes y citas"
```

---

### Task 22: Unidad 18 — Comparaciones

**Files:**
- Create: `unidades/18-comparaciones.tex`

- [ ] **Step 1: Write unidades/18-comparaciones.tex**

```latex
\chapter{⚖️ 比較 — Comparaciones}
\unidadheader{18}{比較}{Comparaciones}{Comparar personas, lugares y cosas}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{一番}{いちばん}{el/la más ~ (superlativo)}{adv.}
\vocabitem{〜より}{—}{más que ~ (comparativo)}{part.}
\vocabitem{〜の方が}{ほうが}{~ es mejor / más ~ que}{expr.}
\vocabitem{同じ}{おなじ}{igual / mismo}{adj-な}
\vocabitem{違う}{ちがう}{diferente / equivocado}{v. gr.1}
\vocabitem{もっと}{—}{más (cantidad/grado)}{adv.}
\vocabitem{少し}{すこし}{un poco}{adv.}
\vocabitem{ずっと}{—}{mucho más / todo el tiempo}{adv.}
\vocabitem{だいぶ}{—}{bastante / considerablemente}{adv.}
\vocabitem{比べる}{くらべる}{comparar}{v. gr.2}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{AとBとどちらが\ruby{好}{す}きですか？}{¿Cuál prefieres, A o B?}
\frase{Aの\ruby{方}{ほう}が\ruby{好}{す}きです。}{Prefiero A.}
\frase{\ruby{日本}{にほん}で\ruby{一番}{いちばん}\ruby{高}{たか}い\ruby{山}{やま}は？}
  {¿Cuál es la montaña más alta de Japón?}
\frase{\ruby{富士山}{ふじさん}が\ruby{一番}{いちばん}\ruby{高}{たか}いです。}
  {El Monte Fuji es el más alto.}

\subsection*{⚙️ Gramática}

\patron{Comparativo: más que ~}
  {A は B より 〜です}
  {\ej{\ruby{東京}{とうきょう}は\ruby{大阪}{おおさか}より\ruby{大}{おお}きいです。}
    {Tokio es más grande que Osaka.}
  \ej{\ruby{電車}{でんしゃ}の\ruby{方}{ほう}がバスより\ruby{速}{はや}いです。}
    {El tren es más rápido que el autobús.}}

\patron{Superlativo: el/la más ~}
  {〜の中で 一番 〜です}
  {\ej{このクラスの中で\ruby{誰}{だれ}が\ruby{一番}{いちばん}\ruby{背}{せ}が\ruby{高}{たか}いですか？}
    {¿Quién es el más alto de esta clase?}
  \ej{\ruby{私}{わたし}が\ruby{一番}{いちばん}\ruby{背}{せ}が\ruby{高}{たか}いです。}
    {Yo soy el más alto.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Compara dos ciudades que conoces usando より.
  \item ¿Cuál es tu materia favorita? Usa 一番 para expresarlo.
  \item Traduce: コーヒーとお茶とどちらの方が好きですか？
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) (personal)\quad
2) (personal)\quad
3) ¿Cuál prefieres, el café o el té?
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{一}{いち・いつ}{ひと}{uno / primero}{\ruby{一番}{いちばん} / \ruby{一つ}{ひとつ}}
\kanjirow{番}{ばん}{—}{número / turno}{\ruby{一番}{いちばん} / \ruby{番号}{ばんごう}}
\kanjirow{同}{どう}{おな}{igual / mismo}{\ruby{同じ}{おなじ} / \ruby{同時}{どうじ}}
\kanjirow{違}{い}{ちが}{diferente / error}{\ruby{違う}{ちがう} / \ruby{違い}{ちがい}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/18-comparaciones.tex
git commit -m "content: add unidad 18 - comparaciones"
```

---

### Task 23: Unidad 19 — Transporte

**Files:**
- Create: `unidades/19-transporte.tex`

- [ ] **Step 1: Write unidades/19-transporte.tex**

```latex
\chapter{🚆 移動と交通 — Transporte}
\unidadheader{19}{移動と交通}{Transporte}{Moverse por la ciudad y viajar}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{電車}{でんしゃ}{tren eléctrico}{sust.}
\vocabitem{飛行機}{ひこうき}{avión}{sust.}
\vocabitem{自転車}{じてんしゃ}{bicicleta}{sust.}
\vocabitem{乗る}{のる}{subir / abordar}{v. gr.1}
\vocabitem{降りる}{おりる}{bajar / descender}{v. gr.2}
\vocabitem{乗り換える}{のりかえる}{hacer transbordo}{v. gr.2}
\vocabitem{切符}{きっぷ}{boleto / ticket}{sust.}
\vocabitem{〜番線}{ばんせん}{andén número ~}{sust.}
\vocabitem{終点}{しゅうてん}{última parada}{sust.}
\vocabitem{〜分かかる}{ふんかかる}{tardar ~ minutos}{expr.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{\ruby{新宿}{しんじゅく}まで\ruby{何}{なん}\ruby{分}{ぷん}かかりますか？}
  {¿Cuántos minutos se tarda hasta Shinjuku?}
\frase{\ruby{電車}{でんしゃ}で\ruby{約}{やく}20\ruby{分}{ぷん}かかります。}
  {En tren se tarda aproximadamente 20 minutos.}
\frase{〜\ruby{線}{せん}に\ruby{乗}{の}り\ruby{換}{か}えてください。}
  {Haga transbordo a la línea ~.}
\frase{〜\ruby{番線}{ばんせん}のホームです。}
  {Es el andén número ~.}

\subsection*{⚙️ Gramática}

\patron{Medio de transporte: で}
  {交通手段 + で + 行く/来る/帰る}
  {\ej{\ruby{自転車}{じてんしゃ}で\ruby{学校}{がっこう}に\ruby{行}{い}きます。}
    {Voy a la escuela en bicicleta.}
  \ej{バスで20\ruby{分}{ぷん}かかります。}
    {En autobús se tarda 20 minutos.}}

\patron{Subir / Bajar transporte: に乗る / を降りる}
  {〜に乗る (subir a ~) / 〜を降りる (bajar de ~)}
  {\ej{\ruby{山手線}{やまのてせん}に\ruby{乗}{の}ってください。}
    {Súbase a la línea Yamanote.}
  \ej{\ruby{渋谷}{しぶや}で\ruby{降}{お}りてください。}
    {Baje en Shibuya.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item ¿Cómo preguntas cuánto tiempo tarda el autobús?
  \item Di cómo llegas a tu trabajo/escuela.
  \item Traduce: \ruby{次}{つぎ}の\ruby{駅}{えき}で\ruby{乗}{の}り\ruby{換}{か}えてください。
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) バスで\ruby{何分}{なんぷん}かかりますか？\quad
2) (personal)\quad
3) Por favor, haga transbordo en la próxima estación.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{電}{でん}{—}{electricidad}{\ruby{電車}{でんしゃ} / \ruby{電話}{でんわ}}
\kanjirow{車}{しゃ}{くるま}{vehículo / coche}{\ruby{電車}{でんしゃ} / \ruby{車}{くるま}}
\kanjirow{飛}{ひ}{と}{volar}{\ruby{飛行機}{ひこうき} / \ruby{飛}{と}ぶ}
\kanjirow{機}{き}{はた}{máquina / avión}{\ruby{飛行機}{ひこうき} / \ruby{機会}{きかい}}
\kanjirow{乗}{じょう}{の}{subir / abordar}{\ruby{乗}{の}る / \ruby{乗車}{じょうしゃ}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/19-transporte.tex
git commit -m "content: add unidad 19 - transporte"
```

---

### Task 24: Unidad 20 — Cuerpo y Salud

**Files:**
- Create: `unidades/20-cuerpo-salud.tex`

- [ ] **Step 1: Write unidades/20-cuerpo-salud.tex**

```latex
\chapter{🏥 体と健康 — Cuerpo y Salud}
\unidadheader{20}{体と健康}{Cuerpo y Salud}{Hablar de síntomas y en el médico}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{頭}{あたま}{cabeza}{sust.}
\vocabitem{目}{め}{ojo}{sust.}
\vocabitem{耳}{みみ}{oreja / oído}{sust.}
\vocabitem{歯}{は}{diente}{sust.}
\vocabitem{足}{あし}{pie / pierna}{sust.}
\vocabitem{お腹}{おなか}{estómago / barriga}{sust.}
\vocabitem{熱}{ねつ}{fiebre}{sust.}
\vocabitem{風邪}{かぜ}{resfriado}{sust.}
\vocabitem{薬}{くすり}{medicina}{sust.}
\vocabitem{医者}{いしゃ}{médico/a}{sust.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{\ruby{頭}{あたま}が\ruby{痛}{いた}いです。}{Me duele la cabeza.}
\frase{\ruby{熱}{ねつ}があります。}{Tengo fiebre.}
\frase{\ruby{風邪}{かぜ}を\ruby{引}{ひ}きました。}{Me resfrié.}
\frase{\ruby{薬}{くすり}を\ruby{飲}{の}んでください。}{Tome la medicina.}
\frase{\ruby{今日}{きょう}は\ruby{無理}{むり}しないでください。}
  {No se esfuerce de más hoy.}

\subsection*{⚙️ Gramática}

\patron{Expresar dolor}
  {部位 + が + 痛いです}
  {\ej{\ruby{歯}{は}が\ruby{痛}{いた}いです。}{Me duele un diente.}
  \ej{のどが\ruby{痛}{いた}いです。}{Me duele la garganta.}}

\patron{Prohibición suave: ないでください}
  {V-ない + でください (por favor, no haga ~)}
  {\ej{\ruby{無理}{むり}しないでください。}
    {Por favor, no se esfuerce de más.}
  \ej{\ruby{辛}{から}いものを\ruby{食}{た}べないでください。}
    {Por favor, no coma cosas picantes.}}

\patron{Consejo: ないほうがいいです}
  {V-ない + ほうがいいです (es mejor no hacer ~)}
  {\ej{お\ruby{酒}{さけ}を\ruby{飲}{の}まないほうがいいです。}
    {Es mejor que no beba alcohol.}
  \ej{しばらく\ruby{運動}{うんどう}しないほうがいいです。}
    {Es mejor que no haga ejercicio por un tiempo.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Di tres síntomas en japonés.
  \item Usa ないほうがいいです para dar un consejo a alguien con fiebre.
  \item Traduce: \ruby{病院}{びょういん}に\ruby{行}{い}ったほうがいいですよ。
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) (personal)\quad
2) \ruby{外}{そと}に\ruby{出}{で}ないほうがいいです。\quad
3) Sería mejor que fueras al hospital.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{頭}{とう・ず}{あたま・かしら}{cabeza}{\ruby{頭}{あたま} / \ruby{頭痛}{ずつう}}
\kanjirow{目}{もく・ぼく}{め}{ojo}{\ruby{目}{め} / \ruby{目標}{もくひょう}}
\kanjirow{歯}{し}{は}{diente}{\ruby{歯}{は} / \ruby{歯医者}{はいしゃ}}
\kanjirow{足}{そく}{あし・たり}{pie / pierna / suficiente}{\ruby{足}{あし} / \ruby{足りる}{たりる}}
\kanjirow{痛}{つう}{いた}{dolor}{\ruby{痛い}{いたい} / \ruby{頭痛}{ずつう}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/20-cuerpo-salud.tex
git commit -m "content: add unidad 20 - cuerpo y salud"
```

---

## Phase 4: Unidades N4 (21–30)

### Task 25: Unidad 21 — Forma Potencial

**Files:**
- Create: `unidades/21-forma-potencial.tex`

- [ ] **Step 1: Write unidades/21-forma-potencial.tex**

```latex
\chapter{💪 可能形 — Forma Potencial}
\unidadheader{21}{可能形}{Forma Potencial}{Expresar lo que puedes o no puedes hacer}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{泳ぐ}{およぐ}{nadar}{v. gr.1}
\vocabitem{歌う}{うたう}{cantar}{v. gr.1}
\vocabitem{弾く}{ひく}{tocar (instrumento)}{v. gr.1}
\vocabitem{運転する}{うんてんする}{conducir}{v. irr.}
\vocabitem{料理する}{りょうりする}{cocinar}{v. irr.}
\vocabitem{説明する}{せつめいする}{explicar}{v. irr.}
\vocabitem{翻訳する}{ほんやくする}{traducir}{v. irr.}
\vocabitem{〜が得意}{とくい}{ser bueno en ~}{expr.}
\vocabitem{なんとか}{—}{de alguna manera / más o menos}{adv.}
\vocabitem{全然}{ぜんぜん}{para nada (+ neg.)}{adv.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\begin{tcolorbox}[phrasebox, title={⚙️ Conjugación a forma potencial}]
\begin{tabular}{llll}
\toprule
\textbf{Grupo} & \textbf{Regla} & \textbf{Original} & \textbf{Potencial} \\
\midrule
1 (う→え段) & う→える & \ruby{書}{か}く & \ruby{書}{か}ける \\
2 (〜る → 〜られる) & る→られる & \ruby{食}{た}べる & \ruby{食}{た}べられる \\
3 (irregulares) & memorizar & する / くる & できる / こられる \\
\bottomrule
\end{tabular}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{\ruby{日本語}{にほんご}が\ruby{話}{はな}せますか？}{¿Puedes hablar japonés?}
\frase{なんとか\ruby{話}{はな}せます。}{Más o menos puedo hablar.}
\frase{\ruby{全然}{ぜんぜん}\ruby{泳}{およ}げません。}{No puedo nadar para nada.}
\frase{ピアノが\ruby{弾}{ひ}けますか？}{¿Puedes tocar el piano?}

\subsection*{⚙️ Gramática}

\patron{Forma potencial: poder hacer ~}
  {V (potencial) + ます / V-ことができます}
  {\ej{\ruby{漢字}{かんじ}が\ruby{読}{よ}めます。}{Puedo leer kanji.}
  \ej{\ruby{車}{くるま}を\ruby{運転}{うんてん}することができません。}
    {No puedo conducir un coche.}
  \ej{スペイン\ruby{語}{ご}が\ruby{話}{はな}せますか？}
    {¿Puedes hablar español?}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Convierte a potencial: \ruby{飲}{の}む / \ruby{見}{み}る / する
  \item Di 2 cosas que puedes hacer bien en japonés.
  \item Traduce: \ruby{子}{こ}どものとき、\ruby{木}{き}に\ruby{登}{のぼ}れましたか？
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) \ruby{飲}{の}める / \ruby{見}{み}られる / できる\quad
2) (personal)\quad
3) Cuando eras niño/a, ¿podías subir a los árboles?
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{泳}{えい}{およ}{nadar}{\ruby{泳}{およ}ぐ / \ruby{水泳}{すいえい}}
\kanjirow{歌}{か}{うた}{cantar / canción}{\ruby{歌}{うた}う / \ruby{歌手}{かしゅ}}
\kanjirow{運}{うん}{はこ}{transporte / suerte}{\ruby{運転}{うんてん} / \ruby{運動}{うんどう}}
\kanjirow{転}{てん}{ころ}{rodar / girar}{\ruby{運転}{うんてん} / \ruby{転ぶ}{ころぶ}}
\kanjirow{能}{のう}{—}{capacidad / habilidad}{\ruby{可能}{かのう} / \ruby{才能}{さいのう}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/21-forma-potencial.tex
git commit -m "content: add unidad 21 - forma potencial"
```

---

### Task 26: Unidad 22 — Deseos

**Files:**
- Create: `unidades/22-deseos.tex`

- [ ] **Step 1: Write unidades/22-deseos.tex**

```latex
\chapter{🌠 欲しい・たい — Deseos}
\unidadheader{22}{欲しい・たい}{Deseos}{Expresar lo que quieres hacer o tener}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{欲しい}{ほしい}{querer (tener algo)}{adj-い}
\vocabitem{夢}{ゆめ}{sueño (aspiración)}{sust.}
\vocabitem{目標}{もくひょう}{meta / objetivo}{sust.}
\vocabitem{将来}{しょうらい}{futuro}{sust.}
\vocabitem{なりたい}{—}{quiero ser/convertirme en}{expr.}
\vocabitem{〜に行きたい}{—}{quiero ir a ~}{expr.}
\vocabitem{ぜひ}{—}{definitivamente / con gusto}{adv.}
\vocabitem{いつか}{—}{algún día}{adv.}
\vocabitem{できれば}{—}{si es posible}{expr.}
\vocabitem{どうしても}{—}{a toda costa / inevitablemente}{adv.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{\ruby{日本}{にほん}に\ruby{行}{い}きたいです。}{Quiero ir a Japón.}
\frase{あたらしいパソコンが\ruby{欲}{ほ}しいです。}{Quiero una computadora nueva.}
\frase{\ruby{将来}{しょうらい}、\ruby{医者}{いしゃ}になりたいです。}
  {En el futuro, quiero ser médico/a.}
\frase{いつかN1に\ruby{合格}{ごうかく}したいです。}
  {Algún día quiero aprobar el N1.}

\subsection*{⚙️ Gramática}

\patron{Querer hacer algo: たい}
  {V(ます-stem) + たいです / たくないです}
  {Solo se usa para deseos PROPIOS, no de terceros.
  \ej{\ruby{寿司}{すし}を\ruby{食}{た}べたいです。}{Quiero comer sushi.}
  \ej{もう\ruby{働}{はたら}きたくないです。}
    {Ya no quiero trabajar más.}
  \ej{どこに\ruby{行}{い}きたいですか？}{¿A dónde quieres ir?}}

\patron{Querer tener algo: 欲しい}
  {モノ + が + 欲しいです / 欲しくないです}
  {\ej{あたらしい\ruby{車}{くるま}が\ruby{欲}{ほ}しいです。}
    {Quiero un coche nuevo.}
  \ej{お\ruby{金}{かね}より\ruby{時間}{じかん}が\ruby{欲}{ほ}しいです。}
    {Quiero tiempo más que dinero.}}

\patron{Querer que alguien haga algo: てほしい}
  {V-て + ほしいです}
  {\ej{もっとゆっくり\ruby{話}{はな}してほしいです。}
    {Quiero que hables más despacio.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Di tres cosas que quieres hacer este año usando たいです.
  \item ¿Qué quieres tener? Usa 欲しいです.
  \item ¿Cuándo NO se puede usar たい? (pista: tercera persona)
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) (personal)\quad
2) (personal)\quad
3) Para hablar de los deseos de terceros se usa 〜たがっています (está queriendo hacer ~) en lugar de たい.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{欲}{よく}{ほ}{desear / codicia}{\ruby{欲しい}{ほしい} / \ruby{欲求}{よっきゅう}}
\kanjirow{夢}{む}{ゆめ}{sueño}{\ruby{夢}{ゆめ} / \ruby{夢中}{むちゅう}}
\kanjirow{目}{もく}{め}{ojo / meta}{\ruby{目標}{もくひょう} / \ruby{目的}{もくてき}}
\kanjirow{標}{ひょう}{しるべ}{señal / meta}{\ruby{目標}{もくひょう} / \ruby{標準}{ひょうじゅん}}
\kanjirow{将}{しょう}{まさ}{futuro / general}{\ruby{将来}{しょうらい} / \ruby{将棋}{しょうぎ}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/22-deseos.tex
git commit -m "content: add unidad 22 - deseos"
```

---

### Task 27: Unidad 23 — Dar y Recibir

**Files:**
- Create: `unidades/23-dar-recibir.tex`

- [ ] **Step 1: Write unidades/23-dar-recibir.tex**

```latex
\chapter{🎁 授受表現 — Dar y Recibir}
\unidadheader{23}{授受表現}{Dar y Recibir}{Expresar intercambio de objetos y favores}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{プレゼント}{—}{regalo}{sust.}
\vocabitem{花}{はな}{flor}{sust.}
\vocabitem{手紙}{てがみ}{carta}{sust.}
\vocabitem{お土産}{おみやげ}{souvenir / regalo de viaje}{sust.}
\vocabitem{贈る}{おくる}{enviar como regalo}{v. gr.1}
\vocabitem{受け取る}{うけとる}{recibir / aceptar}{v. gr.1}
\vocabitem{喜ぶ}{よろこぶ}{alegrarse}{v. gr.1}
\vocabitem{感謝する}{かんしゃする}{agradecer}{v. irr.}
\vocabitem{お世話になる}{おせわになる}{recibir cuidado/ayuda de}{expr.}
\vocabitem{返す}{かえす}{devolver}{v. gr.1}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\begin{tcolorbox}[phrasebox, title={🔄 Diagrama: あげる / もらう / くれる}]
\begin{verbatim}
  [Yo] ---あげます---> [Otro]   (yo doy a otro)
  [Yo] <--もらいます--- [Otro]   (yo recibo de otro)
  [Yo] <---くれます---- [Otro]   (otro da a mí)

  Clave: くれる siempre tiene a 私 (yo/mi grupo) como receptor.
\end{verbatim}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{\ruby{友}{とも}だちにプレゼントをあげました。}
  {Le di un regalo a mi amigo.}
\frase{お\ruby{母}{かあ}さんからセーターをもらいました。}
  {Recibí un suéter de mi mamá.}
\frase{\ruby{田中}{たなか}さんが\ruby{花}{はな}をくれました。}
  {El Sr. Tanaka me dio flores.}
\frase{〜してもらえますか？}{¿Me podrías hacer el favor de ~?}

\subsection*{⚙️ Gramática}

\patron{Dar a alguien: あげます}
  {A が B に もの を あげます}
  {\ej{\ruby{友達}{ともだち}に\ruby{本}{ほん}をあげました。}
    {Le di un libro a mi amigo.}}

\patron{Recibir de alguien: もらいます}
  {A が B に/から もの を もらいます}
  {\ej{せんせいに/からアドバイスをもらいました。}
    {Recibí un consejo del profesor.}}

\patron{Alguien me da: くれます}
  {B が A に もの を くれます (A = yo o mi grupo)}
  {\ej{\ruby{彼女}{かのじょ}がチョコをくれました。}
    {Mi novia me dio chocolate.}}

\patron{Favores con て形}
  {V-て + あげる / もらう / くれる}
  {\ej{\ruby{宿題}{しゅくだい}を\ruby{手伝}{てつだ}ってあげました。}
    {Le ayudé con su tarea.}
  \ej{\ruby{写真}{しゃしん}を\ruby{撮}{と}ってもらえますか？}
    {¿Me podrías tomar una foto?}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item ¿あげる o くれる? Tu amigo te da un libro → ?
  \item Pide un favor usando てもらえますか.
  \item Traduce: \ruby{母}{はは}が\ruby{料理}{りょうり}を\ruby{作}{つく}ってくれました。
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) くれる (\ruby{友達}{ともだち}が\ruby{本}{ほん}をくれました。)\quad
2) (personal)\quad
3) Mi mamá me cocinó (me hizo el favor de cocinar).
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{花}{か}{はな}{flor}{\ruby{花}{はな} / \ruby{花火}{はなび}}
\kanjirow{手}{しゅ}{て}{mano}{\ruby{手紙}{てがみ} / \ruby{手伝う}{てつだう}}
\kanjirow{紙}{し}{かみ}{papel}{\ruby{手紙}{てがみ} / \ruby{紙}{かみ}}
\kanjirow{贈}{ぞう}{おく}{regalar}{\ruby{贈}{おく}る / \ruby{贈り物}{おくりもの}}
\kanjirow{受}{じゅ}{う}{recibir}{\ruby{受}{う}ける / \ruby{受け取る}{うけとる}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/23-dar-recibir.tex
git commit -m "content: add unidad 23 - dar y recibir"
```

---

### Task 28: Unidad 24 — Forma Casual

**Files:**
- Create: `unidades/24-forma-casual.tex`

- [ ] **Step 1: Write unidades/24-forma-casual.tex**

```latex
\chapter{💬 普通形 — Forma Casual}
\unidadheader{24}{普通形}{Forma Casual}{Hablar de manera informal con amigos}

\begin{tcolorbox}[phrasebox, title={⚙️ Tabla de formas: polite vs casual}]
\begin{tabular}{lllll}
\toprule
 & \textbf{Pres. +} & \textbf{Pres. -} & \textbf{Pas. +} & \textbf{Pas. -} \\
\midrule
\textbf{Polite} & 食べます & 食べません & 食べました & 食べませんでした \\
\textbf{Casual} & 食べる & 食べない & 食べた & 食べなかった \\
\midrule
\textbf{Polite} & 静かです & 静かじゃない & 静かでした & 静かじゃなかった \\
\textbf{Casual} & 静かだ & 静かじゃない & 静かだった & 静かじゃなかった \\
\midrule
\textbf{Polite} & 学生です & 学生じゃない & 学生でした & 学生じゃなかった \\
\textbf{Casual} & 学生だ & 学生じゃない & 学生だった & 学生じゃなかった \\
\bottomrule
\end{tabular}
\end{tcolorbox}

\begin{tcolorbox}[vocabbox, title={📌 Partículas y expresiones conversacionales}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Expresión} & \textbf{Uso} & \textbf{Ejemplo} \\
\midrule
〜ね & confirmar / compartir & \ruby{今日}{きょう}、\ruby{暑}{あつ}いね。 \\
〜よ & afirmar / convencer & それ、\ruby{私}{わたし}のだよ。 \\
〜よね & confirmar algo que crees & \ruby{明日}{あした}\ruby{休}{やす}みだよね？ \\
〜かな & preguntarse / dudar & いくらかな？ \\
〜でしょ & ¿ves?, ¿verdad? & ほら、\ruby{言}{い}ったでしょ。 \\
〜じゃない & ¿no es que...? & あれ、\ruby{田中}{たなか}さんじゃない？ \\
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{ねえ、\ruby{今日}{きょう}ひま？}{Oye, ¿estás libre hoy?}
\frase{うん、\ruby{暇}{ひま}だよ。}{Sí, estoy libre.}
\frase{じゃあ、いっしょに\ruby{行}{い}かない？}{Entonces, ¿no vamos juntos?}
\frase{いいね！\ruby{行}{い}こう！}{¡Genial! ¡Vamos!}

\subsection*{⚙️ Gramática}

\patron{Forma casual: verbos}
  {辞書形 (dict.) = casual presente afirmativo}
  {\ej{\ruby{明日}{あした}、\ruby{映画}{えいが}\ruby{見}{み}る？}
    {¿Mañana ves una película?}
  \ej{え、\ruby{行}{い}かないの？}{¿Eh, no vas?}
  \ej{もう\ruby{食}{た}べた？}{¿Ya comiste?}}

\patron{Invitación casual: 〜ない？}
  {V-ない (neg.) + ？ = invitación informal}
  {\ej{いっしょに\ruby{ゲーム}{ゲーム}しない？}
    {¿No jugamos juntos un videojuego?}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Convierte a casual: \ruby{食}{た}べません → ? / \ruby{行}{い}きました → ?
  \item Escribe un mini-diálogo casual de 4 líneas entre amigos.
  \item ¿Cuándo NO debes usar la forma casual en japonés?
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) \ruby{食}{た}べない / \ruby{行}{い}った\quad
2) (personal)\quad
3) Con personas mayores, jefes, clientes, situaciones formales — usar siempre forma polite o keigo.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad (repaso)}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{普}{ふ}{—}{común / ordinario}{\ruby{普通}{ふつう} / \ruby{普段}{ふだん}}
\kanjirow{通}{つう}{とお・かよ}{pasar / comunicar}{\ruby{普通}{ふつう} / \ruby{通学}{つうがく}}
\kanjirow{話}{わ}{はな・はなし}{hablar / conversación}{\ruby{話}{はなし} / \ruby{電話}{でんわ}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/24-forma-casual.tex
git commit -m "content: add unidad 24 - forma casual"
```

---

### Task 29: Unidad 25 — Opinar y Citar

**Files:**
- Create: `unidades/25-opinar-citar.tex`

- [ ] **Step 1: Write unidades/25-opinar-citar.tex**

```latex
\chapter{💭 〜と思う・〜と言う — Opinar y Citar}
\unidadheader{25}{〜と思う・〜と言う}{Opinar y Citar}{Expresar opiniones y reportar lo que dijo alguien}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{意見}{いけん}{opinión}{sust.}
\vocabitem{考え}{かんがえ}{pensamiento / idea}{sust.}
\vocabitem{伝える}{つたえる}{transmitir / comunicar}{v. gr.2}
\vocabitem{知らせる}{しらせる}{notificar / informar}{v. gr.2}
\vocabitem{報告する}{ほうこくする}{reportar / informar}{v. irr.}
\vocabitem{確認する}{かくにんする}{confirmar / verificar}{v. irr.}
\vocabitem{理由}{りゆう}{razón / motivo}{sust.}
\vocabitem{〜らしい}{—}{parece que ~ (evidencia indirecta)}{aux.}
\vocabitem{〜そうだ}{—}{dicen que ~ (rumor / fuente ext.)}{aux.}
\vocabitem{〜によると}{—}{según ~ (fuente de info)}{expr.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{\ruby{私}{わたし}はこれでいいと\ruby{思}{おも}います。}
  {Creo que esto está bien.}
\frase{〜さんは\ruby{来}{こ}ないと\ruby{言}{い}っていました。}
  {El/la Sr/a. ~ dijo que no vendría.}
\frase{\ruby{天気予報}{てんきよほう}によると、\ruby{明日}{あした}は\ruby{雨}{あめ}だそうです。}
  {Según el pronóstico, dicen que mañana lloverá.}

\subsection*{⚙️ Gramática}

\patron{Dar una opinión: と思います}
  {普通形 + と思います}
  {\ej{\ruby{彼}{かれ}は\ruby{正直}{しょうじき}だと\ruby{思}{おも}います。}
    {Creo que él es honesto.}
  \ej{この\ruby{計画}{けいかく}はうまくいかないと\ruby{思}{おも}います。}
    {Creo que este plan no va a funcionar.}}

\patron{Citar lo que dijo alguien: と言っていました}
  {普通形 + と言っていました}
  {\ej{\ruby{田中}{たなか}さんは\ruby{明日}{あした}\ruby{来}{こ}ないと\ruby{言}{い}っていました。}
    {El Sr. Tanaka dijo que mañana no viene.}}

\patron{Rumor / Fuente externa: そうです}
  {普通形 + そうです (dicen que ~ / he escuchado que ~)}
  {\ej{あのレストランはおいしいそうです。}
    {Dicen que ese restaurante es bueno.}
  Nota: そうです del aspecto (〜そう = parece que va a ~) es diferente.}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Da tu opinión sobre estudiar japonés usando と思います.
  \item Reporta: Tu amigo dijo que el examen fue fácil.
  \item Traduce: \ruby{新聞}{しんぶん}によると、\ruby{明日}{あした}\ruby{選挙}{せんきょ}があるそうです。
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) (personal)\quad
2) \ruby{友達}{ともだち}は\ruby{試験}{しけん}が\ruby{簡単}{かんたん}だったと\ruby{言}{い}っていました。\quad
3) Según el periódico, dicen que mañana hay elecciones.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{思}{し}{おも}{pensar / creer}{\ruby{思}{おも}う / \ruby{思想}{しそう}}
\kanjirow{考}{こう}{かんが}{considerar}{\ruby{考}{かんが}える / \ruby{考え}{かんがえ}}
\kanjirow{意}{い}{—}{intención / significado}{\ruby{意見}{いけん} / \ruby{意味}{いみ}}
\kanjirow{言}{げん・ごん}{い・こと}{decir / palabras}{\ruby{言}{い}う / \ruby{言葉}{ことば}}
\kanjirow{報}{ほう}{しら}{reportar / noticia}{\ruby{報告}{ほうこく} / \ruby{情報}{じょうほう}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/25-opinar-citar.tex
git commit -m "content: add unidad 25 - opinar y citar"
```

---

### Task 30: Unidad 26 — Condicional I (と・ば)

**Files:**
- Create: `unidades/26-condicional-1.tex`

- [ ] **Step 1: Write unidades/26-condicional-1.tex**

```latex
\chapter{🔀 条件① — Condicional: と・ば}
\unidadheader{26}{条件①}{Condicional と・ば}{Expresar consecuencias naturales e hipótesis}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{押す}{おす}{presionar / empujar}{v. gr.1}
\vocabitem{引く}{ひく}{jalar / tirar}{v. gr.1}
\vocabitem{開く}{あく}{abrirse (intrans.)}{v. gr.1}
\vocabitem{閉まる}{しまる}{cerrarse (intrans.)}{v. gr.1}
\vocabitem{動く}{うごく}{moverse}{v. gr.1}
\vocabitem{止まる}{とまる}{detenerse}{v. gr.1}
\vocabitem{曲がる}{まがる}{doblar / girar}{v. gr.1}
\vocabitem{まっすぐ}{—}{recto / directo}{adv.}
\vocabitem{角}{かど}{esquina}{sust.}
\vocabitem{〜と〜}{—}{si ~ entonces ~ (natural)}{conj.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{このボタンを\ruby{押}{お}すと、\ruby{開}{あ}きますよ。}
  {Si presionas este botón, se abrirá.}
\frase{まっすぐ\ruby{行}{い}くと、\ruby{駅}{えき}がありますよ。}
  {Si vas recto, encontrarás la estación.}
\frase{お\ruby{金}{かね}があれば、\ruby{旅行}{りょこう}したいです。}
  {Si tuviera dinero, quisiera viajar.}

\subsection*{⚙️ Gramática}

\patron{Consecuencia natural: と}
  {普通形 + と + 結果 (consecuencia automática / instrucciones)}
  {Usado para: instrucciones, hechos naturales, rutas.
  NO para: deseos, peticiones, invitaciones.
  \ej{この\ruby{薬}{くすり}を\ruby{飲}{の}むと、\ruby{眠}{ねむ}くなります。}
    {Si tomas esta medicina, te dará sueño.}
  \ej{\ruby{右}{みぎ}に\ruby{曲}{ま}がると、\ruby{銀行}{ぎんこう}があります。}
    {Si doblas a la derecha, hay un banco.}}

\patron{Hipótesis: ば}
  {V-えば / adj-ければ / N-であれば}
  {Más formal y literario que と. Expresa condición hipotética.
  \ej{\ruby{春}{はる}になれば、\ruby{桜}{さくら}が\ruby{咲}{さ}きます。}
    {Cuando llegue la primavera, florecerán los cerezos.}
  \ej{\ruby{時間}{じかん}があれば、\ruby{手伝}{てつだ}います。}
    {Si tengo tiempo, te ayudaré.}
  \ej{\ruby{高}{たか}くなければ、\ruby{買}{か}います。}
    {Si no es caro, lo compraré.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Usa と para dar instrucciones de cómo llegar a algún lugar.
  \item ¿と o ば? Esta oración: 春\_\_なる\_\_、暖かくなります。
  \item Traduce: \ruby{右}{みぎ}に\ruby{曲}{ま}がれば、\ruby{学校}{がっこう}が\ruby{見}{み}えます。
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) (personal)\quad
2) と (\ruby{春}{はる}になると、\ruby{暖}{あたた}かくなります。)\quad
3) Si doblas a la derecha, verás la escuela.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{押}{おう}{お}{presionar}{\ruby{押}{お}す / \ruby{押入}{おしい}れ}
\kanjirow{引}{いん}{ひ}{jalar}{\ruby{引}{ひ}く / \ruby{引越}{ひっこ}し}
\kanjirow{動}{どう}{うご}{mover(se)}{\ruby{動}{うご}く / \ruby{運動}{うんどう}}
\kanjirow{止}{し}{と・や}{detener(se)}{\ruby{止}{と}まる / \ruby{中止}{ちゅうし}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/26-condicional-1.tex
git commit -m "content: add unidad 26 - condicional to-ba"
```

---

### Task 31: Unidad 27 — Condicional II (たら・なら)

**Files:**
- Create: `unidades/27-condicional-2.tex`

- [ ] **Step 1: Write unidades/27-condicional-2.tex**

```latex
\chapter{🔀 条件② — Condicional: たら・なら}
\unidadheader{27}{条件②}{Condicional たら・なら}{Hablar de situaciones hipotéticas y dar consejos}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{もし}{—}{si (hipotético)}{conj.}
\vocabitem{〜場合}{ばあい}{en caso de ~ / si ~}{sust.}
\vocabitem{〜時}{とき}{cuando ~ / en el momento de ~}{sust.}
\vocabitem{暇}{ひま}{tiempo libre / sin plan}{adj-な/sust.}
\vocabitem{急に}{きゅうに}{de repente / súbitamente}{adv.}
\vocabitem{相談する}{そうだんする}{consultar / pedir consejo}{v. irr.}
\vocabitem{選ぶ}{えらぶ}{elegir / seleccionar}{v. gr.1}
\vocabitem{迷う}{まよう}{dudar / perderse}{v. gr.1}
\vocabitem{後悔する}{こうかいする}{arrepentirse}{v. irr.}
\vocabitem{チャンス}{—}{oportunidad}{sust.}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{もし\ruby{宝}{たから}くじに\ruby{当}{あ}たったら、\ruby{何}{なに}をしますか？}
  {Si ganaras la lotería, ¿qué harías?}
\frase{\ruby{日本}{にほん}に\ruby{行}{い}くなら、\ruby{京都}{きょうと}がおすすめです。}
  {Si vas a Japón, te recomiendo Kioto.}
\frase{\ruby{困}{こま}ったら、\ruby{相談}{そうだん}してください。}
  {Si tienes problemas, consúltame.}

\subsection*{⚙️ Gramática}

\patron{Condición completada: たら}
  {V-た + ら (cuando/si se completa la acción)}
  {Más versátil: acciones, estados, pasado hipotético.
  \ej{\ruby{家}{いえ}に\ruby{帰}{かえ}ったら、\ruby{電話}{でんわ}してください。}
    {Cuando llegues a casa, llámame.}
  \ej{もし100\ruby{万円}{まんえん}あったら、\ruby{旅行}{りょこう}します。}
    {Si tuviera 1 millón de yen, viajaría.}}

\patron{Condición contextual: なら}
  {普通形 + なら (si es el caso que ~, en ese contexto)}
  {なら = recomendación basada en lo que el otro mencionó.
  \ej{\ruby{日本語}{にほんご}を\ruby{勉強}{べんきょう}するなら、アニメがいいですよ。}
    {Si vas a estudiar japonés, el anime es bueno.}
  \ej{あの\ruby{映画}{えいが}を\ruby{見}{み}るなら、\ruby{早}{はや}く\ruby{行}{い}ったほうがいい。}
    {Si vas a ver esa película, mejor ve pronto.}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Usa たら para decir qué harás cuando termines de estudiar.
  \item Da un consejo con なら a alguien que quiere aprender a cocinar.
  \item ¿Cuál es la diferencia principal entre たら y なら?
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) \ruby{勉強}{べんきょう}が\ruby{終}{お}わったら、(personal)\quad
2) \ruby{料理}{りょうり}を\ruby{勉強}{べんきょう}するなら、(recomendación personal)\quad
3) たら = acción/situación que se completa primero; なら = recomendación basada en contexto dado por el interlocutor.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{場}{じょう}{ば}{lugar / situación}{\ruby{場合}{ばあい} / \ruby{場所}{ばしょ}}
\kanjirow{急}{きゅう}{いそ・にわか}{urgente / de repente}{\ruby{急}{きゅう}に / \ruby{急行}{きゅうこう}}
\kanjirow{選}{せん}{えら}{elegir}{\ruby{選}{えら}ぶ / \ruby{選択}{せんたく}}
\kanjirow{迷}{めい}{まよ}{perderse / dudar}{\ruby{迷}{まよ}う / \ruby{迷路}{めいろ}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/27-condicional-2.tex
git commit -m "content: add unidad 27 - condicional tara-nara"
```

---

### Task 32: Unidad 28 — Voz Pasiva

**Files:**
- Create: `unidades/28-voz-pasiva.tex`

- [ ] **Step 1: Write unidades/28-voz-pasiva.tex**

```latex
\chapter{🔄 受身形 — Voz Pasiva}
\unidadheader{28}{受身形}{Voz Pasiva}{Expresar acciones recibidas}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{怒る}{おこる・おこられる}{enojarse / ser regañado}{v. gr.1}
\vocabitem{ほめる}{—}{elogiar}{v. gr.2}
\vocabitem{叱る}{しかる}{regañar / reprender}{v. gr.1}
\vocabitem{助ける}{たすける}{ayudar / rescatar}{v. gr.2}
\vocabitem{守る}{まもる}{proteger}{v. gr.1}
\vocabitem{批判する}{ひはんする}{criticar}{v. irr.}
\vocabitem{評価する}{ひょうかする}{evaluar / valorar}{v. irr.}
\vocabitem{尊敬する}{そんけいする}{respetar}{v. irr.}
\vocabitem{信頼する}{しんらいする}{confiar en}{v. irr.}
\vocabitem{傷つける}{きずつける}{herir / lastimar}{v. gr.2}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\begin{tcolorbox}[phrasebox, title={⚙️ Conjugación: Forma pasiva}]
\begin{tabular}{llll}
\toprule
\textbf{Grupo} & \textbf{Regla} & \textbf{Original} & \textbf{Pasiva} \\
\midrule
1 (う→あ段+れる) & う→あれる & \ruby{読}{よ}む & \ruby{読}{よ}まれる \\
2 (〜る → 〜られる) & る→られる & \ruby{食}{た}べる & \ruby{食}{た}べられる \\
3 & memorizar & する / くる & される / こられる \\
\bottomrule
\end{tabular}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{\ruby{先生}{せんせい}にほめられました。}{El profesor me elogió. (me fue elogiado)}
\frase{あの\ruby{映画}{えいが}は\ruby{世界中}{せかいじゅう}で\ruby{見}{み}られています。}
  {Esa película es vista en todo el mundo.}
\frase{\ruby{財布}{さいふ}を\ruby{盗}{ぬす}まれました。}{Me robaron la cartera.}

\subsection*{⚙️ Gramática}

\patron{Pasiva directa}
  {A が B に V-られる (A recibe la acción de B)}
  {\ej{\ruby{私}{わたし}は\ruby{先生}{せんせい}にほめられました。}
    {El profesor me elogió (lit. fui elogiado por el profesor).}
  \ej{この\ruby{本}{ほん}は\ruby{多く}{おおく}の\ruby{人}{ひと}に\ruby{読}{よ}まれています。}
    {Este libro es leído por muchas personas.}}

\patron{Pasiva de molestia (indirect passive)}
  {A が B に C を V-られる (molesta al sujeto)}
  {\ej{\ruby{電車}{でんしゃ}の\ruby{中}{なか}で\ruby{足}{あし}を\ruby{踏}{ふ}まれました。}
    {Me pisaron el pie en el tren. (me fue pisado, molestia)}
  \ej{\ruby{雨}{あめ}に\ruby{降}{ふ}られて、\ruby{濡}{ぬ}れました。}
    {Me cayó la lluvia y me mojé. (molestia de la lluvia)}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item Convierte a pasiva: 先生が学生をほめる → ?
  \item ¿Cuándo se usa la pasiva de molestia?
  \item Traduce: \ruby{子}{こ}どもの\ruby{時}{とき}、よく\ruby{母}{はは}に\ruby{叱}{しか}られました。
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) \ruby{学生}{がくせい}は\ruby{先生}{せんせい}にほめられた。\quad
2) Cuando la acción de otro te afecta negativamente.\quad
3) Cuando era niño/a, mi mamá me regañaba (era regañado) seguido.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{怒}{ど}{おこ・いか}{enojarse}{\ruby{怒}{おこ}る / \ruby{怒り}{いかり}}
\kanjirow{助}{じょ}{たす}{ayudar / rescatar}{\ruby{助}{たす}ける / \ruby{助言}{じょげん}}
\kanjirow{守}{しゅ}{まも・もり}{proteger / guardar}{\ruby{守}{まも}る / \ruby{守備}{しゅび}}
\kanjirow{批}{ひ}{—}{criticar}{\ruby{批判}{ひはん} / \ruby{批評}{ひひょう}}
\kanjirow{評}{ひょう}{—}{evaluar}{\ruby{評価}{ひょうか} / \ruby{評判}{ひょうばん}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/28-voz-pasiva.tex
git commit -m "content: add unidad 28 - voz pasiva"
```

---

### Task 33: Unidad 29 — Keigo Intro

**Files:**
- Create: `unidades/29-keigo-intro.tex`

- [ ] **Step 1: Write unidades/29-keigo-intro.tex**

```latex
\chapter{🎩 敬語入門 — Japonés Formal Básico}
\unidadheader{29}{敬語入門}{Japonés Formal Básico}{Comunicarse en situaciones formales}

\begin{tcolorbox}[vocabbox, title={📌 Vocabulario Nuevo}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Japonés} & \textbf{Español} & \textbf{Tipo} \\
\midrule
\vocabitem{お客様}{おきゃくさま}{cliente / visita (formal)}{sust.}
\vocabitem{担当者}{たんとうしゃ}{persona a cargo}{sust.}
\vocabitem{上司}{じょうし}{jefe / superior}{sust.}
\vocabitem{承知する}{しょうちする}{entender / aceptar (kenjou)}{v. irr.}
\vocabitem{拝見する}{はいけんする}{ver / leer (kenjou)}{v. irr.}
\vocabitem{伺う}{うかがう}{preguntar / visitar (kenjou)}{v. gr.1}
\vocabitem{参る}{まいる}{ir / venir (kenjou)}{v. gr.1}
\vocabitem{おります}{—}{estar (kenjou de います)}{v. irr.}
\vocabitem{ございます}{—}{ser / estar / haber (formal)}{v. irr.}
\vocabitem{いただく}{—}{recibir / comer (kenjou)}{v. gr.1}
\bottomrule
\end{tabularx}
\end{tcolorbox}

\begin{tcolorbox}[phrasebox, title={⚙️ Los tres niveles de keigo}]
\begin{tabular}{lll}
\toprule
\textbf{Tipo} & \textbf{Para qué} & \textbf{Ejemplo} \\
\midrule
尊敬語 そんけいご & Elevar acciones del OTRO & お\ruby{読}{よ}みになりますか？ \\
謙譲語 けんじょうご & Bajar las propias acciones & \ruby{拝見}{はいけん}します \\
丁寧語 ていねいご & Lenguaje cortés general & ございます / です・ます \\
\bottomrule
\end{tabular}
\end{tcolorbox}

\subsection*{🗣️ Frases Clave}

\frase{少々お待ちください。}{Espere un momento, por favor. (formal)}
\frase{承知いたしました。}{Entendido. / De acuerdo. (muy formal)}
\frase{ただいま担当者が参ります。}
  {Ahora mismo viene la persona a cargo.}
\frase{よろしければ、ご連絡いただけますか？}
  {Si no le molesta, ¿podría contactarme?}

\subsection*{⚙️ Gramática}

\patron{Sonkei-go: elevar al otro}
  {お + V(ます-stem) + になります}
  {\ej{お\ruby{読}{よ}みになりましたか？}
    {¿Lo ha leído (usted)?}
  \ej{お\ruby{分}{わ}かりになりますか？}
    {¿Lo entiende (usted)?}}

\patron{Kenjou-go: humillar las propias acciones}
  {Verbos especiales kenjou: いただく・伺う・参る・申す・おる}
  {\ej{こちらの\ruby{資料}{しりょう}を\ruby{拝見}{はいけん}いたしました。}
    {He tenido la oportunidad de ver este documento.}
  \ej{\ruby{明日}{あした}、\ruby{御社}{おんしゃ}に\ruby{伺}{うかが}います。}
    {Mañana iré a visitar su empresa.}}

\patron{Teineigo: ございます}
  {ございます = forma muy formal de あります / です}
  {\ej{こちらに\ruby{資料}{しりょう}がございます。}
    {Aquí hay/están los documentos. (muy formal)}
  \ej{ありがとうございます。}{Muchas gracias. (ya conocido)}}

\begin{tcolorbox}[ejerciciobox, title={📝 Ejercicios Rápidos}]
\begin{enumerate}
  \item ¿Cómo dices "iré" de manera humilde (kenjou)?
  \item Convierte a formal: 見ましたか？
  \item ¿Cuándo usarías keigo en tu vida cotidiana?
\end{enumerate}
\vspace{0.4em}
\textbf{Respuestas:}
1) \ruby{参}{まい}ります。\quad
2) \ruby{御覧}{ごらん}になりましたか？ (sonkei) / \ruby{拝見}{はいけん}しましたか？ (kenjou propio)\quad
3) Con jefes, clientes, personas mayores, en entrevistas, en tiendas y restaurantes.
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Kanjis de la Unidad}]
\begin{tabularx}{\linewidth}{cllXX}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} \\
\midrule
\kanjirow{様}{よう}{さま}{forma / señor (honorífico)}{\ruby{様子}{ようす} / お\ruby{客様}{きゃくさま}}
\kanjirow{拝}{はい}{おが}{adorar / humilde}{\ruby{拝見}{はいけん} / \ruby{拝啓}{はいけい}}
\kanjirow{承}{しょう}{うけたまわ}{aceptar / entender}{\ruby{承知}{しょうち} / \ruby{承認}{しょうにん}}
\kanjirow{参}{さん}{まい}{ir (kenjou)}{\ruby{参}{まい}る / \ruby{参加}{さんか}}
\kanjirow{丁}{てい}{—}{cortés / respetuoso}{\ruby{丁寧}{ていねい} / \ruby{丁度}{ちょうど}}
\bottomrule
\end{tabularx}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/29-keigo-intro.tex
git commit -m "content: add unidad 29 - keigo intro"
```

---

### Task 34: Unidad 30 — Repaso General

**Files:**
- Create: `unidades/30-repaso-general.tex`

- [ ] **Step 1: Write unidades/30-repaso-general.tex**

```latex
\chapter{🏆 総復習 — Repaso General N5→N4}
\unidadheader{30}{総復習}{Repaso General}{Consolidar todo lo aprendido N5→N4}

\begin{tcolorbox}[phrasebox, title={📋 Resumen de patrones N5→N4}]
\begin{tabular}{lll}
\toprule
\textbf{Patrón} & \textbf{Unidad} & \textbf{Ejemplo clave} \\
\midrule
〜は〜です & 01 & \ruby{私}{わたし}は\ruby{学生}{がくせい}です。 \\
あります/います & 04 & \ruby{駅}{えき}にあります。 \\
ます形 & 05 & \ruby{食}{た}べます。 \\
V-て + ください & 14 & \ruby{待}{ま}ってください。 \\
〜ている & 15 & \ruby{住}{す}んでいます。 \\
〜たことがある & 16 & \ruby{行}{い}ったことがあります。 \\
〜つもり / 予定 & 17 & \ruby{行}{い}くつもりです。 \\
〜より〜の方が & 18 & Aの\ruby{方}{ほう}が\ruby{好}{す}きです。 \\
V-可能形 & 21 & \ruby{泳}{およ}げます。 \\
〜たい / 欲しい & 22 & \ruby{行}{い}きたいです。 \\
あげる/もらう/くれる & 23 & くれました。 \\
〜と思います & 25 & いいと\ruby{思}{おも}います。 \\
〜たら / なら & 27 & \ruby{行}{い}ったら... \\
受身形 & 28 & ほめられました。 \\
\bottomrule
\end{tabular}
\end{tcolorbox}

\subsection*{📝 Ejercicios de Repaso Integrado}

\begin{tcolorbox}[ejerciciobox, title={🏋️ Nivel 1: Traducción directa}]
\begin{enumerate}
  \item Traduce: \ruby{毎朝}{まいあさ}7\ruby{時}{じ}に\ruby{起}{お}きて、コーヒーを\ruby{飲}{の}みながら\ruby{新聞}{しんぶん}を\ruby{読}{よ}みます。
  \item Traduce: もし\ruby{時間}{じかん}があれば、\ruby{日本}{にほん}に\ruby{行}{い}きたいです。
  \item Traduce: \ruby{先生}{せんせい}にほめられてとても\ruby{嬉}{うれ}しかったです。
\end{enumerate}
\end{tcolorbox}

\begin{tcolorbox}[ejerciciobox, title={🏋️ Nivel 2: Construcción de oraciones}]
\begin{enumerate}
  \item Describe tu rutina usando ます形, てから, y ながら.
  \item Cuenta una experiencia usando たことがあります.
  \item Da una recomendación a un amigo usando なら.
  \item Expresa un deseo futuro usando つもりです y たいです.
\end{enumerate}
\end{tcolorbox}

\begin{tcolorbox}[ejerciciobox, title={🏋️ Nivel 3: Mini-diálogo}]
Escribe un diálogo de 8-10 líneas en japonés que incluya:
\begin{itemize}
  \item Una presentación o saludo
  \item Una invitación usando ませんか
  \item Una comparación usando より
  \item Una expresión de deseo usando たいです
  \item Un condicional con たら o なら
\end{itemize}
\end{tcolorbox}

\begin{tcolorbox}[kanjibox, title={🀄 Mini-índice: Kanjis Esenciales N5→N4}]
\small
\begin{tabular}{ccccccccccc}
名 & 前 & 学 & 生 & 先 & 時 & 分 & 年 & 月 & 日 & 今 \\
右 & 左 & 近 & 駅 & 起 & 寝 & 食 & 飲 & 毎 & 好 & 嫌 \\
肉 & 魚 & 水 & 安 & 高 & 大 & 小 & 新 & 古 & 難 & 楽 \\
父 & 母 & 兄 & 姉 & 弟 & 妹 & 見 & 聞 & 買 & 読 & 書 \\
天 & 気 & 雨 & 雪 & 入 & 出 & 持 & 着 & 住 & 知 & 疲 \\
経 & 験 & 度 & 回 & 予 & 定 & 旅 & 一 & 番 & 同 & 電 \\
車 & 飛 & 機 & 乗 & 頭 & 目 & 歯 & 足 & 痛 & 泳 & 歌 \\
運 & 転 & 欲 & 夢 & 花 & 手 & 紙 & 思 & 言 & 意 & 報 \\
押 & 引 & 動 & 止 & 場 & 急 & 選 & 怒 & 助 & 守 & 様 \\
\end{tabular}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add unidades/30-repaso-general.tex
git commit -m "content: add unidad 30 - repaso general"
```

---

## Phase 5: Apéndices

### Task 35: Apéndice — Mapa de Partículas

**Files:**
- Create: `apendices/mapa-particulas.tex`

- [ ] **Step 1: Write apendices/mapa-particulas.tex**

```latex
% apendices/mapa-particulas.tex
\chapter{🗺️ Mapa de Partículas}

\begin{tcolorbox}[vocabbox, title={📌 Partículas esenciales}]
\begin{tabularx}{\linewidth}{llX}
\toprule
\textbf{Part.} & \textbf{Función principal} & \textbf{Ejemplo} \\
\midrule
は (wa) & Tema del discurso & \ruby{私}{わたし}\textbf{は}\ruby{学生}{がくせい}です。 \\
が (ga) & Sujeto gramatical / énfasis & \ruby{猫}{ねこ}\textbf{が}います。 \\
を (wo) & Objeto directo & \ruby{本}{ほん}\textbf{を}\ruby{読}{よ}む。 \\
に (ni) & Destino / existencia / tiempo & \ruby{学校}{がっこう}\textbf{に}\ruby{行}{い}く。 \\
で (de) & Lugar de acción / medio & \ruby{図書館}{としょかん}\textbf{で}\ruby{勉強}{べんきょう}する。 \\
へ (e) & Dirección (más literario que に) & \ruby{日本}{にほん}\textbf{へ}。 \\
の (no) & Posesión / modificación & \ruby{私}{わたし}\textbf{の}\ruby{本}{ほん}。 \\
と (to) & Y (enumeración) / con / cita & \ruby{田中}{たなか}さん\textbf{と}。 \\
も (mo) & También / ni... tampoco & \ruby{私}{わたし}\textbf{も}。 \\
か (ka) & Pregunta & \ruby{学生}{がくせい}です\textbf{か}？ \\
よ (yo) & Afirmación / información nueva & そうです\textbf{よ}。 \\
ね (ne) & Confirmación / acuerdo & いいです\textbf{ね}。 \\
から (kara) & Desde / porque & \ruby{東京}{とうきょう}\textbf{から}。 \\
まで (made) & Hasta & \ruby{駅}{えき}\textbf{まで}。 \\
より (yori) & Más que (comparación) & A\textbf{より}B。 \\
\bottomrule
\end{tabularx}
\end{tcolorbox}

\begin{tcolorbox}[grammarbox, title={⚠️ は vs が — La distinción clave}]
\begin{tabular}{lll}
\toprule
\textbf{Uso} & \textbf{は} & \textbf{が} \\
\midrule
Introducir tema & ✓ & ✗ \\
Nueva información & ✗ & ✓ \\
Respuesta a ¿quién? & ✗ & ✓ \\
Contraste & ✓ & ✗ \\
Con 好き・嫌い・できる & ✗ & ✓ \\
\bottomrule
\end{tabular}\\[6pt]
\ej{\ruby{猫}{ねこ}\textbf{は}\ruby{魚}{さかな}が\ruby{好}{す}きです。}{Los gatos (tema) les gustan los pescados (objeto).}
\ej{\ruby{猫}{ねこ}\textbf{が}います。}{Hay un gato. (nueva información, énfasis)}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add apendices/mapa-particulas.tex
git commit -m "content: add appendix mapa de particulas"
```

---

### Task 36: Apéndice — Tablas de Conjugación

**Files:**
- Create: `apendices/tablas-conjugacion.tex`

- [ ] **Step 1: Write apendices/tablas-conjugacion.tex**

```latex
% apendices/tablas-conjugacion.tex
\chapter{🔢 Tablas de Conjugación}

\begin{tcolorbox}[vocabbox, title={📌 Verbos Grupo 1 (う-verbos) — 書く}]
\begin{tabular}{lll}
\toprule
\textbf{Forma} & \textbf{Afirmativo} & \textbf{Negativo} \\
\midrule
Presente polite & \ruby{書}{か}きます & \ruby{書}{か}きません \\
Pasado polite & \ruby{書}{か}きました & \ruby{書}{か}きませんでした \\
Presente casual & \ruby{書}{か}く & \ruby{書}{か}かない \\
Pasado casual & \ruby{書}{か}いた & \ruby{書}{か}かなかった \\
て形 & \ruby{書}{か}いて & — \\
た形 & \ruby{書}{か}いた & — \\
可能形 & \ruby{書}{か}ける & \ruby{書}{か}けない \\
受身形 & \ruby{書}{か}かれる & — \\
意向形 & \ruby{書}{か}こう & — \\
\bottomrule
\end{tabular}
\end{tcolorbox}

\begin{tcolorbox}[vocabbox, title={📌 Verbos Grupo 2 (る-verbos) — 食べる}]
\begin{tabular}{lll}
\toprule
\textbf{Forma} & \textbf{Afirmativo} & \textbf{Negativo} \\
\midrule
Presente polite & \ruby{食}{た}べます & \ruby{食}{た}べません \\
Pasado polite & \ruby{食}{た}べました & \ruby{食}{た}べませんでした \\
Presente casual & \ruby{食}{た}べる & \ruby{食}{た}べない \\
Pasado casual & \ruby{食}{た}べた & \ruby{食}{た}べなかった \\
て形 & \ruby{食}{た}べて & — \\
可能形 & \ruby{食}{た}べられる & \ruby{食}{た}べられない \\
受身形 & \ruby{食}{た}べられる & — \\
意向形 & \ruby{食}{た}べよう & — \\
\bottomrule
\end{tabular}
\end{tcolorbox}

\begin{tcolorbox}[vocabbox, title={📌 Verbos Irregulares — する / くる}]
\begin{tabular}{lll}
\toprule
\textbf{Forma} & \textbf{する} & \textbf{くる} \\
\midrule
Presente polite & します & きます \\
Pasado polite & しました & きました \\
Negativo pres. & しません & きません \\
Presente casual & する & くる \\
Pasado casual & した & きた \\
て形 & して & きて \\
可能形 & できる & こられる \\
受身形 & される & こられる \\
意向形 & しよう & こよう \\
\bottomrule
\end{tabular}
\end{tcolorbox}

\begin{tcolorbox}[grammarbox, title={⚙️ Adjetivos — 高い (い) vs 便利 (な)}]
\begin{tabular}{lll}
\toprule
\textbf{Forma} & \textbf{高い (adj-い)} & \textbf{便利 (adj-な)} \\
\midrule
Presente + & \ruby{高}{たか}いです & \ruby{便利}{べんり}です \\
Presente - & \ruby{高}{たか}くないです & \ruby{便利}{べんり}じゃないです \\
Pasado + & \ruby{高}{たか}かったです & \ruby{便利}{べんり}でした \\
Pasado - & \ruby{高}{たか}くなかったです & \ruby{便利}{べんり}じゃなかったです \\
+ nombre & \ruby{高}{たか}い〜 & \ruby{便利}{べんり}な〜 \\
\bottomrule
\end{tabular}
\end{tcolorbox}
```

- [ ] **Step 2: Commit**

```bash
git add apendices/tablas-conjugacion.tex
git commit -m "content: add appendix tablas de conjugacion"
```

---

### Task 37: Apéndice — Índice de Kanjis

**Files:**
- Create: `apendices/indice-kanjis.tex`

- [ ] **Step 1: Write apendices/indice-kanjis.tex**

```latex
% apendices/indice-kanjis.tex
\chapter{📇 Índice de Kanjis N5→N4}

{\small Este índice lista todos los kanjis introducidos en estas notas, con su primera unidad de aparición.}

\vspace{0.5em}

\begin{longtable}{cllllc}
\toprule
\textbf{Kanji} & \textbf{On} & \textbf{Kun} & \textbf{Significado} & \textbf{Vocab} & \textbf{Unidad} \\
\midrule
\endhead
% U01
\ruby{名}{} & めい & な & nombre & \ruby{名前}{なまえ} & 01 \\
\ruby{前}{} & ぜん & まえ & frente/antes & \ruby{名前}{なまえ} & 01 \\
\ruby{学}{} & がく & まな & estudiar & \ruby{学生}{がくせい} & 01 \\
\ruby{生}{} & せい & い & vida/nacer & \ruby{先生}{せんせい} & 01 \\
\ruby{先}{} & せん & さき & antes/punta & \ruby{先生}{せんせい} & 01 \\
% U02
\ruby{時}{} & じ & とき & tiempo/hora & \ruby{時間}{じかん} & 02 \\
\ruby{分}{} & ふん & わ & minuto & \ruby{五分}{ごふん} & 02 \\
\ruby{年}{} & ねん & とし & año & \ruby{今年}{ことし} & 02 \\
\ruby{月}{} & がつ & つき & mes/luna & \ruby{一月}{いちがつ} & 02 \\
\ruby{日}{} & にち & ひ & día/sol & \ruby{今日}{きょう} & 02 \\
\ruby{今}{} & こん & いま & ahora & \ruby{今日}{きょう} & 02 \\
% U03
\ruby{何}{} & か & なに & qué & \ruby{何}{なに} & 03 \\
\ruby{誰}{} & すい & だれ & quién & \ruby{誰}{だれ} & 03 \\
\ruby{物}{} & もの & ぶつ & cosa & \ruby{物}{もの} & 03 \\
% U04
\ruby{駅}{} & えき & — & estación & \ruby{駅}{えき} & 04 \\
\ruby{右}{} & ゆう & みぎ & derecha & \ruby{右}{みぎ} & 04 \\
\ruby{左}{} & さ & ひだり & izquierda & \ruby{左}{ひだり} & 04 \\
\ruby{近}{} & きん & ちか & cerca & \ruby{近く}{ちかく} & 04 \\
% U05
\ruby{起}{} & き & お & levantarse & \ruby{起}{お}きる & 05 \\
\ruby{寝}{} & しん & ね & dormir & \ruby{寝}{ね}る & 05 \\
\ruby{食}{} & しょく & た & comer & \ruby{食}{た}べる & 05 \\
\ruby{飲}{} & いん & の & beber & \ruby{飲}{の}む & 05 \\
\ruby{毎}{} & まい & — & cada/todo & \ruby{毎日}{まいにち} & 05 \\
% U06
\ruby{好}{} & こう & す & gustar & \ruby{好き}{すき} & 06 \\
\ruby{嫌}{} & けん & きら & desagradar & \ruby{嫌い}{きらい} & 06 \\
\ruby{音}{} & おん & おと & sonido & \ruby{音楽}{おんがく} & 06 \\
\ruby{楽}{} & がく & たの & música/placer & \ruby{音楽}{おんがく} & 06 \\
\ruby{映}{} & えい & うつ & reflejar & \ruby{映画}{えいが} & 06 \\
% U07
\ruby{肉}{} & にく & — & carne & \ruby{肉}{にく} & 07 \\
\ruby{魚}{} & ぎょ & さかな & pescado & \ruby{魚}{さかな} & 07 \\
\ruby{野}{} & や & の & campo & \ruby{野菜}{やさい} & 07 \\
\ruby{菜}{} & さい & な & vegetal & \ruby{野菜}{やさい} & 07 \\
\ruby{水}{} & すい & みず & agua & \ruby{水}{みず} & 07 \\
% U08
\ruby{安}{} & あん & やす & barato & \ruby{安い}{やすい} & 08 \\
\ruby{高}{} & こう & たか & caro/alto & \ruby{高い}{たかい} & 08 \\
\ruby{大}{} & だい & おお & grande & \ruby{大きい}{おおきい} & 08 \\
\ruby{小}{} & しょう & ちい & pequeño & \ruby{小さい}{ちいさい} & 08 \\
\ruby{色}{} & しょく & いろ & color & \ruby{色}{いろ} & 08 \\
% U09
\ruby{新}{} & しん & あたら & nuevo & \ruby{新しい}{あたらしい} & 09 \\
\ruby{古}{} & こ & ふる & viejo & \ruby{古い}{ふるい} & 09 \\
\ruby{難}{} & なん & むずか & difícil & \ruby{難しい}{むずかしい} & 09 \\
\ruby{便}{} & べん & たよ & conveniente & \ruby{便利}{べんり} & 09 \\
% U10
\ruby{父}{} & ふ & ちち & padre & \ruby{父}{ちち} & 10 \\
\ruby{母}{} & ぼ & はは & madre & \ruby{母}{はは} & 10 \\
\ruby{兄}{} & けい & あに & hermano mayor & \ruby{兄}{あに} & 10 \\
\ruby{姉}{} & し & あね & hermana mayor & \ruby{姉}{あね} & 10 \\
\ruby{弟}{} & てい & おとうと & hermano menor & \ruby{弟}{おとうと} & 10 \\
\ruby{妹}{} & まい & いもうと & hermana menor & \ruby{妹}{いもうと} & 10 \\
% U11
\ruby{見}{} & けん & み & ver & \ruby{見}{み}る & 11 \\
\ruby{聞}{} & もん & き & escuchar & \ruby{聞}{き}く & 11 \\
\ruby{買}{} & ばい & か & comprar & \ruby{買}{か}う & 11 \\
\ruby{読}{} & どく & よ & leer & \ruby{読}{よ}む & 11 \\
\ruby{書}{} & しょ & か & escribir & \ruby{書}{か}く & 11 \\
% U12
\ruby{天}{} & てん & あめ & cielo & \ruby{天気}{てんき} & 12 \\
\ruby{気}{} & き & — & ánimo/clima & \ruby{天気}{てんき} & 12 \\
\ruby{雨}{} & う & あめ & lluvia & \ruby{雨}{あめ} & 12 \\
\ruby{雪}{} & せつ & ゆき & nieve & \ruby{雪}{ゆき} & 12 \\
\ruby{暑}{} & しょ & あつ & caluroso & \ruby{暑い}{あつい} & 12 \\
\ruby{寒}{} & かん & さむ & frío & \ruby{寒い}{さむい} & 12 \\
% U13
\ruby{入}{} & にゅう & はい & entrar & \ruby{入}{はい}る & 13 \\
\ruby{出}{} & しゅつ & で & salir & \ruby{出}{で}る & 13 \\
\ruby{持}{} & じ & も & sostener & \ruby{持}{も}つ & 13 \\
\ruby{借}{} & しゃく & か & pedir prest. & \ruby{借}{か}りる & 13 \\
\ruby{洗}{} & せん & あら & lavar & \ruby{洗}{あら}う & 13 \\
% U14
\ruby{使}{} & し & つか & usar & \ruby{使}{つか}う & 14 \\
\ruby{置}{} & ち & お & poner & \ruby{置}{お}く & 14 \\
\ruby{急}{} & きゅう & いそ & urgente & \ruby{急}{いそ}ぐ & 14 \\
\ruby{休}{} & きゅう & やす & descansar & \ruby{休}{やす}む & 14 \\
\ruby{始}{} & し & はじ & comenzar & \ruby{始}{はじ}める & 14 \\
% U15
\ruby{着}{} & ちゃく & き & ponerse ropa & \ruby{着}{き}る & 15 \\
\ruby{住}{} & じゅう & す & vivir & \ruby{住}{す}む & 15 \\
\ruby{知}{} & ち & し & saber & \ruby{知}{し}る & 15 \\
\ruby{疲}{} & ひ & つか & cansarse & \ruby{疲}{つか}れる & 15 \\
\ruby{終}{} & しゅう & お & terminar & \ruby{終}{お}わる & 15 \\
% U16
\ruby{経}{} & けい & へ & experiencia & \ruby{経験}{けいけん} & 16 \\
\ruby{験}{} & けん & — & examen & \ruby{経験}{けいけん} & 16 \\
\ruby{度}{} & ど & たび & vez/grado & \ruby{一度}{いちど} & 16 \\
\ruby{回}{} & かい & まわ & vuelta/vez & \ruby{三回}{さんかい} & 16 \\
\ruby{初}{} & しょ & はじ & primero & \ruby{初}{はじ}めて & 16 \\
% U17
\ruby{予}{} & よ & — & de antemano & \ruby{予定}{よてい} & 17 \\
\ruby{定}{} & てい & さだ & establecido & \ruby{予定}{よてい} & 17 \\
\ruby{計}{} & けい & はか & calcular & \ruby{計画}{けいかく} & 17 \\
\ruby{旅}{} & りょ & たび & viaje & \ruby{旅行}{りょこう} & 17 \\
% U18
\ruby{番}{} & ばん & — & número/turno & \ruby{一番}{いちばん} & 18 \\
\ruby{同}{} & どう & おな & igual & \ruby{同じ}{おなじ} & 18 \\
\ruby{違}{} & い & ちが & diferente & \ruby{違う}{ちがう} & 18 \\
% U19
\ruby{電}{} & でん & — & electricidad & \ruby{電車}{でんしゃ} & 19 \\
\ruby{車}{} & しゃ & くるま & vehículo & \ruby{車}{くるま} & 19 \\
\ruby{飛}{} & ひ & と & volar & \ruby{飛行機}{ひこうき} & 19 \\
\ruby{機}{} & き & はた & máquina & \ruby{飛行機}{ひこうき} & 19 \\
\ruby{乗}{} & じょう & の & subir & \ruby{乗}{の}る & 19 \\
% U20
\ruby{頭}{} & とう & あたま & cabeza & \ruby{頭}{あたま} & 20 \\
\ruby{目}{} & もく & め & ojo & \ruby{目}{め} & 20 \\
\ruby{歯}{} & し & は & diente & \ruby{歯}{は} & 20 \\
\ruby{足}{} & そく & あし & pie/pierna & \ruby{足}{あし} & 20 \\
\ruby{痛}{} & つう & いた & dolor & \ruby{痛い}{いたい} & 20 \\
% U21
\ruby{泳}{} & えい & およ & nadar & \ruby{泳}{およ}ぐ & 21 \\
\ruby{歌}{} & か & うた & cantar & \ruby{歌}{うた}う & 21 \\
\ruby{運}{} & うん & はこ & transporte & \ruby{運転}{うんてん} & 21 \\
\ruby{転}{} & てん & ころ & rodar & \ruby{運転}{うんてん} & 21 \\
\ruby{能}{} & のう & — & capacidad & \ruby{可能}{かのう} & 21 \\
% U22
\ruby{欲}{} & よく & ほ & desear & \ruby{欲しい}{ほしい} & 22 \\
\ruby{夢}{} & む & ゆめ & sueño & \ruby{夢}{ゆめ} & 22 \\
\ruby{標}{} & ひょう & しるべ & meta & \ruby{目標}{もくひょう} & 22 \\
\ruby{将}{} & しょう & まさ & futuro & \ruby{将来}{しょうらい} & 22 \\
% U23
\ruby{花}{} & か & はな & flor & \ruby{花}{はな} & 23 \\
\ruby{手}{} & しゅ & て & mano & \ruby{手紙}{てがみ} & 23 \\
\ruby{紙}{} & し & かみ & papel & \ruby{手紙}{てがみ} & 23 \\
\ruby{贈}{} & ぞう & おく & regalar & \ruby{贈}{おく}る & 23 \\
\ruby{受}{} & じゅ & う & recibir & \ruby{受}{う}ける & 23 \\
% U24
\ruby{普}{} & ふ & — & común & \ruby{普通}{ふつう} & 24 \\
\ruby{通}{} & つう & とお & pasar & \ruby{普通}{ふつう} & 24 \\
\ruby{話}{} & わ & はな & hablar & \ruby{話}{はなし} & 24 \\
% U25
\ruby{思}{} & し & おも & pensar & \ruby{思}{おも}う & 25 \\
\ruby{考}{} & こう & かんが & considerar & \ruby{考}{かんが}える & 25 \\
\ruby{意}{} & い & — & intención & \ruby{意見}{いけん} & 25 \\
\ruby{言}{} & げん & い & decir & \ruby{言}{い}う & 25 \\
\ruby{報}{} & ほう & しら & reportar & \ruby{報告}{ほうこく} & 25 \\
% U26
\ruby{押}{} & おう & お & presionar & \ruby{押}{お}す & 26 \\
\ruby{引}{} & いん & ひ & jalar & \ruby{引}{ひ}く & 26 \\
\ruby{動}{} & どう & うご & moverse & \ruby{動}{うご}く & 26 \\
\ruby{止}{} & し & と & detener & \ruby{止}{と}まる & 26 \\
% U27
\ruby{場}{} & じょう & ば & lugar & \ruby{場合}{ばあい} & 27 \\
\ruby{選}{} & せん & えら & elegir & \ruby{選}{えら}ぶ & 27 \\
\ruby{迷}{} & めい & まよ & dudar & \ruby{迷}{まよ}う & 27 \\
% U28
\ruby{怒}{} & ど & おこ & enojarse & \ruby{怒}{おこ}る & 28 \\
\ruby{助}{} & じょ & たす & ayudar & \ruby{助}{たす}ける & 28 \\
\ruby{守}{} & しゅ & まも & proteger & \ruby{守}{まも}る & 28 \\
\ruby{批}{} & ひ & — & criticar & \ruby{批判}{ひはん} & 28 \\
\ruby{評}{} & ひょう & — & evaluar & \ruby{評価}{ひょうか} & 28 \\
% U29
\ruby{様}{} & よう & さま & señor(honoríf.) & お\ruby{客様}{きゃくさま} & 29 \\
\ruby{拝}{} & はい & おが & humilde & \ruby{拝見}{はいけん} & 29 \\
\ruby{承}{} & しょう & うけたまわ & aceptar & \ruby{承知}{しょうち} & 29 \\
\ruby{参}{} & さん & まい & ir (kenjou) & \ruby{参}{まい}る & 29 \\
\ruby{丁}{} & てい & — & cortés & \ruby{丁寧}{ていねい} & 29 \\
\bottomrule
\end{longtable}
```

- [ ] **Step 2: Commit**

```bash
git add apendices/indice-kanjis.tex
git commit -m "content: add appendix indice de kanjis"
```

---

## Phase 6: Compilación Final y Deploy

### Task 38: Compilar PDF final y push a GitHub

**Files:**
- Modify: `main.tex` (verificar todos los \input activos)

- [ ] **Step 1: Verificar que todos los archivos existan**

```powershell
cd "D:\Codigo Abierto\ApuntesJapones"
$files = @(
  "preamble.tex","main.tex","assets/portada.tex",
  "unidades/01-presentaciones.tex","unidades/02-numeros-tiempo.tex",
  "unidades/03-kosoado.tex","unidades/04-lugares-direcciones.tex",
  "unidades/05-rutina-diaria.tex","unidades/06-gustos-preferencias.tex",
  "unidades/07-comida-restaurante.tex","unidades/08-compras.tex",
  "unidades/09-adjetivos.tex","unidades/10-familia.tex",
  "unidades/11-pasado.tex","unidades/12-clima-estaciones.tex",
  "unidades/13-te-form-1.tex","unidades/14-te-form-2.tex",
  "unidades/15-te-iru.tex","unidades/16-experiencias.tex",
  "unidades/17-planes-citas.tex","unidades/18-comparaciones.tex",
  "unidades/19-transporte.tex","unidades/20-cuerpo-salud.tex",
  "unidades/21-forma-potencial.tex","unidades/22-deseos.tex",
  "unidades/23-dar-recibir.tex","unidades/24-forma-casual.tex",
  "unidades/25-opinar-citar.tex","unidades/26-condicional-1.tex",
  "unidades/27-condicional-2.tex","unidades/28-voz-pasiva.tex",
  "unidades/29-keigo-intro.tex","unidades/30-repaso-general.tex",
  "apendices/mapa-particulas.tex","apendices/tablas-conjugacion.tex",
  "apendices/indice-kanjis.tex"
)
$missing = $files | Where-Object { -not (Test-Path $_) }
if ($missing) { Write-Output "MISSING: $missing" } else { Write-Output "All files present" }
```

Expected: `All files present`

- [ ] **Step 2: Primera compilación**

```powershell
lualatex -interaction=nonstopmode main.tex
```

Expected: Compila con posibles warnings de referencias no resueltas. Verificar que no haya errores críticos (líneas con `!`).

- [ ] **Step 3: Segunda compilación (para ToC y referencias cruzadas)**

```powershell
lualatex -interaction=nonstopmode main.tex
```

Expected: `main.pdf` generado. Verificar que el PDF se abra y tenga tabla de contenidos.

- [ ] **Step 4: Si hay errores de emoji package, instalar via MiKTeX**

```powershell
# Abrir MiKTeX Package Manager y buscar "emoji" para instalar
# O via línea de comandos:
mpm --install emoji
```

- [ ] **Step 5: Push final a GitHub**

```bash
git add main.pdf  # opcional: trackear el PDF
git add .
git commit -m "feat: complete 30-unit Japanese notes N5-N4"
git push origin main
```

Expected: Repositorio actualizado en https://github.com/AldoZM/ApuntesJapones
