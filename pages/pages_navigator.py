from abc import ABC


class PageNavigator(ABC):
    def __init__(self, next_page, widgets_creator, sections_creator, page_info):
        self.current_page = None
        self.next_page = next_page(widgets_creator, sections_creator, page_info)

    def navigate_to_next_page(self):
        pass

    def set_current_page(self, current_page):
        pass


class ClassicPageNavigator(PageNavigator):
    def __init__(self, next_page, widgets_creator, sections_creator, page_info):
        super().__init__(next_page, widgets_creator, sections_creator, page_info)

    def navigate_to_next_page(self):
        self.next_page.show()
        self.current_page.close()

    def set_current_page(self, current_page):
        self.current_page = current_page
