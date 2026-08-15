\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ipara-handbook}[2026/08/11 v0.3 Experimental I.P.A.R.A standalone Handbook class]

% Public Family class. v0.2 implements standard + experimental margin profiles.
% Geometry is still specimen-backed candidate data, not a frozen typography contract.

\newif\ifiparahandbookmargin
\iparahandbookmarginfalse

\RequirePackage{expl3}
\RequirePackage{l3keys2e}

\ExplSyntaxOn
\tl_new:N \g_ipara_handbook_profile_tl
\bool_new:N \g_ipara_handbook_twoside_bool

\keys_define:nn { ipara / handbook }
  {
    profile .choice: ,
    profile / standard .code:n =
      {
        \tl_gset:Nn \g_ipara_handbook_profile_tl { standard }
        \global\iparahandbookmarginfalse
      } ,
    profile / margin .code:n =
      {
        \tl_gset:Nn \g_ipara_handbook_profile_tl { margin }
        \global\iparahandbookmargintrue
      } ,
    profile .initial:n = standard ,
    twoside .bool_gset:N = \g_ipara_handbook_twoside_bool ,
    twoside .initial:n = false
  }

\ProcessKeyOptions [ ipara / handbook ]

\bool_if:NTF \g_ipara_handbook_twoside_bool
  { \PassOptionsToClass{twoside}{scrartcl} }
  { \PassOptionsToClass{oneside}{scrartcl} }
\ExplSyntaxOff

\LoadClass[
  11pt,
  a4paper,
  DIV=11
]{scrartcl}

% Chinese infrastructure only. Heading mechanics stay with KOMA.
\RequirePackage[UTF8,fontset=none,heading=false,scheme=chinese]{ctex}
\RequirePackage{ipara-core}
\RequirePackage{scrlayer-scrpage}
\RequirePackage{caption}
\RequirePackage{xltabular}

% Page geometry is configured only after CTeX/Core establish the actual baseline.
\ifiparahandbookmargin
  \RequirePackage{marginnote}
  \KOMAoptions{areasetadvanced=true,headinclude=true,footinclude=false,headheight=18pt,footheight=18pt}
  \areaset{116mm}{220mm}% candidate specimen geometry, not yet a frozen token
  \setlength{\marginparsep}{5mm}%
  \setlength{\marginparwidth}{39mm}%
  \setlength{\marginparpush}{7pt}%
\else
  \KOMAoptions{areasetadvanced=true,headinclude=true,footinclude=false,headheight=18pt,footheight=18pt}
  \areaset{170mm}{220mm}% candidate standard geometry; real-topic backed, not yet frozen
\fi

\ExplSyntaxOn
\NewExpandableDocumentCommand \iparaHandbookProfile { }
  { \tl_use:N \g_ipara_handbook_profile_tl }
\ExplSyntaxOff

% -----------------------------------------------------
% KOMA-owned heading mechanics
% Standalone Canonical Handbooks are article-like booklets: section is top level.
% -----------------------------------------------------
\setkomafont{section}{\normalfont\Large\bfseries\sffamily\color{iparaDeep}}
\setkomafont{subsection}{\normalfont\large\bfseries\sffamily\color{iparaDeep}}
\setkomafont{subsubsection}{\normalfont\normalsize\bfseries\sffamily}
\setkomafont{pageheadfoot}{\normalfont}
\setkomafont{pagehead}{\normalfont}
\setkomafont{pagefoot}{\normalfont}

\RedeclareSectionCommand[beforeskip=1.15em,afterskip=0.55em]{section}
\RedeclareSectionCommand[beforeskip=0.9em,afterskip=0.4em]{subsection}
\RedeclareSectionCommand[beforeskip=0.7em,afterskip=0.3em]{subsubsection}

% -----------------------------------------------------
% Page style via scrlayer-scrpage
% -----------------------------------------------------
\newcommand{\iparaHeaderLeft}{I.P.A.R.A · Handbook}
\newcommand{\iparaHeaderRight}{\headmark}
\newcommand{\iparaPdfTitle}{I.P.A.R.A Handbook}

