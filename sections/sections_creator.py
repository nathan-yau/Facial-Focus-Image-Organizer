from typing import Protocol

from PyQt6.QtWidgets import QHBoxLayout


class SectionsCreator(Protocol):
    def create_sections(self, outer_layout, widget_creator) -> QHBoxLayout:
        pass
