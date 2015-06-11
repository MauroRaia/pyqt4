# -*- coding: utf-8 -*-
import sys
sys.path.append("../Modelo")
from modelo import *

class MainController():

    def __init__(self, una_ventana):
        self.auto = Auto()
        self.ventana = una_ventana

    def handler_subir_persona(self):
        self.auto.subir_persona()
        print self.auto.cantidad_personas
        self.actualizar_label()

    def handler_bajar_persona(self):
        self.auto.bajar_persona()
        print self.auto.cantidad_personas
        self.actualizar_label()

    def actualizar_label(self):
        self.ventana.label.setText(str(self.auto.cantidad_personas))
#    def handler_cantidad_persona(self):
#        print self.auto.cantidad_personas