\newcommand{\handbooksetup}[3]{%
  \renewcommand{\iparaPdfTitle}{#1}%
  \renewcommand{\iparaHeaderLeft}{#2}%
  \renewcommand{\iparaHeaderRight}{#3}%
  \hypersetup{pdftitle={#1}}%
}

\clearpairofpagestyles
\ihead{\small\sffamily\color{iparaDeep}\textbf{\iparaHeaderLeft}}
\ohead{\small\sffamily\color{iparaDeep}\iparaHeaderRight}
\cfoot{\small\pagemark}
\automark[subsection]{section}
\pagestyle{scrheadings}

\hypersetup{
  unicode=true,
  colorlinks=true,
  linkcolor=iparaDeep,
  urlcolor=iparaAccent,
  citecolor=iparaGreen,
  pdfcreator={XeLaTeX + ipara-handbook}
}

% -----------------------------------------------------
% Handbook reading rhythm
% -----------------------------------------------------
\raggedbottom
\setlength{\parindent}{2em}
\setlength{\parskip}{0.32em plus 0.08em minus 0.04em}

\newcommand{\handbooktitle}[3]{%
  \par\noindent
  \begin{center}
    {\LARGE\bfseries\sffamily #1\par}
    \vspace{0.35em}
    {\large #2\par}
    \if\relax\detokenize{#3}\relax\else
      \vspace{0.35em}{\small\color{black!65}#3\par}
    \fi
  \end{center}
  \vspace{0.35em}
}

% -----------------------------------------------------
% Profile-dependent supplementary channel + width state
% -----------------------------------------------------
\ifiparahandbookmargin
  \NewDocumentCommand{\semanticmargin}{m m}{%
    \marginnote{%
      \RaggedRight\footnotesize\sffamily
      \setlength{\emergencystretch}{1.5em}%
      \textbf{#1}\par
      \vspace{0.2em}%
      \normalfont\footnotesize #2%
    }%
  }

  % KOMA addmargin* mirrors the outer side automatically on odd/even pages.
  % V1 widecontent is local: crossing a page intentionally triggers KOMA's warning.
  \NewDocumentEnvironment{widecontent}{+b}{%
    \par\addvspace{0.55em}%
    \begin{addmargin*}[0pt]{-\dimexpr\marginparsep+\marginparwidth\relax}%
      #1%
    \end{addmargin*}%
    \par\addvspace{0.55em}%
  }{}
\else
  % Standard profile preserves supplementary content inline instead of dropping it.
  \NewDocumentCommand{\semanticmargin}{m m}{%
    \par\addvspace{0.35em}%
    \begin{tcolorbox}[
      enhanced,breakable,
      colback=iparaSoft,colframe=iparaRule,
      boxrule=0pt,leftrule=1.2pt,arc=0pt,
      left=1.6mm,right=1.6mm,top=0.9mm,bottom=0.9mm,
      before skip=0pt,after skip=0pt
    ]
      {\small\sffamily\textbf{#1}\quad\normalfont #2}
    \end{tcolorbox}%
    \par\addvspace{0.35em}%
  }

  % Same Canonical Source remains valid: widecontent is identity in standard profile.
  \NewDocumentEnvironment{widecontent}{+b}{%
    \par\addvspace{0.55em}%
    #1%
    \par\addvspace{0.55em}%
  }{}
\fi

% Generic Core table under Handbook-friendly naming.
\NewDocumentEnvironment{handbooktable}{m +b}{%
  \begin{iparatable}{#1}#2\end{iparatable}%
}{}

% Multi-page table with tabularx-style X/Y columns. Prefer this over manually
% making fixed p/L widths sum to \linewidth: column padding is part of the budget.
\NewDocumentEnvironment{handbooklongtable}{m +b}{%
  \par\addvspace{0.45em}%
  \begingroup\small
  \renewcommand{\arraystretch}{1.22}%
  \setlength{\tabcolsep}{4pt}%
  \setlength{\extrarowheight}{1pt}%
  \begin{xltabular}{\linewidth}{@{}#1@{}}%
    #2%
  \end{xltabular}%
  \par\endgroup\addvspace{0.45em}%
}{}

% Canonical 5-column concept-boundary table for the exam Handbook domain.
\NewDocumentEnvironment{boundarytable}{+b}{%
  \par\addvspace{0.45em}%
  \begingroup\small
  \renewcommand{\arraystretch}{1.22}%
  \setlength{\tabcolsep}{4pt}%
  \noindent\begin{tabularx}{\linewidth}{@{}L{0.16\linewidth} C{0.035\linewidth} L{0.16\linewidth} Y Y@{}}%
    #1%
  \end{tabularx}%
  \par\endgroup\addvspace{0.45em}%
}{}

\newcommand{\boundarytablehead}{%
  \toprule
  \textbf{概念 A} & \textbf{≠} & \textbf{概念 B} & \textbf{真正区别与题目信号} & \textbf{混淆后果}\\
  \midrule
}

\newenvironment{handbookdiagram}{%
  \par\addvspace{0.55em}%
  \begin{center}
}{%
  \end{center}%
  \par\addvspace{0.35em}%
}
\newcommand{\diagramcaption}[1]{{\captionsetup{hypcap=false}\captionof{figure}{#1}}}

% -----------------------------------------------------
% Ordered process chain
% Structural display component, not a new Knowledge asset type.
% Stages remain atomic; line breaks are allowed only at arrow boundaries.
% -----------------------------------------------------
\tikzset{
  iparaStageCard/.style={
    draw=iparaDeep,
    fill=iparaSoft,
    rounded corners=1.8mm,
    minimum height=0.78cm,
    align=center,
    font=\small\sffamily\bfseries\color{iparaDeep},
    line width=0.65pt,
    inner xsep=7pt,
    inner ysep=4pt
  },
  iparaStageArr/.style={
    ->,
    >=Stealth,
    line width=0.8pt,
    draw=iparaAccent
  }
}

% Ordered process chain. This is a structural display primitive rather than a
% new knowledge type: stages stay atomic, while line breaks are allowed only at
% arrow boundaries. It mirrors the experimental Handbook Family API.
\ExplSyntaxOn
\seq_new:N \l_ipara_process_chain_seq
\int_new:N \l_ipara_chain_count_int
\int_new:N \l_ipara_chain_idx_int

\cs_new_protected:Npn \ipara_process_stage:n #1
  { \seq_put_right:Nn \l_ipara_process_chain_seq {#1} }

\cs_new_protected:Npn \ipara_process_chain_render:
  {
    \par\addvspace{0.75em}
    \int_set:Nn \l_ipara_chain_count_int { \seq_count:N \l_ipara_process_chain_seq }
    \int_set:Nn \l_ipara_chain_idx_int { 0 }
    
    \begin{center}
    \begin{tikzpicture}[>=Stealth]
    
    \int_compare:nTF { \l_ipara_chain_count_int <= 4 }
      {
        \seq_map_inline:Nn \l_ipara_process_chain_seq
          {
            \int_incr:N \l_ipara_chain_idx_int
            \int_compare:nTF { \l_ipara_chain_idx_int == 1 }
              {
                \node[iparaStageCard] (node1) at (0,0) {\textcolor{iparaAccent}{\footnotesize\textbf{1.}}\hspace{0.35em}##1};
              }
              {
                \int_set:Nn \l_tmpa_int { \l_ipara_chain_idx_int - 1 }
                \node[iparaStageCard, right=0.55cm~of~node\int_use:N \l_tmpa_int] (node\int_use:N \l_ipara_chain_idx_int) {\textcolor{iparaAccent}{\footnotesize\textbf{\int_use:N \l_ipara_chain_idx_int.}}\hspace{0.35em}##1};
                \draw[iparaStageArr] (node\int_use:N \l_tmpa_int) -- (node\int_use:N \l_ipara_chain_idx_int);
              }
          }
      }
      {
        \seq_map_inline:Nn \l_ipara_process_chain_seq
          {
            \int_incr:N \l_ipara_chain_idx_int
            
            \int_case:nn { \l_ipara_chain_idx_int }
              {
                { 1 } { \node[iparaStageCard] (node1) at (0,0) {\textcolor{iparaAccent}{\footnotesize\textbf{1.}}\hspace{0.35em}##1}; }
                { 2 } { 
                  \node[iparaStageCard, right=0.55cm~of~node1] (node2) {\textcolor{iparaAccent}{\footnotesize\textbf{2.}}\hspace{0.35em}##1}; 
                  \draw[iparaStageArr] (node1) -- (node2);
                }
                { 3 } { 
                  \node[iparaStageCard, right=0.55cm~of~node2] (node3) {\textcolor{iparaAccent}{\footnotesize\textbf{3.}}\hspace{0.35em}##1}; 
                  \draw[iparaStageArr] (node2) -- (node3);
                }
                { 4 } { 
                  \node[iparaStageCard, below=0.75cm~of~node1] (node4) {\textcolor{iparaAccent}{\footnotesize\textbf{4.}}\hspace{0.35em}##1}; 
                  \draw[iparaStageArr] (node3.south) .. controls +(0,-0.4) and +(0,0.4) .. (node4.north);
                }
                { 5 } { 
                  \node[iparaStageCard, right=0.55cm~of~node4] (node5) {\textcolor{iparaAccent}{\footnotesize\textbf{5.}}\hspace{0.35em}##1}; 
                  \draw[iparaStageArr] (node4) -- (node5);
                }
                { 6 } { 
                  \node[iparaStageCard, right=0.55cm~of~node5] (node6) {\textcolor{iparaAccent}{\footnotesize\textbf{6.}}\hspace{0.35em}##1}; 
                  \draw[iparaStageArr] (node5) -- (node6);
                }
              }
          }
      }
      
    \end{tikzpicture}
    \end{center}
    \par\addvspace{0.75em}
  }

\NewDocumentEnvironment{processchain}{}{%
  \seq_clear:N \l_ipara_process_chain_seq
  \RenewDocumentCommand \processstage { m }
    { \ipara_process_stage:n {##1} }
}{%
  \ipara_process_chain_render:
}
\ProvideDocumentCommand \processstage { m }
  { \ClassError{ipara-handbook}{\string\processstage~outside~processchain}{Place~\string\processstage\space commands~inside~a~processchain~environment.} }
\ExplSyntaxOff

\endinput
