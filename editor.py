from PyQt4.QtGui import QPlainTextEdit

class Editor(QPlainTextEdit):
    """
    El Editor de la aplicacion
    """
    def __init__(self):
        super(Editor,self).__init__()
        self.es_nuevo = True
        self.nombre = "Nuevo_archivo"
        self.modificado = False

