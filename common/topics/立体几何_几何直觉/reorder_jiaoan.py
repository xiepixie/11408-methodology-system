import re

with open('教案.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the sections we want to move
sec_workflow = r'(\\section\{120 分钟 Workflow 设计\}.*?)(?=\\section|\Z)'
sec_theory = r'(\\section\{立体几何核心知识清单与教学背景\}.*?)(?=\\section\{开场图感检测\})'
sec_intro = r'(\\section\{高一立体几何教学理念与核心主线\}.*?)(?=\\section\{120 分钟 Workflow 设计\})'

# Wait, regex with re.DOTALL is better
m_workflow = re.search(sec_workflow, content, re.DOTALL)
m_theory = re.search(sec_theory, content, re.DOTALL)

if m_workflow and m_theory:
    workflow_text = m_workflow.group(1)
    theory_text = m_theory.group(1)
    
    # Remove them from original content
    content = content.replace(workflow_text, '')
    content = content.replace(theory_text, '')
    
    # Now insert workflow before "高一立体几何教学理念与核心主线"
    content = content.replace('\\section{高一立体几何教学理念与核心主线}', workflow_text + '\n\\section{高一立体几何教学理念与核心主线}')
    
    # Insert theory at the end, right before \end{document}
    # Wait, the theory text might be better placed as \section{附录：立体几何核心知识清单与教学背景}
    theory_text = theory_text.replace('\\section{立体几何核心知识清单与教学背景}', '\\section*{附录：立体几何核心知识清单与教学背景}')
    content = content.replace('\\end{document}', theory_text + '\n\\end{document}')
    
    with open('教案.tex', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Reordered successfully.")
else:
    print("Could not match sections.")
