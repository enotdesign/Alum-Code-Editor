from PyQt4.QtGui import QMainWindow, QAction, QToolBar, QIcon, QFileDialog, QMessageBox
from PyQt4.QtCore import Qt
from status_bar import StatusBar
from editor import Editor

class MainWindow(QMainWindow):
    """
    Esta es la ventana principal de la App
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(self.tr("Alum Code Editor"))
        self.setMinimumSize(750,500)

        #Barra de Menu TOP
        menu = self.menuBar()
        self.__crear_acciones()
        self.__crear_menu(menu)

        #Widget Cetral
        self.editor = Editor()
        self.setCentralWidget(self.editor)
        self.editor.setStyleSheet("background-color:#1e1e1e;color:white;font-size:18px;border-color:black;")
        self.editor.cursorPositionChanged.connect(self._actualizar_status_bar)
        #ToolBar
        self.toolbar = QToolBar()
        self.__crear_Toolbar(self.toolbar)
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)

        #satusBar
        self.status = StatusBar()
        self.setStatusBar(self.status)
        self.status.setStyleSheet("background-color:#252526;")

        #Conexiones
        self.abrir.triggered.connect(self._abrir_archivo)
        self.guardar.triggered.connect(self._guardar_archivo)
        self.nuevo.triggered.connect(self._nuevo_archivo)

    def __crear_acciones(self):
        #Menu Archivo
        self.nuevo = QAction("Nuevo", self)
        self.nuevo.setShortcut("Ctrl+N")
        self.nuevo.setIcon(QIcon("images/nuevo.svg"))

        self.abrir = QAction("Abrir", self)
        self.abrir.setShortcut("Ctrl+O")
        self.abrir.setIcon(QIcon("images/abrir.svg"))

        self.guardar = QAction("Guardar", self)
        self.guardar.setShortcut("Ctrl+S")
        self.guardar.setIcon(QIcon("images/guardar.svg"))

        self.salir = QAction("Salir", self)
        self.salir.setShortcut("Ctrl+Q")


        #Menu Editar
        self.desacer = QAction("Desacer", self)
        self.desacer.setShortcut("Ctrl+Z")
        self.desacer.setIcon(QIcon("images/desacer.svg"))

        self.rehacer = QAction("Rehacer", self)
        self.rehacer.setShortcut("Ctrl+Y")
        self.rehacer.setIcon(QIcon("images/rehacer.svg"))

        self.cortar = QAction("Cortar", self)
        self.cortar.setShortcut("Ctrl+X")
        self.cortar.setIcon(QIcon("images/cortar.svg"))

        self.copiar = QAction("Copiar", self)
        self.copiar.setShortcut("Ctrl+C")
        self.copiar.setIcon(QIcon("images/copiar.svg"))

        self.pegar = QAction("Pegar", self)
        self.pegar.setShortcut("Ctrl+V")
        self.pegar.setIcon(QIcon("images/pegar.svg"))


        #Menu Ayuda
        self.ayuda = QAction("Documentacion", self)

        #Menu About
        self.about = QAction("About", self)
        self.github = QAction("GitHub", self)


    def __crear_menu(self, menu_bar):
        menu_archivo = menu_bar.addMenu("&Archivo")
        menu_archivo.addAction(self.nuevo)
        menu_archivo.addAction(self.abrir)
        menu_archivo.addAction(self.guardar)
        menu_archivo.addSeparator()
        menu_archivo.addAction(self.salir)

        menu_editar = menu_bar.addMenu("&Editar")
        menu_editar.addAction(self.desacer)
        menu_editar.addAction(self.rehacer)
        menu_editar.addSeparator()
        menu_editar.addAction(self.cortar)
        menu_editar.addAction(self.copiar)
        menu_editar.addAction(self.pegar)

        menu_ayuda = menu_bar.addMenu("&Ayuda")
        menu_ayuda.addAction(self.ayuda)

        menu_about = menu_bar.addMenu("About Us")
        menu_about.addAction(self.about)
        menu_about.addAction(self.github)

    def __crear_Toolbar(self, toolbar):
        toolbar.addAction(self.nuevo)
        self.toolbar.setStyleSheet("background-color:#333333;")
        toolbar.addAction(self.abrir)
        toolbar.addAction(self.guardar)
        toolbar.addSeparator()
        toolbar.addAction(self.cortar)
        toolbar.addAction(self.copiar)
        toolbar.addAction(self.pegar)

    def _abrir_archivo(self):
        nombre = QFileDialog.getOpenFileName(self, self.tr("Abrir archivo"))

        if nombre:
            with open(nombre) as archivo:
                contenido = archivo.read()
            self.editor.setPlainText(contenido)
            self.editor.es_nuevo = False
            self.editor.nombre = nombre

    def _guardar_archivo(self):
        if self.editor.es_nuevo:
            self._guardar_como()
        else:
            contenido = self.editor.toPlainText()
            with open(self.editor.nombre, 'w') as archivo:
                archivo.write(contenido)

    def _guardar_como(self):
        nombre = QFileDialog.getSaveFileName(self, self.tr("Guardar archivo"))
        if nombre:
            contenido = self.editor.toPlainText()
            with open(nombre, 'w') as archivo:
                archivo.write(contenido)

    def _nuevo_archivo(self):
        #ESTE METODO ME ESTA TIRANDO ERROR
        if self.editor.modificado:
            SI = QMessageBox.Yes
            NO = not QMessageBox
            CANCELAR = QMessageBox.Cancel
            respuesta = QMessageBox.question(self, self.tr("Modificado!"),
                                             self.tr("El archivo %s fue modificado/n"
                                                     "Quardar?") % self.editor.nombre,
                                             SI | NO | CANCELAR)
            if respuesta == CANCELAR:
                return
            elif respuesta == SI:
                self._abrir_archivo()
            else:
                self.editor.setPlainText("")
                self.editor.modificado = False
        else:
            self.editor.setPlainText("")
            self.editor.modificado = False

    def _modificado(self, valor):
        if valor:
            self.editor.modificado = True
        else:
            self.editor.modificao = False

    def _actualizar_status_bar(self):
        linea = self.editor.textCursor().blockNumber() + 1
        columna = self.editor.textCursor().columnNumber()
        self.status.actualizar_label(linea, columna)

    def closeEvent(self, evento):
        if self.editor.modificado:
            flags = QMessageBox.Yes
            flags |= QMessageBox.No
            flags |= QMessageBox.Cancel
            r = QMessageBox.information(self, self.tr("Modificado!"),
                                    self.tr("Cerrar la aplicacion sin guardar?"),
                                    flags

                                    )
            if r == QMessageBox.Yes:
                self._guardar_archivo()
            elif r == QMessageBox.No:
                evento.accept()
            else:
                evento.ignore()




