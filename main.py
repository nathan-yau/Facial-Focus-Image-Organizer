import sys

from PyQt6.QtWidgets import QApplication

from pages.operation_page import OperationPage
from pages.welcome_page import WelcomePage
from pages.pages_navigator import ClassicPageNavigator
from sections.operation_page_sections_creator import OperationPageSectionsCreator
from sections.welcome_page_sections_creator import WelcomePageSectionsCreator
from widgets.operation_page_widgets_creator import OperationPageWidgetsCreator
from widgets.welcome_page_widgets_creator import WelcomePageWidgetsCreator


def main():
    app = QApplication(sys.argv)
    operation_page_info = ("User Interface", 200, 200, 600, 350)
    operation_widgets_creator = OperationPageWidgetsCreator()
    operation_sections_creator = OperationPageSectionsCreator()
    next_page_navigator = ClassicPageNavigator(OperationPage, operation_widgets_creator,
                                               operation_sections_creator, operation_page_info)

    welcome_page_widget_creator = WelcomePageWidgetsCreator(next_page_navigator)
    welcome_page_section_creator = WelcomePageSectionsCreator()
    welcome_page_info = ("Facial Focus Image Organizer", 500, 500, 400, 400)
    welcome_page_window = WelcomePage(welcome_page_widget_creator, welcome_page_section_creator, welcome_page_info)
    next_page_navigator.set_current_page(welcome_page_window)
    welcome_page_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
