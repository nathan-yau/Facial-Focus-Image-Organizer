from typing import Protocol


class PageNavigator(Protocol):
    def navigate_to_next_page(self):
        pass
