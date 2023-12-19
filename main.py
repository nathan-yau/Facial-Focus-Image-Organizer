import sys

from PyQt6.QtWidgets import QApplication

from pages.welcome_page import WelcomePage, WelcomePageNavigator
from sections.welcome_page_sections_creator import WelcomePageSectionsCreator
from widgets.welcome_page_widgets_creator import WelcomePageWidgetsCreator


def main():
    app = QApplication(sys.argv)
    welcome_page_navigator = WelcomePageNavigator()
    welcome_page_widget_creator = WelcomePageWidgetsCreator(welcome_page_navigator)
    welcome_page_section_creator = WelcomePageSectionsCreator()
    welcome_page_info = ("Facial Focus Image Organizer", 500, 500, 400, 400)
    welcome_page_window = WelcomePage(welcome_page_widget_creator, welcome_page_section_creator, welcome_page_info)
    welcome_page_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
