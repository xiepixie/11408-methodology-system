import os

topic_dir = '/Users/xpx/Data/xpx/Documents/I.P.A.R.A/工作领域/资源/common/topics/圆锥曲线的四种定义'
os.makedirs(topic_dir, exist_ok=True)

# questions.tex
questions_content = r"""\input{../../../common/pool/解析几何/中档/q_conic_def0_angle.tex}
\input{../../../common/pool/解析几何/中档/q_conic_def0_pyramid.tex}
\input{../../../common/pool/解析几何/中档/q_conic_def0_cone_beta.tex}
\input{../../../common/pool/解析几何/中档/q_conic_def0_apollonius.tex}
\input{../../../common/pool/解析几何/中档/q_conic_def0_coordinates_multi.tex}
\input{../../../common/pool/解析几何/中档/q_conic_def0_cuboid_multi.tex}
"""
with open(os.path.join(topic_dir, 'questions.tex'), 'w', encoding='utf-8') as f:
    f.write(questions_content)

# 专题讲义_学案.tex
student_content = r"""\documentclass[11pt,a4paper]{ctexart}
\usepackage[student]{../../../common/ipara}
\input{questions.tex}

\pagestyle{fancy}
\fancyhf{}
\lhead{\small 专题讲义版}
\rhead{\small 姓名：\blank{2.5cm}}
\cfoot{\small 第 \thepage\ 页\quad 共 \pageref{LastPage} 页}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}

\newcommand{\lessoninfo}[4]{%
  \begin{center}
    {\LARGE\bfseries #1}\par
    \vspace{0.8em}
    {\small 姓名：#2 \quad 日期：#3 \quad 讲次：#4}
  \end{center}
  \vspace{0.6em}
}

\begin{document}

\lessoninfo{圆锥曲线的四种定义大总结}{\blank{2.6cm}}{\blank{2.6cm}}{第 X 讲}

\section{本讲目标与核心思维}

\begin{itemize}[itemsep=0.3em]
  \item \textbf{学完本讲后，你应该能够：}
  \item 熟练运用第一、第二、第三定义进行“设而不求”与轨迹识别。
  \item 掌握“第零定义（截面定义）”，破解立体几何包装下的轨迹大题。
\end{itemize}

\mindsetcard{第一定义}{左加右减，抛物看准线}{椭圆 $PF_1+PF_2=2a$；双曲线 $|PF_1-PF_2|=2a$；抛物线 $PF=d(P,l)$。\\
焦半径公式：椭圆左焦点 $a+ex_0$，右焦点 $a-ex_0$；抛物线 $PF=x_0+\frac{p}{2}$。}

\mindsetcard{第二定义}{点点距 比 点线距}{距离之比为常数 $e$。$e<1$ 为椭圆，$e=1$ 为抛物线，$e>1$ 为双曲线。}

\mindsetcard{第三定义}{斜率积 定值}{椭圆 $k_{PA_1} \cdot k_{PA_2} = -\frac{b^2}{a^2}$；双曲线 $k_{PA_1} \cdot k_{PA_2} = \frac{b^2}{a^2}$。中点弦同样适用。}

\newpage

\section{核心考向突破：第零定义（空间截面定义）}

\prehint{
  做“立体几何动点轨迹类型判断”的题目时，请按这三步走：\\
  1. \textbf{找轴线}：看题目中哪条线是固定的。\\
  2. \textbf{找母线角 $\theta$}：动点与轴线连线形成的夹角。\\
  3. \textbf{找线面角 $\beta$}：动点所在平面与轴线的夹角。\\
  最后比大小：$\beta > \theta$ 椭圆；$\beta = \theta$ 抛物线；$\beta < \theta$ 双曲线。
}

\studentproblem{例题 1}
{\small \qConicDefZeroAngleStem}
\mcoptions[4]{圆}{椭圆}{双曲线的一部分}{抛物线的一部分}
\answerblank[4cm]{解：}

\studentproblem{例题 2}
{\small \qConicDefZeroPyramidStem}
\qConicDefZeroPyramidOptions
\answerblank[6cm]{解：}

\studentthink{
  \item $\square$ 我是否能够准确地在立体图形中找到圆锥的“旋转轴”？
  \item $\square$ 比较时，我是否混淆了线面角 $\beta$ 和平面与底面的二面角？
}

\newpage

\section{课堂错因大起底}

\vspace{0.5em}
\noindent\textbf{本讲我的主要问题集中在（请打勾）：}
\begin{itemize}[itemsep=0.4em]
  \item \checkbox 焦点弦计算：抛物线焦点弦长度和坐标积韦达定理不熟练。
  \item \checkbox 距离转化失败：在长方体中，不知道把“点到侧面距离”降维到“底面点到边距离”。
  \item \checkbox 第零定义角度找错：找不到截面与轴线的夹角 $\beta$。
  \item \checkbox 离心率公式乱用：没有记住 $e = \frac{\cos\beta}{\cos\theta}$。
\end{itemize}

\vspace{1em}
\noindent\textbf{本讲我最需要记住的一句话是：}
\vspace{0.5em}

\blank{14cm}

\end{document}
"""
with open(os.path.join(topic_dir, '专题讲义_学案.tex'), 'w', encoding='utf-8') as f:
    f.write(student_content)

