from PyQt4.QtGui import QApplication
#Hago import del modulo Main Window
from main_window import MainWindow

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()

    sys.exit(app.exec_())