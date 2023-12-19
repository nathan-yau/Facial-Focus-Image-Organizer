from typing import Protocol


class WidgetsCreator(Protocol):

    def top_layout_widgets(self):
        pass

    def middle_layout_widgets(self):
        pass

    def bottom_layout_widgets(self):
        pass

    def get_top_layout_widgets(self):
        pass

    def get_middle_layout_widgets(self):
        pass

    def get_bottom_layout_widgets(self):
        pass
