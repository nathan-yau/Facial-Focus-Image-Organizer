from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from pages.operation_page import OperationPage
from sections.sections_creator import SectionsCreator
from widgets.widgets_creator import WidgetsCreator


from pages.pages_navigator import PageNavigator
from sections.operation_page_sections_creator import OperationPageSectionsCreator
from widgets.operation_page_widgets_creator import OperationPageWidgetsCreator


class WelcomePageNavigator(PageNavigator):
    def __init__(self, current_page):
        self.current_page = current_page
        self.next_page = None

    def navigate_to_next_page(self):
        operation_page_info = ("Facial Focus Image Organizer", 500, 500, 400, 400)
        operation_page_widget_creator = OperationPageWidgetsCreator(WelcomePageNavigator)
        operation_page_section_creator = OperationPageSectionsCreator()
        self.next_page = OperationPage(operation_page_widget_creator, operation_page_section_creator, operation_page_info)
        self.next_page.show()
        self.current_page.close()


class WelcomePage(QMainWindow):

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

    def close_page(self):
        self.close()
