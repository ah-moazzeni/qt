import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
import pkgutil
def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Hello World App')
    window.setGeometry(100, 100, 280, 80)
    helloMsg = QLabel('<h1>Hello, World!</h1>', parent=window)
    helloMsg.move(60, 15)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
