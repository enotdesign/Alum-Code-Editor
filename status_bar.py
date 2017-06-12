from PyQt4.QtGui import QStatusBar, QLabel

class StatusBar(QStatusBar):
    """
    Status Bar, muestro las Lineas de codigo
    """
    def __init__(self):
        super(StatusBar, self).__init__()
        self.posicion_cursor = "Linea: %s, Columna: %s"
        self.linea_columna = QLabel(self.posicion_cursor % (0,0))
        self.addWidget(self.linea_columna)

    def actualizar_label(self, linea, columna):
        self.linea_columna.setText(self.posicion_cursor % (linea, columna))