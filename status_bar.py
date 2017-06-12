from PyQt4.QtGui import QStatusBar

class StatusBar(QStatusBar):
    """
    Status Bar, muestro las Lineas de codigo
    """
    def __init__(self):
        super(StatusBar, self).__init__()