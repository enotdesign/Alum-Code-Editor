from PyQt4.QtGui import QApplication
from main_window import MainWindow


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()

    sys.exit(app.exec_())