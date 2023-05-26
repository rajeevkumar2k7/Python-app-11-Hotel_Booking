from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='a4')
pdf.add_page()
pdf.set_font(family="Times",style='B', size=12)
pdf.cell(w=20, h=12, txt='Invoice', align='left', ln=1)
pdf.line(x1=10,x2=200, y1=20,y2=20)
pdf.output('invoice.pdf')
