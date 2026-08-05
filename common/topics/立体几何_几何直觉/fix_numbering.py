import re

with open('教案.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all \subsection{ with \subsection*{
content = content.replace('\\subsection{', '\\subsection*{')

with open('教案.tex', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed numbering.")
