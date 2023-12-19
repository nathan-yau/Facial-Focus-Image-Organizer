from pages.pages_navigator import PageNavigator
from widgets.widgets_creator import WidgetsCreator
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtWidgets import QPushButton, QLabel


class OperationPageWidgetsCreator(WidgetsCreator):

    def __init__(self, navigator: PageNavigator):
        super().__init__()
        self.navigator = navigator
        self._list_of_top_layout_widgets = []
        self._list_of_middle_layout_widgets = []
        self._list_of_bottom_layout_widgets = []

    @staticmethod
    def switch_to_ui():
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
        return self._list_of_top_layout_widgets

    def get_middle_layout_widgets(self):
        if not self._list_of_middle_layout_widgets:
            self.middle_layout_widgets()
        return self._list_of_middle_layout_widgets

    def get_bottom_layout_widgets(self):
        if not self._list_of_bottom_layout_widgets:
            self.bottom_layout_widgets()
        return self._list_of_bottom_layout_widgets
