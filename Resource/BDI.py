from datetime import datetime, timedelta
from decimal import getcontext, Decimal
from os.path import join
import pdfrw
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4, landscape
from textwrap import wrap
pdfmetrics.registerFont(TTFont('THSarabunNew', 'THSarabunNew.ttf'))


y = 792.52
Building = 'Cedar'
Date = '18/09/2020'
Floor = '4A'
Location = '15AB'
Damage = 3 #1Severe 2Moderate 3Least
can = canvas.Canvas('File_merge.pdf', pagesize=(A4))


can.setFillColorRGB(0, 0, 0)
can.setFont("Helvetica", 20)
can.drawString(195, y-630, u'\u2713')
if Damage == 1:
    can.drawString(167, y-676, u'\u2713')
elif Damage == 2:
    can.drawString(275, y-676, u'\u2713')
elif Damage == 3:
    can.drawString(420, y-676, u'\u2713')


can.setFont("THSarabunNew", 14)
can.drawString(128, y-149, Building)
can.drawString(433, y-93, Date)
can.drawString(323, y-120, Floor)
can.drawString(425, y-120, Location)

can.drawImage('IMG_0526.jpg', 72, y-597, width=240, height=140,
                     preserveAspectRatio=True)
can.showPage()
can.setFillColorRGB(0,0,0)
can.setFont("THSarabunNew", 10)
can.save()

PATH = open('Floor.pdf')
base_pdf = pdfrw.PdfReader('Floor.pdf')
pdfrw.PdfWriter().write('Outpath.pdf', base_pdf)
base = pdfrw.PdfReader('Outpath.pdf')
watermark_pdf = pdfrw.PdfReader('File_merge.pdf')
for page in range(len(base.pages)):
    mark = watermark_pdf.pages[page]
    merger = pdfrw.PageMerge(base.pages[page])
    merger.add(mark).render()

writer = pdfrw.PdfWriter()
writer.write('Outpath.pdf', base)
