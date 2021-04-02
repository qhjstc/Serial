"""
This project is for QtSide2 learning
"""

from PySide2.QtWidgets import QApplication, QMainWindow


def main():
    app = QApplication([])

    windows = QMainWindow()
    windows.resize(500, 400)
    windows.move(300, 310)

    windows.show()
    app.exec_()


if __name__ == '__main__':
    print("Hello this is QtSide2!")
    main()