# 专题讲义_教案.tex
teacher_content = r"""\documentclass[11pt,a4paper]{ctexart}
\usepackage[teacher]{../../../common/ipara}
\input{questions.tex}

\pagestyle{fancy}
\fancyhf{}
\lhead{\small 专题讲义：教师备课版}
\rhead{\small 数学一对一}
\cfoot{\small 第 \thepage\ 页\quad 共 \pageref{LastPage} 页}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}

\newcommand{\lessoninfo}[2]{%
  \begin{center}
    {\LARGE\bfseries #1 \quad (教师版)}\par
    \vspace{0.8em}
    {\small 学生：#2 \quad 时长：120 分钟}
  \end{center}
  \vspace{0.6em}
}

\begin{document}

\lessoninfo{圆锥曲线的四种定义大总结}{\blank{2.4cm}}

\section{备课指导与学情预判}

\begin{tabularx}{\textwidth}{p{2.8cm}p{3.2cm}X}
\toprule
时间 & 环节 & 教师动作\\
\midrule
0--30 分钟 & 第一到第三定义回顾 & 快速梳理焦半径公式（左加右减）、离心率定义、斜率积点差法。\\ \hline
30--50 分钟 & 第零定义引入 & 画出圆锥截面图。强调查找母线角 $\theta$ 和截面角 $\beta$。\\ \hline
50--90 分钟 & 立体包装轨迹题突破 & 讲解例 1、例 2。演示如何寻找空间中的轴线和角度。\\ \hline
90--110 分钟 & 压轴与多选拔高 & 讲授坐标系法求法向量夹角（多选题）。\\ \hline
110--120 分钟 & 错因复盘 & 引导学生总结降维思想和避坑指南。\\
\bottomrule
\end{tabularx}

\section{核心考向突破：第零定义应用}

\teacherproblem{例题 1}{线面角基本辨识}
\teachvalue{训练学生首次将立体几何中“斜线段与平面成角”转化为圆锥模型，找出 $\theta$ 和 $\beta$。}

{\small \qConicDefZeroAngleStem}
\qConicDefZeroAngleOptions

\begin{paracol}{2}
\teachblock{标准解答}{
  \qConicDefZeroAngleSolution
}

\switchcolumn
\teachblock{学生问题分析}{
  \qConicDefZeroAngleDiagnosis
}
\teachblock{追问设计}{
  若将题中的定角 $\frac{\pi}{6}$ 改为 $\frac{\pi}{3}$，轨迹会变成什么？（引导答出双曲线，因为 $\beta < \theta$）。
}
\end{paracol}

\teacherproblem{例题 2}{正三棱锥中的隐藏定角}
\teachvalue{难点在于学生需要自己算出 $\beta$。}

{\small \qConicDefZeroPyramidStem}
\qConicDefZeroPyramidOptions

\begin{paracol}{2}
\teachblock{标准解答}{
  \qConicDefZeroPyramidSolution
}
\switchcolumn
\teachblock{学生问题分析}{
  1. \textbf{找不到轴线}：看不到 $PA$ 与底面内所有方向的对称性，从而想不到以 $PA$ 为轴。\\
  2. \textbf{投影点算错}：不知道 $PA=PB=PC$ 意味着投影是外心。
}
\end{paracol}

\remedy{对于算不出外心和 $\beta$ 的学生，课后务必补发“正多面体与三棱锥的外心/重心计算专练”。}

\end{document}
"""
with open(os.path.join(topic_dir, '专题讲义_教案.tex'), 'w', encoding='utf-8') as f:
    f.write(teacher_content)

