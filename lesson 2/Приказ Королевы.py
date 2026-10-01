from docx import Document

ruler, item, palace = input().split('/')

doc = Document('decree_template.docx')

for p in doc.paragraphs:
    text = ''.join(run.text for run in p.runs)
    text = text.replace('{{ ruler }}', ruler)
    text = text.replace('{{ item }}', item)
    text = text.replace('{{ palace }}', palace)
    if p.runs:
        p.runs[0].text = text
        for run in p.runs[1:]:
            run.text = ''

doc.save('order.docx')
