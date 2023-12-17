import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout
from abc import ABC, abstractmethod


class WidgetCreator(ABC):
    @abstractmethod
    def create_buttons(self):
        pass

    @abstractmethod
    def create_labels(self):
        pass

    @abstractmethod
    def get_buttons(self):
        pass

    @abstractmethod
    def get_labels(self):
        pass


class SectionCreator(ABC):
    @abstractmethod
    def create_section(self, widget_creator, upper_layout) -> QHBoxLayout:
        pass


class MainPageWidgetCreator(WidgetCreator):

    def __init__(self):
        self._list_of_buttons = []
        self._list_of_labels = []

    def _create_standard_button(self, display, width, height, font_size):
        button = QPushButton(display)
        button.setFixedSize(QSize(width, height))
        font = QFont()
        font.setPointSize(font_size)
        button.setFont(font)
        self._list_of_buttons.append(button)

    def _create_standard_label(self, display, width, height):
        label = QLabel()
        pixmap = QPixmap(display)
        resized_pixmap = pixmap.scaled(width, height)
        label.setPixmap(resized_pixmap)
        label.setFixedSize(width, height)
        self._list_of_labels.append(label)

    def create_labels(self):
        self._create_standard_label("./resource/logo.png", 200, 200)

    def create_buttons(self):
        self._create_standard_button("Start App", 120, 40, 10)
        # self._create_standard_button("Exit", 80, 40, 10)

    def get_buttons(self):
        return self._list_of_buttons

    def get_labels(self):
        print(self._list_of_labels)
        return self._list_of_labels


class MainWindowMiddleSection(SectionCreator):
    def create_section(self, widget_creator, outer_layout):
        middle_layout = QHBoxLayout()
        widget_creator.create_labels()
        for label in widget_creator.get_labels():
            middle_layout.addWidget(label)
        outer_layout.addStretch(1)
        outer_layout.addLayout(middle_layout)
        outer_layout.addStretch(1)


class MainWindowBottomSection(SectionCreator):
    def create_section(self, widget_creator, outer_layout):
        bottom_layout = QHBoxLayout()
        widget_creator.create_buttons()
        bottom_layout.addStretch(1)
        for button in widget_creator.get_buttons():
            bottom_layout.addWidget(button)

        bottom_layout.addStretch(1)
        outer_layout.addLayout(bottom_layout)
        outer_layout.addStretch(1)


class MainWindow(QMainWindow):
    def __init__(self, widget_creator: WidgetCreator, middle_section: SectionCreator, 
                 bottom_section: SectionCreator, window_info: tuple):
        super().__init__()
        title, x_position, y_position, width, height = window_info
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon('./resource/icon.png'))
        self.setGeometry(x_position, y_position, width, height)
        self.setFixedSize(width, height)

        # Outer Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()

        # Middle Section
        middle_section.create_section(widget_creator, main_layout)

        # Button Section
        bottom_section.create_section(widget_creator, main_layout)

        # Outer Widget Completion
        central_widget.setLayout(main_layout)


def main():
    app = QApplication(sys.argv)
    main_widget_creator = MainPageWidgetCreator()
    top_section = MainWindowMiddleSection()
    bottom_section = MainWindowBottomSection()
    main_window_info = ("Facial Focus Image Organizer", 500, 500, 400, 400)
    main_window = MainWindow(main_widget_creator, top_section, bottom_section, main_window_info)
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
