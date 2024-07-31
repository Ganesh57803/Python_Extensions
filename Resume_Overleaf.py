import requests

def compile_latex(latex_code):
    url = "https://www.overleaf.com/docs"
    params = {"snip": latex_code}
    response = requests.get(url, params=params)
    import re

def compile_latex(latex_code):
    url = "https://www.overleaf.com/docs"
    params = {"snip": latex_code}
    response = requests.get(url, params=params)
    project_url = response.url
    return project_url

latex_code = r'''
\documentclass{article}
\begin{document}
My world!
\end{document}
'''

pdf_file = compile_latex(latex_code)
print(pdf_file)
