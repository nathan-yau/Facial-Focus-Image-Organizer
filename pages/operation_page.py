from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout

from sections.sections_creator import SectionsCreator
from widgets.widgets_creator import WidgetsCreator


class OperationPage(QMainWindow):

    def __init__(self, widget_creator: WidgetsCreator, section_creator: SectionsCreator, window_info: tuple):
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

