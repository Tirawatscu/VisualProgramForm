from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox, QFileDialog
from Template import Ui_MainWindow
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4, landscape
import pdfrw
import os

BASE_DIR = os.path.expanduser("~/Documents/Output")
print(BASE_DIR)
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)

class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.project.setText('The President Park Sukhumvit 24')
        self.date = self.ui.dateEdit.date().toString("dd/MM/yyyy")
        self.ui.CC1.setChecked(True)
        self.ui.DL1.setChecked(True)
        self.ui.pushButton.clicked.connect(self.generateFloor)
        self.ui.clearpic.clicked.connect(self.CLEAR)
        self.PicPathFloor = {
            'Pic1': '',
            'Pic2': '',
            'Pic3': '',
            'Pic4': '',
            'Pic5': '',
            'Pic6': '',
            'Pic7': '',
            'Pic8': '',
            'Pic9': '',
            'Pic10': '',
        }

        self.ui.project2.setText('The President Park Sukhumvit 24')
        #self.ui.CC1_2.setChecked(True)
        self.ui.DL1_2.setChecked(True)
        self.ui.pushButton2.clicked.connect(self.generateColumn)
        self.ui.clearpic_2.clicked.connect(self.CLEAR2)
        self.PicPathColumn = {
            'Pic1': '',
            'Pic2': '',
            'Pic3': '',
            'Pic4': '',
            'Pic5': '',
            'Pic6': '',
            'Pic7': '',
            'Pic8': '',
            'Pic9': '',
            'Pic10': '',
        }

        self.ui.project3.setText('The President Park Sukhumvit 24')
        #self.ui.CC1_3.setChecked(True)
        self.ui.DL1_3.setChecked(True)
        self.ui.pushButton3.clicked.connect(self.generateBeam)
        self.ui.clearpic_3.clicked.connect(self.CLEAR3)
        self.PicPathBeam = {
            'Pic1': '',
            'Pic2': '',
            'Pic3': '',
            'Pic4': '',
            'Pic5': '',
            'Pic6': '',
            'Pic7': '',
            'Pic8': '',
            'Pic9': '',
            'Pic10': '',
        }

    def generateFloor(self):
        pdfmetrics.registerFont(TTFont('THSarabunNew', 'THSarabunNew.ttf'))
        y = 792.52
        Building = self.ui.comboBox.currentText()
        Date = self.ui.dateEdit.date().toString("dd/MM/yyyy")
        Floor = self.ui.floor.text()
        self.PicPathFloor = {
            'Pic1': self.ui.Pic1.topath(),
            'Pic2': self.ui.Pic2.topath(),
            'Pic3': self.ui.Pic3.topath(),
            'Pic4': self.ui.Pic4.topath(),
            'Pic5': self.ui.Pic5.topath(),
            'Pic6': self.ui.Pic6.topath(),
            'Pic7': self.ui.Pic7.topath(),
            'Pic8': self.ui.Pic8.topath(),
            'Pic9': self.ui.Pic9.topath(),
            'Pic10': self.ui.Pic10.topath(),
        }
        A1 = self.ui.A1.text()
        A2 = self.ui.A2.text()
        N1 = self.ui.N1.text()
        N2 = self.ui.N2.text()
        Location = A1 + ', ' + A2 + ' - ' + N1 + ', ' + N2

        can = canvas.Canvas('File_merge.pdf', pagesize=(A4))
        can.setFillColorRGB(0, 0, 0)
        can.setFont("Helvetica", 20)

        if self.ui.CC1.isChecked():
            can.drawString(195, y - 630, u'\u2713')
        else:
            can.drawString(195, y - 649, u'\u2713')

        if self.ui.DL1.isChecked():
            can.drawString(167, y - 676, u'\u2713')
        elif self.ui.DL2.isChecked():
            can.drawString(275, y - 676, u'\u2713')
        elif self.ui.DL3.isChecked():
            can.drawString(420, y - 676, u'\u2713')

        can.setFont("THSarabunNew", 14)
        can.drawString(128, y - 149, Building)
        can.drawString(433, y - 93, Date)
        can.drawString(323, y - 120, Floor)
        can.drawString(425, y - 120, Location)
        can.drawString(128, y - 214, N1)
        can.drawString(128, y - 430, N2)
        can.drawString(166, y - 190, A1)
        can.drawString(440, y - 190, A2)

        if self.PicPathFloor['Pic1'] != '':
            can.drawImage(self.PicPathFloor['Pic1'], 72, y - 597, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathFloor['Pic2'] != '':
            can.drawImage(self.PicPathFloor['Pic2'], 315, y - 597, width=240, height=140,
                          preserveAspectRatio=True)
        can.drawString(135, y - 710, self.ui.textEdit.toPlainText())

        can.showPage()
        can.setFillColorRGB(0, 0, 0)
        can.setFont("THSarabunNew", 14)
        can.drawString(128, y - 149, Building)
        can.drawString(433, y - 93, Date)
        can.drawString(323, y - 120, Floor)
        can.drawString(425, y - 120, Location)

        if self.PicPathFloor['Pic3'] != '':
            can.drawImage(self.PicPathFloor['Pic3'], 72, y - 315, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathFloor['Pic4'] != '':
            can.drawImage(self.PicPathFloor['Pic4'], 315, y - 315, width=240, height=140,
                          preserveAspectRatio=True)

        if self.PicPathFloor['Pic5'] != '':
            can.drawImage(self.PicPathFloor['Pic5'], 72, y - 460, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathFloor['Pic6'] != '':
            can.drawImage(self.PicPathFloor['Pic6'], 315, y - 460, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathFloor['Pic7'] != '':
            can.drawImage(self.PicPathFloor['Pic7'], 72, y - 605, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathFloor['Pic8'] != '':
            can.drawImage(self.PicPathFloor['Pic8'], 315, y - 605, width=240, height=140,
                          preserveAspectRatio=True)

        if self.PicPathFloor['Pic9'] != '':
            can.drawImage(self.PicPathFloor['Pic9'], 72, y - 750, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathFloor['Pic10'] != '':
            can.drawImage(self.PicPathFloor['Pic10'], 315, y - 750, width=240, height=140,
                          preserveAspectRatio=True)

        can.save()

        Outpath = os.path.join(BASE_DIR, Building + '_' + Location + '_' + Floor + '.pdf')
        base_pdf = pdfrw.PdfReader('Floor.pdf')
        pdfrw.PdfWriter().write('Temp.pdf', base_pdf)
        base = pdfrw.PdfReader('Temp.pdf')
        watermark_pdf = pdfrw.PdfReader('File_merge.pdf')
        for page in range(len(base.pages)):
            mark = watermark_pdf.pages[page]
            merger = pdfrw.PageMerge(base.pages[page])
            merger.add(mark).render()
        writer = pdfrw.PdfWriter()
        writer.write('Temp.pdf', base)
        inpfn = 'Temp.pdf'
        out = pdfrw.PdfWriter()
        write = pdfrw.PdfReader(inpfn)
        if self.PicPathFloor['Pic3'] == '':
            out.addpage(write.pages[0])
            out.write(Outpath)
        else:
            out.addpages(write.pages)
            out.write(Outpath)
        os.remove("Temp.pdf")

    def generateColumn(self):
        pdfmetrics.registerFont(TTFont('THSarabunNew', 'THSarabunNew.ttf'))
        y = 792.52
        Building = self.ui.comboBox2.currentText()
        Date = self.ui.dateEdit.date().toString("dd/MM/yyyy")
        Floor = self.ui.floor2.text()
        self.PicPathColumn = {
            'Pic1': self.ui.Pic1_2.topath(),
            'Pic2': self.ui.Pic2_2.topath(),
            'Pic3': self.ui.Pic3_2.topath(),
            'Pic4': self.ui.Pic4_2.topath(),
            'Pic5': self.ui.Pic5_2.topath(),
            'Pic6': self.ui.Pic6_2.topath(),
            'Pic7': self.ui.Pic7_2.topath(),
            'Pic8': self.ui.Pic8_2.topath(),
            'Pic9': self.ui.Pic9_2.topath(),
            'Pic10': self.ui.Pic10_2.topath(),
        }
        A1 = self.ui.A1_2.text()
        N1 = self.ui.N1_2.text()
        Location = A1 + N1

        can = canvas.Canvas('File_merge.pdf', pagesize=(A4))
        can.setFillColorRGB(0, 0, 0)
        can.setFont("Helvetica", 20)

        if self.ui.CC1_2.isChecked():
            can.drawString(195, y - 615, u'\u2713')
        elif self.ui.CC2_2.isChecked():
            can.drawString(386, y - 615, u'\u2713')
        elif self.ui.CC3_2.isChecked():
            can.drawString(195, y - 632, u'\u2713')

        if self.ui.DL1_2.isChecked():
            can.drawString(167, y - 668, u'\u2713')
        elif self.ui.DL2_2.isChecked():
            can.drawString(275, y - 668, u'\u2713')
        elif self.ui.DL3_2.isChecked():
            can.drawString(420, y - 668, u'\u2713')

        can.setFont("THSarabunNew", 14)
        can.drawString(128, y - 149, Building)
        can.drawString(433, y - 93, Date)
        can.drawString(323, y - 120, Floor)
        can.drawString(425, y - 120, Location)

        if self.PicPathColumn['Pic1'] != '':
            can.drawImage(self.PicPathColumn['Pic1'], 72, y - 580, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathColumn['Pic2'] != '':
            can.drawImage(self.PicPathColumn['Pic2'], 315, y - 580, width=240, height=140,
                          preserveAspectRatio=True)

        can.drawString(135, y - 700, self.ui.remark2.toPlainText())

        can.showPage()
        can.setFillColorRGB(0, 0, 0)
        can.setFont("THSarabunNew", 14)
        can.drawString(128, y - 149, Building)
        can.drawString(433, y - 93, Date)
        can.drawString(323, y - 120, Floor)
        can.drawString(425, y - 120, Location)

        if self.PicPathColumn['Pic3'] != '':
            can.drawImage(self.PicPathColumn['Pic3'], 72, y - 315, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathColumn['Pic4'] != '':
            can.drawImage(self.PicPathColumn['Pic4'], 315, y - 315, width=240, height=140,
                          preserveAspectRatio=True)

        if self.PicPathColumn['Pic5'] != '':
            can.drawImage(self.PicPathColumn['Pic5'], 72, y - 460, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathColumn['Pic6'] != '':
            can.drawImage(self.PicPathColumn['Pic6'], 315, y - 460, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathColumn['Pic7'] != '':
            can.drawImage(self.PicPathColumn['Pic7'], 72, y - 605, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathColumn['Pic8'] != '':
            can.drawImage(self.PicPathColumn['Pic8'], 315, y - 605, width=240, height=140,
                          preserveAspectRatio=True)

        if self.PicPathColumn['Pic9'] != '':
            can.drawImage(self.PicPathColumn['Pic9'], 72, y - 750, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathColumn['Pic10'] != '':
            can.drawImage(self.PicPathColumn['Pic10'], 315, y - 750, width=240, height=140,
                          preserveAspectRatio=True)

        can.save()

        Outpath = os.path.join(BASE_DIR, Building + '_' + Location + '_' + Floor + '.pdf')
        base_pdf = pdfrw.PdfReader('Column.pdf')
        pdfrw.PdfWriter().write('Temp.pdf', base_pdf)
        base = pdfrw.PdfReader('Temp.pdf')
        watermark_pdf = pdfrw.PdfReader('File_merge.pdf')
        for page in range(len(base.pages)):
            mark = watermark_pdf.pages[page]
            merger = pdfrw.PageMerge(base.pages[page])
            merger.add(mark).render()
        writer = pdfrw.PdfWriter()
        writer.write('Temp.pdf', base)
        inpfn = 'Temp.pdf'
        out = pdfrw.PdfWriter()
        write = pdfrw.PdfReader(inpfn)
        if self.PicPathColumn['Pic3'] == '':
            out.addpage(write.pages[0])
            out.write(Outpath)
        else:
            out.addpages(write.pages)
            out.write(Outpath)
        os.remove("Temp.pdf")

    def generateBeam(self):
        pdfmetrics.registerFont(TTFont('THSarabunNew', 'THSarabunNew.ttf'))
        y = 792.52
        Building = self.ui.comboBox3.currentText()
        Date = self.ui.dateEdit.date().toString("dd/MM/yyyy")
        Floor = self.ui.floor3.text()
        self.PicPathBeam = {
            'Pic1': self.ui.Pic1_3.topath(),
            'Pic2': self.ui.Pic2_3.topath(),
            'Pic3': self.ui.Pic3_3.topath(),
            'Pic4': self.ui.Pic4_3.topath(),
            'Pic5': self.ui.Pic5_3.topath(),
            'Pic6': self.ui.Pic6_3.topath(),
            'Pic7': self.ui.Pic7_3.topath(),
            'Pic8': self.ui.Pic8_3.topath(),
            'Pic9': self.ui.Pic9_3.topath(),
            'Pic10': self.ui.Pic10_3.topath(),
        }
        A1 = self.ui.A1_3.text()
        N1 = self.ui.N1_3.text()
        Location = A1 + N1

        can = canvas.Canvas('File_merge.pdf', pagesize=(A4))
        can.setFillColorRGB(0, 0, 0)
        can.setFont("Helvetica", 20)

        if self.ui.CC1_3.isChecked():
            can.drawString(195, y - 615, u'\u2713')
        elif self.ui.CC2_3.isChecked():
            can.drawString(386, y - 615, u'\u2713')
        elif self.ui.CC3_3.isChecked():
            can.drawString(195, y - 632, u'\u2713')

        if self.ui.DL1_3.isChecked():
            can.drawString(167, y - 668, u'\u2713')
        elif self.ui.DL2_3.isChecked():
            can.drawString(275, y - 668, u'\u2713')
        elif self.ui.DL3_3.isChecked():
            can.drawString(420, y - 668, u'\u2713')

        can.setFont("THSarabunNew", 14)
        can.drawString(128, y - 149, Building)
        can.drawString(433, y - 93, Date)
        can.drawString(323, y - 120, Floor)
        can.drawString(425, y - 120, Location)

        if self.PicPathBeam['Pic1'] != '':
            can.drawImage(self.PicPathBeam['Pic1'], 72, y - 580, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathBeam['Pic2'] != '':
            can.drawImage(self.PicPathBeam['Pic2'], 315, y - 580, width=240, height=140,
                          preserveAspectRatio=True)

        can.drawString(135, y - 710, self.ui.remark3.toPlainText())

        can.showPage()
        can.setFillColorRGB(0, 0, 0)
        can.setFont("THSarabunNew", 14)
        can.drawString(128, y - 149, Building)
        can.drawString(433, y - 93, Date)
        can.drawString(323, y - 120, Floor)
        can.drawString(425, y - 120, Location)

        if self.PicPathBeam['Pic3'] != '':
            can.drawImage(self.PicPathBeam['Pic3'], 72, y - 315, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathBeam['Pic4'] != '':
            can.drawImage(self.PicPathBeam['Pic4'], 315, y - 315, width=240, height=140,
                          preserveAspectRatio=True)

        if self.PicPathBeam['Pic5'] != '':
            can.drawImage(self.PicPathBeam['Pic5'], 72, y - 460, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathBeam['Pic6'] != '':
            can.drawImage(self.PicPathBeam['Pic6'], 315, y - 460, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathBeam['Pic7'] != '':
            can.drawImage(self.PicPathBeam['Pic7'], 72, y - 605, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathBeam['Pic8'] != '':
            can.drawImage(self.PicPathBeam['Pic8'], 315, y - 605, width=240, height=140,
                          preserveAspectRatio=True)

        if self.PicPathBeam['Pic9'] != '':
            can.drawImage(self.PicPathBeam['Pic9'], 72, y - 750, width=240, height=140,
                          preserveAspectRatio=True)
        if self.PicPathBeam['Pic10'] != '':
            can.drawImage(self.PicPathBeam['Pic10'], 315, y - 750, width=240, height=140,
                          preserveAspectRatio=True)

        can.save()

        Outpath = os.path.join(BASE_DIR, Building + '_' + Location + '_' + Floor + '.pdf')
        base_pdf = pdfrw.PdfReader('Beam.pdf')
        pdfrw.PdfWriter().write('Temp.pdf', base_pdf)
        base = pdfrw.PdfReader('Temp.pdf')
        watermark_pdf = pdfrw.PdfReader('File_merge.pdf')
        for page in range(len(base.pages)):
            mark = watermark_pdf.pages[page]
            merger = pdfrw.PageMerge(base.pages[page])
            merger.add(mark).render()
        writer = pdfrw.PdfWriter()
        writer.write('Temp.pdf', base)
        inpfn = 'Temp.pdf'
        out = pdfrw.PdfWriter()
        write = pdfrw.PdfReader(inpfn)
        if self.PicPathBeam['Pic3'] == '':
            out.addpage(write.pages[0])
            out.write(Outpath)
        else:
            out.addpages(write.pages)
            out.write(Outpath)
        os.remove("Temp.pdf")

    def CLEAR(self):
        QApplication.processEvents()
        self.ui.Pic1.path = ''
        self.ui.Pic2.path = ''
        self.ui.Pic3.path = ''
        self.ui.Pic4.path = ''
        self.ui.Pic5.path = ''
        self.ui.Pic6.path = ''
        self.ui.Pic7.path = ''
        self.ui.Pic8.path = ''
        self.ui.Pic9.path = ''
        self.ui.Pic10.path = ''
        self.ui.Pic1.setText('Drop Picture here')
        self.ui.Pic2.setText('Drop Picture here')
        self.ui.Pic3.setText('Drop Picture here')
        self.ui.Pic4.setText('Drop Picture here')
        self.ui.Pic5.setText('Drop Picture here')
        self.ui.Pic6.setText('Drop Picture here')
        self.ui.Pic7.setText('Drop Picture here')
        self.ui.Pic8.setText('Drop Picture here')
        self.ui.Pic9.setText('Drop Picture here')
        self.ui.Pic10.setText('Drop Picture here')

    def CLEAR2(self):
        QApplication.processEvents()
        self.ui.Pic1_2.path = ''
        self.ui.Pic2_2.path = ''
        self.ui.Pic3_2.path = ''
        self.ui.Pic4_2.path = ''
        self.ui.Pic5_2.path = ''
        self.ui.Pic6_2.path = ''
        self.ui.Pic7_2.path = ''
        self.ui.Pic8_2.path = ''
        self.ui.Pic9_2.path = ''
        self.ui.Pic10_2.path = ''
        self.ui.Pic1_2.setText('Drop Picture here')
        self.ui.Pic2_2.setText('Drop Picture here')
        self.ui.Pic3_2.setText('Drop Picture here')
        self.ui.Pic4_2.setText('Drop Picture here')
        self.ui.Pic5_2.setText('Drop Picture here')
        self.ui.Pic6_2.setText('Drop Picture here')
        self.ui.Pic7_2.setText('Drop Picture here')
        self.ui.Pic8_2.setText('Drop Picture here')
        self.ui.Pic9_2.setText('Drop Picture here')
        self.ui.Pic10_2.setText('Drop Picture here')

    def CLEAR3(self):
        QApplication.processEvents()
        self.ui.Pic1_3.path = ''
        self.ui.Pic2_3.path = ''
        self.ui.Pic3_3.path = ''
        self.ui.Pic4_3.path = ''
        self.ui.Pic5_3.path = ''
        self.ui.Pic6_3.path = ''
        self.ui.Pic7_3.path = ''
        self.ui.Pic8_3.path = ''
        self.ui.Pic9_3.path = ''
        self.ui.Pic10_3.path = ''
        self.ui.Pic1_3.setText('Drop Picture here')
        self.ui.Pic2_3.setText('Drop Picture here')
        self.ui.Pic3_3.setText('Drop Picture here')
        self.ui.Pic4_3.setText('Drop Picture here')
        self.ui.Pic5_3.setText('Drop Picture here')
        self.ui.Pic6_3.setText('Drop Picture here')
        self.ui.Pic7_3.setText('Drop Picture here')
        self.ui.Pic8_3.setText('Drop Picture here')
        self.ui.Pic9_3.setText('Drop Picture here')
        self.ui.Pic10_3.setText('Drop Picture here')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())
