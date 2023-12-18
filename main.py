import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout
from abc import ABC, abstractmethod


class WidgetsCreator(ABC):

    @abstractmethod
    def top_layout_widgets(self):
        pass

    @abstractmethod
    def middle_layout_widgets(self):
        pass

    @abstractmethod
    def bottom_layout_widgets(self):
        pass

    @abstractmethod
    def get_top_layout_widgets(self):
        pass

    @abstractmethod
    def get_middle_layout_widgets(self):
        pass

    @abstractmethod
    def get_bottom_layout_widgets(self):
        pass


class SectionCreator(ABC):
    @abstractmethod
    def create_sections(self, outer_layout, widget_creator) -> QHBoxLayout:
        pass


class MainPageWidgetsCreator(WidgetsCreator):

    def __init__(self):
        self._list_of_top_layout_widgets = []
        self._list_of_middle_layout_widgets = []
        self._list_of_bottom_layout_widgets = []

    def switch_to_ui(self):
        print("Button clicked!")
    @staticmethod
    def _create_standard_button(layout_list: list, display, width, height, font_size, object_name: str,
                                icon=None, button_action=None):
        if icon:
            button = QPushButton(icon=QIcon(icon), text=display)
        else:
            button = QPushButton(display)
        button.setFixedSize(QSize(width, height))
        font = QFont()
        font.setPointSize(font_size)
        button.setFont(font)
        if button_action:
            button.clicked.connect(button_action)
        button.setObjectName(object_name)
        list.append(layout_list, button)

    @staticmethod
    def _create_standard_image(layout_list: list, display, width, height, object_name: str):
        label = QLabel()
        pixmap = QPixmap(display)
        resized_pixmap = pixmap.scaled(width, height)
        label.setPixmap(resized_pixmap)
        label.setFixedSize(width, height)
        label.setObjectName(object_name)
        list.append(layout_list, label)

    @staticmethod
    def _create_standard_label(layout_list: list, text, width, height, font_size, object_name: str):
        label = QLabel()
        label.setText(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFixedSize(width, height)
        font = QFont()
        font.setPointSize(font_size)
        font.setBold(True)
        label.setFont(font)
        label.setObjectName(object_name)
        list.append(layout_list, label)

    def top_layout_widgets(self):
        self._create_standard_image(self._list_of_top_layout_widgets, "./resource/logo.png", 200, 200, "app_logo")

    def middle_layout_widgets(self):
        self._create_standard_label(self._list_of_middle_layout_widgets, "Image Organizer", 200, 50, 15, "app_name")

    def bottom_layout_widgets(self):
        self._create_standard_button(self._list_of_bottom_layout_widgets, " Start App", 120, 40, 10, "start_button",
                                     "./resource/start.svg", self.switch_to_ui)

    def get_top_layout_widgets(self):
        if not self._list_of_top_layout_widgets:
            self.top_layout_widgets()
            print("Hello")
        return self._list_of_top_layout_widgets

    def get_middle_layout_widgets(self):
        if not self._list_of_middle_layout_widgets:
            self.middle_layout_widgets()
        return self._list_of_middle_layout_widgets

    def get_bottom_layout_widgets(self):
        if not self._list_of_bottom_layout_widgets:
            self.bottom_layout_widgets()
        return self._list_of_bottom_layout_widgets


class MainWindowSection(SectionCreator):

    def _populate_section(self, outer_layout, widgets_function, object_name):
        layout = QHBoxLayout()
        widgets = widgets_function()
        for widget in widgets:
            layout.addWidget(widget)
        layout.setObjectName(object_name)
        outer_layout.addLayout(layout)
    def create_sections(self, outer_layout, widget_creator):
        self._populate_section(outer_layout, widget_creator.get_top_layout_widgets, "top_layout")
        self._populate_section(outer_layout, widget_creator.get_middle_layout_widgets, "middle_layout")
        self._populate_section(outer_layout, widget_creator.get_bottom_layout_widgets, "bottom_layout")


class MainWindow(QMainWindow):
    def __init__(self, widget_creator: WidgetsCreator, section_creator: SectionCreator, window_info: tuple):
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
        section_creator.create_sections(main_layout, widget_creator)

        # Outer Widget Completion
        central_widget.setLayout(main_layout)


def main():
    app = QApplication(sys.argv)
    main_widget_creator = MainPageWidgetsCreator()
    main_section_creator = MainWindowSection()
    main_window_info = ("Facial Focus Image Organizer", 500, 500, 400, 400)
    main_window = MainWindow(main_widget_creator, main_section_creator, main_window_info)
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
