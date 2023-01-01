import sys
from pathlib import Path

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

from design import *


class App(QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None):
    super().__init__(parent)
    super().setupUi(self)

    self.btnEscolherArquivo.clicked.connect(self.open_image)
    self.btnRedimensionar.clicked.connect(self.redimensionar)
    self.btnSalvar.clicked.connect(self.salvar)

  def open_image(self):
    image, _ = QFileDialog.getOpenFileName(
        None, 'Abrir imagem', r'/home', options=QFileDialog.DontUseNativeDialog)

    self.inputAbrirArquivo.setText(image)
    self.original_img = QPixmap(image)
    self.labelImg.setPixmap(self.original_img)
    self.inputLargura.setText(str(self.original_img.width()))
    self.inputAltura.setText(str(self.original_img.height()))

  def redimensionar(self):
    largura = int(self.inputLargura.text())
    altura = int(self.inputAltura.text())
    self.nova_imagem = self.original_img.scaledToWidth(largura)
    self.labelImg.setPixmap(self.nova_imagem)

    self.inputLargura.setText(str(self.nova_imagem.width()))
    self.inputAltura.setText(str(self.nova_imagem.height()))

  def salvar(self):
    imagem, _ = QFileDialog.getSaveFileName(
      None,
      'Salvar imagem',
      r'/home',
      options=QFileDialog.DontUseNativeDialog
    )
    self.nova_imagem.save(imagem, 'PNG')

if __name__ == '__main__':
  app = QApplication(sys.argv)

  w = App()

  w.show()

  app.exec()
