# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
sys.path.append("../Controlador")
from contolador import *

class MainWindow(QtGui.QWidget):

  def __init__(self):
    super(MainWindow, self).__init__()
    self.controlador = MainController(self)
    self.init_ui()

  def init_ui(self):
    self.label = QtGui.QLabel("CANTIDAD DE PERSONAS")
    h_layout = QtGui.QHBoxLayout()
    h_layout.addWidget(self.label)
    button_subir = QtGui.QPushButton("Subir persona")
    button_bajar = QtGui.QPushButton("Bajar persona")
    h_layout.addWidget(button_subir)
    h_layout.addWidget(button_bajar)
#    label2 = QtGui.QLabel(self.controlador.handler_cantidad_personas)
#    h_layout.addWidget(label2)

    button_subir.clicked.connect(self.controlador.handler_subir_persona)
    button_bajar.clicked.connect(self.controlador.handler_bajar_persona)

    self.setLayout(h_layout)
    self.setWindowTitle("Maru y Mau lindos")
    self.setGeometry(200, 200, 200, 200)
    self.show()

app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())

