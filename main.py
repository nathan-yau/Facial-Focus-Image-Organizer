import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout
from abc import ABC, abstractmethod


class ButtonCreator(ABC):
    @abstractmethod
    def create_buttons(self):
        pass

    @abstractmethod
    def get_buttons(self):
        pass


class MainPageButtonCreator(ButtonCreator):

    def __init__(self):
        self._list_of_buttons = []

    def _create_standard_button(self, display, width, height, font_size):
        button = QPushButton(display)
        button.setFixedSize(QSize(width, height))
        font = QFont()
        font.setPointSize(font_size)
        button.setFont(font)
        self._list_of_buttons.append(button)

    def create_buttons(self):
        self._create_standard_button("Start App", 120, 40, 10)
        # self._create_standard_button("Exit", 80, 40, 10)

    def get_buttons(self):
        return self._list_of_buttons


class MainWindow(QMainWindow):
    def __init__(self, button_creator: ButtonCreator, window_info: tuple):
        super().__init__()
        title, x_position, y_position, width, height = window_info
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon('./resource/icon.png'))
        self.setGeometry(x_position, y_position, width, height)
        self.setFixedSize(width, height)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        label = QLabel(self)
        pixmap = QPixmap('./resource/logo.png')
        resized_pixmap = pixmap.scaled(200, 200)
        label.setPixmap(resized_pixmap)
        label.setFixedSize(200, 200)

        main_layout.addStretch(1)
        main_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addStretch(1)

        buttons_layout = QHBoxLayout()
        button_creator.create_buttons()
        buttons_layout.addStretch(1)
        for button in button_creator.get_buttons():
            buttons_layout.addWidget(button)
        buttons_layout.addStretch(1)

        main_layout.addLayout(buttons_layout)
        main_layout.addStretch(1)
        central_widget.setLayout(main_layout)


def main():
    app = QApplication(sys.argv)
    button_creator = MainPageButtonCreator()
    main_window_info = ("Facial Focus Image Organizer", 500, 500, 400, 400)
    main_window = MainWindow(button_creator, main_window_info)
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
